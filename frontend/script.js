const API_URL = "https://todo-fastapi-6u5x.onrender.com"

const token = localStorage.getItem("token")


// LOAD TODOS
async function loadTodos(){

    const response = await fetch(
        `${API_URL}/todos`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    )

    if(response.status === 401){

        localStorage.removeItem("token")

        window.location.href = "login.html"
    }

    const todos = await response.json()

    const todoList =
        document.getElementById("todoList")

    todoList.innerHTML = ""

    if(todos.length === 0){

        todoList.innerHTML = `
            <p class="empty">
                No todos yet
            </p>
        `

        return
    }

    todos.forEach(todo => {

        const li = document.createElement("li")

        li.innerHTML = `

            <span class=" ${todo.completed ? "completed" : ""}">
                ${todo.task}
            </span>
            <span>
                ${todo.description}
            </span>

            <div class="todo-buttons">

                <button
                    onclick="toggleTodo(${todo.id})"
                >
                    ${todo.completed ? "Undo" : "Done"}
                </button>

                <button
                    onclick="deleteTodo(${todo.id})"
                >
                    Delete
                </button>

            </div>
        `

        todoList.appendChild(li)
    })
}

// ADD TODO
async function addTodo(){

    try{

        const taskInput =
            document.getElementById("taskInput")

        const taskDescription =
            document.getElementById("taskDecription")

        const task = taskInput.value

        const description = taskDescription.value

        

        if(task === "" && description === "") return

        await fetch(`${API_URL}/todos`, {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

                Authorization: `Bearer ${token}`
            },

            body: JSON.stringify({
                task,
                description
            })
        })

        taskInput.value = ""

        taskDescription.value = ""

        loadTodos()

    }catch(error){

        console.log(error)

        alert("Something went wrong")
    }
}

// DELETE TODO
async function deleteTodo(id){
    await fetch(`${API_URL}/todos/${id}`, {
        method: "DELETE",
        headers: {
            Authorization: `Bearer ${token}`
        }
    })
    loadTodos()
}

async function toggleTodo(id){

    await fetch(`${API_URL}/todos/${id}`, {
        method: "PUT",
        headers: {
            Authorization: `Bearer ${token}`
        }
    })

    loadTodos()
}
function logout(){

    localStorage.removeItem("token")

    window.location.href = "login.html"
}

loadTodos()
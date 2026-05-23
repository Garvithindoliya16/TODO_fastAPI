const API_URL = "http://127.0.0.1:8000"


async function register(){

    const username =
        document.getElementById("username").value

    const email =
        document.getElementById("email").value

    const password =
        document.getElementById("password").value

    const response = await fetch(
        `${API_URL}/register`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                email,
                password
            })
        }
    )

    if(response.ok){

        alert("Registration successful")

        window.location.href = "login.html"
    }
}
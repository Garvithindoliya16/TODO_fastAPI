const API_URL = "http://127.0.0.1:8000"


async function login(){

    const email = document.getElementById("email").value

    const password = document.getElementById("password").value

    const formData = new URLSearchParams()

    formData.append("username", email)

    formData.append("password", password)

    const response = await fetch(
        `${API_URL}/login`,
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/x-www-form-urlencoded"
            },

            body: formData
        }
    )

    const data = await response.json()

    localStorage.setItem(
        "token",
        data.access_token
    )

    window.location.href = "index.html"
}
const emailInput = document.getElementsByClassName("email");
const passwordInput = document.getElementsByClassName("password");
const loginButton = document.getElementsByClassName("login");

window.onload = checkSavedUser;

function saving() {
    const email = emailInput.value;
    const password = passwordInput.value;

    localStorage.setItem("email", email);
    localStorage.setItem("password", password);
}

// Attach click event listener to login button
loginButton.addEventListener("click", saving);

// Function to check if user is already logged in
function checkSavedUser() {
    const email = localStorage.getItem("email");
    const password = localStorage.getItem("password");

    if (email && password) {
        window.location.href = "http://127.0.0.1:5000/home";
    }
}

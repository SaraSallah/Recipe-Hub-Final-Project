const userEmail = document.getElementById("userEmail");
const loginButton = document.getElementById("login");

function saveUserInLocalStorage() {
    const email = userEmail.value;
    const password = userPassword.value;
    localStorage.setItem("email", email);
}

loginButton.addEventListener("click", function() {
    saveUserInLocalStorage();
});

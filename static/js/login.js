const userEmail = document.getElementById("userEmail");
const loginButton = document.getElementById("login");

function saveUserInLocalStorage() {
    const email = userEmail.value;
    localStorage.setItem("email", email);
}

loginButton.addEventListener("click", function() {
    saveUserInLocalStorage();
});

const userEmail = document.getElementById("userEmail");
const loginButton = document.getElementById("login");

function saveUserInLocalStorage() {
    const email = userEmail.value; // Get the value of an input field with the id userEmail
    localStorage.setItem("email", email); // Save the email address in the browser's localStorage with the key "email"
}

loginButton.addEventListener("click", function() {
    saveUserInLocalStorage(); // Call the saveUserInLocalStorage function when the login button is clicked
});

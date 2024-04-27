const userEmail = document.getElementById("userEmail");
const loginButton = document.getElementById("login");

  

loginButton.addEventListener("click", function() {
    const email = userEmail.value; // Get the value of an input field with the id userEmail
    localStorage.setItem("email", email); // Save the email address in the browser's localStorage with the key "email"
    
});

const userEmail = document.getElementById("user-email"); 
const logout = document.getElementById("logout-button");
const favPage =document.getElementById("fav-recipe")
const deleteAccount = document.getElementById("delete-account") ;
const home = document.getElementById("home");


let localEmail = localStorage.getItem("email"); 
if (localEmail) {
    userEmail.textContent = "Welcome, " + localEmail; 
} else {
    userEmail.textContent = "No email found"; 
}


favPage.addEventListener("click", function() {
    window.location.href = "/fav-recipe";
});


home.addEventListener("click", function() {
    window.location.href = "/home";


});

logout.addEventListener("click", function() {
    fetch("/logout", { method: "POST" })
        .then(() => {
            // After logging out, redirect to the login page
            window.location.href = "/";
        })
});

// Delete the user's account 
deleteAccount.addEventListener("click", function() {
    fetch("/deleteAccount", { method: "POST" })
        .then(() => {
            // After deleting the account, redirect to the sign-up page
            window.location.href = "/signUp"; 
        })
});
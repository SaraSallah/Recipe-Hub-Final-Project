const categoryCard = document.getElementById("category-card");
const recipeItems = document.querySelectorAll(".recipe-list-card");
const userEmail = document.getElementById("user-email"); 
const logout = document.getElementById("logout-button");
const deleteAccount = document.getElementById("delete-account") ;
const favRecipe = document.getElementById("fav-recipe")
const recipeCard = document.getElementById("recipe-card");
const recipeCardPosition = recipeCard.offsetTop;

// get user's email from local storage
let localEmail = localStorage.getItem("email"); 
if (localEmail) {
    userEmail.textContent = "Welcome, " + localEmail; 
} else {
    userEmail.textContent = "No email found"; 
}

// Redirect to favorite recipes page 
document.getElementById("fav-recipe").addEventListener("click", function() {
    window.location.href = "/fav-recipe";
});

// Redirect to category page when clicking on the element with id "categoryCard"
categoryCard.addEventListener("click", function() {
    window.location.href = "/category";
});

//  redirect to recipe details page by get id 
recipeItems.forEach(function(item) {
    item.addEventListener("click", function() {
        const recipeId = item.dataset.id;
        window.location.href = `/recipe-details/${recipeId}`;
    });
});

// Log out event
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

// Function to scroll to a specific position smoothly
function scrollToRecipe() {
    window.scrollTo({
        top: recipeCardPosition, 
        behavior: "smooth" 
    });
}





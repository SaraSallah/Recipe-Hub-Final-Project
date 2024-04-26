const categoryCard = document.getElementById("category-card");
const recipeItems = document.querySelectorAll(".recipe-list-card");
const userEmail = document.getElementById("user-email"); 
const logout = document.getElementById("logout-button");
const deleteAccount = document.getElementById("delete-account") ;
const favRecipe = document.getElementById("fav-recipe")
const recipeCard = document.getElementById("recipe-card");
const recipeCardPosition = recipeCard.offsetTop;

let localEmail = localStorage.getItem("email"); 
if (localEmail) {
    userEmail.textContent = "Welcome " + localEmail; 
} else {
    userEmail.textContent = "No email found"; 
}





document.getElementById("fav-recipe").addEventListener("click", function() {
    window.location.href = "/fav-recipe";
});


categoryCard.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:5000/category";
});

recipeItems.forEach(function(item) {
    item.addEventListener("click", function() {
        const recipeId = item.dataset.id;
        window.location.href = `/recipe-details/${recipeId}`;
    });
});


logout.addEventListener("click", function() {
    fetch("/logout", { method: "POST" })
        .then(() => {
            window.location.href = "/";
        })
});

deleteAccount.addEventListener("click", function() {
    fetch("/deleteAccount", { method: "POST" })
        .then(() => {
            window.location.href = "/signUp"; 
        })
});

function scrollToRecipe() {
   

    window.scrollTo({
        top: recipeCardPosition,
        behavior: "smooth" 
    });
}




const categoryCard = document.getElementById("category-card");
const recipeItems = document.querySelectorAll(".recipe-list-card");
const logout = document.getElementById("logout-button")
const deleteAccount = document.getElementById("delete-account") 
const recipeCard = document.getElementById("recipe-card");
const recipeCardPosition = recipeCard.offsetTop;


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




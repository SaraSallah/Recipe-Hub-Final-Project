const categoryCard = document.getElementById("category-card");
const recipeItems = document.querySelectorAll(".recipe-list-card");

categoryCard.addEventListener("click", function() {
    window.location.href = "http://127.0.0.1:5000/category";
});

recipeItems.forEach(function(item) {
    item.addEventListener("click", function() {
        const recipeId = item.dataset.id;
        window.location.href = `/recipe-details/${recipeId}`;
    });
});
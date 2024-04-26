const recipeItems = document.querySelectorAll(".favorite-item");


recipeItems.forEach(function(item) {
    item.addEventListener("click", function() {
        const recipeId = item.dataset.id;
        window.location.href = `/recipe-details/${recipeId}`;
    });
});
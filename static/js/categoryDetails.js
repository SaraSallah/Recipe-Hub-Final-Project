const recipeItems = document.querySelectorAll(".recipe-list-card");

recipeItems.forEach(function(item) {
    item.addEventListener("click", function() {
        // Get the data-id attribute value from the clicked item
        const recipeId = item.dataset.id; 
        // Redirect the user to the recipe details page 
        window.location.href = `/recipe-details/${recipeId}`; 
    });
});

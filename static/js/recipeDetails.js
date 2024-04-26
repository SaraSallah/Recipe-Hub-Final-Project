
function toggleFavorite(recipeId) {
    fetch(`/add-to-fav/${recipeId}`, { 
        method: "POST" // Send a POST request to add/remove the recipe from favorites
    })
    .then(() => {
        // After the request is successful, redirect the user to the recipe details page
        window.location.href = `/recipe-details/${recipeId}`;
    });
}









    function toggleFavorite(recipeId) {
        fetch(`/add-to-fav/${recipeId}`, { 
            method: "POST"
        })
        
        .then(() => {
            window.location.href = `/recipe-details/${recipeId}`;
        })
    }







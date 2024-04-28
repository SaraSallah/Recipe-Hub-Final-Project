const categoryItem = document.querySelectorAll(".category-card");

categoryItem.forEach(function(item) {
    item.addEventListener("click", function() {
        // Get the data-id attribute value from the clicked item
        const categoryName = item.dataset.id; 
        // Redirect the user to the recipe details page .
        window.location.href = "/category/" + categoryName;
    });
});


const categoryCard = document.getElementById("category-card");
const categoryNameElement = document.getElementById("category-name");

categoryCard.addEventListener("click", function() {
    const categoryName = categoryNameElement.textContent;
    clickCategory(categoryName);
});


function clickCategory(categoryName) {
    window.location.href = "/category/" + categoryName;
}



function toggleFavorite(data) {
    const button = event.target.closest('.favorite-button');
    const heartIcon = button.querySelector('i.fa-heart');
    const isFavorite = button.classList.toggle('favorited');

    // Simulate adding data to favorites
    const favoriteData = JSON.parse(data); // Parse JSON string to object

    // Read existing users.json file
    fetch('users.json')
        .then(response => response.json())
        .then(userData => {
            // Update favorite list for the specific user
            const currentUser = userData.find(user => user.email === favoriteData.email);

            if (!currentUser) {
                console.error('User not found.');
                return;
            }

            if (isFavorite) {
                // Add to favorites
                if (!currentUser.favorites) {
                    currentUser.favorites = [];
                }
                currentUser.favorites.push(favoriteData);
                heartIcon.classList.add('fas');
                heartIcon.classList.remove('far');
            } else {
                // Remove from favorites
                if (currentUser.favorites) {
                    const index = currentUser.favorites.findIndex(fav => fav.email === favoriteData.email);
                    if (index !== -1) {
                        currentUser.favorites.splice(index, 1);
                        heartIcon.classList.add('far');
                        heartIcon.classList.remove('fas');
                    }
                }
            }

            // Write updated userData back to users.json
            const updatedData = JSON.stringify(userData);
            // Update users.json with updated data
            fetch('users.json', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: updatedData
            });
        })
        .catch(error => console.error('Error:', error));
}
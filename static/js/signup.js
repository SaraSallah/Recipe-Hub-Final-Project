// document.getElementById('signup-form').addEventListener('submit', function(event) {
//     event.preventDefault();
//     const formData = new FormData(this);
//     const data = {
//         email: formData.get('email'),
//         password: formData.get('password'),
//         username: formData.get('username')
//     };
//     fetch('/signUp', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     })
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.error('Error:', error));
// });

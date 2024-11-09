document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('registrationModal');
    const btns = document.querySelectorAll('.get-ticket-btn');
    const closeBtn = document.querySelector('.close-btn');
    const messageDiv = document.getElementById('message'); // Reference to the message div

    // Open modal on "Get a Ticket" button click
    btns.forEach(btn => {
        btn.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default action
            modal.style.display = 'block'; // Show the modal
            messageDiv.textContent = ''; // Clear previous messages
        });
    });

    // Close modal on close button click
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none'; // Hide the modal
    });

    // Close modal when clicking outside of the modal content
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none'; // Hide the modal
        }
    });

    // Handle form submission
    const registrationForm = document.getElementById('registrationForm');
    registrationForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent form from submitting

        // Get input values
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;

        // Hard-coded event ID
        const eventId = 3; // Change this to the actual event ID you want to register for

        // Create data object
        const registrationData = {
            event: eventId, // Include hard-coded event ID
            name: name,
            phone_number: phone,
            email: email,
        };

        try {
            // Send data to Django backend
            const response = await fetch('/eventRegistration/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'), // Ensure CSRF token is sent
                },
                body: JSON.stringify(registrationData),
            });

            const result = await response.json(); // Parse JSON response

            // Check response status
            if (!response.ok) {
                throw new Error(result.message || 'Network response was not ok');
            }

            // Display success message
            messageDiv.textContent = result.message || 'You have successfully registered for the event! Check your email for the ticket.';
            messageDiv.style.color = 'green'; // Set message color to green for success

            // Reset form fields
            registrationForm.reset(); // Clear input fields

        } catch (error) {
            console.error('Error:', error);
            messageDiv.textContent = error.message; // Display error message from API
            messageDiv.style.color = 'red'; // Set message color to red for errors
        }
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

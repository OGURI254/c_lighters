// Function to fetch event data from the Django API
async function fetchEvent() {
    try {
        // Fetch event data from the Django REST API
        const response = await fetch('https://localhost:8000/events/');
        if (!response.ok) {
            throw new Error('Event data could not be fetched.');
        }
        const eventsData = await response.json();

        // If there are no events, handle accordingly
        if (!eventsData.length) {
            console.log('No upcoming events found.');
            return;
        }

        // Assuming you want to show the first event in the list
        const event = eventsData[0];

        // Populate fields with the event data
        document.querySelector('.event-content .section-title h3').innerText = "Upcoming Event";
        document.querySelector('.event-content .section-title h2').innerHTML = `${event.name} <span>Festival</span>`;
        
        // Format the date correctly for display
        const eventDate = new Date(event.date);
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        const formattedDate = eventDate.toLocaleDateString(undefined, options);
        
        document.querySelectorAll('.event-body .event-item-content p')[0].innerText = `${formattedDate} - ${event.time}`;
        document.querySelectorAll('.event-body .event-item-content p')[1].innerText = event.venue;
        document.querySelector('.event-footer p').innerText = event.description;

        // Update the event image, or use the default if none is available
        const eventImage = document.querySelector('.event-image img');
        eventImage.src = event.image ? event.image : '/static/images/event-image.jpg';
    } catch (error) {
        console.error('Error fetching event data:', error);
    }
}

// Call the fetch function on page load
window.onload = fetchEvent;

// Function to increment and display the visitor count
function incrementVisitorCount() {
    // Check if the count exists in local storage
    if (localStorage.getItem("visitorCount")) {
        // If it exists, increment it
        localStorage.setItem("visitorCount", parseInt(localStorage.getItem("visitorCount")) + 1);
    } else {
        // If it doesn't exist, initialize it to 1
        localStorage.setItem("visitorCount", 1);
    }

    // Display the updated count on the webpage
    document.getElementById("visitorCount").textContent = localStorage.getItem("visitorCount");
}

// Call the function to increment and display the count
incrementVisitorCount();

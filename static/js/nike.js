document.querySelectorAll('.dropbtn').forEach(button => {
    button.addEventListener('click', function(event) {
        event.stopPropagation();  // Prevents the click from propagating to the window
        const targetMenu = document.getElementById(this.getAttribute('data-target'));

        // Close any other open dropdowns
        document.querySelectorAll('.dropdown-content').forEach(menu => {
            if (menu !== targetMenu) {
                menu.classList.remove('show');
            }
        });

        // Toggle the target menu
        targetMenu.classList.toggle('show');
    });
});

// Close dropdowns when clicking outside
window.addEventListener('click', function() {
    document.querySelectorAll('.dropdown-content').forEach(menu => {
        menu.classList.remove('show');
    });
});

// add to bag
// Initialize count
let count = 0;

// Get button and count display elements
const addToBagButton = document.getElementById('addToBagButton');
const bagCount = document.getElementById('bagCount');

// Add click event listener to the button
addToBagButton.addEventListener('click', () => {
    count++; // Increment the count
    bagCount.textContent = count; // Update the displayed count
});
// Toggle navigation menu on small screens
const navToggle = document.getElementById("nav-toggle");
const navList = document.getElementById("nav-list");

navToggle.addEventListener("click", () => {
    // Toggles the active class to show or hide the navigation menu
    navList.classList.toggle("active");
});

document.getElementById('searchButton').onclick = function() {
    var popupMenu = document.getElementById('popupMenu');
    popupMenu.style.display = (popupMenu.style.display === 'none' || popupMenu.style.display === '') ? 'block' : 'none';
};

document.querySelectorAll('.user-checkbox').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        this.parentNode.classList.toggle('selected', this.checked);
    });
});

// Optional: Close the popup when clicking outside of it
window.onclick = function(event) {
    var popupMenu = document.getElementById('popupMenu');
    if (!popupMenu.contains(event.target) && event.target.id !== 'searchButton') {
        popupMenu.style.display = 'none';
    }
};
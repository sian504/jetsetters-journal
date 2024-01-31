$(document).ready(function () {
    // MaterializeCSS initialization
    $(".sidenav").sidenav({ edge: "right" });
    $('.collapsible').collapsible();
    $('select').formSelect();

    // Code assisted by Leaflet JS documentation - https://leafletjs.com

    // Leaflet.js map initialization
    var map = null; 
    var mapInitialized = false;

    // Function to set up the map based on screen width
    function setupMap() {
        // Check if the map is already initialized
        if (mapInitialized) {
            // If already initialized, just update the view or perform other actions
            map.setView([0, 0], 2);
            return;
        }

        // Default view for larger screens
        var defaultView = [0, 0];
        var defaultZoom = 2;

        // View for smaller screens
        var mobileView = [0, 0];
        var mobileZoom = 0.5;

       
        if ($(window).width() < 600) { 
            map = L.map('map').setView(mobileView, mobileZoom);
        } else {
            map = L.map('map').setView(defaultView, defaultZoom);
        }

        // Add tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        // Add markers 
        L.marker([40.7128, -74.0060]).addTo(map)
            .bindPopup('<a href="#" class="city-link" data-city="New York City"><b>New York City</b></a>');

        L.marker([13.7563, 100.5018]).addTo(map)
            .bindPopup('<a href="#" class="city-link" data-city="Bangkok"><b>Bangkok</b></a>');

        // Event handler for popup links
        map.on('popupopen', function (e) {
            var popup = e.popup;

            // Bind click event to links inside the popup
            popup.getElement().querySelector('.city-link').addEventListener('click', function (event) {
                event.preventDefault();
                var city = this.getAttribute('data-city');

                // Redirect to the Flask route for the selected city
                window.location.href = '/city/' + encodeURIComponent(city);
            });
        });

        // Set the flag to indicate that the map is initialized
        mapInitialized = true;
    }

    // Call the setupMap function on document ready and window resize
    $(window).on('load resize', function () {
        setupMap();
    });
});

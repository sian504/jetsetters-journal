/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();    
});

/*
    jQuery for Leaflet.JS map 
*/

$(document).ready(function () {
    var map = L.map('map').setView([0, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // Add marker for New York City
    L.marker([40.7128, -74.0060]).addTo(map)
        .bindPopup('<a href="#" class="city-link" data-city="New York City"><b>New York City</b></a>');

    // Add marker for Bangkok
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
});




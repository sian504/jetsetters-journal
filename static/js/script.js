/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
});

/*
    jQuery for Leaflet.JS map initialization
*/

$(document).ready(function () {
    // Initialize the map
    var map = L.map('map').setView([0, 0], 2);

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

     // Add marker for New York City
    L.marker([40.7128, -74.0060]).addTo(map)
     .bindPopup('<a href="#"><b>New York City</b></a>');

    // Add marker for Bangkok
    L.marker([13.7563, 100.5018]).addTo(map)
     .bindPopup('<a href="#"><b>Bangkok</b></a>');

});

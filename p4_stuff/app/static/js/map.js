var map = L.map('map').setView([51.505, -0.09], 13);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var mapBounds = (e) => {
    var bounds = map.getBounds();
    console.log(bounds);
};


map.addEventListener('click', mapBounds);
var map = L.map('map').setView([51.505, -0.09], 13);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var mapBounds = (e) => {
    var bounds = map.getBounds();
    console.log(bounds);
};


function getFlightPos(data){
    var pos = [data[5], data[6]]
    return pos;
};

const myIcon = new L.icon({
    iconUrl: 'static/img/plane.png',
    iconSize: [25, 41],
   
});


function makeFlights(data){
    flights = [];
    for (let i = 0; i < data.length; i++) {
        pos = getFlightPos(flightData[i]);
        console.log(pos);
        L.marker([pos[0],pos[1]], {icon: myIcon}).addTo(map);
    }
};


async function getData(bounds) {
    var lamin = bounds["_southWest"]["lat"];
    var lomin = bounds["_southWest"]["lng"];
    var lamax = bounds["_northEast"]["lat"];
    var lomax = bounds["_northEast"]["lng"];
    const response = await fetch(`https://opensky-network.org/api/states/all?lamin=${lamin}&lomin=${lomin}&lamax=${lamax}&lomax=${lomax}`, {
        method: "GET",
    });
    const jsonData = await response.json();
    flightData = jsonData["states"];
    console.log(flightData);
    if (flightData != null){
        makeFlights(flightData);
    }
  };


map.on('zoomend moveend load', function () {
    var bounds = map.getBounds();
    console.log(bounds);
    getData(bounds);
});



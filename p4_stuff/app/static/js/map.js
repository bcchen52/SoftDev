var map = L.map('map',{
    minZoom: 5,
});

map.setView([40.7128, -74.0060], 10);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 15,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var layerGroup = L.layerGroup().addTo(map);

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
    iconSize: [50, 50],
   
});


function makeFlights(data){
    flights = [];
    layerGroup.clearLayers();
    for (let i = 0; i < data.length; i++) {
        pos = getFlightPos(flightData[i]);
        console.log(pos);
        L.marker([pos[1],pos[0]], {icon: myIcon}).addTo(layerGroup);
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
    //console.log(flightData);
    if (flightData != null){
        makeFlights(flightData);
    }
  };


map.on('zoomend moveend load', function () {
    var bounds = map.getBounds();
    console.log(bounds);
    getData(bounds);
});



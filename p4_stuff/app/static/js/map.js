var map = L.map('map',{
    minZoom: 5,
});




L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 10,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var layerGroup = L.layerGroup().addTo(map);

var mapBounds = (e) => {
    var bounds = map.getBounds();
    console.log(bounds);
};

(function() {
    // save these original methods before they are overwritten
    var proto_initIcon = L.Marker.prototype._initIcon;
    var proto_setPos = L.Marker.prototype._setPos;

    var oldIE = (L.DomUtil.TRANSFORM === 'msTransform');

    L.Marker.addInitHook(function () {
        var iconOptions = this.options.icon && this.options.icon.options;
        var iconAnchor = iconOptions && this.options.icon.options.iconAnchor;
        if (iconAnchor) {
            iconAnchor = (iconAnchor[0] + 'px ' + iconAnchor[1] + 'px');
        }
        this.options.rotationOrigin = this.options.rotationOrigin || iconAnchor || 'center bottom' ;
        this.options.rotationAngle = this.options.rotationAngle || 0;

        // Ensure marker keeps rotated during dragging
        this.on('drag', function(e) { e.target._applyRotation(); });
    });

    L.Marker.include({
        _initIcon: function() {
            proto_initIcon.call(this);
        },

        _setPos: function (pos) {
            proto_setPos.call(this, pos);
            this._applyRotation();
        },

        _applyRotation: function () {
            if(this.options.rotationAngle) {
                this._icon.style[L.DomUtil.TRANSFORM+'Origin'] = this.options.rotationOrigin;

                if(oldIE) {
                    // for IE 9, use the 2D rotation
                    this._icon.style[L.DomUtil.TRANSFORM] = 'rotate(' + this.options.rotationAngle + 'deg)';
                } else {
                    // for modern browsers, prefer the 3D accelerated version
                    this._icon.style[L.DomUtil.TRANSFORM] += ' rotateZ(' + this.options.rotationAngle + 'deg)';
                }
            }
        },

        setRotationAngle: function(angle) {
            this.options.rotationAngle = angle;
            this.update();
            return this;
        },

        setRotationOrigin: function(origin) {
            this.options.rotationOrigin = origin;
            this.update();
            return this;
        }
    });
})();



function getFlightPos(data){
    var pos = [data[5], data[6], data[10]]
    return pos;
};




function makeFlights(data){
    flights = [];

    layerGroup.clearLayers();
    
    var zoom = map.getZoom();
    console.log(zoom);
    var x = 50/(Math.abs(zoom-11));
    console.log(x);
    var myIcon = new L.icon({
        iconUrl: 'static/img/plane.png',
        iconSize: [x, x],
    });

    for (let i = 0; i < data.length; i++) {
        pos = getFlightPos(flightData[i]);
        //console.log(pos);
        L.marker([pos[1],pos[0]], {
            icon: myIcon,
            rotationAngle: pos[2],
        }).addTo(layerGroup);
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
    if (flightData != null){
        makeFlights(flightData);
    }


    //console.log(flightData);

  };



map.on('zoomend moveend load', function () {
    var bounds = map.getBounds();
    getData(bounds);
});


map.setView([40.7128, -74.0060], 10);
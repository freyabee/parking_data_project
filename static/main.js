// custom javascript

BASE_COORDINATES = [50.7192, -1.8808]

var map = L.map('map').setView(BASE_COORDINATES, 11);
var layer = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
});
map.addLayer(layer);


// Define a style
var myStyle = {
	"color": "#ff7800",
	"weight": 5,
	"opacity": 0.65
};

// Add the style to your layer    
var geoj = new L.GeoJSON.AJAX("./map1.geojson",{
	 style:myStyle});
console.log(geoj)


var latlngs = []

function onEachFeature(feature, layer) {
	latlngs.push(feature.geometry.coordinates);

};

L.GeoJSON(geoj, {
    onEachFeature: onEachFeature
})

//ar heat = L.heatLayer(coords).addTo(map);

// Animation
var index = 0;
var id = setInterval(function () {
	heat.addLatLng(latlngs[index++]);
	if (index >= latlngs.length - 1) {
		clearInterval(id);
	}
}, 200);


// add markers
latlngs.forEach(function (d, i) {
	L.marker(d, {
			opacity: 0
		}) // hide points
		.bindPopup("Index: " + i, {
			keepInView: true
		})
		.addTo(map);
});


INTENSITY = 10
var heat = L.heatLayer([], {
	radius: 35,
	opacity: 0.8,
	gradient: {
		0.45: "rgb(0,0,255)",
		0.55: "rgb(0,255,255)",
		0.65: "rgb(0,255,0)",
		0.95: "rgb(255,255,0)",
		1.0: "rgb(255,0,0)"
	}
}).addTo(map);


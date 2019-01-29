// custom javascript

BASE_COORDINATES = [50.7192, -1.8808]

var map = L.map('map').setView(BASE_COORDINATES, 11);
var layer = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
});
map.addLayer(layer);

var heat = L.heatLayer([
	[50.7192, -1.8808, 50], // lat, lng, intensity
], {radius: 40}).addTo(map);

console.log("Read!!!")
// custom javascript

BASE_COORDINATES = [50.7192, -1.8808]

var map = L.map('map', {
	timeDimension: true,
	timeDimensionControl: true
}).setView(BASE_COORDINATES, 11);
var layer = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
});
map.addLayer(layer);


function geoJson2heat(geojson, intensity) {
  return geojson.features.map(function(feature) {
    return [
      feature.geometry.coordinates[0][1],
      feature.geometry.coordinates[0][0],
      feature.properties[intensity]
    ];
  });
}






INTENSITY = 10
var heat = L.heatLayer([
	[50.7192, -1.8808, INTENSITY], // lat, lng, intensity
], {
	radius: 25
}).addTo(map);

var timeDimensionControl = new L.Control.TimeDimensionCustom({
    playerOptions: {
        buffer: 1,
        minBufferReady: -1
    }
});
map.addControl(this.timeDimensionControl);

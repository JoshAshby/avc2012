var query = {};
location.search.replace( /[A-Z0-9]+?=(\w*)/gi, function(a) {
	query[ a.split( '=' ).shift() ] = a.split( '=' ).pop();
} );

Reveal.initialize({
	// Display controls in the bottom right corner
	controls: false,
	// Display a presentation progress bar
	progress: false,
	// If true; each slide will be pushed to the browser history
	history: true,
	// Loops the presentation, defaults to false
	loop: true,
	// Flags if mouse wheel navigation should be enabled
	mouseWheel: true,
	// Apply a 3D roll to links on hover
	rollingLinks: true,
	// UI style
	theme: query.theme || 'default', // default/neon
	// Transition style
	transition: query.transition || 'default' // default/cube/page/concave/linear(2d)
});

$.get('/avc/scoreboard/checkIn/', function(data) {
	$('#checkInDiv').html(data);
});

$.get('/avc/scoreboard/heat/0/', function(data) {
	$('#schedule').html(data);
});

$.ajaxSetup({cache: false});
var query = {};
var heat;
var view;

location.search.replace( /[A-Z0-9]+?=(\w*)/gi, function(a){
	query[ a.split( '=' ).shift() ] = a.split( '=' ).pop();
});

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

function tableRefresh(){
	$.getJSON('admin/', {"t": "json"}, function(data){
		heat = data['admin']['heat'];
		view = data['admin']['viewScreen'];
	}).complete(function(){
		if(view != null){
			window.location = '#/' + view;
		}

		window.setTimeout($.get('checkIn/', function(data) {
			table = $('checkInTable').html();
			if(table != data){
				$('#checkInTable').html(data);
			}
		}), 500);

		window.setTimeout($.get(('heat/' + (heat+1) + '/'), function(data) {
			$("#upNextId").html(heat+1);
			table = $('#upNextTable').html();
			if(table != data){
				$('#upNextTable').html(data);
			}
		}), 500);

		window.setTimeout($.get(('heat/' + (heat) + '/'), function(data) {
			$("#currentId").html(heat);
			table = $('#currentTable').html();
			if(table != data){
				$('#currentTable').html(data);
			}
		}), 500);
	});
	t=setTimeout(tableRefresh, 5000);
};

tableRefresh();
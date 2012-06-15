$.ajaxSetup({cache: false});
var query = {};
var heat;
var view;
var current;

var screens = {
	'0': '',
	'1': '1',
	'2': '2',
	'3': '2/1',
	'4': '3',
	'5': '3/1'
};

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
		heat = data['admin']['waveId'];
		heatNext = data['admin']['waveNextId']
		view = data['admin']['viewScreen'];
	}).complete(function(){
		if(view != 0){
			window.location = '#/' + view;
		} else {
			window.location = '#/' + screens[current];
			if (current <= 4) {
				current++;
			} else {
				current = 0;
			}
		}
		
		window.setTimeout($.get('checkIn/', function(data) {
			table = $('checkInTable').html();
			if(table != data){
				$('#checkInTable').html(data);
			}
		}), 10000);

		window.setTimeout($.get(('heat/' + (heatNext) + '/'), function(data) {
			$("#upNextId").html(heatNext);
			table = $('#upNextTable').html();
			if(table != data){
				$('#upNextTable').html(data);
			}
		}), 10000);
		
		window.setTimeout($.get(('heat/' + (heat) + '/'), function(data) {
			$("#currentId").html(heat);
			table = $('#currentTable').html();
			if(table != data){
				$('#currentTable').html(data);
			}
		}), 10000);

		window.setTimeout($.get(('stand/'), {"type": 'air'}, function(data) {
			$('#airTop5Table').html(data);
		}), 10000);

		window.setTimeout($.get(('stand/'), {"type": 'ground'}, function(data) {
			$('#groundTop5Table').html(data);
		}), 10000);
	});
	t=setTimeout(tableRefresh, 10000);
};

tableRefresh();

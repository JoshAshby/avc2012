$('#checkIn').click(function(){
	$.post("/avc/admin/scoreboard/", {view: "1"});
});

$('#schedule').click(function(){
	$.post("/avc/admin/scoreboard/", {view: "2"});
});

$('#current').click(function(){
	$.post("/avc/admin/scoreboard/", {view: "2/1"});
});

$('#top5Ground').click(function(){
	$.post("/avc/admin/scoreboard/", {view: "3"});
});

$('#top5Air').click(function(){
	$.post("/avc/admin/scoreboard/", {view: "3/1"});
});

$('#idle').click(function(){
	$.post("/avc/admin/scoreboard/", {view: "0"});
});

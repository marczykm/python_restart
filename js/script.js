$(document).ready(function(){
    $("#shutdown").click(function(){
	$('#shutdownAlert').fadeIn();
        $.get("/shutdown", function(){});
    });
    $("#restart").click(function(){
	$('#restartAlert').fadeIn();
        $.get("/restart", function(){});
    });	
});

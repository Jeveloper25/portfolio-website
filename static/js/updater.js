$(document).ready(function() {
    $.ajax({
        url: "/password_demo_form1",
        success: function(data) {
           $("#message").text(data.message); 
        }
    });
});
var add_player = function() {
    var empty_row = $("#empty-player-row tr:first").html();
    $('#player-list tr:last').after("<tr>" + empty_row + "</tr>");
    $('#player-list tr:last input:first').focus();
};

$(document).ready(function() {
    $("#add-player").click(function() {
        add_player();
    });

    $("div.main").on("click", "button.remove-player", function() {
        if($("button.remove-player").size() > 2) {
            $(this).closest("tr").remove();
        }
    });

    $('#make-roster-form').on('keyup keypress', function(e) {
        var code = e.keyCode || e.which;
        if (code == 13) { 
            e.preventDefault();
            if(e.type == "keyup") {
                add_player();
            }
            return false;
        }
    });
})
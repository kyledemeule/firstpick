$(document).ready(function() {
    $("#add-player").click(function() {
        var empty_row = $("#empty-player-row tr:first").html();
        $('#player-list tr:last').after("<tr>" + empty_row + "</tr>");
    });

    $("div.main").on("click", "button.remove-player", function() {
        if($("button.remove-player").size() > 2) {
            $(this).closest("tr").remove();
        }
    });
})
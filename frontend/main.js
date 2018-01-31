$(function() {

    console.log("whee!")

    // event handler
    $("#btn-click").click(function() 
    {
        if ($('input').val() !== '') 
        {
            var input = $("input").val()
            console.log(input)
        }
    });
});

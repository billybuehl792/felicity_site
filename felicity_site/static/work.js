$(window).on("load", function() {
    // Masonry
    $(".grid").masonry({
        // options
        // columnWidth: ".grid-sizer",
        itemSelector: ".grid-item",
        percentPosition: true,
        isAnimated: true
    });

    // grid-item hover
    $(".grid-item").hover(function() {
        $(this).children(".item-text").slideDown(100);
    }, function() {
        $(this).find(".item-text").slideUp(100);
    });

    // exit viewer
    $("#viewer").children(".viewer-exit").click(function() {
        $("#viewer").slideUp(200);
    });

    $(document).on('keydown', function(event) {
        if(event.key == "Escape") {
            $("#viewer").slideUp(100);
        }
    });       
});

// image viewer
function viewer(title, image, info) {
    textItems = "";
    textItems += "<h3>" + title + "</h3>";
    for (item in info) {
        if (info[item][1]) {
            textItems += "<h5>" + info[item][0] + ": <span class='important'>" + info[item][1] + "</span></h5>";
        }
    }
    $("#viewer").find(".viewer-text").html(textItems);
    $("#viewer").find(".viewer-image img").attr("src", image);
    $("#viewer").find(".viewer-image img").attr("alt", title);
    $("#viewer").slideDown(100);
}
function scroll() {
    $("#one").click(function(event) {
        event.preventDefault();

        $('html, body').animate({
            scrollTop: $("#test").offset().top-500
        }, 2000);
    });
}
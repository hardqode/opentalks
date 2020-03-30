$('#burger-menu').on('click', function () {
    var menu = $('#scaling-menu');
    menu.find('#close-menu').show();
    menu.css('transform', 'scale(1)');
    menu.css('top', '0%');
    menu.css('right', '0%');
    menu.css('border-radius', '0');
    menu.css('border-radius', '0');
    menu.css('opacity', '1');
});
$('#close-menu').on('click',function () {
    var menu = $('#scaling-menu');
    menu.find('#close-menu').hide();
    menu.css('transform', 'scale(0)');
    menu.css('border-radius', '100%');
    menu.css('opacity', '0');
    // setTimeout(function () {
        menu.css('top', '-42%');
        menu.css('right', '-39%');
    // },1000)
})
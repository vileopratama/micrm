$(document).ready(function () {
    "use strict";
    $(".toggle_leftmenu").click(function() {
            $(".o_sub_menu").animate({
            width: 'toggle'
        }, 0);
    });
});

$(document).ready(function () {
    
    $(".main-div").mouseenter(function () { 
        $(this).addClass("main-div-zoom")
        $(".main-div h1").addClass("main-div-h1-zoom")
        $(".main-div-buttons-a-tag").addClass("main-div-buttons-a-tag-zoom")
        $(".main-div-buttons p").addClass("oppure")
    })

    $(".main-div").mouseleave(function () { 
        $(this).removeClass("main-div-zoom")
        $(".main-div h1").removeClass("main-div-h1-zoom")
        $(".main-div-buttons-a-tag").removeClass("main-div-buttons-a-tag-zoom")
        $(".main-div-buttons p").removeClass("oppure")
    })

});
$(document).ready(function () {
    function AjaxRequestSubjects() {
        $.ajax({
            type: "GET",
            url: "",
            data: "subjects_request",
            success: function (response) {
                if (response["response"] == false){
                    $(".subject-window").css("display", "flex")
                    $(".div-table").css("display","none")
                    $(".button-annulla").hide()
                }

                console.log(response)
                
            }
        });
    }   

    AjaxRequestSubjects();

    $(".button").click(function () {
        $.ajax({
            type: "GET",
            url: "",
            data: {"subject_name": $(".input-field").val()},
            success: function (response) {
                if("None" != response["response"]){
                    $(".div-input-field p").text(response["response"]["subject_name"])
                }
                else{
                    window.location = "/grades"
                }

                
            }
        });
    })

    $(".add-button input").click(function () {
        $(".subject-window").css("display", "flex");
        $(".subject-window").css("position", "absolute");
        $(".div-table").css("filter", "blur(4px)");
        $(".div-table").css("pointer-events", "none");
    })

    $(".button-annulla").click(function () {
        $(".subject-window").css("display", "none");
        $(".subject-window").css("position", "absolute");
        $(".div-table").css("filter", "none");
        $(".div-table").css("pointer-events", "all");
        $(".div-input-field p").text(" ");

    })

    $("th").click(function () {
        $(".tt1").val($(this).text());
        $.ajax({
            type: "GET",
            url: "",
            data: {"subject-options":$(this).text()},
            success: function (response) {
                if (response["response"] == true){              
                    $(".subject-options").css("display", "flex");
                    $(".subject-options").css("position", "absolute");
                    $(".div-table").css("filter", "blur(4px)");
                    $(".div-table").css("pointer-events", "none");
                }
            }
        });
    })

    $(".annulla").click(function () {
        $(".subject-options").css("display", "none");
        $(".div-table").css("filter", "none");
        $(".div-table").css("pointer-events", "all");
        $(".tt1").css("box-shadow","0 0 10px 0 rgb(38, 38, 38)")
        $(".grade-field").css("box-shadow","0 0 10px 0 rgb(38, 38, 38)")
        $(".grade-field").val("")
    })

    $(".aggiorna").click(function () {
        $.ajax({
            type: "GET",
            url: "",
            data: {"update-name-subject":$(".tt1").val()},
            success: function (response) {
                if (response["response"] == true){
                    window.location = "/grades"
                }
                else{
                    $(".tt1").css("box-shadow","0 0 10px 0 rgb(237, 64, 64)")
                }
            }
        });
    })


    $(".salva-voto").click(function () {
        $.ajax({
            type: "GET",
            url: "",
            data: {"save-grade" : $(".grade-field").val()},
            success: function (response) {
                if (response["response"] == true){
                    window.location = "/grades"
                }
                else{
                    $(".grade-field").css("box-shadow","0 0 10px 0 rgb(237, 64, 64)")
                }
            }
        });
    })

    $(".reset-voti").click(function () {
        $.ajax({
            type: "GET",
            url: "",
            data: {"reset-grades":true},
            success: function (response) {
                if (response["response"] == true){
                    window.location = "/grades"
                }
            }
        });
    })

    $(".elimina-materia").click(function () {
        $.ajax({
            type: "GET",
            url: "",
            data: {"delete-subject":true},
            success: function (response) {
                if (response["response"] == true){
                    window.location = "/grades"
                }
            }
        });
    })

    $("td").click(function () {
        
    })

});
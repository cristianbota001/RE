$(document).ready(function () {
    $(".button").mouseenter(function () { 
        $(this).addClass("button-zoom-in")
        $(".input-field, .password-field").addClass("input-text-zoom-out")
    })
    
    $(".button").mouseleave(function () { 
        $(this).removeClass("button-zoom-in")
        $(".input-field, .password-field").removeClass("input-text-zoom-out")
    })

    function sendd_post(method, field) {
        $.ajax({
            type: "POST",
            url: "",
            data: {"username" : $(".input-field").val(), "password" : $(".password-field").val(), csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), "method":method},
            success: function (response) {

                console.log(response)
                 
                if (field == "input-field" || method == "submit"){
                    if ("username" in response["errors"])
                        $(".form-error-1").text(response["errors"]["username"])     
                    else
                        $(".form-error-1").text("") 
                }
                
                if (field == "password-field" || method == "submit"){
                    if ("password" in response["errors"])
                        $(".form-error-2").text(response["errors"]["password"])
                    else
                        $(".form-error-2").text("") 
                }
                
                if (method == "submit" && response["errors"][0] == "None"){
                    window.location = "/grades"
                }
                
            }
        });
    }

    $(".input-field, .password-field").keyup(function () {
        sendd_post("key", this.className);
    })
     
    $(".button").click(function () {
        sendd_post("submit", null)
    })


});
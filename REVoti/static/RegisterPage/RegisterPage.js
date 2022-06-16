$(document).ready(function () {
    $(".button").mouseenter(function () { 
        $(this).addClass("button-zoom-in")
        $(".username, .password1, .password2").addClass("input-text-zoom-out")
        $("::placeholder").attr("font-size", "5px")
    })
    
    $(".button").mouseleave(function () { 
        $(this).removeClass("button-zoom-in")
        $(".username, .password1, .password2").removeClass("input-text-zoom-out")
    })

    function sendd_post(method, field) {
        $.ajax({
            type: "POST",
            url: "",
            data: {"username" : $(".username").val(), "password1" : $(".password1").val(), "password2" : $(".password2").val(), csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(), "method":method},
            success: function (response) {
                 
                if (field == "username" || method == "submit"){
                    if ("username" in response["errors"])
                        $(".form-error-1").text(response["errors"]["username"])     
                    else
                        $(".form-error-1").text("") 
                }
                
                if (field == "password1" || method == "submit"){
                    if ("password1" in response["errors"])
                        $(".form-error-2").text(response["errors"]["password1"])
                    else
                        $(".form-error-2").text("") 
                }
                
                if ((field == "password2" || field == "password1") || method == "submit"){
                    if ("password2" in response["errors"])
                        $(".form-error-3").text(response["errors"]["password2"])
                    else
                        $(".form-error-3").text("") 
                }

                if (method == "submit" && response["errors"][0] == "None"){
                    window.location = "/login"
                }
                
            }
        });
    }


    $(".username, .password1, .password2").keyup(function () {
        sendd_post("key", this.className);
    })
     
    $(".button").click(function () {
        sendd_post("submit", null)
    })



    
    


});
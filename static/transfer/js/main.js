
(function ($) {
    "use strict";


    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })
  
  
    /*==================================================================
    [ Validate ]*/
    var from = $('.validate-input input[name="from_scheme"]');
    var to = $('.validate-input input[name="to_scheme"]');
    var Quantity = $('.validate-input input[name="Quantity"]');


    $('.validate-form').on('submit',function(){
        var check = true;
       
        if($(Quantity).val().trim().match(/[0-9]/)== null) {
            showValidate(Quantity);
            check=false;
        }
        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
       });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    

})(jQuery);
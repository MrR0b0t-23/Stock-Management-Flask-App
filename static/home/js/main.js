
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
    
    var name = $('.validate-input input[name="contactor_name"]');
    var phone = $('.validate-input input[name="phno"]');
    var place = $('.validate-input input[name="place"]');
    var work = $('.validate-input textarea[name="name_of_work"]');
    var Quantity = $('.validate-input input[name="Quantity"]');


    $('.validate-form').on('submit',function(){
        var check = true;

        if($(name).val().trim() == ''){
            showValidate(name);
            check=false;
        }


        if($(phone).val().trim().match(/[1-9]/)== null) {
            showValidate(phone);
            check=false;
        }
        if($(place).val().trim()== '') {
            showValidate(place);
            check=false;
        }
       
        if($(work).val().trim() == ''){
            showValidate(work);
            check=false;
        }
        if($(Quantity).val().trim()== '') {
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
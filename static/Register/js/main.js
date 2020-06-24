
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
    
    var username = $('.validate-input input[name="username"]');
    var passwd = $('.validate-input input[name="Password"]');
    var block = $('.validate-input input[name="block_name"]');
    var u_passwd = $('.validate-input input[name="password"]');
    var o_passwd = $('.validate-input input[name="new_password"]');



    $('.validate-form').on('submit',function(){
        var check = true;

        if($(username).val().trim() == ''){
            showValidate(username);
            check=false;
        }


        if($(block).val().trim()== '') {
            showValidate(block);
            check=false;
        }
       
        if($(passwd).val().trim() == ''){
            showValidate(passwd);
            check=false;
        }
        if($(u_passwd).val().trim() == ''){
            showValidate(u_passwd);
            check=false;
        }
        if($(o_passwd).val().trim() == ''){
            showValidate(o_passwd);
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

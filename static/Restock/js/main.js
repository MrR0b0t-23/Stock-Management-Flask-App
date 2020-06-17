
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
    
    var name = $('.validate-input input[name="supplier_name"]');
    var invoice = $('.validate-input input[name="invoice_no"]');
    var vehicle_no = $('.validate-input input[name="vehicle_no"]');
   
    var Quantity = $('.validate-input input[name="quantity"]');


    $('.validate-form').on('submit',function(){
        var check = true;

        if($(name).val().trim() == ''){
            showValidate(name);
            check=false;
        }


        if($(invoice).val().trim().match(/[1-9]/)== null) {
            showValidate(invoice);
            check=false;
        }
        if($(vehicle_no).val().trim()== '') {
            showValidate(vehicle_no);
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
$(document).ready(function(){
    var signin_form = $('#signin_form');
    var login_form = $('#login_form');

    signin_form.submit(function () {
        console.log(signin_form.serialize)
        $.ajax({
            type: signin_form.attr('method'),
            url: signin_form.attr('action'),
            data: signin_form.serialize(),
            success: function (data) {
                $(".alert-success").show();
            },
            error: function(data) {
                $(".alert-warning").show();
            }
        });
        return false;
    });

    login_form.submit(function () {
        $.ajax({
            type: login_form.attr('method'),
            url: login_form.attr('action'),
            data: login_form.serialize(),
            success: function (data) {
                $(".alert-success").show();
            },
            error: function(data) {
                $(".alert-warning").show();
            }
        });
        return false;
    });

    $(document).on('click', '#alumno', function(){
        $("#alumno_input").val(true);
        $("#alumno_inputs").show();
    });

    $(document).on('click', '#cocinero', function(){
        $("#alumno_input").val('');
        $("#alumno_inputs").hide();
    });
    
    $( "#signin_btn" ).submit(function(event) {
        event.preventDefault();
        signin_form.submit();
    });

    $( "#login_btn" ).submit(function(event) {
        event.preventDefault();
        login_form.submit();
    });

    $(document).on('mouseenter', '.alert', function(){
        $(this).hide();
    });

    $(document).on('click', '#login', function(){
        $("#div_login_form").show();
        $("#div_signin_form").hide();
    });

    $(document).on('click', '#signin', function(){
        $("#div_login_form").hide();
        $("#div_signin_form").show();
    });
});
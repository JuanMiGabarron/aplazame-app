$(document).ready(function(){
    
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        });
    });

    var clear_form = function(){
        $('#nombre').val('')
        $('#descripcion').val('')
        $('#fecha_inicio').text('')
        $('#fecha_fin').text('')
    };

    var curso_success = function(){
        clear_form();
        $('.alert-success').show();
    };

    $(document).on('click', '#create_curso', function(){
        var data = '{\
                        "cocinero":"' + $('#cocinero').val() + '",\
                        "nombre":"' + $('#nombre').val() + '",\
                        "descripcion":"' + $('#descripcion').val() + '",\
                        "fecha_inicio":"' + $('#fecha_inicio').val() + '",\
                        "fecha_fin":"' + $('#fecha_fin').val() + '",\
                        "alumnos": []\
                    }';
        $.ajax({
            type: "POST",
            url: '/api/cursos/',
            data: data,
            success: curso_success,
            contentType: 'application/json',
            dataType: 'json'
        });
       
    });

    $(document).on('mouseenter', '.alert', function(){
        $(this).hide();
    });
});
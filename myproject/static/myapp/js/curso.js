$(document).ready(function(){
    var url = "/api/cursos/" + $("#curso").val();
    var json_data;
    $.getJSON(url+".json", function(data) {
        json_data = data;
        var curso = '<tr>';
        $.each(data, function(key, val) {
            if(key=='alumnos'){
                curso += "<th>"
                $.each(val, function(pos_a, obj_a){
                    curso += obj_a
                });
                curso += "</th>"
            }else{
                curso += ("<th>" + val + "</th>");
            }
        });
        curso += "</tr>"
        $( "<tbody/>", {
            html: curso
        }).appendTo("#cursos_table");
    });

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

    $(document).on('click', '#joinin', function(){
        console.log(json_data['alumnos'])
        json_data['alumnos'].push(parseInt($("#alumno_id").val()));
        console.log(json_data)
        $.ajax({
            type: "PUT",
            url: url+"/",
            data: JSON.stringify(json_data),
            success: function(){
                $(".alert-success").show()
            },
            contentType: 'application/json',
            dataType: 'json'
        });
       
    });

    $(document).on('mouseenter', '.alert', function(){
        $(this).hide();
    });
});
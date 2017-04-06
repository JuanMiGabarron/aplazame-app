$(document).ready(function(){

    $.getJSON( "/api/cursos.json", function(data) {
        var cursos = [];
        var curso = '';
        $.each(data, function(pos, obj) {
            curso = '<tr>';
            $.each(obj, function(key, val) {
                if(key=='alumnos'){
                    curso += "<th>"
                    $.each(val, function(pos_a, obj_a){
                        curso += obj_a
                    });
                    curso += "</th>"
                }else if(key=='nombre'){
                    curso += ("<th><a href=/curso/"+val+">" + val + "<a></th>");
                }else{
                    curso += ("<th>" + val + "</th>");
                }
            });
            curso += '</tr>';
            cursos.push(curso);
        });
        $( "<tbody/>", {
            html: cursos.join("")
        }).appendTo("#cursos_table");
    });
});
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function(){
	cargartabla()
});

var $pagination = $('#pagination');
totalRecords = 0;
displayRecords = [];
recPerPage = 100;
page = 1;
totalPages = 0;
endRec = 0
var tabla = [];

function cargartabla(){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
<<<<<<< HEAD
        url : "https://damianra.pythonanywhere.com/btcdata/btchistory/",
=======
        url : "http://127.0.0.1:8000/btcdata/btchistory/",
>>>>>>> cf6b9cace8aae826b75c52fc48eccf39193095d5
		type : "GET",
        success: function(json){
            json.forEach(element => {
                tabla.push("<tr><td>" + element.date + "</td><td>" + element.price + "</td><td>" + element.var + "</td></tr>")
            });
            totalRecords = tabla.length;
            totalPages = Math.ceil(totalRecords/recPerPage);
            pagination();
        },
        error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
<<<<<<< HEAD

=======
        
>>>>>>> cf6b9cace8aae826b75c52fc48eccf39193095d5
    });

    function generate_table(){
        $('#table').html(displayRecords);
    }


    function pagination(){
        $pagination.twbsPagination({
            totalPages: totalPages,
            visiblePages: 5,
            onPageClick: function(event, page){
                displayRecords = Math.max(page -1, 0) * recPerPage;
                endRec = (displayRecords) + recPerPage;
                displayRecords = tabla.slice(displayRecords, tabla.length);
                generate_table();

                $('html, body').animate({scrollTop: 0}, 800);
            }
        });
<<<<<<< HEAD

=======
        
>>>>>>> cf6b9cace8aae826b75c52fc48eccf39193095d5
    }
}
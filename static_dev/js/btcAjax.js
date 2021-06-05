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
        url : "https://damianra.pythonanywhere.com/btcdata/btchistory/",
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

    }
}
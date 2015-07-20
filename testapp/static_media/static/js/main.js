$(document).ready(function(){

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({

    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('body').on('click','.add', function(event){
    event.preventDefault();
    var answer = $('#id_String-TOTAL_FORMS').val();
     var id_ansrwer = answer - 1;
     var insert =  '<input id="id_String-'+ answer +'-string"  name="String-'+ answer +'-string" type="text">'
     var lable = '<label for="id_String-'+ answer +'-string">string:</label>';
     var into = "#id_String-"+ id_ansrwer +"-string"
    $(insert).insertAfter( into );
     $(lable).insertAfter( into );
    answer = ++answer ;
    $('#id_String-TOTAL_FORMS').val(answer);
     $('.del').show()
});

$('body').on('click','.del', function(event) {
    event.preventDefault();
    var answer = $('#id_String-TOTAL_FORMS').val();
    var id_ansrwer = answer - 1;
    var into = "#id_String-" + id_ansrwer + "-string";
    var into_lable = "id_String-" + id_ansrwer + "-string";
    var lable = 'label[for='+into_lable+']';
    $(lable).remove();
    $(into).remove();



    answer = --answer;
    $('#id_String-TOTAL_FORMS').val(answer);
    if (id_ansrwer == 2){
        $('.del').hide()
    }

});


});
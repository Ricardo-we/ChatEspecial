$(document).on('submit', '#post-form', function(e){
    e.preventDefault()

    $.ajax({
        type:'POST',
        url:'/send',
        
        data:{
            user_name: $('#user_name').val(),
            room_id: $('#room_id').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        
        success: function (data) {
            // alert(data)
        }
    });

    document.getElementById('message').value = '';
})
$(document).ready(function(){
    $('#add-form').submit(function(){
        var url = $('#add-url-text').val();
        var name = $('#add-url-text').attr('name');
        var params = {};
        params[name] = url;
        if (url != ''){
            $.ajax({
                url: '/add-url/',
                dataType: 'json',
                data: params,
                type: 'POST',
                success: function(data){
                    if (data.status == 'ok'){
                        $('#add-url-text').val(data.short_url).select();
                    }
                }
            });
        }
        return false;
    });
});
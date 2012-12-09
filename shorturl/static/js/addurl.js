$(document).ready(function(){
    $('#add-form').submit(function(){
        $('#url-info').text('');
        var url = $('#add-url-text').val();
        var params = {'url': url};
        if (url != ''){
            $.ajax({
                url: '/add-url/',
                dataType: 'json',
                data: params,
                type: 'POST',
                success: function(data){
                    if (data.status == 'ok'){
                        $('#add-url-text').val(data.short_url).select();
                        if (data.clicks){
                            $('#url-info').text('clicks: '+data.clicks);
                        }
                    }
                    else if(data.status == 'error'){

                    }
                }
            });
        }
        return false;
    });
});
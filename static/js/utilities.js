(function($){

    var resetViewport = function(){
        var bottom = $('footer').height();
        $('body').css({'padding-bottom': bottom + 'px'});
    };

    $(document).ready(function(){
        $('.extra-tab').click(function(){

            if ($(this).attr('href') == '#add-form' && !$(this).hasClass('active')) {
                gmapmarker.setVisible(true);
                addresspickerMap.data().addresspicker.reloadPosition();
            } else {
                gmapmarker.setVisible(false);
            }

            $('body').css({'padding-bottom': '0px'});
            var self = $(this);
            if (self.hasClass('active')) {
                $('.extra:visible').slideUp(200, resetViewport);
                $('.extra-tab.active').removeClass('active');
            } else {
                if ($('.extra:visible').length > 0) {
                    $('.extra:visible').slideUp(200, function(){
                        $(self.attr('href')).slideDown(500, resetViewport);
                    });
                } else {
                    $(self.attr('href')).slideDown(500, resetViewport);
                }
                $('.extra-tab.active').removeClass('active');
                self.addClass('active');
            }
            return false;
        });

        $('a[href="#mypos"]').click(function(){
            navigator.geolocation.getCurrentPosition(locationSuccess, locationFail);
            return false;
        });

        $('footer .control-group').each(function(){
            $(this).find('input').attr('placeholder', $.trim($(this).find('label').text()));
            $(this).find('label').hide();
        });

        $('.ajax-form').submit(function(){
            var self = $(this);
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function(data){
                    if (data.status == 'ok') {
                        self.find('input[type="text"]').val('');
                        self.append('<div class="msg">Thank you! Check your email.</div>');
                        gmapmarker.setVisible(false);
                        setTimeout(function(){ $('footer .msg').fadeOut(); $('.extra:visible').slideUp(200, resetViewport); $('.extra-tab.active').removeClass('active'); }, 2500);
                    } else {
                        for (var err in data.errors) {
                            $('#div_id_' + err).addClass('error');
                        }
                    }
                }
            });
            return false;
        });
        $('.ajax-form input').bind('click focus change', function(){
            $(this).parents('.error').removeClass('error');
        });
    });

})(jQuery);
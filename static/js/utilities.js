(function($){

    var resetViewport = function(){
        var bottom = $('footer').height();
        $('body').css({'padding-bottom': bottom + 'px'});
    };

    $(document).ready(function(){
        $('#add-form-toggle').click(function(){

            var self = $(this);
            if (!self.hasClass('active')) {
                gmapmarker.setVisible(true);
                $('.hint1').css('top', '75px');
                self.addClass('active');
                $('#add-form').addClass('visible');
                $('body').css({'padding-right': '240px'});
                addresspickerMap.data().addresspicker.reloadPosition();
            } else {
                gmapmarker.setVisible(false);
                $('.hint1').css('top', '-50px');
                self.removeClass('active');
                $('#add-form').removeClass('visible');
                $('body').css({'padding-right': '0'});
                
                timer = setInterval(function(){ google.maps.event.trigger(gmap, 'resize'); }, 220);
            }

            return false;
        });

        $('.datepicker').datepicker({
            format: 'yyyy-mm-dd'
        });

        $('a[href="#mypos"]').click(function(){
            if (myposmarker === undefined) {
                navigator.geolocation.getCurrentPosition(locationSuccess, locationFail);
            } else {
                if ($(this).hasClass('active')) {
                    myposmarker.setVisible(false);
                    $(this).removeClass('active');
                } else {
                    myposmarker.setVisible(true);
                    $(this).addClass('active');
                }
            }
            return false;
        });

        $('footer .control-group').each(function(){
            $(this).find('input').attr('placeholder', $.trim($(this).find('label').text()));
            $(this).find('label').hide();
        });

        $('.ajax-form').submit(function(){
            var self = $(this);
            self.find('[type="submit"]').val('saving...').addClass('disabled').attr('disabled', 'disabled');
            $.ajax({
                type: 'POST',
                url: self.attr('action'),
                data: self.serialize(),
                success: function(data){
                    self.find('.alert').remove();
                    if (data.status == 'ok') {
                        self.find('input[type="text"]:not([readonly])').val('');
                        self.find('.form-actions').before('<div class="alert alert-success">Thank you! Check your email, you will receive the instructions to activate the TchoukPoint.</div>');
                        setTimeout(function(){ $('.ajax-form .alert').fadeOut(); $('#add-form-toggle').click(); }, 10000);
                    } else {
                        for (var err in data.errors) {
                            self.find('#div_id_' + err).addClass('error');
                        }
                        if(data.errors.__all__ !== undefined) {
                            self.find('.form-actions').before('<div class="alert alert-error">' + data.errors.__all__ + '</div>');
                        }
                    }
                    self.find('[type="submit"]').val('Save').removeClass('disabled').removeAttr('disabled');
                }
            });
            return false;
        });
        $('.ajax-form input').bind('click focus change', function(){
            $(this).parents('.error').removeClass('error');
        });
    });

})(jQuery);
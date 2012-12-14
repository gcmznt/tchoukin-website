(function($){

	$(document).ready(function(){
		$('#add').click(function(){
			$('.add-form').slideDown();
			gmapmarker.setVisible(true);
			return false;
		});
	});

})(jQuery);
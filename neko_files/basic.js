//全ページ共通のjs

/*現在の画面サイズ*/
var displayWidth = ($(window).width());

//================================================================================
//  ページTOPに戻る
//================================================================================

$(document).ready(function() {
  var pagetop = $('#pagetop');
    $(window).scroll(function () {
       if ($(this).scrollTop() > 100) {
            pagetop.fadeIn();
       } else {
            pagetop.fadeOut();
            }
       });
       pagetop.click(function () {
           $('body, html').animate({ scrollTop: 0 }, 500);
              return false;
   });
});

//================================================================================
//  アプリバナーの表示
//================================================================================
$(document).ready(function() {
	if ( displayWidth < 1023) {
		
		var close_flg = true;
		var appLink = $('#app_link');
	
		if($.cookie("head_overlay_close")){
			appLink.css({display:'none'});
		}else{
			$(window).scroll(function () {
			if ($(this).scrollTop() > 150) {
				if( close_flg ){
					appLink.addClass('banner_open');
				}else{
					appLink.css({display:'none'});
				}
			} else {
					appLink.removeClass('banner_open');
			}
			});
			appLink.click(function(){
				close_flg = false;
			});
			$('#app_close').click(function(){
				appLink.css({display:'none'});
				$.cookie("head_overlay_close", '1', { expires: 1 });
				close_flg = false;
			});
		}
	}
});


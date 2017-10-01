/* pre-loader */
$(window).load(function() {
   $(".pre-loader").fadeOut("slow");
});
 
 
/* active link */
for (var i = 0; i < document.links.length; i++) {
    if (document.links[i].href == document.URL) {
        document.links[i].className = 'active';
}}


/* click add class */	
// on click Toggle body class add "BodyClass" /
$('.toggle').click(function() {
	$('body').toggleClass('body-class');
});

/* on click .toggle-nav .fa 991 max side menu toggle class add "SideMenuToggleClass" */
$('.toggle-nav .fa').click(function() {
	$('body').toggleClass('side-menu-toggle-class');
});


/* slideDown animation to dropdown */	
$('.animate-dropdown .dropdown').on('show.bs.dropdown', function(e){
  $(this).find('.dropdown-menu').first().stop(true, true).slideDown(300);
});
$('.animate-dropdown .dropdown').on('hide.bs.dropdown', function(e){
  $(this).find('.dropdown-menu').first().stop(true, true).slideUp(300);
});	


/* date-pick class */  
$(function() {
   $( ".date-pick" ).datepicker();
});  


/* animate tab */
  $(function(){var b="bounce";var c;var a;d($(".nav a"),$(".tab-content"));function d(e,f,g){e.click(function(i){i.preventDefault();$(this).tab("show");var h=$(this).data("easein");if(c){c.removeClass(a);}if(h){f.find(".active").addClass("animated "+h);a=h;}else{if(g){f.find(".active").addClass("animated "+g);a=g;}else{f.find(".active").addClass("animated "+b);a=b;}}c=f.find(".active");});}$("a[rel=popover]").popover().click(function(f){f.preventDefault();if($(this).data("easein")!=undefined){$(this).next().removeClass($(this).data("easein")).addClass("animated "+$(this).data("easein"));}else{$(this).next().addClass("animated "+b);}});});
  
  
// show hide password
$(function () {
        $('.show-hide-pass').password().on('show.bs.password',function (e) {
            $('#eventLog').text('On show event');
            $('#methods').prop('checked', true);
        }).on('hide.bs.password', function (e) {
                    $('#eventLog').text('On hide event');
                    $('#methods').prop('checked', false);
                });
        $('#methods').click(function () {
            $('.show-hide-pass').password('toggle');
        });
 });  
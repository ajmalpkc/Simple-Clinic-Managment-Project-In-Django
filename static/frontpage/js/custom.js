/* pre-loader */
$(window).load(function() {
   $(".pre-loader").fadeOut("slow");
});
 
/* active link */
for (var i = 0; i < document.links.length; i++) {
    if (document.links[i].href == document.URL) {
        document.links[i].className = 'active';
}}
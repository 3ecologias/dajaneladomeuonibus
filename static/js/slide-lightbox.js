// SLIDE POSTS TOP-HEADER
$( document ).ready(function() {
  var slider = new MasterSlider();

slider.control('arrows');
slider.control('lightbox');
slider.control('thumblist' , {autohide:false ,dir:'h',align:'bottom', width:130, height:85, margin:5, space:5 , hideUnder:400});
slider.control('slideinfo',{insertTo:'#masterslider3'});
slider.setup('masterslider3' , {
   width:750,
   height:500,
   space:5,
   loop:true,
   view:'fade'
});

$("a[rel^='prettyPhoto']").prettyPhoto();
});

// SLIDE POSTS TOP-HEADER
$( document ).ready(function() {
 var slider = new MasterSlider();
    slider.setup('masterslider' , {
        loop:true,
        width:240,
        height:240,
        speed:20,
        view:'focus',
        preload:'all',
        space:0,
        wheel:true,
        loop: true,
        filters: {
          grayscale: 1,
          opacity: 0.5,
          brightness: 1
        },
        autoplay: true
    });
    slider.control('arrows');
    slider.control('slideinfo',{insertTo:'#staff-info'});

});

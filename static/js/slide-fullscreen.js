// SLIDE POSTS TOP-HEADER
$( document ).ready(function() {
        var slider = new MasterSlider();
        slider.control('arrows' ,{insertTo:'#masterslider1'});
        slider.control('bullets');
        slider.setup('masterslider1' , {
            width:1024,
            height:768,
            space:5,
            view:'parallaxMask',
            layout:'fullscreen',
            fullscreenMargin:0,
            speed:10,
            autoplay:true,
            filters: {
              grayscale: 2,
              opacity: 1,
              brightness: .7
            },
            loop:true
        });
});

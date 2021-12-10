const seccionesPaginaPrincipal = new fullpage('#fullpage', {
    autoScrolling: true,
    easing: 'easeInOutCubic',
    scrollingSpeed: 700,
    css3: true,
    easingcss3: 'ease-out',
    loopBottom: false,

    /*---Barra de Navegación---*/
    navigation: true,
    menu: '#menu',
    anchors:['Sallqa Pacha', 'Quiénes somos', 'ODS', 'Foros'],
    navigationTooltips: ['Sallqa Pacha', 'Quiénes somos', 'ODS', 'Foros'],
    showAtiveTooltip: false,
});

    
    
    
    /*
    sectionsColor: ['#000', '#c2c2c2', '#000'],
    verticalCentered: true,
    controlArrows: true,
    slidesNavigation: false,
    afterLoad: function(origin, detination){
        if(AudioDestinationNode.anchor == 'Foro'){
            document.querySelector('.footer').querySelector('h2').style.opacity = 1;
        }
    }

    */
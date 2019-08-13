$(function () {
    "use strict";
    
    $("#carouselExampleIndicators").carousel('pause');
    var position_slide_carousel = 0;

    $("#form").submit(function(){

/* loader en attendant que ca charge (<div id="loader"></div>) */ 
/*ajouter une slide provisoire et la rendre active*/
      var div_provisoire = document.createElement("div");
      div_provisoire.className="carousel-item active";
      div_provisoire.id="supprimer";



      var div_loader = document.createElement("div");
      div_loader.className = "carousel-caption d-none d-md-block";

      var text2 = $(div_loader)
      text2.html('<div id="loader"></div>')

      div_provisoire.append(div_loader)
      document.querySelector('.active').classList.remove('active')
      $(".carousel-inner").prepend(div_provisoire)
















      var div_reponse = document.createElement("div");
      div_reponse.className="carousel-item active";
      position_slide_carousel++;
      div_reponse.id = position_slide_carousel;
  
      var wiki_requete = $.get("/wikiRequest/" + $("#query").val());
      wiki_requete.done(function(data){
        /* creer une balise et la remplie avec les info envoyé en ajax */

        var div_carousel = document.createElement("div");
        div_carousel.className = "carousel-caption d-none d-md-block";

        var text2 = $(div_carousel)
        text2.html("<h3 class='display-4'>" + data["title"] + "</h3><p class='lead'>" + data["resume"] + "</p>") 

       
        div_reponse.append(div_carousel)
        /*enlever l'element du carousel qui a deja la classe active
        document.querySelector('.active').classList.remove('active')*/

        $(".carousel-inner").prepend(div_reponse)

      
        var div_carte = document.createElement("div");
        var id = new Date().getTime();
        div_carte.id = id;
        div_carousel.prepend(div_carte);
        
        div_carte.style.width= "100%";
        div_carte.style.height = "400px";

        var carte = {lat:  data["latitude"], lng:  data["longitude"]};
        var map = new google.maps.Map(
          div_carte, {zoom: 4, center: carte}
        );
        var marker = new google.maps.Marker({position: carte, map: map});
      });
      console.log("ok");
      document.querySelector('.carousel-item:first-child').classList.add('active')
      document.querySelector('#supprimer').remove()

      return false;
  });
});

/* rajouter durant le chargement d'une slide une icone de chargement*/
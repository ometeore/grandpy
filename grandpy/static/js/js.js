$(function () {

    "use strict";

    $("#search").click(function(){
      console.log("ok");
      var wiki_requete = $.get("/wikiRequest/" + $("#query").val());
      wiki_requete.done(function(data){


        var section_reponse = document.createElement("div");
        section_reponse.className="ligne_align section";

        var div_text = document.createElement("div");
        div_text.className="margin_30";

        var div_carte = document.createElement("div");
        var text2 = $(div_text)
        text2.html("<p class='titre_wiki'>" + data["title"] + "</p><p class='contenu_wiki'>" + data["resume"] + "</p>") 

        var balise = document.createElement("img");
        balise.src = data["image"];
        balise.className="photo_lieu";

        var div_image = document.createElement("div");
        div_image.className="margin_30";
        div_image.append(balise)

        section_reponse.append(div_image, div_text)
        $("#main").prepend(section_reponse)
      
        var div_carte = document.createElement("div");
        div_carte.id = "map";
        div_image.append(div_carte);

        var carte = {lat:  data["latitude"], lng:  data["longitude"]};
        var map = new google.maps.Map(
          document.getElementById('map'), {zoom: 4, center: carte}
        );
        var marker = new google.maps.Marker({position: carte, map: map});
      
      });


      
  });
});

/**************************************************************************************** */

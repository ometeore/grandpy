$(function () {

    "use strict";

    $("#search").click(function(){
      var wiki_requete = $.get("/wikiRequest/" + $("#query").val());
      wiki_requete.done(function(data){
        $("#titre_wiki").html(data["title"]);
        $("#contenu_wiki").html(data["resume"]);
        $("#image").html(data["image"]);
      });
      
  });
});

/**************************************************************************************** */

/*function initMap(dico) {
  var uluru = {lat: dico[lat], lng: dico [lng]};
  var map = new google.maps.Map(document.getElementById('map'));
}


    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
    </script>
*/
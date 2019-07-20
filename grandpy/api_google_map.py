from grandpy.key import key
import requests, imghdr

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

class Ggmap:
    """gère l'interaction avec google map"""

    def __init__(self, query):
        self.info_recherche = {"key":key, "query":query}
        self.requete_resultat = requests.get(search_url, params=self.info_recherche)
        
        self.resultat_json = self.requete_resultat.json()

        self.photo_id = self.resultat_json["results"][0]["photos"][0]["photo_reference"]
        self.latitude = self.resultat_json["results"][0]["geometry"]["location"]["lat"]
        self.longitude = self.resultat_json["results"][0]["geometry"]["location"]["lng"]

        self.photo_payload = {"key" : key, "maxwidth" : 500, "photoreference" : self.photo_id}
        self.photo_request = "https://maps.googleapis.com/maps/api/place/photo?" + "key=" + key + "&maxwidth=500&photoreference=" + self.photo_id
        self.map_reference = "https://maps.googleapis.com/maps/api/js?key="+ key +"&callback=initMap"


    def resultat(self):
        resultat=[self.photo_request, self.map_reference]
        print (resultat)
        return resultat
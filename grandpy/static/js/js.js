$(function () {
    
    /***ty stackoverflow where they are the real heroes***/
    "use strict";
        
    //comentaire pour le bouton label les autres sont construit de manière analogue
    $('#req1').on("click", function () {
       
        //Désactive les boutons
        $('#req2').prop("disabled", true);
        $('#req3').prop("disabled", true);
        
        // ajout dans la bande de droite d'une phraase (span) et d'un texte (input) et des trois boutons ( id -> ack1 ak1 ac1) apparition fondue (fadeIn)
        $('#droite').append('<div id="tect1"><hr><span>Texte du label: </span><input type="text" id="rep1"><button id="ack1" class="shadow"> ok </button><br><button id="ak1"> clean </button><button id="ac1">annuler</button></div>').hide().fadeIn(2000);
       
        //bouton annuler (revenir au choix des boutons id->ac1)
        $('#ac1').on('click', function (){
            $('#req2').prop("disabled", false);
            $('#req3').prop("disabled", false);
            $('#tect1').fadeOut(2000, function () {
                $(this).remove();
            });
        });
        
        //efface l'intérieur de l'input (bouton clean id ->ak1)
        $('#ak1').on('click', function () {
            $('#rep1').val('');
        });
        
        //envoie de l'intérier de l'input dans la partie gauche (id->ack1)
        $('#ack1').on('click', function () {
            $('#gauche').append('<span>' + $('#rep1').val() + '</span>');
            $('#req2').prop("disabled", false);
            $('#req3').prop("disabled", false);
                $('#tect1').fadeOut(2000, function () {
                    $(this).remove();
                });
        });
        

    });

    $('#req2').on("click", function () {
        $('#req1').prop("disabled", true);
        $('#req3').prop("disabled", true);
        $('#droite').append('<div id="tect2"><hr><span>Zone de texte: </span><input type="text" id="rep2"><button class="shadow" id="ack2"> ok </button> <br><button id="ak2"> clean </button><button id="ac2"> annuler </button></div>').hide().fadeIn(2000);
        $('#ak2').on('click', function() {
            $('#rep2').val('');
        });
        $('#ac2').on('click', function (){
            $('#req1').prop("disabled", false);
            $('#req3').prop("disabled", false);
            $('#tect2').fadeOut(2000, function () {
                    $(this).remove();
        });
        });
        $('#ack2').on('click', function () {
            $('#req1').prop("disabled", false);
            $('#req3').prop("disabled", false);
            $('#gauche').append('<input type="text" id="' + $('#rep2').val() + '">');
            $('#tect2').fadeOut(2000, function () {
                $('#tect2').remove();
            });
        });
    });
    
    $('#req3').on("click", function () {
        $('#req1').prop("disabled", true);
        $('#req2').prop("disabled", true);
        $('#droite').append('<div id="tect0"><hr><span>Texte du bouton: </span><input type="text" id="rep0"><button id="ack0" class="shadow"> ok </button><button id="ak0"> clean </button><button id="ac0"> annuler </button></div>');
        $('#ac0').on('click', function (){
            $('#tect0').fadeOut(2000, function () {
                $('#req1').prop("disabled", false);
                $('#req2').prop("disabled", false);
                $(this).remove();
            });
        });
        $('#ak0').on('click', function () {
            $('#rep0').val('');
        });
        $('#ack0').on('click', function () {
            $('#req1').prop("disabled", false);
            $('#req2').prop("disabled", false);
            $('#gauche').append('<br><button>' + $('#rep0').val() + '</button>');
            $('#tect0').fadeOut(2000, function () {
                $('#tect0').remove();
            });
        });
    });
});
var host = window.location.hostname == 'localhost'
? 'http://localhost:8000/'
: 'http://' + window.location.hostname + '/';

var user_id = "";
user_id = document.getElementById('id').innerHTML;

console.log(user_id)

setTimeout(() => {
    

var pos = [];
function initialize() {

    var myLatLng = new google.maps.LatLng( 6.6577124, 6.3185216 ),
        myOptions = {
            zoom: 12,
            center: myLatLng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
            },
        map = new google.maps.Map( document.getElementById( 'profile-canvas' ), myOptions ),
        marker = new google.maps.Marker( {position: myLatLng, map: map} );

    marker.setMap( map );
    setInterval(() => {
        recheck();
        // console.log(pos)
        moveBus(map, marker, pos);

    }, 1000);
    // moveBus( map, marker );

}

function moveBus( map, marker, position ) {
    // console.log(position);
    marker.setPosition( new google.maps.LatLng( position[0], position[1] ) );
    map.panTo( new google.maps.LatLng( position[0], position[1] ) );

};

initialize();
    
    
var numDeltas = 100;
var delay = 10; //milliseconds
var i = 0;
var deltaLat;
var deltaLng;

function transition(result){
    latlng = new google.maps.LatLng(result[0], result[1])
    i = 0;
    x +=0.01;
    deltaLat = (result[0] - position[0])/numDeltas;
    deltaLng = (result[1] - position[1])/numDeltas;
    moveMarker();
}

function moveMarker(){
    position[0] += deltaLat;
    position[1] += deltaLng;

    marker.setTitle("Latitude:"+position[0]+" | Longitude:"+position[1]);

    marker.setPosition(latlng);

    if(i!=numDeltas){
        i++;
        setTimeout(moveMarker, delay);
    }
}


function recheck(){
    let position = [];
    $.ajax({
                
        type: "GET",
        url: `${host}get_lat_lng/${user_id}`,
            async: true,
        success: function(res) {
            result = JSON.parse(res);
            console.log([result.lat,  result.lng]);
            pos = [result.lat,  result.lng];
            // let pos = [result.fields.lat,  result.fields.lng];
            
        },
        error: function(){
        console.log("connection probs")
        }
    });
    
};

}, 1000);
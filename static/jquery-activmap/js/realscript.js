// host = 'http://localhost:8000/';
var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/';

var position = [6.6577124, 6.3185216];
var x = 0;
var lineCoordinates = [];
var addresses = [];
const slug = document.getElementById("slug").value;

 var promise = $.getJSON(host + "check/" + slug);

 promise.done(function(res) {
    result = res
    console.log(result[result.length-1].fields.lat)
    pos = [result[result.length - 1].fields.lat,  result[result.length - 1].fields.lng]
    var latlng = new google.maps.LatLng(position[0],position[1]);
    let myOptions = {
        zoom: 18,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    trail_map = new google.maps.Map(document.getElementById("activmap-canvas"), myOptions);
    marker = new google.maps.Marker({
        position: latlng,
        map: trail_map,
        title: "POSITION"
    });


    setInterval(() => {
        $.ajax({
             
             type: "GET",
             url: host + "check/"+ slug,
                   async: true,
             success: function(res) {
                 result = (JSON.parse(res))
                //  console.log((result))
    
                 pos = [result[result.length - 1].fields.lat,  result[result.length - 1].fields.lng]
                 transition(pos);
                 
                 if (result[result.length - 1].fields.action == "ok"){
                     alert("Panic Resolved");
                     window.location.replace(host);
                 }
             },
             error: function(){
                alert("connection probs")
             }
         })
    }, 3000); 
         
         
     
    
        google.maps.event.addListener(trail_map, 'click', function(event) {
             // position[0] = position[0] + 0.0001;
             // position[1] = position[1] + 0.0001;
             // transition(position);
             x=1
         });
     
     
    //  //Load google map
    //  google.maps.event.addDomListener(window, 'load', initialize);




    
 
})


 
 
 var numDeltas = 100;
 var delay = 10; //milliseconds
 var i = 0;
 var deltaLat;
 var deltaLng;
 
 function transition(result){
     latlng = new google.maps.LatLng(result[0], result[1])
     console.log(result)
     trail_map.setCenter(latlng);
     //   console.log(lineCoordinates);
       i = 0;
       x +=0.01;
       deltaLat = (result[0] - position[0])/numDeltas;
       deltaLng = (result[1] - position[1])/numDeltas;
       moveMarker();
 }
 
 function moveMarker(){
     // console.log(position)
     position[0] += deltaLat;
     position[1] += deltaLng;
     var latlng = new google.maps.LatLng(position[0], position[1]);
     marker.setTitle("Latitude:"+position[0]+" | Longitude:"+position[1]);
     marker.setPosition(latlng);
     if(i!=numDeltas){
         i++;
         setTimeout(moveMarker, delay);
     }
 }





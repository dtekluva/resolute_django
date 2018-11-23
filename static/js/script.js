host = 'http://localhost:8000/'
 var position = [6.6577124, 6.3185216];
 var x = 0;
 var lineCoordinates = [];
 function startmap(position){
    // clearInterval(monitorcustomers)
    function initialize() { 
        var latlng = new google.maps.LatLng(position[0], position[1]);
        var myOptions = {
            zoom: 16,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById("mapCanvas"), myOptions);
    
        marker = new google.maps.Marker({
            position: latlng,
            map: map,
            title: "Latitude:"+position[0]+" | Longitude:"+position[1]
        });

   setInterval(() => {
       $.ajax({
            
            type: "GET",
            url: host + "check",
                  async: true,
            success: function(res) {
                result = (JSON.parse(res))
                console.log((result))

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
        
        
    

       google.maps.event.addListener(map, 'click', function(event) {
            // position[0] = position[0] + 0.0001;
            // position[1] = position[1] + 0.0001;
            // transition(position);
            x=1
        });
    }
    
    //Load google map
    google.maps.event.addDomListener(window, 'load', initialize);
    
    
    var numDeltas = 100;
    var delay = 10; //milliseconds
    var i = 0;
    var deltaLat;
    var deltaLng;
    
    function transition(result){
        latlng = new google.maps.LatLng(result[0], result[1])
        map.setCenter(latlng);
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

}
$.ajax({
            
    type: "GET",
    url: `${host}check`,
          async: true,
    success: function(res) {
        result = JSON.parse(res)
        pos = [result[result.length - 1].fields.lat,  result[result.length - 1].fields.lng]
        
        startmap(pos);
            result.forEach(element => { 
        });
    },
    error: function(){
       alert("connection probs")
    }
})

var load_trail = (()=>{
    $.ajax({
            
        type: "GET",
        url: `${host}check`,
              async: true,
        success: function(res) {
            result = JSON.parse(res)
            pos = [result[result.length - 1].fields.lat,  result[result.length - 1].fields.lng]
            var latlng = new google.maps.LatLng(pos[0],pos[1]);
            let myOptions = {
                zoom: 16,
                center: latlng,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            trail_map = new google.maps.Map(document.getElementById("mapCanvas1"), myOptions);
            var color = '#fd7d14e5'
            result.forEach(element => {
                // console.log(lineCoordinates.length)
                lineCoordinates.push({"lat":element.fields.lat, "lng":element.fields.lng})
                let old_location = lineCoordinates[lineCoordinates.length-1]

                var image = { //MAPS MARKER CUSTOMIZED
                    url: 'http://www.ssglobalsupply.com/images/location-contact.png',
                    // This marker is 50 pixels wide by 50 pixels high.
                    size: new google.maps.Size(20, 20),
                    // The origin for this image is (0, 0).
                    origin: new google.maps.Point(0, 0),
                    // The anchor for this image is the base of the flagpole at (0, 32).
                    anchor: new google.maps.Point(0, 32)
                  };
                  alert("corect script")
                if (lineCoordinates.length !== 0 && element.model == "main.location") {
                        color = '#fd7d14e5'
                        if (dist_is_far(old_location.lng, old_location.lat, element.fields.lat, element.fields.lng )){ //check distance change to make sure for long range travel
                            
                            lineCoordinates.push({"lat":element.fields.lat, "lng":element.fields.lng})//add values to array for drawing of trail  lines
                            
                            latlng = new google.maps.LatLng(element.fields.lat,element.fields.lng);
                            _time = (new Date(element.fields.date));

                            new google.maps.Marker({
                                position: latlng,
                                map: trail_map,
                                title:  element.fields.address + ` - @${String(_time)}`,
                                icon :  'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';

                            });
                        }   
                    } else{
                        color = '#ff0000';
                    }
                });
                var linePath = new google.maps.Polyline({
                    path: lineCoordinates,
                    geodesic: false,
                    strokeColor: color
                });

            linePath.setMap(trail_map);

        },
        error: function(){
           alert("connection probs")
        }
    })
})
load_trail();

function dist_is_far(old_lng, new_lng, old_lat, new_lat){ // calculate distance to make sure to only display long range travel on map

    a =  old_lat - new_lat //lat difference as opposite
    b =  old_lng - new_lng //lng difference as adjacent
    c = Math.pow(a, 2) + Math.pow(b, 2) //hypothenus as distance between two points

    c = Math.sqrt(c)

    if (c <= 0.001){
        console.log(c)
        return true
    }
    else{
        return false
    }
        
}
// host = 'http://localhost:8000/';
var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/';

var position = [6.6577124, 11.3185216];
var x = 0;
var lineCoordinates = [];
var addresses = [];
var latlng;
var old_lat_lng = false;

window.onload = ()=>{
    const user_id = document.getElementById("id").innerHTML;
    const username = document.getElementById("username").innerHTML;
    const incident_id = document.getElementById("incident_id").innerHTML;

    setTimeout(() => {

    var promise = $.getJSON(host + "get_lat_lng/" + user_id);
    var promise_for_old_trail = $.getJSON(host + "get_latlng_incident/" + username + "/"+ incident_id);

    promise.done(function(res) {
        result = res

        pos = [result.lat,  result.lng]
        latlng = new google.maps.LatLng(pos[0],pos[1]);
        let myOptions = {
            zoom: 16,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        trail_map = new google.maps.Map(document.getElementById("profile-canvas"), myOptions);
    
            }).then( (result)=>{

                create_trail(latlng);

            }).then(()=>{
                promise_for_old_trail.done((result)=>{
                    draw_Old_Line_Path(result);

                });
    
            });


    var create_trail = ( (latlng)=>{

                markers = new google.maps.Marker({
                                        position: latlng,
                                        map: trail_map,
                                        animation: google.maps.Animation.DROP
                                    });
                
            setInterval(() => {
                $.getJSON(host + "get_lat_lng/" + user_id).done((res)=>{
                    result = res
                    pos = [result.lat,  result.lng]
                    latlng = new google.maps.LatLng(pos[0],pos[1]);
                    markers.setPosition( latlng );

                    setTimeout(()=>{
                        if (old_lat_lng){
                            
                            create_linepath(old_lat_lng, latlng, trail_map)
                        }
                        old_lat_lng = latlng;
                    },0.5)
                });
            }, 1000);
    });



    var create_linepath = ( (old_lat_lng, latlng, trail_map)=>{

        var color = "#6610f2";

        for (let index = 0; index < 2; index++) {

            let Polyline = [old_lat_lng,latlng];
          
            var linePath = new google.maps.Polyline({
                path: Polyline,
                strokeColor: color,
                strokeOpacity: 1.0,
                strokeWeight: 4,
                geodesic: true
                });
            
            linePath.setMap(trail_map);

                            
        }


    });

    var draw_Old_Line_Path = ((result)=>{

        // console.log(result)
        let old_lat_lng = new google.maps.LatLng(result.data.start_latlng[0], result.data.start_latlng[1]);
        console.log(result)
        result.data.user_positions.forEach((element)=>{
            if (true) {

                latlng = new google.maps.LatLng(element[0], element[1]);

                create_linepath(old_lat_lng, latlng, trail_map);
                // console.log(latlng)

                old_lat_lng = latlng;

            }
        })
    })

    function dist_is_far(old_lng, new_lng, old_lat, new_lat){ // calculate distance to make sure to only display long range travel on map

        a =  old_lat - new_lat //lat difference as opposite
        b =  old_lng - new_lng //lng difference as adjacent
        // console.log(a,b)
        c = Math.pow(a, 2) + Math.pow(b, 2) //hypothenus as distance between two points
        // console.log(c)

        c = Math.sqrt(c)
        console.log(c)
        if (c >= 0.0004){
            
            return true
        }
        else{
            return false
        }
            
    }


    function toggleBounce(e) {
        console.log(e)
        if (marker.getAnimation() !== null) {
        marker.setAnimation(null);
        } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
        }
    }

    }, 2000);
};




var load_trail = ((element)=>{

lineCoordinates.push({"lat":element.fields.lat, "lng":element.fields.lng})//add values to array for drawing of trail  lines
                
                latlng = new google.maps.LatLng(element.fields.lat,element.fields.lng);
                _time = (new Date(element.fields.date));

                markers[count] = new google.maps.Marker({
                        position: latlng,
                        map: trail_map,
                        animation: google.maps.Animation.DROP,
                        title:  element.fields.address + ` - @${String(_time)}`
                    });
                markers[count].addListener('click', (e)=>{
                    toggleBounce(e)
                });
                
        

    linePath.setMap(trail_map);
    });




      
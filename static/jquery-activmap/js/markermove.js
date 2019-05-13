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

 var promise = $.getJSON(host + "get_lat_lng/" + user_id);

 promise.done(function(res) {
    result = res
    console.log(result)
    console.log(user_id)
    pos = [result.lat,  result.lng]
    latlng = new google.maps.LatLng(pos[0],pos[1]);
    let myOptions = {
        zoom: 16,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    trail_map = new google.maps.Map(document.getElementById("profile-canvas"), myOptions);
        // console.log(document.getElementById("slug"))
 
           }).then( (result)=>{
            create_trail(latlng);
           }).then(()=>{
            
 
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
                // trail_map.panTo(latlng );
                console.log(old_lat_lng)
                setTimeout(()=>{
                    if (old_lat_lng){
                        
                        create_linepath(old_lat_lng, latlng, trail_map)
                    }
                    old_lat_lng = latlng;
                },0.5)
            });
        }, 2000);
});



var create_linepath = ( (old_lat_lng, latlng, trail_map)=>{

    var color = "#6610f2";

    for (let index = 0; index < 2; index++) {

        let Polyline = [old_lat_lng,latlng];
        // let Polyline = [lineCoordinates[index],lineCoordinates[index+1]];

        // if (dist_is_far(Polyline[1].lng, Polyline[0].lng, Polyline[1].lat, Polyline[0].lat)){
        // if (true){
        //      color = "#5eb314";
            
        // }else{
        //      color = "#e65252";

        // }
        var linePath = new google.maps.Polyline({
            path: Polyline,
            strokeColor: color,
            strokeOpacity: 1.0,
            strokeWeight: 4,
            geodesic: true
            // icons: [{
            //     icon: {path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW},
            //     offset: '100%'
            // }]
            });
        
        linePath.setMap(trail_map);

                           
    }


});

var prepareLinePath = ((result)=>{
    result.forEach((element)=>{
        if ( element.model == "main.location" && element.fields.lat != 0 && element.fields.lng != 0) {
            lineCoordinates.push({"lat":element.fields.lat, "lng":element.fields.lng});
            addresses.push( element.fields.address);
        }
    })
})

function dist_is_far(old_lng, new_lng, old_lat, new_lat){ // calculate distance to make sure to only display long range travel on map
    // console.log(old_lng, new_lng, old_lat, new_lat)

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
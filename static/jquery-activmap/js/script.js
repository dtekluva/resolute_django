// host = 'http://localhost:8000/';
var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/';

var position = [6.6577124, 6.3185216];
var x = 0;
var lineCoordinates = [];
var addresses = [];
const slug = document.getElementById("slug").value;
console.log(slug);

 var promise = $.getJSON(host + "check/" + slug);

 promise.done(function(res) {
    result = res
    pos = [result[result.length - 1].fields.lat,  result[result.length - 1].fields.lng]
    var latlng = new google.maps.LatLng(pos[0],pos[1]);
    let myOptions = {
        zoom: 19,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    trail_map = new google.maps.Map(document.getElementById("activmap-canvas"), myOptions);
        // console.log(document.getElementById("slug"))
 
           }).then( (result)=>{
            prepareLinePath(result);
            create_trail(lineCoordinates);
           }).then(()=>{
            
 
           });



var prepareLinePath = ((result)=>{
    result.forEach((element)=>{
        if ( element.model == "main.location") {
            lineCoordinates.push({"lat":element.fields.lat, "lng":element.fields.lng});
            addresses.push( element.fields.address);
        }
    })
})

var create_trail = ( (lineCoordinates)=>{

    var color = "#6610f2";
    console.log(lineCoordinates)
    for (let index = 0; index < lineCoordinates.length-1; index++) {

        let Polyline = [lineCoordinates[index],lineCoordinates[index+1]];

        if (dist_is_far(Polyline[1].lng, Polyline[0].lng, Polyline[1].lat, Polyline[0].lat)){
             color = "#5eb314";
            
        }else{
             color = "#e65252";

        }
                var linePath = new google.maps.Polyline({
                    path: Polyline,
                    strokeColor: color,
                    strokeOpacity: 1.0,
                    strokeWeight: 3,
                    geodesic: true,
                    icons: [{
                        icon: {path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW},
                        offset: '100%'
                    }]
                 });
                
                linePath.setMap(trail_map);
    }


});



var load_trail = ((result)=>{

                push({"lat":element.fields.lat, "lng":element.fields.lng})//add values to array for drawing of trail  lines
                            
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


// locations_from_server = [{ "model": "main.location", "pk": 27, "fields": { "customer": 1, "lng": 3.316564, "lat": 6.657832, "address": "xxxxxxx", "date": "2018-10-28T22:00:20.863Z" } }, { "model": "main.location", "pk": 28, "fields": { "customer": 1, "lng": 3.316564, "lat": 6.657832, "address": "xxxxxxx", "date": "2018-10-28T22:09:07.078Z" } }, { "model": "main.location", "pk": 29, "fields": { "customer": 1, "lng": 3.31725, "lat": 6.657805, "address": "xxxxxxx", "date": "2018-10-28T22:09:18.547Z" } }, { "model": "main.location", "pk": 30, "fields": { "customer": 1, "lng": 3.31805, "lat": 6.657742, "address": "xxxxxxx", "date": "2018-10-28T22:09:31.477Z" } }, { "model": "main.location", "pk": 31, "fields": { "customer": 1, "lng": 3.318559, "lat": 6.65772, "address": "xxxxxxx", "date": "2018-10-28T22:09:49.035Z" } }, { "model": "main.location", "pk": 32, "fields": { "customer": 1, "lng": 3.318586, "lat": 6.658093, "address": "xxxxxxx", "date": "2018-10-28T22:10:04.372Z" } }, { "model": "main.location", "pk": 33, "fields": { "customer": 1, "lng": 3.318634, "lat": 6.658498, "address": "xxxxxxx", "date": "2018-10-28T22:10:19.810Z" } }, { "model": "main.location", "pk": 34, "fields": { "customer": 1, "lng": 3.31867, "lat": 6.658797, "address": "xxxxxxx", "date": "2018-10-29T14:35:19.486Z" } }, { "model": "main.location", "pk": 35, "fields": { "customer": 1, "lng": 3.318727, "lat": 6.659341, "address": "Seyinsola Coker St, Ifako-Ijaiye, Lagos", "date": "2018-10-29T14:37:30.773Z" } }, { "model": "main.location", "pk": 36, "fields": { "customer": 1, "lng": 3.318753, "lat": 6.659623, "address": "Seyinsola Coker St, Ifako-Ijaiye, Lagos", "date": "2018-10-29T17:08:03.805Z" } }, { "model": "main.location", "pk": 37, "fields": { "customer": 1, "lng": 3.31915, "lat": 6.659554, "address": "Seyinsola Coker St, Ifako-Ijaiye, Lagos", "date": "2018-10-29T17:09:13.183Z" } }, { "model": "main.location", "pk": 38, "fields": { "customer": 1, "lng": 3.319382, "lat": 6.659497, "address": "Seyinsola Coker St, Ifako-Ijaiye, Lagos", "date": "2018-10-29T17:11:48.999Z" } }, { "model": "main.customer", "pk": 1, "fields": { "name": "inyang", "surname": "kpongette", "userid": 1, "lng": 3.319382, "lat": 6.659497, "slug": "inyang", "address": "Seyinsola Coker St, Ifako-Ijaiye, Lagos", "panicked": "2018-10-29", "is_panicking": true, "date": "2018-04-18" } }]
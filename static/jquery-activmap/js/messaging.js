// host = 'http://localhost:8000/';
var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/';

$(function(){
    $('.fa-minus').click(function(){    $(this).closest('.chatbox').toggleClass('chatbox-min');
    });
    $('.fa-close').click(function(){
        $(this).closest('.chatbox').hide();
    });
    });

window.onload = ()=>{
    
    
        
    setTimeout(() => {

    var promise = $.getJSON(host + "get_lat_lng/" + user_id);

    promise.done(function(res) {
        
            }).then( (result)=>{

                
            }).then(()=>{
                

                });
    
            });
};
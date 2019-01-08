var host = window.location.hostname == 'localhost'
? 'http://localhost:8000/'
: 'http://' + window.location.hostname + '/';

setInterval(() => {
check_for_panick()
}, 4000);

var has_been_shown = true;
var farm_cached = [];
var herd_cached = [];
var audio = new Audio(`${host}static/sounds/plucky.mp3`);


function check_for_panick(){
var promise = $.getJSON(host + "check_panic");

promise.done(function(res) {
    result = res
    console.log(res);
    
    res.forEach(element => {
        // console.log(element);
        has_been_shown = true;

        if (element.model == "main.farmland"){
            // console.log(!farm_cached.includes(element.pk));
            if (!farm_cached.includes(element.pk)){
                data = {type: 'farmer', name: element.fields.full_name, state: element.fields.community};
                farm_cached.push(element.pk)
                has_been_shown = false;
            };
            
        }else if (element.model == "main.herdsman"){

            if (!herd_cached.includes(element.pk)){
                // console.log(!herd_cached.includes(element.pk));
                data = {type: 'herdsman', name: element.fields.name, state: element.fields.state}
                herd_cached.push(element.pk)
                has_been_shown = false;
            };
        }

        if (!has_been_shown) show_alert(data);
        localStorage.setItem('farm_data', farm_cached)
        localStorage.setItem('herd_data', herd_cached)
    });
  }).then(()=>{

  });
}

function show_alert(data){
    // console.log(data);
    audio.play();
    let promise = new Promise(function(resolve, reject) {
        $.notify((`New ${data.type} distress:  ${data.name} sent in a distress from ${data.state}`).toUpperCase(), options);
        resolve(
            'Done'
        );
    });

    promise.then(
    result =>{

        let target = document.querySelectorAll('div.notifyjs-bootstrap-base');
        console.log(target);
        target.forEach(element => {
            
            element.onclick = e =>{
                console.log(e.target.innerHTML);
                e.preventDefault();    
                
            }
        });
    },
    error => alert(error) // doesn't run
    );
}

const options = {
    // whether to hide the notification on click
    clickToHide: true,
    // whether to auto-hide the notification
    autoHide: false,
    // if autoHide, hide after milliseconds
    autoHideDelay: 5000,
    // show the arrow pointing at the element
    style: 'bootstrap',
    // default class (string or [string])
    className: 'warn',
    // show animation duration
    showDuration: 300,
    // hide animation
    hideAnimation: 'slideUp',
    // hide animation duration
    hideDuration: 200,
    // padding between element and notification
    };
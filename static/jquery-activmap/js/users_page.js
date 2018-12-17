// host = 'http://localhost:8000/';
var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/';

var last_id = 0;
 //SCRIPT CONTROLLING USER PAGE TO SHOW OR HIDE THE ADD USER FORM

function show_form(event){
    form = document.querySelector('#target_form');

    // SHOW THE FORM
    form.removeAttribute('hidden');
    get_users();
    
    // HIDE THE DATATABLE LIST
    $('.reg_users').hide();
    
}

function hide_form(event){
    
    form = document.querySelector('#target_form');
    form.setAttribute('hidden', true);
    get_users();

    // SHOW THE DATATABLE LIST
    $('.reg_users').show();
}

          
//UPDATE USER LIST DATA-TABLE

function get_users(){
    var promise = $.getJSON(host + "auth/get_users");
    
    promise.done(function(res) {
        result = res

        if (res[0].id != last_id){

            res.forEach(element => {

                $(document).ready(function() {
                    let t = $('#example').DataTable();
                 
                        t.row.add( [
                            element.id,
                            titleCase(element.first_name) ,
                            titleCase(element.last_name),
                            element.email,
                            element.phone,
                            titleCase(element.agency),
                        ] ).draw( false );
                        
                } );
        
                
            });
        }
      })
    }

// GET THE LAST ID SO AS NOT TO POST DOUBLE DATA

var promise = $.getJSON(host + "auth/get_users");

promise.done(function(res) {
    last_id = res[0].id
    });


// TITLE CASE
function titleCase(str) {
    return str.toLowerCase().split(' ').map(function(word) {
      return word.replace(word[0], word[0].toUpperCase());
    }).join(' ');
  }
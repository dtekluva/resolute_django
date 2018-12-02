'use strict'
// var host ="http://localhost:8000/";
var host = window.location.hostname == 'localhost'
    ? 'http://localhost:8000/'
    : 'http://' + window.location.hostname + '/'

    
$('#add_form').on('submit', async e => {
    e.preventDefault()
    let data = $('#add_form') // add lives_in select value to post data
    console.log(data)
    swal({
      title: "Are you sure?",
      text: `${data[0][1].value} ${data[0][2].value}, from ${(data[0][5].value).toUpperCase()} will be granted login access to this dashboard!`,
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willDelete) => {
      if (willDelete) {
        
        // POST DATA IF USER CLICKS YES
        post();
      } else {
        swal(`Post Cancelled !!!`);
      }
    });



// FUNCTION TO POST NOW HANDLED BY SWAL FROM SWEET ALERT
    const post = ()=>{
      let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
      let page = 'create_user'
    
      let form_data = `${$('#add_form').serialize()}` // add lives_in select value to post data
    
      function csrfSafeMethod (method) {
            // these HTTP methods do not require CSRF protection
        return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method)
      }
    
      $.ajaxSetup({
        beforeSend: function (xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken)
          }
        }
      })
    
      $.post(host + 'auth/'+ page , form_data)
            .then(resp => {
              console.log(JSON.parse(resp))
              resp = JSON.parse(resp)
    
              if (resp.response == 'success') {
                swal({
                  title: "Successful",
                  text : `${data[0][1].value} ${data[0][2].value} granted access.!!!`,
                  icon: "success",
                });
              } else if (resp.response == 'fail') {
                swal({
                  title: "Possible Duplicate error",
                  text: `User with similar record possibly exists. Please confirm`,
                  icon: "error",
                });
              }
            })
            .catch(() => {
              swal( {
                title: "Network Error",
                text: `Please check your internet connection.!!`,
                icon: "error",
              });
            }) // post data


    }
    
    
  })
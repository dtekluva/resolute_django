function make_alert(event, incident_id) {

    let csrftoken = $('[name="csrfmiddlewaretoken"]')[0].value
    // let user_id = $('[name="user_id"]')[0].value
    // let lives_in = $('#lives_in')[0].value
    // let is_active = $('#is_active')[0].checked
  console.log(event);
  
  //  CREATE POST DATA JSON FORMAT 
  
  let data = JSON.stringify({	
              "data": {
                "incident_id": incident_id,
                "panic_status": "False"
              },
              "user_type": "farmer"
            });

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
    $.post(host + 'resolve_panic', data)
          .then(resp => {
            console.log(JSON.parse(resp))
            resp = JSON.parse(resp)
  
            if (resp.response == 'success') {
              $('.bd-example-modal-sm').modal('show')
            } else {
              $('.bd-example-modal-sm-fail').modal('show')
            }
          })
          .catch(() => {
            $('.bd-example-modal-sm-fail').modal('show')
          }) // post data
    }
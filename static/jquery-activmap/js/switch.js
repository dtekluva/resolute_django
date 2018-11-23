panick_list_div = document.getElementsByClassName('panick')[0]
okaydiv = document.getElementsByClassName('okaywrap')[0]

host = 'http://localhost:8000/'
x = '{ "name":"John", "age":30, "city":"0.215587, 52.325658"}'

//<------------- get data of new position from server----->
setInterval(() => {
        $.ajax({
            type: "GET",
            url: host + "check",
                async: true,
            success: function(res) {
                result = JSON.parse(res)
                console.log(result)

                result = result[result.length - 1].fields

                if (result.is_panicking) {
                    // console.log(result.lat, "---" , result.lng);

                    panick_list_div.style.display = "";
                    panick_list_div.innerHTML = ` <div class="">
                    <div class="balance">
                      <div class="balance-title">
                        <h4  style= "color: brown;">Customer : ${result.surname} ${result.name}</h4>
                      </div>
                      <div class="balance-value">
                        Location : ${result.location}
                      </div>
                      <div class="balance-value">
                        Coordinates : ${result.lat}, ${result.lng}
                      </div>
                      <div class="balance-link">
                        <a class="btn btn-link btn-underlined" href="/track"><span>Start tracking</span><i class="os-icon os-icon-arrow-right4"></i></a>
                      </div>
                    </div>
                    
                  </div>
                  <hr>`;
                    okaydiv.style.display = "none";
                    pos = [result.lat,  result.lng]
                   
                } else{
                    console.log(result.status)
                }
            },
            error: function(){
            alert("something went wrong")
            }
        })
    }, 5000);
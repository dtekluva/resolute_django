mapdiv = document.getElementsByClassName('mapdiv')[0]
okaydiv = document.getElementsByClassName('okaywrap')[0]

host = 'http://localhost:8000/'
x = '{ "name":"John", "age":30, "city":"0.215587, 52.325658"}'

//post data to server like position and address
// $.ajax({
//     type: "POST",
//     url: host + "end",
//     data: JSON.parse( x),
//           async: true,
//     success: function(res) {
//         console.log(res)
//     },
//     error: function(){
//        1
//     }
// })



//<------------- get data of new position from server----->
var monitorcustomers = setTimeout(() => {
        $.ajax({
            type: "GET",
            url: host + "check",
                async: true,
            success: function(res) {
                result = JSON.parse(res)
                
                if (result.status == 1) {
                    console.log(result.lat, "---" , result.lng);
                    mapdiv.style.display = "";
                    okaydiv.style.display = "none";
                    pos = [result.lat,  result.lng]
                    console.log("reached here");
                    startmap(pos);
                    
                    
                } else{
                    console.log(result.status)
                }
            },
            error: function(){
            alert("something went wrong")
            }
        })
    }, 5000);

//init the map
var myMap = new L.Map('map', {
    key: 'web.9b465fd6aff4474584be621d67b6d894',
    maptype: 'dreamy',
    poi: true,
    traffic: false,
    center: [37.55288, 45.076228],
    zoom: 14
});
var help = document.getElementById("help");

var originMarker = ''
var destinationMarker = ''
var resultMatrix = [];
var flag = false;
var markerIsOrigin = true;

var originAddress = ''
var destAddress = ''
var originCity = ''
var destCity = ''
var duration = ''
var distance = ''
var originLoc = []
var destLoc = []

myMap.on('click', async function (e) {
    //is start button is clicked
    if (flag) {
        if (markerIsOrigin) {
            if (originMarker != '') {
                myMap.removeLayer(originMarker);
                originMarker = ''; 
            }
            originMarker = L.marker(e.latlng, {
                title: "orgin",
                icon: L.AwesomeMarkers.icon({
                    icon: '',
                    markerColor: 'darkblue',
                    prefix: 'fa',
                    html: 'مبدا'
                })
            }).addTo(myMap);
            try {
                const res = await getLocation(originMarker);
                originAddress = res[0]
                originCity = res[1]
                document.getElementById("origins").innerHTML =  "<b>مبدا: </b> " + originCity + "-" + originAddress;
            } catch (error) {
                console.error("Error fetching location:", error);
            }
        } else {
            document.getElementById("eta").disabled = false;
            if (destinationMarker != '') {
                myMap.removeLayer(destinationMarker);
                destinationMarker = '';
            }

            destinationMarker = L.marker(e.latlng, {
                title: "Destination",
                icon: L.AwesomeMarkers.icon({
                    icon: '',
                    markerColor: 'darkred',
                    prefix: 'fa',
                    html: 'مقصد'
                })
            }).addTo(myMap);
            try {
                const res = await getLocation(destinationMarker);
                destAddress = res[0]
                destCity = res[1]
                document.getElementById("destinations").innerHTML = "<b>مقصد: </b> " + destCity + "-" + destAddress;
            } catch (error) {
                console.error("Error fetching location:", error);
            }

            try {
                const res = await getDuration()
                duration = res[0]
                distance = res[1]
                document.getElementById("duration").innerHTML = "<b>زمان: </b> " + duration ;
                document.getElementById("distance").innerHTML = "<b>مسافت: </b> " + distance ;
            } catch (error) {
                console.error("Error fetching location:", error);
            }

            finish()
            
        }
    }
});
//restarting the layers
function reset() {
    help.textContent = "لطفا مبدا را انتخاب کنید"
    markerIsOrigin = true;
    document.getElementById("marker").textContent = "مقصد";
    document.getElementById("marker").disabled = false;
    flag = true;
    document.getElementById("start").textContent = "دوباره";
    document.getElementById("origins").textContent = "مبدا";
    document.getElementById("destinations").textContent = "مقصد";
    document.getElementById("result").innerHTML = ""

    myMap.removeLayer(originMarker);
    originMarker = '';

    myMap.removeLayer(destinationMarker);
    destinationMarker = '';


}
//send http get request to distance matrix api
function finish() {
    flag = false;

    document.getElementById('o-ad').value = originAddress
    document.getElementById('d-ad').value = destAddress
    document.getElementById('o-city').value = originCity
    document.getElementById('d-city').value = destCity
    document.getElementById('dur').value = duration
    document.getElementById('dis').value = distance

    // var data = {
    //     "origin_ad": originAddress,
    //     "destination_ad": destAddress,
    //     "origin_city": originCity,
    //     "destination_city": destCity,
    //     "duration": duration,
    //     "distance": distance,
    //     "origin_location": originLoc,
    //     "destination_location": destLoc,
    // }

}

// origin or destination marker
function changeMarker() {
    if (markerIsOrigin) {
        help.textContent = "لطفا مقصد را انتخاب کنید.برای تغییر مبدا دکمه 'مبدا' فشار دهید.";
        document.getElementById("marker").textContent = "مبدا";
        markerIsOrigin = false;
    } else {
        document.getElementById("marker").textContent = "مقصد";
        help.textContent = "لطفا مبدا را انتخاب کنید.برای انتخاب مقصد دکمه 'مقصد' فشار دهید.";
        markerIsOrigin = true;
    }
}

async function getLocation(marker){
    let lat = marker.getLatLng().lat
    let lng = marker.getLatLng().lng

    if(markerIsOrigin){
        originLoc = []
        originLoc.push(lat)
        originLoc.push(lng)
    }else{
        destLoc = []
        destLoc.push(lat)
        destLoc.push(lng)
    }

    var url = `https://api.neshan.org/v5/reverse?lat=${lat}&lng=${lng}`
    
    url = encodeURI(url);
    var params = {
        headers: {
            'Api-Key': 'service.af273ac198a94d8c8b9e9862c895f4de'
        },

    };

    try {
        const response = await axios.get(url, params);
        if (response.data.city == null){return [response.data.formatted_address, response.data.county];}
        else {return [response.data.formatted_address, response.data.city];}
         
    } catch (err) {
        console.error("Error fetching location:", err);
        throw err; 
    }


}

async function getDuration(){
    var url = `https://api.neshan.org/v4/direction?type=car&origin=${originLoc[0]},${originLoc[1]}&destination=${destLoc[0]},${destLoc[1]}&avoidTrafficZone=false&avoidOddEvenZone=false&alternative=false&bearing=0`

    url = encodeURI(url);
    var params = {
        headers: {
            'Api-Key': 'service.611c3f1549e94ae9aad6544b06fbf6d7'
        },

    };

    try {
        const response = await axios.get(url, params);
        return [response.data.routes[0].legs[0].duration.text , response.data.routes[0].legs[0].distance.text]  
    } catch (err) {
        console.error("Error fetching location:", err);
        throw err; 
    }

}

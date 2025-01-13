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
//marker layers

var originMarker = ''
var destinationMarker = ''
var resultMatrix = [];
var flag = false;
var markerIsOrigin = true;
//adding on map click listner
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
                const location = await getLocation(originMarker);
                document.getElementById("origins").innerHTML =  "<b>مبدا: </b> " + location;
            } catch (error) {
                console.error("Error fetching location:", error);
            }
        } else {
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
                const location = await getLocation(destinationMarker);
                document.getElementById("destinations").innerHTML = "<b>مقصد: </b> " + location;
            } catch (error) {
                console.error("Error fetching location:", error);
            }


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
function eta() {
    help.textContent = "برای شروع دوباره گزینه 'دوباره' را فشار دهید."
    document.getElementById("eta").disabled = true;
    flag = false;
    //making the url
    var destination = "";
    var origin = "";

    
}

// origin or destination marker
function changeMarker() {
    if (markerIsOrigin) {
        document.getElementById("eta").disabled = false;
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

    var url = `https://api.neshan.org/v5/reverse?lat=${lat}&lng=${lng}`
    //urlencode the url
    url = encodeURI(url);
    var params = {
        headers: {
            'Api-Key': 'service.af273ac198a94d8c8b9e9862c895f4de'
        },

    };

    try {
        const response = await axios.get(url, params);
        return response.data.formatted_address; 
    } catch (err) {
        console.error("Error fetching location:", err);
        throw err; 
    }



}





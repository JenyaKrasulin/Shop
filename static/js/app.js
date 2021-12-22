function map() {
    var mymap = L.map('mapid').setView([50.020757888009605, 32.983711780001094], 17);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(mymap);

    var marker = L.marker([50.020757888009605, 32.983711780001094]).addTo(mymap);
    marker.bindPopup("<b>Карта!</b><br>Местоположение").openPopup();
    circle.bindPopup("I am a circle.");
    polygon.bindPopup("I am a polygon.");
}


function Check() {
    document.querySelector("#home,#about,#login,#logout,#contacts,#bucket").classList.remove('h-menu__item');
    document.querySelector("#home,#about,#login,#logout,#contacts,#bucket").classList.add('h-menu__item_long');

}


map()

function click_cart(product_id, url) {
    $.ajax({
        url: url, // the endpoint
        type: "GET", // http method
        data: {
            param_first: product_id,
            permission: true
        },
        success:
            function (result) {

                $("#" + product_id).html(result);
            }

    });
    $.ajax({
        url: "get_full_price/", // the endpoint
        type: "GET", // http method
        data: {
            permission: true
        },
        success:
            function (result) {
                $("#full_price").html(result);
            }

    });


};

function add_to_cart(product_id, url) {
    $.ajax({
        url: url, // the endpoint
        type: "GET", // http method
        data: {
            param_first: product_id,
        },
        success:
            function (result) {
                $("#add_to_cart").html(result);
            }
    });
}



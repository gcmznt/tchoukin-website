var addresspickerMap;
var gmap;
var gmapmarker;
var point,
    points = new google.maps.LatLngBounds();


function locationSuccess(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    var pos = new google.maps.LatLng(latitude, longitude);
    var marker = addresspickerMap.data().addresspicker.marker();
    marker.setPosition(pos);

    addresspickerMap.data().addresspicker._markerMoved();
    find_closest_marker(latitude, longitude);
}
function locationFail() {
}


function addMarker(map, point, image, title, infoWindowContent, zIndex) {
    zIndex = zIndex || 1;
    var marker = new google.maps.Marker({
        map: map,
        position: point,
        draggable: false,
        icon: image,
        title: title,
        zIndex: zIndex
    });
    if (infoWindowContent !== undefined) {
        var infowindow = new google.maps.InfoWindow({
            content: infoWindowContent,
            maxWidth: 300
        });
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map, marker);
        });
    }
    return marker;
}


function rad(x) {return x*Math.PI/180;}
function find_closest_marker(lat, lon) {
    var R = 6371; // radius of earth in km
    var distances = [];
    var closest = -1;
    for( i=0;i<points.length; i++ ) {
        var mlat = points[i].position.lat();
        var mlng = points[i].position.lng();
        var dLat  = rad(mlat - lat);
        var dLong = rad(mlng - lng);
        var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(rad(lat)) * Math.cos(rad(lat)) * Math.sin(dLong/2) * Math.sin(dLong/2);
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        var d = R * c;
        distances[i] = d;
        if ( closest == -1 || d < distances[closest] ) {
            closest = i;
        }
    }

    alert(gmap.markers[closest].title);
}


$(function() {
    addresspickerMap = $(".addresspicker").addresspicker({
        // regionBias: "it",
        map: ".map",
        typeaheaddelay: 500,
        mapOptions: {
            scrollwheel: true
        }
    });

    var componentsMapping = {
        'administrative_area_level_1': $('.addresspicker_administrative_area_level_1'),
        'administrative_area_level_2': $('.addresspicker_administrative_area_level_2'),
        'administrative_area_level_3': $('.addresspicker_administrative_area_level_3'),
        'formatted_address': $('.addresspicker_address'),
        'country': $('.addresspicker_country'),
        'locality': $('.addresspicker_locality'),
        'postal_code': $('.addresspicker_postal_code'),
        'route': $('.addresspicker_route'),
        'street_number': $('.addresspicker_street_number')
    };


    addresspickerMap.on("addressChanged", function(evt, address) {
        if (address) {
            $('.addresspicker_lat').val(address.geometry.location.lat());
            $('.addresspicker_lng').val(address.geometry.location.lng());
            var components = {};
            for (var i = address.address_components.length - 1; i >= 0; i--) {
                var c = address.address_components[i];
                components[c.types[0]] = c.long_name;
            }
            components['formatted_address'] = address.formatted_address;
            for(var el in componentsMapping) {
                // console.log('el: ', el, componentsMapping[el]);
                if (components[el]) {
                    componentsMapping[el].attr('readonly', 'readonly').val(components[el]);
                } else {
                    componentsMapping[el].removeAttr('readonly').val('');
                }
            }
            $('#add').show();
        }
    });
    addresspickerMap.on("positionChanged", function(evt, markerPosition) {
        markerPosition.getAddress( function(address) {
            if (address) {
                $( ".addresspicker").val(address.formatted_address);
            }
        });
    });


    gmap = addresspickerMap.data().addresspicker.map();
    gmapmarker = addresspickerMap.data().addresspicker.marker();


    var pinColor = "FFFF00";
    var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34));

    
    // point = new google.maps.LatLng(40.842147, 14.249948);
    // points.extend(point);
    // addMarker(
    //     gmap,
    //     point,
    //     pinImage,
    //     'fd (RF00000004)',
    //     'Saronno 4<br />www.saronnocomets.it',
    //     100,
    //     '#RF00000004'
    // );
    
    // point = new google.maps.LatLng(45.455948, 9.157624);
    // points.extend(point);
    // addMarker(
    //     gmap,
    //     point,
    //     pinImage,
    //     'Milano via Stendhal (RF00000003)',
    //     'Saronno 3<br />www.saronnocomets.it',
    //     100,
    //     '#RF00000003'
    // );
    
    // point = new google.maps.LatLng(45.932233, 8.482546);
    // points.extend(point);
    // addMarker(
    //     gmap,
    //     point,
    //     pinImage,
    //     'Casa al lago (RF00000001)',
    //     'Saronno 1<br />www.saronnocomets.it',
    //     100,
    //     '#RF00000001'
    // );
    
    // point = new google.maps.LatLng(44.386367, 9.035111);
    // points.extend(point);
    // addMarker(
    //     gmap,
    //     point,
    //     pinImage,
    //     'Amabile appartamento in zona verdeggiante (RF00000002)',
    //     'Saronno 2<br />www.saronnocomets.it',
    //     100,
    //     '#RF00000002'
    // );
    
    // gmap.fitBounds(points);


    var markers = [];
    for (var i = data.clubs.length; i > 0; i--) {
        var clubs = data.clubs[i-1];
        var latLng = new google.maps.LatLng(clubs.address_lat,
            clubs.address_lon);
        var marker = addMarker(
            gmap,
            latLng,
            pinImage,
            'Titolo',
            'Saronno<br />www.saronnocomets.it',
            100
        );
        markers.push(marker);
    }
    var markerCluster = new MarkerClusterer(gmap, markers);




    $(document).ready(function(){
        navigator.geolocation.getCurrentPosition(locationSuccess, locationFail);
    });

});

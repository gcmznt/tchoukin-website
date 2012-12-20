var addresspickerMap;
var gmap;
var gmapmarker;
var point,
    points = new google.maps.LatLngBounds();

var pinImage = new google.maps.MarkerImage("/static/img/ico_club.png",
    new google.maps.Size(32, 32),
    new google.maps.Point(0,0),
    new google.maps.Point(16, 16),
    new google.maps.Size(32, 32));


function locationSuccess(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    var pos = new google.maps.LatLng(latitude, longitude);
    var marker = addresspickerMap.data().addresspicker.marker();
    marker.setPosition(pos);

    addresspickerMap.data().addresspicker._markerMoved();
    // find_closest_marker(latitude, longitude);
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


var info = new google.maps.InfoWindow({});    // global InfoWindow object

function multiChoice(mc) {
    var cluster = mc.clusters_;
     // if more than 1 point shares the same lat/long
     // the size of the cluster array will be 1 AND
     // the number of markers in the cluster will be > 1
     // REMEMBER: maxZoom was already reached and we can't zoom in anymore
     if (cluster.length == 1 && cluster[0].markers_.length > 1)
     {
      var markers = cluster[0].markers_;
      var html = '';
      html += '<div id="infoWin">';
      html += '<h4>At this location:</h4>';
      html += '<ul class="addrlist">';
      for (var i=0; i < markers.length; i++)
      {
          html += '<li><a id="p' + markers[i].propertyId + '" href="javascript:;" rel="'+i+'">' + markers[i].title + '</a></li>';
      }
      html += '</ul>';
      html += '</div>';

          // I'm re-using the same global InfoWindow object here
          info.close();
          $('#infoWin').remove();
          $(html).appendTo('body');

          info.setContent(document.getElementById('infoWin'));
          info.open(gmap, markers[0]);
          // bind a click event to the list items to popup an InfoWindow
          $('ul.addrlist li').click(function() {
              var p = $(this).find("a").attr("rel");
              // $(markers[p]).click();
              google.maps.event.trigger(markers[p], 'click');
              info.close();
          });
          return false;
      }

      return true;
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




    
    // gmap.fitBounds(points);







    var markers = [];
    for (var i = data.clubs.length; i > 0; i--) {
        var clubs = data.clubs[i-1];
        var latLng = new google.maps.LatLng(clubs.address_lat, clubs.address_lon);
        var marker = addMarker(
            gmap,
            latLng,
            pinImage,
            clubs.name,
            clubs.name + '<br />' + clubs.email + '<br />' + clubs.website
        );
        markers.push(marker);
    }
    var markerCluster = new MarkerClusterer(gmap, markers);
    markerCluster.onClick = function() { return multiChoice(markerCluster); };



    $(document).ready(function(){
    });

});

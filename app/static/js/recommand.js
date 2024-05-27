$(function () {
    navigator.geolocation.getCurrentPosition((position) => {
        new naver.maps.Map('map', {
            center: new naver.maps.LatLng(position.coords.latitude, position.coords.longitude),
            zoom: 16
        });
    });
    
  })
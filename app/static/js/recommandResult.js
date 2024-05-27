const mask = document.querySelector('.mask');



function loadPage() {
    const radius = document.getElementById("radius").textContent;
    const contentTypeId = document.getElementById("contentTypeId").textContent;
    const param = {};
    navigator.geolocation.getCurrentPosition((position) => {
        param.longitude = position.coords.longitude;
        param.latitude = position.coords.latitude;
        param.radius = radius;
        param.contentTypeId = contentTypeId;
        getData(param);
    });

}
///recommandAPIResult
loadPage();


function getData(param) {
    $.ajax({
        url: "/recommandAPIResult",
        type: "POST",
        data: param,
        success: function (data) {
            if (data === null) {
                $('#resultTitle').text("검색결과가 없습니다.");
                return;
            }
            if (data.title != null) {
                $('#resultTitle').text(data.title);
            }
            if (data.addr1 != null) {
                $('#areaAddress').text(data.addr1);
            }
            if (data.firstimage != null) {
                $("#firstimage").attr("src", data.firstimage);
            }
            if (data.mapx != null && data.mapy != null) {
                var map = new naver.maps.Map('map', {
                    center: new naver.maps.LatLng(data.starty, data.startx),
                    zoom: 12
                });
                new naver.maps.Marker({
                    position: new naver.maps.LatLng(data.mapy, data.mapx),
                    map: map
                });
            }
            if (data.overview != null) {
                $('#resultInfo').text('상세정보');
                $('#overView').text(data.overview);
            }
            if (data.addr1 != null) {
                $('#addr1').text('주소 : ' + data.addr1);
            }
            if (data.infocenter != null) {
                $('#infocenter').text('문의 및 안내 : ' + data.infocenter);
            }
            if (data.usetime != null) {
                $('#usetime').text('이용시간 : ' + data.usetime);
            }
            if (data.homepage != null) {

            }
            if (data.path != null) {
                const polylinePath = data.path;
                new naver.maps.Polyline({
                    path: polylinePath,
                    strokeColor: '#FF0000',
                    strokeOpacity: 0.8,
                    strokeWeight: 6,
                    map: map
                });

                new naver.maps.Marker({
                    position: new naver.maps.LatLng(data.starty, data.startx),
                    map: map
                });

            }
            let href = 'http://map.naver.com/index.nhn?slng=' + data.startx + '&slat=' + data.starty + '&stext=출발지명&elng=' + data.mapx + '&elat=' + data.mapy + '&pathType=0&showMap=true&etext=' + data.title + '&menu=route';
            $("#directionPage").attr("href", href);
            $("#directionPage").show();
            mask.style.opacity = '0';
            mask.style.display = 'none';
        }
    });

}
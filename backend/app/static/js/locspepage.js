// 카카오맵 초기화
function initMap() {
    const mapContainer = document.getElementById('map'); // 지도를 표시할 div
    const mapOption = { 
        center: new kakao.maps.LatLng(36, 127.9), // 지도의 중심 좌표 (한국 중심)
        level: 13 // 지도의 확대 레벨
    };

    const map = new kakao.maps.Map(mapContainer, mapOption);

    // 주요 도시와 특산물 정보
    const cities = [
        { name: "서울", lat: 37.5665, lng: 126.9780, specialty: "한우" },
        { name: "대구", lat: 35.8714, lng: 128.6014, specialty: "사과" },
        { name: "부산", lat: 35.1796, lng: 129.0756, specialty: "어묵" },
        { name: "전주", lat: 35.8242, lng: 127.1480, specialty: "비빔밥" },
        { name: "제주", lat: 33.4996, lng: 126.5312, specialty: "감귤" },
    ];

    cities.forEach(city => {
        // 마커 생성
        const markerPosition  = new kakao.maps.LatLng(city.lat, city.lng); 
        const marker = new kakao.maps.Marker({
            position: markerPosition
        });
        marker.setMap(map);

        // 정보 창 생성
        const infoWindowContent = `<div class="info-window"><strong>${city.name}</strong><br>특산물: ${city.specialty}</div>`;
        const infoWindow = new kakao.maps.CustomOverlay({
            position: markerPosition,
            content: infoWindowContent,
            yAnchor: 1.5
        });

        // 마커에 마우스 이벤트 등록
        kakao.maps.event.addListener(marker, 'mouseover', () => {
            infoWindow.setMap(map);
        });
        kakao.maps.event.addListener(marker, 'mouseout', () => {
            infoWindow.setMap(null);
        });
    });
}

// 페이지 로딩 후 지도 초기화
window.onload = initMap;

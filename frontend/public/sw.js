self.addEventListener('install', (event) => {
    console.log('Service Worker installing.');
    // 캐시 또는 초기 설정 작업
});

self.addEventListener('fetch', (event) => {
    console.log('Service Worker fetching.', event.request.url);
    // 네트워크 요청을 처리하는 코드
});

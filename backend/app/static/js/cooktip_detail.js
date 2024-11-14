document.addEventListener("DOMContentLoaded", function() {
    const shareIcon = document.querySelector(".icon.share");

    shareIcon.addEventListener("click", function() {
        const url = window.location.href;
        navigator.clipboard.writeText(url).then(() => {
            // 복사 성공 시 팝업 창으로 메시지 표시
            alert("URL이 복사되었습니다!");
        }).catch(err => {
            console.error("URL 복사에 실패했습니다:", err);
        });
    });
});
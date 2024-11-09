// 메뉴 슬라이드 기능
function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

// 상호작용 아이콘 클릭 이벤트
document.addEventListener("DOMContentLoaded", function() {
    const likeIcon = document.querySelector(".icon.like");
    const scrapIcon = document.querySelector(".icon.scrap");
    const shareIcon = document.querySelector(".icon.share");

    likeIcon.addEventListener("click", function() {
        alert("이 레시피를 좋아요 했습니다!");
    });

    scrapIcon.addEventListener("click", function() {
        alert("이 레시피를 스크랩했습니다!");
    });

    shareIcon.addEventListener("click", function() {
        alert("이 레시피 링크가 복사되었습니다!");
    });
});

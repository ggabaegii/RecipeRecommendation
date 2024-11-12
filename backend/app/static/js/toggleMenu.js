function toggleMenu() {
    const menu = document.getElementById("menu");
    const menuIcon = document.getElementById("menuIcon");

    if (menu.style.transform === "translateX(0%)") {
        menu.style.transform = "translateX(-100%)";  // 메뉴를 화면 밖으로 이동
        menuIcon.style.display = "block";            // 원래 위치에서 메뉴 아이콘 다시 표시
    } else {
        menu.style.transform = "translateX(0%)";     // 메뉴를 화면에 표시
        menuIcon.style.display = "none";             // 메뉴가 열렸을 때 아이콘 숨기기
    }
}

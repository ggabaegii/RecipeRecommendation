// 메뉴 슬라이드 기능
function toggleMenu() {
    const menu = document.getElementById("menu");
    // 메뉴 너비가 250px이면 0으로, 아니면 250px로 변경하여 슬라이드 토글
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

// 계절별 필터링 기능
function filterRecipes(season) {
    const recipes = document.querySelectorAll(".item-box"); // 모든 레시피 항목 선택
    const buttons = document.querySelectorAll(".category-tabs button"); // 모든 계절 버튼 선택

    // 모든 버튼에서 "active" 클래스를 제거하여 스타일 초기화
    buttons.forEach(button => button.classList.remove("active"));

    // 클릭한 버튼에만 "active" 클래스를 추가하여 활성화 상태로 표시
    const activeButton = document.querySelector(`.category-tabs button[onclick="filterRecipes('${season}')"]`);
    activeButton.classList.add("active");

    // 각 레시피 항목에 대해 필터링 처리
    recipes.forEach(recipe => {
        if (season === 'all') {
            // "전체" 버튼을 클릭했을 경우, 모든 레시피 항목을 보이도록 설정
            recipe.style.display = "block";
        } else {
            // 특정 계절을 클릭했을 경우, 해당 계절에 맞는 레시피만 보이도록 설정
            recipe.style.display = recipe.getAttribute("data-season") === season ? "block" : "none";
        }
    });
}

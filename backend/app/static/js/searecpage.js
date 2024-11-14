// 메뉴 슬라이드 기능
function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

// 계절별 필터링 기능
function filterRecipes(season) {
    const recipes = document.querySelectorAll(".item-box");
    recipes.forEach(recipe => {
        recipe.style.display = season === 'all' || recipe.getAttribute("data-season") === season ? "block" : "none";
    });
}

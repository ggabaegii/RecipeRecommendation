// 메뉴 슬라이드 기능
function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

// 계절별 레시피 표시 기능
function showSeasonalRecipes(season) {
    const recipes = {
        spring: [
            { name: "딸기 샐러드", description: "신선한 봄 딸기로 만든 샐러드", img: "spring_recipe.jpg" },
            { name: "두릅 된장 무침", description: "고소한 두릅과 된장의 조화", img: "spring_recipe2.jpg" }
        ],
        summer: [
            { name: "수박 화채", description: "시원한 수박으로 만든 여름 별미", img: "summer_recipe.jpg" }
        ],
        fall: [
            { name: "밤죽", description: "영양 가득한 가을밤으로 만든 죽", img: "fall_recipe.jpg" }
        ],
        winter: [
            { name: "호박죽", description: "따뜻하고 달콤한 겨울 호박죽", img: "winter_recipe.jpg" }
        ]
    };

    const container = document.getElementById("seasonal-recipes");
    container.innerHTML = ""; // 기존 내용 초기화

    recipes[season].forEach(recipe => {
        const recipeCard = document.createElement("div");
        recipeCard.className = "item-box";
        recipeCard.innerHTML = `
            <img src="{{ url_for('static', filename='images/${recipe.img}') }}" alt="${recipe.name}">
            <hr>
            <h3>${recipe.name}</h3>
            <p>${recipe.description}</p>
        `;
        container.appendChild(recipeCard);
    });
}

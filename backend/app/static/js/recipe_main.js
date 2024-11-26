function displayRecipes() {
    const recipeGrid = document.getElementById('recipe-grid');
    recipeGrid.innerHTML = ""; // 기존 레시피 카드 초기화

    const sortedRecipes = sortRecipes(recipes);

    sortedRecipes.forEach(recipe => {
        const col = document.createElement('div');
        col.className = "col-md-3 col-sm-6"; // 반응형 그리드 클래스

        const card = `
            <div class="card h-100">
                <img src="recipe-image-placeholder.jpg" class="card-img-top" alt="${recipe.name} 사진" onclick="location.href='${recipe.url}'">
                <div class="card-body text-center">
                    <a href="${recipe.url}" class="recipe-card-title korean-font">${recipe.name}</a>
                    <p class="recipe-card-text korean-font">#해시태그 #레시피</p>
                </div>
            </div>
        `;

        col.innerHTML = card;
        recipeGrid.appendChild(col);
    });
}

document.addEventListener('DOMContentLoaded', displayRecipes);

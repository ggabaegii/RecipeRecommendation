// 메뉴 슬라이드 기능
function toggleMenu() {
    const menu = document.getElementById("menu");
    if (menu.style.width === "250px") {
        menu.style.width = "0";
    } else {
        menu.style.width = "250px";
    }
}

// 이미지 미리보기 기능
function previewImage(event) {
    const input = event.target;
    const file = input.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const foodImage = document.getElementById('food-image');
            foodImage.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
}

// 재료 항목 추가 기능
function addIngredientRow() {
    const ingredientList = document.getElementById("ingredient-list");
    const newRow = document.createElement("tr");

    newRow.innerHTML = `
        <td><input type="text" placeholder="재료명"></td>
        <td><input type="text" placeholder="필요한 양"></td>
        <td><input type="checkbox"></td>
    `;

    ingredientList.appendChild(newRow);
}

// 최근 검색어 추가 및 삭제 기능 (ingredient-search 필드만 저장)
function addRecentIngredient(ingredient) {
    const recentIngredientsContainer = document.getElementById("recent-ingredients");

    // 이미 화면에 있는 재료는 중복 추가하지 않음
    if (Array.from(recentIngredientsContainer.children).some(item => item.textContent.trim() === ingredient)) {
        return;
    }

    // 최근 검색어 아이템 생성
    const ingredientItem = document.createElement("span");
    ingredientItem.className = "recent-item";
    ingredientItem.textContent = ingredient;

    // 삭제 버튼 추가
    const removeBtn = document.createElement("button");
    removeBtn.className = "remove-btn";
    removeBtn.innerHTML = "×";
    removeBtn.onclick = function () {
        recentIngredientsContainer.removeChild(ingredientItem);
        removeRecentIngredient(ingredient); // 로컬 스토리지에서 삭제
    };

    ingredientItem.appendChild(removeBtn);
    recentIngredientsContainer.appendChild(ingredientItem);
}

// 로컬 스토리지에 최근 검색어 저장
function saveRecentIngredients(ingredients) {
    let recentIngredients = JSON.parse(localStorage.getItem('recentIngredients')) || [];
    ingredients.forEach(ingredient => {
        if (!recentIngredients.includes(ingredient)) {
            recentIngredients.push(ingredient);
        }
    });
    localStorage.setItem('recentIngredients', JSON.stringify(recentIngredients));
}

// 로컬 스토리지에서 최근 검색어 삭제
function removeRecentIngredient(ingredient) {
    let recentIngredients = JSON.parse(localStorage.getItem('recentIngredients')) || [];
    recentIngredients = recentIngredients.filter(item => item !== ingredient);
    localStorage.setItem('recentIngredients', JSON.stringify(recentIngredients));
}

// 로컬 스토리지에서 최근 검색어 로드
function loadRecentIngredients() {
    const recentIngredients = JSON.parse(localStorage.getItem('recentIngredients')) || [];
    recentIngredients.forEach(ingredient => addRecentIngredient(ingredient));
}

// 입력 필드 지우기 함수
function clearInput(inputId) {
    document.getElementById(inputId).value = '';
}

// Enter 키 입력 처리 및 재료 추가 (ingredient-search 필드만 최근 검색어에 저장)
function handleIngredientInput(event) {
    const ingredientInput = document.getElementById('ingredient-search').value.trim();
    const excludedInput = document.getElementById('excluded-ingredient').value.trim();

    if (event.key === "Enter") {
        const inputField = event.target; // 엔터키가 눌린 input 필드
        const ingredients = inputField.value.trim().split(' ').filter(Boolean); // 공백으로 구분된 재료들
        
        if (ingredients.length > 0) {
            // ingredient-search에 입력된 재료들만 최근 검색어에 추가
            if (inputField.id === "ingredient-search") {
                ingredients.forEach(ingredient => addRecentIngredient(ingredient));
            }
            inputField.value = ""; // 입력창 초기화
            event.preventDefault(); // 폼 제출 방지
            
            // 검색 함수 호출
            submitSearch(ingredientInput, excludedInput);
        } else {
            alert("사용할 재료 혹은 제외할 재료를 입력해 주세요.");
        }
    }
}

// 검색 제출 함수 (검색 시 ingredient-search 재료들만 로컬 스토리지에 저장)
function submitSearch(ingredientInput, excludedInput) {


    if (!ingredientInput && !excludedInput) {
        alert("사용할 재료 혹은 제외할 재료를 입력해 주세요.");
        return;
    }

    // 재료와 제외 재료 배열 생성
    const ingredientsArray = ingredientInput.split(' ').filter(item => item);
    const excludedIngredients = excludedInput.split(' ').filter(item => item);

    // 입력 제한 체크
    if (ingredientsArray.length > 3 || excludedIngredients.length > 3) {
        alert("재료는 최대 3개까지만 입력가능합니다.");
        return;
    }

    // ingredient-search에 입력된 재료만 로컬 스토리지에 최근 검색어로 저장
    saveRecentIngredients(ingredientsArray);

    // URL 파라미터로 전달
    const url = `/ingres?ingredients=${encodeURIComponent(ingredientsArray.join(','))}&excluded=${encodeURIComponent(excludedIngredients.join(','))}`;
    window.location.href = url;
}

// 페이지 로드 시 로컬 스토리지에서 최근 검색어 로드
window.addEventListener('DOMContentLoaded', loadRecentIngredients);

// Enter 키 이벤트 리스너 추가
document.getElementById('ingredient-search').addEventListener('keydown', handleIngredientInput);
document.getElementById('excluded-ingredient').addEventListener('keydown', handleIngredientInput);

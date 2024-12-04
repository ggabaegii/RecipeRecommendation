//최근 검색어 추가 및 삭제 기능
// X 버튼 클릭 시 동작: 검색되지 않고 로컬 스토리지에서만 삭제
function removeRecentIngredient(ingredient) {
    let recentIngredients = JSON.parse(localStorage.getItem('recentIngredients')) || [];
    recentIngredients = recentIngredients.filter(item => item !== ingredient);
    localStorage.setItem('recentIngredients', JSON.stringify(recentIngredients));

    const recentIngredientsContainer = document.getElementById("recent-ingredients");
    Array.from(recentIngredientsContainer.children).forEach(item => {
        if (item.textContent.trim().startsWith(ingredient)) {
            recentIngredientsContainer.removeChild(item);
        }
    });
}

// 최근 검색어 클릭 시 해당 검색어로 페이지 이동
function searchWithIngredient(ingredient) {
    const ingredientInput = document.getElementById('ingredient-search');
    ingredientInput.value = ingredient;
    submitSearch(ingredient);
}

// 검색 버튼 클릭 시 검색 동작 수정
function submitSearch(ingredientInput = '') {
    // 사용자의 입력값을 가져오기
    ingredientInput = ingredientInput || document.getElementById('ingredient-search').value.trim();
    
    if (!ingredientInput) {
        alert("사용할 재료를 입력해 주세요.");
        return;
    }

    // 재료 배열 생성
    const ingredientsArray = ingredientInput.split(' ').filter(item => item);

    // 입력 제한 체크
    if (ingredientsArray.length > 3) {
        alert("재료는 최대 3개까지만 입력가능합니다.");
        return;
    }

    showLoading();

    // ingredient-search에 입력된 재료만 로컬 스토리지에 최근 검색어로 저장
    saveRecentIngredients(ingredientsArray);


    // 재료 데이터를 백엔드로 전달
    fetch('/send_ingredients_to_gemini', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients: ingredientsArray })
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();
        // 예: 페이지를 이동하거나 UI 업데이트
        window.location.href = '/ingr_sea';
        }
    )
    .catch(error => {
        hideLoading();
        console.error("서버로 데이터 전송 중 오류:", error);
    });
}

// X 버튼 추가
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

    // 클릭 시 해당 재료로 검색 수행
    ingredientItem.onclick = function () {
        searchWithIngredient(ingredient);
    };

    // 삭제 버튼 추가
    const removeBtn = document.createElement("button");
    removeBtn.className = "remove-btn";
    removeBtn.innerHTML = "×";
    removeBtn.onclick = function (event) {
        event.stopPropagation(); // X 버튼 클릭 시 검색이 진행되지 않도록 이벤트 버블링 방지
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

// 로컬 스토리지에서 최근 검색어 로드
function loadRecentIngredients() {
    const recentIngredients = JSON.parse(localStorage.getItem('recentIngredients')) || [];
    recentIngredients.forEach(ingredient => addRecentIngredient(ingredient));
}

// Enter 키 입력 처리
function handleIngredientInput(event) {
    if (event.key === "Enter") {
        const ingredientInput = document.getElementById('ingredient-search').value.trim();
        //검색 함수 호출
        submitSearch(ingredientInput);
        event.preventDefault(); // 폼 제출 방지
    }
}

// 입력 필드 지우기 함수
function clearInput(inputId) {
    document.getElementById(inputId).value = '';
}

// 카메라 버튼 클릭 처리
function openCameraOrFile() {
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";
    input.capture = isMobile ? "camera" : ""; // 모바일의 경우 카메라 사용

    input.onchange = () => {
        const file = input.files[0];
        if (file) {
            processImageWithServer(file); // 서버로 파일 전송
        }
    };

    input.click();
}

// 서버로 이미지를 전송하여 Roboflow API 호출을 처리
async function processImageWithServer(file) {
    const formData = new FormData();
    formData.append("file", file);

    showLoading();

    try {
        // 서버로 이미지 전송
        const response = await fetch("/prdict", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        hideLoading();
        window.location.href = '/ingr_sea';
        
    } catch (error) {
        console.error("서버 호출 중 오류 발생:", error);
        hideLoading();
        alert("이미지 처리 중 오류가 발생했습니다.");
    }
}


// 로딩창 표시
function showLoading() {
    const loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'flex';
}

// 로딩창 숨김
function hideLoading() {
    const loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'none';
}

// 페이지 로드 시 로컬 스토리지에서 최근 검색어 로드
window.addEventListener('DOMContentLoaded', loadRecentIngredients);

// Enter 키 이벤트 리스너 및 검색 버튼 이벤트 리스너
document.getElementById('ingredient-search').addEventListener('keydown', handleIngredientInput);
document.getElementById('search-button').addEventListener('click', function () {
    submitSearch();
});

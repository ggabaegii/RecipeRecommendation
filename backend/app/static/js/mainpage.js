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

    // 클릭 시 해당 재료로 검색 수행
    ingredientItem.onclick = function () {
        searchWithIngredient(ingredient);
    };

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

// 클릭된 최근 검색어로 검색 수행
function searchWithIngredient(ingredient) {
    document.getElementById('ingredient-search').value = ingredient;
    submitSearch();
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
    const url = `/ingr_sea?ingredients=${encodeURIComponent(ingredientsArray.join(','))}&excluded=${encodeURIComponent(excludedIngredients.join(','))}`;
    window.location.href = url;
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

    try {
        // 서버로 이미지 전송
        const response = await fetch("/prdict", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        if (result && result.ingredients) {
            displayRecognizedIngredients(result.ingredients);
        } else {
            alert("이미지에서 재료를 인식하지 못했습니다.");
        }
    } catch (error) {
        console.error("서버 호출 중 오류 발생:", error);
        alert("이미지 처리 중 오류가 발생했습니다.");
    }
}

// 인식된 재료 화면에 표시
function displayRecognizedIngredients(ingredients) {
    const ingredientList = document.getElementById("ingredient-list");
    ingredientList.innerHTML = ""; // 기존 목록 초기화

    ingredients.forEach(ingredient => {
        const listItem = document.createElement("li");
        listItem.textContent = ingredient;
        ingredientList.appendChild(listItem);
    });
}

// 인식된 재료를 백엔드로 전달
function sendIngredientsToBackend(ingredients) {
    fetch("/process_ingredients", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ingredients })
    })
    .then(response => response.json())
    .then(data => {
        console.log("백엔드에서 처리된 결과:", data);
    })
    .catch(error => console.error("백엔드로 재료 전송 중 오류:", error));
}

// 페이지 로드 시 로컬 스토리지에서 최근 검색어 로드
window.addEventListener('DOMContentLoaded', loadRecentIngredients);

// Enter 키 이벤트 리스너 추가
document.getElementById('ingredient-search').addEventListener('keydown', handleIngredientInput);
document.getElementById('excluded-ingredient').addEventListener('keydown', handleIngredientInput);

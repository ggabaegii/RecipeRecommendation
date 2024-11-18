// 요리 재료 추가 함수
function addIngredientField() {
  const ingredientGroup = document.querySelector('.ingredient-group');
  const newIngredient = document.createElement('div');
  newIngredient.className = "ingredient-item";
  newIngredient.innerHTML = `
      <input type="text" name="ingredient" placeholder="재료명" class="korean-font">
      <input type="text" name="ingredient_amount" placeholder="재료양" class="korean-font">
      <button type="button" onclick="removeField(this)" class="remove-btn korean-font">삭제</button>
  `;
  ingredientGroup.appendChild(newIngredient);
}

// 소스 추가 함수
function addSauceField() {
  const sauceGroup = document.querySelector('.sauce-group');
  const newSauce = document.createElement('div');
  newSauce.className = "sauce-item";
  newSauce.innerHTML = `
      <input type="text" name="sauce_name" placeholder="소스명" class="korean-font">
      <input type="text" name="sauce_amount" placeholder="소스양" class="korean-font">
      <button type="button" onclick="removeField(this)" class="remove-btn korean-font">삭제</button>
  `;
  sauceGroup.appendChild(newSauce);
}

// 대체 재료 추가 함수
function addSubstituteField() {
  const substituteGroup = document.querySelector('.substitute-group');
  const newSubstitute = document.createElement('div');
  newSubstitute.className = "substitute-item";
  newSubstitute.innerHTML = `
      <input type="text" name="substitute" placeholder="원재료" class="korean-font">
      <input type="text" name="substitute_alt" placeholder="대체 재료" class="korean-font">
      <button type="button" onclick="removeField(this)" class="remove-btn korean-font">삭제</button>
  `;
  substituteGroup.appendChild(newSubstitute);
}

// 필드 삭제 함수
function removeField(button) {
  button.parentElement.remove();
}

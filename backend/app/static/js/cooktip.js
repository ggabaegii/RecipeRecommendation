function showCategory(category) {
    // 모든 카테고리 콘텐츠 숨기기
    const categories = document.querySelectorAll('.category-content');
    categories.forEach(cat => {
        cat.style.display = 'none';
    });

    // 선택한 카테고리만 표시
    document.getElementById(category).style.display = 'block';
}
<script>
    // 필요한 데이터 (예: 레시피 목록)를 가져오거나 설정할 수 있습니다.
    let recipes = [
        { id: 1, title: "레시피 제목", author: "작성자", date: "작성일" },
        { id: 2, title: "레시피 제목", author: "작성자", date: "작성일" },
        { id: 3, title: "레시피 제목", author: "작성자", date: "작성일" },
        // 추가 레시피 항목을 여기에 추가
    ];
</script>

<style>
    /* 전체 배경 */
    .search-page {
        background-color: #F2EDEC;
        padding: 20px;
    }

    /* 검색 상자 스타일 */
    .search-box {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }

    .search-box input[type="text"] {
        width: 300px;
        padding: 10px;
        border: 1px solid #042C57;
        border-radius: 4px 0 0 4px;
        font-size: 16px;
    }

    .search-box button {
        padding: 10px;
        background-color: #042C57;
        color: #fff;
        border: none;
        border-radius: 0 4px 4px 0;
        cursor: pointer;
    }

    /* 해시태그 스타일 */
    .hashtags {
        text-align: center;
        color: #666;
        margin-bottom: 20px;
    }

    /* 레시피 목록 스타일 */
    .recipe-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .recipe-item {
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid #042C57;
        padding: 10px 0;
        font-size: 18px;
    }

    .recipe-item .title {
        font-weight: bold;
        color: #042C57;
    }
</style>

<div class="search-page">
    <!-- 검색 상자 -->
    <div class="search-box">
        <input type="text" placeholder="레시피 검색" />
        <button>🔍</button>
    </div>

    <!-- 해시태그 -->
    <div class="hashtags">
        #해시태그 #레시피 #요리꿀팁
    </div>

    <!-- 레시피 목록 -->
    <div class="recipe-list">
        {#each recipes as recipe}
            <div class="recipe-item">
                <div>{recipe.id}</div>
                <div class="title">{recipe.title}</div>
                <div>{recipe.author}</div>
                <div>{recipe.date}</div>
            </div>
        {/each}
    </div>
</div>

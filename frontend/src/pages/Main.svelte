<script>
    import { onMount } from 'svelte';
    import 'src/styles/main.css';
    let isLoggedIn = false;
    let showMenu = false;
    const hashtags = ["#레시피", "#요리꿀팁"];
    const topRecipes = ["Top 1", "Top 2", "Top 3", "Top 4"];
  
    function toggleMenu() {
      showMenu = !showMenu;
    }
  
    function goTo(page) {
      alert(`${page} 화면으로 이동합니다.`);
    }
  </script>
    
  <div class="container">
    <!-- 슬라이드 메뉴 -->
    <div class="menu" class:open={showMenu}>
      <div class="menu-item" on:click={() => goTo("마이페이지")}>닉네임</div>
      <div class="menu-item" on:click={() => goTo("홈")}>Home</div>
      <div class="menu-item" on:click={() => goTo("레시피")}>레시피</div>
      <div class="menu-item" on:click={() => goTo("최근 본 레시피")}>최근 본 레시피</div>
      <div class="menu-item" on:click={() => goTo("즐겨찾기 레시피")}>즐겨찾기 레시피</div>
      <div class="menu-item" on:click={() => goTo("게시판")}>게시판</div>
      <div class="menu-item" on:click={() => goTo("정보")}>정보</div>
      {#if isLoggedIn}
        <button class="menu-button" on:click={() => goTo("레시피 작성")}>레시피 작성</button>
        <button class="menu-button" on:click={() => { isLoggedIn = false }}>로그아웃</button>
      {:else}
        <button class="menu-button" on:click={() => goTo("로그인")}>로그인</button>
        <button class="menu-button" on:click={() => goTo("회원가입")}>회원가입</button>
      {/if}
    </div>
  
    <!-- 메인 화면 -->
    <div class="content" class:menu-open={showMenu}>
      <div class="header">
        <span on:click={() => goTo("홈")}>요리의 정원</span>
        <span class="search-icon" on:click={toggleMenu}>☰</span>
      </div>
  
      <!-- 검색 바 -->
      <div class="search-bar">
        <input type="text" placeholder="재료 검색" />
        <span class="search-icon" on:click={() => goTo("사진 검색")}>📷</span>
        <span class="search-icon" on:click={() => goTo("재료 검색")}>🔍</span>
      </div>
  
      <!-- 해시태그 -->
      <div class="highlight">
        {#each hashtags as hashtag}
          <span on:click={() => goTo(hashtag)}>{hashtag}</span>&nbsp;
        {/each}
      </div>
  
      <!-- 오늘의 꿀팁 -->
      <div class="highlight" on:click={() => goTo("꿀팁")}>
        오늘의 꿀팁: 랜덤 꿀팁 제목
      </div>
  
      <!-- 최다 검색량 레시피 카드 -->
      <div class="top-recipes">
        {#each topRecipes as recipe, index}
          <div class="card" on:click={() => goTo(`레시피 ${index + 1}`)}>
            사이트 내 최다 검색량 레시피<br />{recipe}
          </div>
        {/each}
      </div>
    </div>
  </div>
  
// 메뉴 슬라이드 기능
function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

// 상호작용 아이콘 클릭 이벤트
document.addEventListener("DOMContentLoaded", function() {
    const likeIcon = document.querySelector(".icon.like");
    const scrapIcon = document.querySelector(".icon.scrap");
    const shareIcon = document.querySelector(".icon.share");

    likeIcon.addEventListener("click", function() {
        alert("이 레시피를 좋아요 했습니다!");
    });

    scrapIcon.addEventListener("click", function() {
        alert("이 레시피를 스크랩했습니다!");
    });

    shareIcon.addEventListener("click", shareRecipe);
});

// 공유 기능
function shareRecipe() {
    const recipeUrl = window.location.href;

    if (navigator.share) {
        navigator.share({
            title: '레시피 공유',
            text: '이 레시피를 확인해보세요!',
            url: recipeUrl,
        })
        .then(() => console.log('공유 완료'))
        .catch((error) => console.log('공유 실패', error));
    } else {
        navigator.clipboard.writeText(recipeUrl)
            .then(() => alert("링크가 복사되었습니다!"))
            .catch((error) => alert("링크 복사에 실패했습니다."));
    }
}

// 말풍선 표시 및 숨기기 기능
function toggleTooltip(event, text) {
    const checkbox = event.target;
    let tooltip = checkbox.parentNode.querySelector(".tooltip");

    // 말풍선이 이미 있으면 삭제하여 숨김
    if (tooltip) {
        checkbox.parentNode.removeChild(tooltip);
    } else {
        // 말풍선 생성 및 표시
        tooltip = document.createElement("div");
        tooltip.className = "tooltip";
        tooltip.textContent = text;
        checkbox.parentNode.appendChild(tooltip);
        tooltip.style.display = "block";
        adjustTooltipPosition(tooltip);
    }
}

// 말풍선 위치 조정 기능
function adjustTooltipPosition(tooltip) {
    const rect = tooltip.getBoundingClientRect();

    if (rect.left < 0) {
        tooltip.style.left = "10px";
    } else if (rect.right > window.innerWidth) {
        tooltip.style.right = "10px";
    }
}

// 사용자가 댓글 입력창에 텍스트를 입력하고 "댓글 추가" 버튼을 클릭했을 때 댓글 목록에 새 댓글을 추가하는 JavaScript 코드

document.querySelector('.comment-submit-button').addEventListener('click', function () {
    const commentInput = document.querySelector('.comment-input');
    const commentText = commentInput.value.trim();

    if (commentText) {
        const commentList = document.querySelector('.comment-list');
        const newComment = document.createElement('li');
        newComment.innerHTML = `<span class="comment-author">익명:</span> <span class="comment-text">${commentText}</span>`;
        commentList.appendChild(newComment);

        // 입력창 초기화
        commentInput.value = '';
    } else {
        alert('댓글을 입력하세요.');
    }
});


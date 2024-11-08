// 숫자랑 한글은 '나눔글씨 외할머니글씨' / 영어는 'Marcellus' 되도록 작성

document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll("h1, h2, h3, p, a, button");

    elements.forEach(element => {
        const words = element.textContent.split(/(\s+)/);  // 공백을 기준으로 분리
        const formattedWords = words.map(word => {
            if (/^[\u3131-\uD79D]+$/.test(word) || /^\d+$/.test(word)) { // 한글 또는 숫자
                return `<span class="korean-font">${word}</span>`;
            } else if (/^[a-zA-Z]+$/.test(word)) { // 영어
                return `<span class="english-font">${word}</span>`;
            } else {
                return word;
            }
        });
        element.innerHTML = formattedWords.join("");
    });
});

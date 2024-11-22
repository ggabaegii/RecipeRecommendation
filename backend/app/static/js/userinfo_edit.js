// 닉네임 랜덤 생성 함수
function generateRandomNickname() {
    const adjectives = ["멋진", "행복한", "똑똑한", "귀여운", "용감한"];
    const nouns = ["호랑이", "토끼", "독수리", "사자", "팬더"];
    const randomAdjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const randomNoun = nouns[Math.floor(Math.random() * nouns.length)];
    const randomNickname = `${randomAdjective} ${randomNoun}`;
    document.getElementById("nickname").value = randomNickname;
}

// 사용자 정보 저장
document.getElementById("edit-user-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const nickname = document.getElementById("nickname").value;
    const userName = document.getElementById("user_name").value;
    const userEmail = document.getElementById("user_email").value;
    const phone = document.getElementById("phone").value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const allergies = document.getElementById("allergies").value;

    const userData = {
        nickname,
        user_name: userName,
        user_email: userEmail,
        phone,
        gender,
        allergies,
    };

    try {
        const response = await fetch("/update_user_info", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
        });

        if (response.ok) {
            alert("사용자 정보가 성공적으로 업데이트되었습니다!");
            window.location.href = "/mypagemain";
        } else {
            alert("사용자 정보를 업데이트하는 데 실패했습니다.");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("서버와의 통신 중 오류가 발생했습니다.");
    }
});

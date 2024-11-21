// 닉네임 랜덤 생성 함수
function generateRandomNickname() {
    const adjectives = ["멋진", "행복한", "똑똑한", "귀여운", "용감한"];
    const nouns = ["호랑이", "토끼", "독수리", "사자", "팬더"];
    const randomAdjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const randomNoun = nouns[Math.floor(Math.random() * nouns.length)];
    const randomNickname = `${randomAdjective} ${randomNoun}`;
    document.getElementById("nickname").value = randomNickname;
}

// 전화번호 입력 형식 자동 처리 및 유효성 검사
document.getElementById("phone").addEventListener("input", function (event) {
    const input = event.target;
    const value = input.value.replace(/[^0-9]/g, ""); // 숫자만 남기기
    let formattedValue = "";

    if (value.length > 3) {
        formattedValue += value.substring(0, 3) + "-";
        if (value.length > 6) {
            formattedValue += value.substring(3, 6) + "-";
            formattedValue += value.substring(6, 10);
        } else {
            formattedValue += value.substring(3);
        }
    } else {
        formattedValue = value;
    }

    input.value = formattedValue;

    const isValid = /^[0-9]{3}-[0-9]{3}-[0-9]{4}$/.test(formattedValue);
    document.getElementById("phone-error").style.display = isValid ? "none" : "block";
});

// 사용자 정보 저장
document.getElementById("edit-user-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const nickname = document.getElementById("nickname").value;
    const userName = document.getElementById("user_name").value;
    const userEmail = document.getElementById("user_email").value;
    const phone = document.getElementById("phone").value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const allergies = document.getElementById("allergies").value;

    const isValidPhone = /^[0-9]{3}-[0-9]{3}-[0-9]{4}$/.test(phone);
    if (!isValidPhone) {
        alert("전화번호 형식을 확인해주세요 (000-000-0000).");
        return;
    }

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
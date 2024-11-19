document.getElementById("edit-user-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    // 사용자 정보 가져오기
    const userName = document.getElementById("user_name").value;
    const userEmail = document.getElementById("user_email").value;
    const allergies = document.getElementById("allergies").value;
    const vegetarianPreference = document.getElementById("vegetarian_preference").value === "true";

    // JSON 데이터 생성
    const userData = {
        user_name: userName,
        user_email: userEmail,
        allergies: allergies,
        vegetarian_preference: vegetarianPreference,
    };

    try {
        // 서버에 데이터 전송
        const response = await fetch("/update_user_info", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData),
        });

        if (response.ok) {
            alert("사용자 정보가 성공적으로 업데이트되었습니다!");
            window.location.href = "/mypagemain"; // mypagemain으로 리다이렉트
        } else {
            alert("사용자 정보를 업데이트하는 데 실패했습니다.");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("서버와의 통신 중 오류가 발생했습니다.");
    }
});

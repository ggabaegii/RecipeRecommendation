document.addEventListener('DOMContentLoaded', () => {
    // 전화번호 형식 자동 추가
    document.getElementById('phone').addEventListener('input', function (event) {
        const input = event.target;
        let value = input.value.replace(/\D/g, ''); // 숫자만 남기기
        if (value.length > 3 && value.length <= 7) {
            value = `${value.slice(0, 3)}-${value.slice(3)}`;
        } else if (value.length > 7) {
            value = `${value.slice(0, 3)}-${value.slice(3, 7)}-${value.slice(7)}`;
        }
        input.value = value;
    });

    // 비밀번호 확인 및 엿보기 기능
    document.getElementById('editForm').addEventListener('submit', function (event) {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        if (password !== confirmPassword) {
            event.preventDefault(); // 폼 제출 중단
            alert('비밀번호가 일치하지 않습니다. 다시 확인해주세요.');
        }
    });

    // 비밀번호 엿보기 기능
    document.querySelectorAll('.toggle-password').forEach(button => {
        button.addEventListener('click', function () {
            const targetId = this.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);
            const type = targetInput.getAttribute('type') === 'password' ? 'text' : 'password';
            targetInput.setAttribute('type', type);

            // 버튼 아이콘 변경
            this.textContent = type === 'password' ? '👁' : '🙈';
        });
    });
});

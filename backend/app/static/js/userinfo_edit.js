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

// 형용사 및 동물 세트
const adjectives = [
    '가냘픈', '가는', '가엾은', '가파른', '같은', '거센', '거친', '검은', '게으른', '고달픈', '고른', '고마운',
    '고운', '고픈', '곧은', '괜찮은', '구석진', '굳은', '굵은', '귀여운', '그런', '그른', '그리운', '기다란',
    '기쁜', '긴', '깊은', '깎아지른', '깨끗한', '나쁜', '나은', '난데없는', '날랜', '날카로운', '낮은', '너그러운',
    '너른', '널따란', '넓은', '네모난', '노란', '높은', '누런', '눅은', '느닷없는', '느린', '늦은', '다른'
];
const animals = [
    '고양이', '강아지', '거북이', '토끼', '뱀', '사자', '호랑이', '표범', '치타', '하이에나', '기린', '코끼리',
    '코뿔소', '하마', '악어', '펭귄', '부엉이', '올빼미', '곰', '돼지', '소', '닭', '독수리', '타조', '고릴라'
];

// 기존 닉네임 (테스트 데이터)
const existingNicknames = ['멋진 고양이 1234', '귀여운 강아지 5678'];

// 랜덤 닉네임 생성
document.getElementById('generateNickname').addEventListener('click', function () {
    const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    const animal = animals[Math.floor(Math.random() * animals.length)];
    const randomNumber = Math.floor(Math.random() * 9000) + 1000;
    const newNickname = `${adjective} ${animal} ${randomNumber}`;
    document.getElementById('nickname').value = newNickname;
});

// 닉네임 중복 체크
document.getElementById('checkNickname').addEventListener('click', function () {
    const nickname = document.getElementById('nickname').value.trim();
    if (nickname.length === 0) {
        alert('닉네임을 입력해주세요.');
        return;
    }
    if (existingNicknames.includes(nickname)) {
        alert('이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요.');
    } else {
        alert('사용 가능한 닉네임입니다!');
    }
});

// 폼 제출 이벤트 처리
document.getElementById('editForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch('/update_userinfo', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('정보가 성공적으로 저장되었습니다.');
            window.location.href = '/mypagemain';
        } else {
            alert('저장 중 문제가 발생했습니다. 다시 시도해주세요.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('서버 오류가 발생했습니다.');
    });
});

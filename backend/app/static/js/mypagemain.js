// 편집 모드 토글 기능
function toggleEditMode() {
    const editButton = document.querySelector(".edit-info-button");
    const isEditing = editButton.textContent === "저장하기";

    if (isEditing) {
        document.getElementById("name-display").textContent = document.getElementById("name-input").value;
        document.getElementById("phone-display").textContent = document.getElementById("phone-input").value;
        document.getElementById("email-display").textContent = document.getElementById("email-input").value;
        document.getElementById("allergy-display").textContent = document.getElementById("allergy-input").value;

        toggleInputFields(false);

        editButton.textContent = "정보 수정하기";
    } else {
        toggleInputFields(true);

        editButton.textContent = "저장하기";
    }
}

function toggleInputFields(isEditing) {
    const fields = ["name", "phone", "email", "allergy"];
    fields.forEach(field => {
        document.getElementById(`${field}-display`).style.display = isEditing ? "none" : "inline";
        document.getElementById(`${field}-input`).style.display = isEditing ? "inline" : "none";
    });
}

function editNickname() {
    document.getElementById("nickname-display").style.display = "none";
    document.getElementById("nickname-input").style.display = "inline";
    document.getElementById("nickname-input").focus();
}

function saveNickname() {
    const nicknameInput = document.getElementById("nickname-input");
    document.getElementById("nickname-display").textContent = nicknameInput.value;
    document.getElementById("nickname-display").style.display = "inline";
    nicknameInput.style.display = "none";
}

function toggleMenu() {
    const menu = document.getElementById("menu");
    menu.style.width = menu.style.width === "250px" ? "0" : "250px";
}

function previewProfileImage(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const profileImage = document.getElementById('profile-image');
            profileImage.src = e.target.result;
            profileImage.onload = function() {
                profileImage.style.objectFit = "cover";
            };
        };

        reader.readAsDataURL(file);
    }
}

function resetProfileImage() {
    const profileImage = document.getElementById('profile-image');
    // 기본 이미지로 되돌리기
    profileImage.src = "{{ url_for('static', filename='images/default-profile.png') }}";
    profileImage.style.objectFit = "cover";
}

# 요리의 정원
신세계I&C 디지털스마트부산 5기 팀프로젝트  
**재료 사진 인식 레시피 추천 프로그램**

---
## 1. 프로젝트 개요
최근 1인 가구 증가와 집밥을 선호하는 인구 증가로 사용자가 집에 있는 재료를 어떻게 활용할 수 있을지 고민하는 상황이 많아졌습니다.  
이 프로젝트는 사용자가 보유한 식재료 이미지를 업로드하면, 이미지 인식 모델을 통해 재료를 판별하고 해당 재료로 만들 수 있는 레시피를 추천하는 웹 서비스입니다.  
재료 인식에는 Roboflow 기반 YOLO 모델을 활용하였고, 레시피 추천에는 Gemini API를 사용하여 사용자에게 3개의 요리 후보를 JSON 형태로 제공합니다.  

본 프로젝트의 목표는 사용자가 가진 재료를 효율적으로 활용하도록 돕고, 요리 선택 과정의 번거로움을 줄이는 것입니다.
***
## 2. 주요 기능

### 2.1 재료 이미지 인식

사용자가 식재료 이미지를 업로드하면 Roboflow API를 통해 이미지 속 재료를 인식합니다.

- 업로드된 이미지를 base64로 인코딩
- Roboflow API에 이미지 전달
- 신뢰도 50% 이상인 예측 결과만 사용
- 모델 클래스 ID를 실제 재료명으로 변환
- 최대 3개의 재료를 추천 입력값으로 사용

| 함수명 | 위치 | 설명 |
|---|---|---|
| `map_class_to_material()` | `backend/app/api.py` | YOLO 클래스 ID를 실제 재료명으로 변환합니다. |
| `predict_from_image()` | `backend/app/api.py` | 업로드 이미지를 Roboflow API에 전달하고 인식된 재료 목록을 반환합니다. |

### 2.2 Gemini 기반 레시피 추천

인식된 재료 목록을 Gemini API에 전달하여 만들 수 있는 요리 레시피를 추천받습니다.

Gemini는 다음 정보를 포함한 레시피 데이터를 JSON 형식으로 반환합니다.

- 레시피 번호
- 요리 이름
- 카테고리
- 요리 설명
- 필요한 재료
- 대체 가능한 재료
- 조리 단계
- 조리 시간
- 난이도
- 이미지 URL

| 함수명 | 위치 | 설명 |
|---|---|---|
| `get_recipes_from_gemini()` | `backend/app/api.py` | 인식된 재료를 기반으로 Gemini API에 레시피 추천을 요청하고 JSON 응답을 반환합니다. |

### 2.3 추천 레시피 저장 및 조회

Gemini API에서 반환된 레시피 데이터는 SQLite 데이터베이스에 저장됩니다.  
사용자는 추천 결과 화면과 상세 페이지에서 레시피 정보를 확인할 수 있습니다.

| 함수명 | 위치 | 설명 |
|---|---|---|
| `create_recipes_table()` | `backend/app/database_setup.py` | 레시피 저장을 위한 SQLite 테이블을 생성합니다. |
| `insert_recipes_to_db()` | `backend/app/database_operations.py` | Gemini가 반환한 레시피 데이터를 DB에 저장합니다. |
| `recipe_detail()` | `backend/app/__init__.py` | 저장된 레시피를 조회하여 상세 페이지에 전달합니다. |

---

## 3. 서비스 흐름

```text
사용자 이미지 업로드
        ↓
Roboflow API를 통한 재료 인식
        ↓
클래스 ID를 실제 재료명으로 변환
        ↓
Gemini API에 재료 목록 전달
        ↓
레시피 3개 추천
        ↓
SQLite DB 저장
        ↓
추천 결과 및 상세 페이지 출력
```

---

## 4. 개발 환경

| 항목 | 내용 |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Database | SQLite |
| AI API | Roboflow API, Gemini API |
| IDE | Visual Studio Code |
***
## 5. 사용 기술 및 모델

### 5.1 YOLOv11 기반 재료 인식

- Roboflow를 활용한 식재료 이미지 데이터 학습
- 총 30개의 식재료 클래스 사용
- 예시 클래스: 양파, 마늘, 당근, 오이, 토마토, 육류 등
- 신뢰도 50% 이상인 예측 결과만 추천 로직에 반영

| Metric | Score |
|---|---|
| mAP | 73.9% |
| Precision | 71.3% |
| Recall | 72.6% |

### 5.2 Gemini 1.5 Flash 기반 레시피 추천

Gemini API를 활용하여 인식된 식재료로 만들 수 있는 레시피를 생성합니다.

- 입력: 인식된 재료 목록
- 출력: 레시피 3개
- 응답 형식: JSON
- 포함 정보: 요리명, 카테고리, 설명, 재료, 대체재, 조리 단계, 조리 시간, 난이도

---

## 6. 데이터 수집 및 학습

- 데이터 출처: Roboflow 활용 라벨링 데이터
- 이미지 수: 22,816장
- 클래스 수: 30개
- 데이터 분할:
  - Train: 87%
  - Validation: 4%
  - Test: 8%

| 항목 | 값 |
|---|---|
| Epochs | 30 |
| Image Size | 640x640 |

---

## 7. 프로젝트 구조

```text
RecipeRecommendation/
├── backend/
│   ├── app.py
│   └── app/
│       ├── __init__.py
│       ├── api.py
│       ├── database_setup.py
│       ├── database_operations.py
│       ├── config.py
│       ├── templates/
│       └── static/
├── tests/
├── requirements.txt
└── README.md
```

| 파일 | 설명 |
|---|---|
| `backend/app.py` | Flask 앱 실행 진입점입니다. |
| `backend/app/__init__.py` | Flask 앱 생성, 라우트 정의, 화면 연결을 담당합니다. |
| `backend/app/api.py` | Roboflow API와 Gemini API 연동 로직을 담당합니다. |
| `backend/app/database_setup.py` | SQLite 데이터베이스 테이블 생성 로직을 담당합니다. |
| `backend/app/database_operations.py` | 추천 레시피 데이터를 DB에 저장하는 로직을 담당합니다. |
| `requirements.txt` | 프로젝트 실행에 필요한 Python 패키지 목록입니다. |

---

## 8. 실행 방법

### 8.1 저장소 클론

```bash
git clone 저장소_URL
cd RecipeRecommendation
```

### 8.2 가상환경 생성 및 실행

```bash
python -m venv venv
venv\Scripts\activate
```

### 8.3 패키지 설치

```bash
pip install -r requirements.txt
```

### 8.4 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 값을 설정합니다.

```env
roboflow_API_URL=Roboflow API URL
roboflow_API_KEY=Roboflow API Key
genai_api_key=Gemini API Key
```

### 8.5 서버 실행

```bash
python backend/app.py
```

실행 후 브라우저에서 아래 주소로 접속합니다.

```text
http://127.0.0.1:5000
```

---

## 9. 주요 API 및 라우트

| Route | Method | 설명 |
|---|---|---|
| `/` | GET | 메인 페이지를 렌더링합니다. |
| `/prdict` | POST | 이미지 파일을 업로드받아 재료 인식 및 레시피 추천을 수행합니다. |
| `/send_ingredients_to_gemini` | POST | 사용자가 선택한 재료 목록을 Gemini API에 전달하여 레시피를 추천받습니다. |
| `/ingr_sea` | GET | 추천된 레시피 목록을 보여줍니다. |
| `/recipe_detail/<recipe_id>` | GET | 선택한 레시피의 상세 정보를 보여줍니다. |
| `/recipe_main` | GET | 레시피 메인 페이지를 렌더링합니다. |
| `/recipe_search` | GET | 레시피 검색 페이지를 렌더링합니다. |

---
## 10. 시연 영상
[![Video Lable](http://img.youtube.com/vi/MzjG3QHGCoM/0.jpg)](https://youtu.be/MzjG3QHGCoM)
***
## 11. 한계점 및 개선 방향

현재 프로젝트는 이미지 인식 결과와 Gemini API 응답에 의존하기 때문에, 재료 인식이 실패하거나 Gemini 응답 형식이 예상과 다를 경우 추천 결과가 정상적으로 표시되지 않을 수 있습니다.

또한 현재 DB 경로가 로컬 절대 경로로 작성되어 있어 다른 환경에서 실행할 때 경로 수정이 필요할 수 있습니다. 향후 환경 변수 또는 상대 경로 기반으로 DB 설정 개선이 필요합니다.

***
## 12. 팀 구성원
| 이름 | 역할 | 담당 |
|---|---|---|
| 조승일 | 팀원 | 계획서 작성, Web 구현, 최종 발표 ppt 제작 |
| 임수현 | 팀원 | DB 설계, 백엔드 구축, Web 구현, 포스터 제작 |
| 권주회 | 팀원 | 계획서 작성, 화면 설계서 작성, Web 구현, 포스터 제작 |
| 김소희 | 팀장 | 모델 설계, 백엔드 API, DB 설계, Web 구현, 산출물 작성 |
| 황예민 | 팀원 | 화면 설계서 작성, Web 구현, 최종 발표 ppt 제작 |

---
## 13. 프로젝트 산출물

| 구분 | 파일 | 설명 |
|---|---|---|
| 최종 발표자료 | [최종 발표자료](docs/presentation/final-presentation.pdf) | 프로젝트 목표, 구현 결과, 시연 흐름을 정리한 발표자료 |
| ERD | [ERD](docs/design/erd.xlsx) | 데이터베이스 테이블 구조와 관계도 |
| 화면 정의서 | [화면 정의서](docs/requirements/screen-definition.pdf) | 페이지별 화면 구성과 기능 정의 |
| 요구사항 정의서 | [요구사항 정의서](docs/requirements/requirements.xlsx) | 요구사항 정의 |
| 서비스 요구사항 | [서비스 요구사항](docs/requirements/service-requirements.pdf) | 서비스 기능 요구사항 발표 자료 |
| WBS | [WBS](docs/planning/wbs.xlsx) | 프로젝트 일정 및 작업 분해 구조 |
| 타당성 조사서 | [타당성 조사서](docs/planning/feasibility-study.pdf) | 서비스 필요성과 구현 가능성 검토 |
| 포스터 | [포스터](docs/presentation/poster.pdf) | 프로젝트 요약 포스터 |

ERD, 요구사항 정의서, WBS는 표 구조 확인을 위해 Excel 원본 파일로 제출합니다.

---

## 14. License
본 프로젝트는 교육 과정 팀 프로젝트 및 포트폴리오 목적으로 제작되었습니다.

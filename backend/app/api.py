import base64
import requests

def predict_from_image(image_file, api_url, api_key):
    """
    Roboflow API를 호출하여 이미지에서 재료를 예측합니다.
    :param image_file: 업로드된 이미지 파일
    :param api_url: Roboflow API URL
    :param api_key: Roboflow API Key
    :return: 예측된 재료 리스트
    """
    # 이미지를 base64로 인코딩
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    
    try: # API 호출
        response = requests.post(
            api_url,
            params={"api_key": api_key},
            data=encoded_image,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        # 응답 확인 및 결과 반환
        response.raise_for_status()
        data = response.json()
        print("Roboflow Response:", data)
        predictions = data.get("predictions", [])
        ingredients = [pred["class"] for pred in predictions]
        return {"ingredients": ingredients}
    except requests.exceptions.RequestException as e:
        print("API Request Error:", e)
        raise
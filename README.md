# Flask Card Draw App 🎴
트럼프 카드를 테이블별로 뽑을 수 있는 웹 애플리케이션입니다.

## 🚀 배포
Render를 사용하여 배포되었습니다: [배포 사이트](https://card-game-iolm.onrender.com)

## 🛠️ 설치 방법
1. 필요한 패키지 설치
    ```sh
    pip install -r requirements.txt
    ```
2. 로컬 실행
    ```sh
    python app.py
    ```

## 🐳 Docker 실행 (선택)
```sh
docker build -t flask-card-app .
docker run -p 5000:5000 flask-card-app

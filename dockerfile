# 1️⃣ Python 3.9 기반 이미지 사용
FROM python:3.9

# 2️⃣ 작업 디렉토리 설정
WORKDIR /app

# 3️⃣ 필요한 파일 복사
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates templates
COPY static static

# 4️⃣ 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Flask 서버 실행
CMD ["python", "app.py"]

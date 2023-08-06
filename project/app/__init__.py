# pip install torch torchvision Flask google-cloud-speech google-cloud-texttospeech pytesseract Pillow
# pip freeze > requirements.txt
from flask import Flask

app = Flask(__name__)

# 필요한 라우트 및 설정 초기화
from app import routes

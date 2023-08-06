from flask import request, jsonify, send_file, render_template
from PIL import Image
import pytesseract
import io
from app.models.resnet_model import classify_image
from app.services.stt_service import stt
from app.services.tts_service import tts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['file'].read()
    label = classify_image(file)
    return jsonify({'prediction': label})

@app.route('/stt-tts', methods=['POST'])
def stt_tts_route():
    audio_data = request.data
    transcript = stt(audio_data)
    if "메타버스" in transcript:
        response_audio = tts("반갑습니다")
        return send_file(
            io.BytesIO(response_audio),
            attachment_filename='response.mp3',
            mimetype='audio/mp3'
        )
    return "메타버스라는 말을 찾을 수 없습니다.", 400

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    image = Image.open(file.stream)
    
    extracted_text = pytesseract.image_to_string(image, lang='kor')
    
    return jsonify({'text': extracted_text})

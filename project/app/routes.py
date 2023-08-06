from flask import request, jsonify, send_file
from app.models.resnet_model import classify_image
from app.services.stt_service import stt
from app.services.tts_service import tts

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
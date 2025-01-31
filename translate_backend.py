from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

model_name = "Helsinki-NLP/opus-mt-en-zh"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    text = data['text']
    translation = translate_text(text)
    return jsonify({"translation": translation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

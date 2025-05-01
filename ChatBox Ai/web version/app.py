from flask import Flask, render_template, request, jsonify
import datetime
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini AI (use environment variable in production)
genai.configure(api_key=os.getenv('GEMINI_API_KEY', "YOUR API"))


def get_greeting():
    current_time = datetime.datetime.now()
    if 6 < current_time.hour < 12:
        return "Good Morning"
    elif 12 <= current_time.hour < 16:
        return "Good Afternoon"
    return "Good Evening"

@app.route('/')
def home():
    return render_template('index.html', greeting=get_greeting())

@app.route('/ask', methods=['POST'])
def ask_question():
    user_input = request.json.get('question')
    if not user_input or not user_input.strip():
        return jsonify({'error': 'Please enter a question'})
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)
openai.api_key = "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" # Thay YOUR_API_KEY bằng API key của bạn

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data['question']
    prompt = f"Question: {question}\nAnswer:"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

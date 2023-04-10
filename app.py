import openai
import os
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    question = request.form['question']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response["choices"][0]["text"].strip()
    return render_template("index.html", answer=answer)
if __name__ == '__main__':
    app.run()

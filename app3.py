from flask import Flask, render_template, jsonify, request
import openai
import os

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "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"

# Define the chatbot API endpoint
@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    # Get the question from the request
    question = request.json["question"]

    # Generate the answer using OpenAI ChatGPT
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Return the answer to the user
    return jsonify({"answer": response.choices[0].text.strip()})

# Define the home page
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

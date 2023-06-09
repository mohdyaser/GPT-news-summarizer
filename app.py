from flask import Flask, render_template, request, jsonify
from summarizer import chatGPT
from summarizer import extract_content

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = request.form['url']
    summary = chatGPT(userinput = extract_content(url))
    return jsonify(summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
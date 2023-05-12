import os
from flask import Flask, render_template, request, jsonify
from server import ClassroomServer

app = Flask(__name__)
server = ClassroomServer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instructor')
def instructor():
    return render_template('instructor.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/post_question', methods=['POST'])
def post_question():
    question = request.form.get('question')
    question_type = request.form.get('question_type')
    server.post_question(question, question_type)
    return jsonify(success=True)

@app.route('/get_question')
def get_question():
    return jsonify(server.get_question())

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form.get('answer')
    server.submit_answer(answer)
    return jsonify(success=True)

@app.route('/get_results')
def get_results():
    return jsonify(server.get_results())

@app.route('/results')
def show_results():
    results = server.get_results()
    if results:
        return render_template('results.html', question=results['question'],
                               question_type=results['question_type'],
                               answers=results['answers'])
    else:
        return "No results available."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)

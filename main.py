import os
from flask import Flask, render_template, request, jsonify, abort
from server import ClassroomServer

PASSWORD_FILE = 'password.txt'

app = Flask(__name__)

def values_filter(dictionary):
    return dictionary.values()
app.jinja_env.filters['values'] = values_filter

server = ClassroomServer()

@app.before_request
def check_instructor_auth():
    if request.path == '/instructor':
        if request.method == 'POST':
            password = request.form.get('password')
        else:
            password = request.args.get('password')
        with open(PASSWORD_FILE, 'r') as f:
            stored_password = f.read().strip()
        if password != stored_password:
            abort(401)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html')

@app.route('/instructor', methods=['GET', 'POST'])
def instructor():
    return render_template('instructor.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/post_question', methods=['POST'])
def post_question():
    question = request.form.get('question')
    question_type = request.form.get('question_type')
    choices = request.form.get('choices')
    server.post_question(question, question_type, choices)
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
                               answers=results['answers'],
                               choices=results.get('choices'))
    else:
        return "No results available."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)

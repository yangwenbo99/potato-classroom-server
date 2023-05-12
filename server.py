import time
from collections import defaultdict

class ClassroomServer:
    def __init__(self):
        self.questions = []
        self.current_question = None
        self.answers = defaultdict(list)
        self.start_time = time.time()

    def post_question(self, question, question_type):
        self.current_question = {
            'question': question,
            'question_type': question_type,
            'timestamp': time.time()
        }
        self.questions.append(self.current_question)
        self.answers[self.current_question['timestamp']] = []

    def get_question(self):
        if self.current_question:
            return {
                'question': self.current_question['question'],
                'question_type': self.current_question['question_type']
            }
        else:
            return None

    def submit_answer(self, answer):
        if self.current_question:
            self.answers[self.current_question['timestamp']].append(answer)
            print(self.answers)

    def get_results(self):
        if self.current_question:
            results = {
                'question': self.current_question['question'],
                'question_type': self.current_question['question_type'],
                'answers': self.answers[self.current_question['timestamp']]
            }
            return results
        else:
            return None

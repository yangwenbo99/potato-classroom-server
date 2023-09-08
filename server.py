import time
from collections import defaultdict

class ClassroomServer:
    def __init__(self):
        self.questions = []
        self.current_question = None
        self.answers = defaultdict(list)
        self.start_time = time.time()

    def post_question(self, question, question_type, choices=None):
        if choices is not None: 
            choices = choices.split('\n')
        self.current_question = {
            'question': question,
            'question_type': question_type,
            'choices': choices,
            'timestamp': time.time()
        }
        self.questions.append(self.current_question)
        self.answers[self.current_question['timestamp']] = []

    def get_question(self):
        if self.current_question:
            res = {
                'question': self.current_question['question'],
                'question_type': self.current_question['question_type']
            }
            if self.current_question['choices']: 
                res['choices'] = self.current_question['choices']
            return res
        else:
            return None

    def submit_answer(self, answer):
        if self.current_question:
            print(answer)
            if (self.current_question['question_type'] == 'poll' and
                answer in self.current_question['choices']):
                self.answers[self.current_question['timestamp']].append(answer)
            elif self.current_question['question_type'] != 'poll':
                self.answers[self.current_question['timestamp']].append(answer)

    def get_results(self):
        if self.current_question:
            results = {
                'question': self.current_question['question'],
                'question_type': self.current_question['question_type']
            }
            if self.current_question['question_type'] == 'poll':
                results['answers'] = {}
                for choice in self.current_question['choices']:
                    results['answers'][choice] = self.answers[
                        self.current_question['timestamp']].count(choice)
            else:
                results['answers'] = self.answers[
                    self.current_question['timestamp']]
            return results
        else:
            return None

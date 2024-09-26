class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Survey:
    def __init__(self, survey_id, title, description):
        self.survey_id = survey_id
        self.title = title
        self.description = description
        self.questions = []
        
    def add__question(self, question):
        self.questions.append(question)

class Question: 
    def __init__(self, question_id, text, question_type):
        self.question_id = question_id
        self.text = text
        self.question_type = question_type  

class Feedback:
    def __init__(self, feedback_id, user, car_model, feedback_text):
        self.feedback_id = feedback_id
        self.user = user
        self.car_model = car_model
        self.feedback_text = feedback_text
        self.category = self.assign_category()

    def assign_category(self):
        if 'comfort' in self.feedback_text:
            return 'Comfort'
        elif 'performance' in self.feedback_text:
            return 'Performance'
        else:
            return 'General'

class Response:
    def __init__(self, response_id, question, user, answer):
        self.response_id = response_id
        self.question = question
        self.user = user
        self.answer = answer

class SurveySummary:
    def __init__(self, survey):
        self.survey = survey
        self.responses = []
    
    def add_response(self, response):
        self.responses.append(response)

    def generate_summary(self):
        summary = {
            'total_responses': len(self.responses),
            'responses_by_question': {},
        }
        for response in self.responses:
            if response.question.text not in summary['responses_by_question']:
                summary['responses_by_question'][response.question.text] = []
            summary['responses_by_question'][response.question.text].append(response.answer)
        return summary

class FeedbackSystem:
    def __init__(self):
        self.users = {}
        self.surveys = {}
        self.feedbacks = {}

    def create_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users[user_id] = user
        return user

    def create_survey(self, survey_id, title, description):
        survey = Survey(survey_id, title, description)
        self.surveys[survey_id] = survey
        return survey

    def create_feedback(self, feedback_id, user_id, car_model, feedback_text):
        user = self.users.get(user_id)
        feedback = Feedback(feedback_id, user, car_model, feedback_text)
        self.feedbacks[feedback_id] = feedback
        return feedback

    def read_feedback(self, feedback_id):
        return self.feedbacks.get(feedback_id)

    def update_feedback(self, feedback_id, new_feedback_text):
        if feedback_id in self.feedbacks:
            feedback = self.feedbacks[feedback_id]
            feedback.feedback_text = new_feedback_text
            feedback.category = feedback.assign_category()
            return feedback
        return None

    def delete_feedback(self, feedback_id):
        if feedback_id in self.feedbacks:
            del self.feedbacks[feedback_id]

    def analyze_feedback(self):
        analysis = {}
        for feedback in self.feedbacks.values():
            category = feedback.category
            if category not in analysis:
                analysis[category] = []
            analysis[category].append(feedback.feedback_text)
        return analysis

system = FeedbackSystem()

user1 = system.create_user(1, 'Praveen', 'praveen@example.com')
user2 = system.create_user(2, 'Ajay', 'ajay@example.com')

survey1 = system.create_survey(1, 'Defender Feedback', 'Feedback on the Land Rover Defender')
survey2 = system.create_survey(2,'Safari Feedback','Feedback on the Tata Safari')

question1 = Question(1, "How satisfied are you with the Defender?", "Rating")
survey1.add__question(question1)

question2 =Question(2,"How satisfied are you with the Safari?","Rating")
survey2.add__question(question2)

feedback1 = system.create_feedback(1, user1.user_id, 'Defender', 'The performance is amazing  the 3000cc engine is monster but comfort could improve.')
feedback2 = system.create_feedback(2, user2.user_id, 'Safari', 'Very comfortable ride and great features power is like a beast .')

analysis = system.analyze_feedback()
print("Feedback Analysis:", analysis)

system.update_feedback(1, 'Performance is excellent, but I wish the comfort improved.')
system.update_feedback(2,'Very comfortable ride and great features power is like a beast .')
print("Updated Feedback:", system.read_feedback(1))
print("Updated Feedback:", system.read_feedback(2))

summary = SurveySummary(survey1)
summary.add_response(Response(1, question1, user1, 'Very satisfied right decision for buying this car'))
summary.add_response(Response(2, question1, user2, 'Satisfied by the comfort of driving its the best made in India suv'))

print("Survey Summary:", summary.generate_summary())

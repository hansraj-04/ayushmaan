class User:
    def _init_(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Survey:
    def _init_(self, survey_id, title, description):
        self.survey_id = survey_id
        self.title = title
        self.description = description
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

class Question:
    def _init_(self, question_id, text, question_type):
        self.question_id = question_id
        self.text = text
        self.question_type = question_type

class Feedback:
    def _init_(self, feedback_id, user, car_model, feedback_text):
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
    def _init_(self, response_id, question, user, answer):
        self.response_id = response_id
        self.question = question
        self.user = user
        self.answer = answer

class SurveySummary:
    def _init_(self, survey):
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
    def _init_(self):
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

def main():
    system = FeedbackSystem()

    while True:
        print("\nFeedback System")
        print("1. Create User")
        print("2. Create Survey")
        print("3. Create Feedback")
        print("4. Read Feedback")
        print("5. Update Feedback")
        print("6. Analyze Feedback")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            user_id = int(input("Enter User ID: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            user = system.create_user(user_id, name, email)
            print(f"User created: {user.name}")

        elif choice == '2':
            survey_id = int(input("Enter Survey ID: "))
            title = input("Enter Survey Title: ")
            description = input("Enter Survey Description: ")
            survey = system.create_survey(survey_id, title, description)
            print(f"Survey created: {survey.title}")

        elif choice == '3':
            feedback_id = int(input("Enter Feedback ID: "))
            user_id = int(input("Enter User ID for Feedback: "))
            car_model = input("Enter Car Model: ")
            feedback_text = input("Enter Feedback Text: ")
            feedback = system.create_feedback(feedback_id, user_id, car_model, feedback_text)
            print(f"Feedback created: {feedback.feedback_text}")

        elif choice == '4':
            feedback_id = int(input("Enter Feedback ID to read: "))
            feedback = system.read_feedback(feedback_id)
            if feedback:
                print(f"Feedback: {feedback.feedback_text} (Category: {feedback.category})")
            else:
                print("Feedback not found.")

        elif choice == '5':
            feedback_id = int(input("Enter Feedback ID to update: "))
            new_feedback_text = input("Enter new feedback text: ")
            updated_feedback = system.update_feedback(feedback_id, new_feedback_text)
            if updated_feedback:
                print(f"Updated Feedback: {updated_feedback.feedback_text} (Category: {updated_feedback.category})")
            else:
                print("Feedback not found.")

        elif choice == '6':
            analysis = system.analyze_feedback()
            print("Feedback Analysis:", analysis)

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
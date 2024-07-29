import datetime

class SimpleChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hi there! How can I help you today?",
            "hi":"Hi there how can i help you ?",
            "bye": "Goodbye! Have a nice day!",
            "how are you": "I'm just a bunch of code, but I'm doing great! How about you?",
            "name": "I'm a simple chatbot created as part of a project from codsoft",
            "help": "Yes ,  tell me what you wanna ask?"
        }
    def get_time(self):
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    def get_response(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input:
            return self.responses["hello"]
        elif "bye" in user_input:
            return self.responses["bye"]
        elif "how are you" in user_input:
            return self.responses["how are you"]
        elif "what's your name" in user_input:
            return self.responses["what's your name"]
        elif "help" in user_input:
            return self.responses["help"]
        elif "time" in user_input:
            return f"The current time is {self.get_time()}"
        elif "thank you" in user_input:
            return self.responses["thank you"]
        else:
            return "I'm currently learning can u rephrase it ?"

chatbot = SimpleChatbot()
def chat():
    bot = SimpleChatbot()
    print("Hii Welcome to Chatbot. you can Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

chat()

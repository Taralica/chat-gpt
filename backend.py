import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "_"

    def get_responce(self, user_input):
        responce = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens=3000,
            temperature=0.5

        ).choices[0].text
        return responce

if __name__ == "__main__":
    chatbot = Chatbot()
    responce = chatbot.get_responce("write a joke about the birds")
    print(responce)

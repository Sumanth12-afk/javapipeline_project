import json

def load_responses(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_response(user_input, responses):
    user_input = user_input.lower()  
    return next((q["response"] for q in responses["questions"] if q["question"].lower() == user_input), 
                "I'm sorry, I don't understand that.")

def main():
    responses = load_responses("responses.json")
    print("Welcome to ChatBot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input, responses)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()


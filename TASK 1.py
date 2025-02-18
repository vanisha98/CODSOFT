# TASK 1
def chatbot():
    print("Hello! I'm a simple chatbot. Type 'hello' to start the conversation.")

    user_inputs = ["hello", "how are you", "your name", "month name", "exit"]  # Simulated inputs
    for user_input in user_inputs:
        print(f"You: {user_input}")
        user_input = user_input.lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a wonderfull day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hii! How can I guide you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")
        elif "month name" in user_input:
            print("Chatbot: present month name is february.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()

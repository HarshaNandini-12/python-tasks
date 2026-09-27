def chatbot():
    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Bot: Hi!")
        elif message == "how are you":
            print("Bot: I'm fine, thanks!")
        elif message == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand.")

chatbot()
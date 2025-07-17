while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hello! How can I help you?")
    elif user == "what is the use of import random in python":
        print("Chatbot: It is used to access functions that generate random numbers or make random choices.")
    elif user == "who invented python?":
        print("Chatbot: Python was invented by Guido van Rossum.")
    elif user == "thank you" or user == "bye" or user == "thank you, bye":
        print("Chatbot: Here for you. Goodbye!")
        break
    else:
        print("Chatbot: Sorry, I didn't understand that.")

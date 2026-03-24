while True:
    user = input("You: ")
    if user.lower() in ["hi", "hello"]:
        print("Bot: Hello!")
    elif user.lower() == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I am learning...")

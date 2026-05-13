def chatbot():
    print(" Welcome to Customer Support Chatbot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        # Exit condition
        if user == "exit":
            print("Bot: Thank you! Have a great day ")
            break

        # Greetings
        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")

        # Order status
        elif "order" in user:
            print("Bot: Please provide your Order ID.")
            order_id = input("Order ID: ")
            print(f"Bot: Order {order_id} is being processed and will arrive soon.")

        # Refund
        elif "refund" in user:
            print("Bot: Refund will be processed within 5-7 working days.")

        # Product info
        elif "product" in user:
            print("Bot: We offer electronics, clothing, and accessories.")

        # Contact
        elif "contact" in user:
            print("Bot: You can contact us at support@example.com")

        # Default response
        else:
            print("Bot: Sorry, I didn't understand that. Please try again.")


# Run chatbot
chatbot()
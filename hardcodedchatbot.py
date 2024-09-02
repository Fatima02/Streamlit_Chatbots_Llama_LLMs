import streamlit as st
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "goodbye": "Goodbye! Have a great day!",
}
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    elif user_input in responses:
        print("Chatbot:", responses[user_input])
    else:
        print("Chatbot: I'm sorry, I don't understand that.")

user_input = st.text_input("You:")
if user_input:
    response = chatbot_response(user_input.lower())
    st.write("Chatbot:", response)
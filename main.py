import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am good, thank you!', 'I am doing well!', 'I am fine, thanks for asking!']],
    ['what is your name?', ['My name is ChatBot!', 'I am ChatBot, nice to meet you!']],
    ['bye|goodbye', ['Bye!', 'Goodbye!', 'See you later!']],
    ['default', ['I am not sure what you mean, can you please rephrase your question?']]
]

# Create the chatbot using the pairs of responses
chatbot = Chat(pairs, reflections)

# Define a function to handle user input and chatbot responses
def chatbot_response():
    user_input = input_box.get("1.0", tk.END)[:-1]
    response = chatbot.respond(user_input)
    output_box.configure(state='normal')
    output_box.insert(tk.END, "You: " + user_input + "\n\n")
    output_box.insert(tk.END, "ChatBot: " + response + "\n\n")
    output_box.configure(state='disabled')
    input_box.delete("1.0", tk.END)

# Create the tkinter interface
window = tk.Tk()
window.title("H3XChat")
window.geometry("400x500")

# Create the input box for user input
input_box = scrolledtext.ScrolledText(window, height=5, width=50)
input_box.pack(pady=10)

# Create the output box for chatbot responses
output_box = scrolledtext.ScrolledText(window, height=25, width=50)
output_box.pack(pady=10)
output_box.configure(state='disabled')

# Create the send button to trigger the chatbot response function
send_button = tk.Button(window, text="Send", command=chatbot_response)
send_button.pack()

# Start the tkinter event loop
window.mainloop()

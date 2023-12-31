import tkinter as tk
from tkinter import scrolledtext

class ChatBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Box")

        # Create a scrolled text widget to display the chat messages
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.chat_display.pack(padx=10, pady=10)

        # Create an entry widget for user input
        self.user_input = tk.Entry(root, width=40)
        self.user_input.pack(padx=10, pady=10)

        # Create a button to send messages
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=10)

    def send_message(self):
        # Get user input
        message = self.user_input.get()

        # Display the user's message in the chat box
        self.display_message(f"You: {message}")

        # Clear the user input
        self.user_input.delete(0, tk.END)

        # Simulate a response (you can replace this with actual logic to generate responses)
        response = "Bot: Thanks for your message!"

        # Display the bot's response in the chat box
        self.display_message(response)

    def display_message(self, message):
        # Insert the message into the chat display
        self.chat_display.insert(tk.END, f"{message}\n")

        # Autoscroll to the bottom of the chat display
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the ChatBoxApp class
    app = ChatBoxApp(root)

    # Run the Tkinter event loop
    root.mainloop()

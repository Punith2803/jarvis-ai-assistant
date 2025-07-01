import webbrowser

print("Hello, I am JARVIS — your personal AI Assistant.")
print("How can I help you today? (Type your command below)")

# Get user input
command = input(">>> ").lower()

# Handle basic commands
if "youtube" in command:
    print("Opening YouTube...")
    webbrowser.open("https://www.youtube.com")
elif "google" in command:
    print("Opening Google...")
    webbrowser.open("https://www.google.com")
elif "exit" in command:
    print("Goodbye! Have a nice day.")
else:
    print("Sorry, I don't understand that command yet.")

import tkinter as tk
from main import start_hand_track

def quit_window():
    window.destroy()

def start_hand_gesture():
    name = str(saved_contact_name.get())
    mess = str(message_entry.get())
    window.destroy()  # Close the tkinter window
    start_hand_track(name, mess)  # Start the hand gesture tracking function

window = tk.Tk()
window.title("Hand Gesture Tracker")
window.geometry("600x650")  # Set the window size
window.configure(background='#87CEEB')  # Light blue color

# Create labels and entry fields
phone_number_label = tk.Label(window, text="Contact Saved", font=("Arial", 20, "italic", "bold"), fg="black", bg='#87CEEB')
phone_number_label.pack(pady=20)
saved_contact_name = tk.Entry(window, width=30, font=("Arial", 20, "italic"), fg="black", bg="white", highlightthickness=2, highlightcolor="black", highlightbackground="black")
saved_contact_name.pack(pady=20)

message_label = tk.Label(window, text="Message:", font=("Arial", 20, "italic", "bold"), fg="black", bg='#87CEEB')
message_label.pack(pady=20)
message_entry = tk.Entry(window, width=30, font=("Arial", 20, "italic"), fg="black", bg="white", highlightthickness=2, highlightcolor="black", highlightbackground="black")
message_entry.pack(pady=20)

# Create buttons
start_button = tk.Button(window, text="Start Hand Gesture", command=start_hand_gesture, font=("Arial", 20, "italic", "bold"), fg="black", bg="#C6F7D0", height=2, width=20)
start_button.pack(pady=20)

quit_button = tk.Button(window, text="Quit", command=quit_window, font=("Arial", 20, "italic", "bold"), fg="black", bg="#FFC5C5", height=2, width=20)
quit_button.pack(pady=20)

window.mainloop()
import cv2
import mediapipe as mp
from message_2 import send_message
import tkinter as tk 
import time
from PIL import Image, ImageTk

def start_hand_track(Check):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Create a hand detector using MediaPipe
    hand_detector = mp.solutions.hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    # Replace with your WhatsApp phone number (including country code)
    # phone_number = "+91 9219083613"

    # Replace with the name of the contact you want to send the message to
    # contact_name = "Chuwii 👻"

    # Replace with the message you want to send
    # message = "Hello from Python!"

    while Check == True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Flip the frame horizontally to mirror the real hand
        frame = cv2.flip(frame, 1)

        # Convert the frame from BGR to RGB (required by MediaPipe)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame using the hand detector
        output = hand_detector.process(rgb_frame)

        # Get the detected hand landmarks
        hands = output.multi_hand_landmarks

        # Draw the hand landmarks on the original frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if hands:
            # Iterate through each hand
            for hand in hands:
                mp_draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)

                # Get the individual landmarks for the hand
                landmarks = hand.landmark

                # Get the coordinates of the yellow circled index (id=8)
                yellow_x = int(landmarks[8].x * frame.shape[1])
                yellow_y = int(landmarks[8].y * frame.shape[0])

                # Get the coordinates of the blue circled index (id=5)
                blue_x = int(landmarks[5].x * frame.shape[1])
                blue_y = int(landmarks[5].y * frame.shape[0])

                # Calculate the distance between the yellow and blue circled indices
                distance = ((yellow_x - blue_x) ** 2 + (yellow_y - blue_y) ** 2) ** 0.5

                # If the distance is low, send a message to the contact
                if distance < 50:
                    send_message(name,mess)
                    print("Message sent! to the user succesfully")

        # Convert the frame back to BGR for display
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Display the output
        cv2.imshow('Hand Tracking', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            Check=False
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

def quit_window():
    window.destroy()

def start_hand_gesture():
    global mess 
    global name
    name = str(saved_contact_name.get())
    mess = str(message_entry.get())
    window.destroy()  # Close the tkinter window
    start_hand_track(True)  # Start the hand gesture tracking function

# Load the image from the subdirectory
image_path = "Designer (2).png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create the main window
window = tk.Tk()
window.title("Hand Gesture Tracker")
window.geometry("600x650")  # Set the window size
window.configure(background='#87CEEB')  # Light blue color

# Load the image from the subdirectory
image_path = "Designer (2).png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(window, image=photo)
image_label.pack()

# Define a function to fade in the image
def fade_in():
    for i in range(26):
        image_label.image = photo  # Keep a reference to the image
        image_label.config(bg=f"#87CEEB{hex(i*10)[2:].zfill(2)}")  # Adjusting alpha by modifying the background color
        window.update()
        time.sleep(0.1)

# Define a function to fade out the image
def fade_out():
    for i in range(25, -1, -1):
        image_label.config(bg=f"#87CEEB{hex(i*10)[2:].zfill(2)}")  # Adjusting alpha by modifying the background color
        window.update()
        time.sleep(0.1)
    image_label.pack_forget()  # Remove the image label
    show_main_ui()  # Show the main UI after fade-out

# Function to show the main UI
def show_main_ui():
    # Create labels and entry fields
    phone_number_label = tk.Label(window, text="Contact Saved", font=("Arial", 20, "italic", "bold"), fg="black", bg='#87CEEB')
    phone_number_label.pack(pady=20)
    global saved_contact_name
    saved_contact_name = tk.Entry(window, width=30, font=("Arial", 20, "italic"), fg="black", bg="white", highlightthickness=2, highlightcolor="black", highlightbackground="black")
    saved_contact_name.pack(pady=20)

    message_label = tk.Label(window, text="Message:", font=("Arial", 20, "italic", "bold"), fg="black", bg='#87CEEB')
    message_label.pack(pady=20)
    global message_entry
    message_entry = tk.Entry(window, width=30, font=("Arial", 20, "italic"), fg="black", bg="white", highlightthickness=2, highlightcolor="black", highlightbackground="black")
    message_entry.pack(pady=20)

    # Create buttons
    start_button = tk.Button(window, text="Start Hand Gesture", command=start_hand_gesture, font=("Arial", 20, "italic", "bold"), fg="black", bg="#C6F7D0", height=2, width=20)
    start_button.pack(pady=20)

    quit_button = tk.Button(window, text="Quit", command=quit_window, font=("Arial", 20, "italic", "bold"), fg="black", bg="#FFC5C5", height=2, width=20)
    quit_button.pack(pady=20)

# Fade in the image when the window is opened
fade_in()

# Bind the fade out function to a click event on the window
window.bind("<Button-1>", lambda event: fade_out())

window.mainloop()
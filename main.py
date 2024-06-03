import cv2
import mediapipe as mp
from message_2 import send_message
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super(MainUI, self).__init__(**kwargs)
        # self.background_color = (0.529, 0.807, 0.917, 1)
        self.orientation = 'vertical'
        self.spacing = 10  # Reduce the spacing between widgets
        self.padding = 20

        # self.Name = Label(text='[i][b]Automatic Message Sender[/b][/i]', color = [0,0,1,0],font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.95},markup=True)
        # self.add_widget(self.Name)
        
        self.phone_label = Label(text='[i]Contact Saved:[/i]', color = [0,0,0,1],font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.9},markup=True)
        self.add_widget(self.phone_label)

        self.contact_name = TextInput(hint_text='Enter contact name', multiline=False, size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.85}, padding='3dp')  # Add padding to the TextInput
        self.add_widget(self.contact_name)

        self.message_label = Label(text='[i]Message:[/i]',color = [0,0,0,1], font_size=24+6, pos_hint={'center_x': 0.5, 'center_y': 0.5}, markup=True)
        self.add_widget(self.message_label)

        self.message_entry = TextInput(hint_text='Enter message', multiline=True, size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.45}, padding='3dp')  # Add padding to the TextInput
        self.add_widget(self.message_entry)
        
        self.start_button = Button(text='[i][b]Start Hand Gesture[/b][/i]', size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.1}, background_color=[1, 0, 0, 0.7], color=[0, 0, 0, 1], markup=True)
        self.start_button.bind(on_press=self.start_hand_gesture)
        self.add_widget(self.start_button)
        
        self.quit_button = Button(text='[i]Quit[/i]', size_hint=(None, None), size=(300, 60), pos_hint={'center_x': 0.5, 'center_y': 0.05}, background_color=[0, 1, 0, 0.7], color=[0, 0, 0, 1], markup=True)
        self.quit_button.bind(on_press=self.quit_application)
        self.add_widget(self.quit_button)
    
    def start_hand_gesture(self, instance):
        global name, mess
        name = self.contact_name.text
        mess = self.message_entry.text
        # Close the Kivy app
        App.get_running_app().stop()
        # Start hand tracking
        start_hand_track(True)
        
    def quit_application(self, instance):
        App.get_running_app().stop()

class LogoWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(LogoWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.image = Image(source='Designer (2).png', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image)
        
        Clock.schedule_once(self.fade_in, 1)
    
    def fade_in(self, dt):
        fade_in = Animation(opacity=1, duration=3)
        fade_in.start(self.image)
        self.image.bind(on_touch_down=self.on_logo_touch)
    
    def on_logo_touch(self, instance, touch):
        if self.collide_point(*touch.pos):
            self.fade_out()
    
    def fade_out(self):
        fade_out = Animation(opacity=0, duration=3)
        fade_out.bind(on_complete=self.switch_to_main)
        fade_out.start(self.image)
    
    def switch_to_main(self, *args):
        app = App.get_running_app()
        app.root.clear_widgets()
        app.root.add_widget(MainUI())

class MyApp(App):
    def build(self):
        Window.clearcolor = (0.8, 0.6, 0.6, 1) # Set the background color here
        root = BoxLayout(orientation='vertical')
        root.add_widget(LogoWidget())
        return root

def start_hand_track(Check):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Create a hand detector using MediaPipe
    hand_detector = mp.solutions.hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    while Check:
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
                    send_message(name, mess)
                    print("Message sent to the user successfully")

        # Convert the frame back to BGR for display
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Display the output
        cv2.imshow('Hand Tracking', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            Check = False
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    MyApp().run()

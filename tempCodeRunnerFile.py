def send_message(name,mess):
    import pyautogui
    import time
    
    # Open WhatsApp desktop application
    pyautogui.press('winleft')  # Open Start menu (Windows) or Command + Space (Mac)
    pyautogui.typewrite('WhatsApp')  # Type WhatsApp in the search bar
    pyautogui.press('enter')  # Open WhatsApp
    
    # Open WhatsApp desktop application using Windows key + 7
    # pyautogui.hotkey('winleft', '7')
    # time.sleep(2)  # Wait for WhatsApp to open
    
    
    
    # Wait for WhatsApp to load
    time.sleep(5)
    
    # Simulate Ctrl+F shortcut to search for the recipient's name
    pyautogui.hotkey('ctrl', 'f')
    
    # Type the recipient's name
    pyautogui.typewrite(name)
    
    
    # Move the mouse to the search result
    # pyautogui.moveTo(263, 234)  # Adjust the coordinates to match your screen
    # time.sleep(1)
    # pyautogui.click()
    #opened the chat now will type the message 
    
    # Simulate down arrow key press to select the search result
    pyautogui.press('down') 
    pyautogui.press('enter')
    time.sleep(0.5)
    # to open the chat another approach 
    
    
    # pyautogui.press('enter')
    time.sleep(1.2)
    
    # Click on the chat window
    # pyautogui.click(300, 200)  # Adjust the coordinates to match your screen
    
    # Type the message
    pyautogui.typewrite(mess)
    pyautogui.press('enter')
    
    # Wait for the message to be sent
    time.sleep(2)
    
    # Close the WhatsApp window
    pyautogui.hotkey('alt', 'f4')
    
    exit
    
send_message('Aditya','Hey another test message ')
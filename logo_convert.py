from PIL import Image

# Load the PNG file
filename = r'Main_Logo.png'
img = Image.open(filename)

# Save it as an ICO file
img.save('logo.ico')

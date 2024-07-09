import gtts as gt
import os

# Specify the path to your text file
text_file_path = "output_text.txt"

# Open the text file in read mode
with open(text_file_path, "r") as text_file:
  # Read the entire content of the file
  text = text_file.read()

# Convert text to speech
tts = gt.gTTS(text=text)
print("@@@@@@@@@ Text Are converting Into MP3 File @@@@@@@@@@@@@")

# Save the audio file
tts.save("dravit.mp3")
print("@@@@@@@@@ Text Are Saved Into MP3 File @@@@@@@@@@@@@")

# Play the audio using the system command (optional)
os.system("dravit.mp3")

print("@@@@@@@@@  Spoke Text @@@@@@@@@@@@@")
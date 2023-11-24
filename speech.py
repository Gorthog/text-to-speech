import os
import constants
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = constants.APIKEY

client = OpenAI()

audio_file = open("audio/speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

if not os.path.exists('text'):
  # Create the directory
  os.mkdir('text')

# Write transcript.text to a file
with open("text/speech.txt", "w") as file:
    file.write(transcript.text)


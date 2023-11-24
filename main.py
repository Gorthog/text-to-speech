import os
import constants
import sys
from pathlib import Path
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = constants.APIKEY
text = sys.argv[1]

client = OpenAI()

# Check if the directory does not exist
if not os.path.exists('audio'):
  # Create the directory
  os.mkdir('audio')

speech_file_path = Path(__file__).parent / "audio" / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input=text
)
response.stream_to_file(speech_file_path)

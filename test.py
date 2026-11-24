from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from dotenv import load_dotenv
load_dotenv()
source="https://www.youtube.com/watch?v=7pJ0Rjh5V1o"
language="hinglish"

chunks=process_input(source)
transcript=transcribe_all(chunks,language=language)
print("\n===TRANSCRIPT===\n")
print(transcript)
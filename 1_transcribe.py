import transformers
import json

# Transcribe audio file
transcriber = transformers.pipeline(task='automatic-speech-recognition', model='openai/whisper-large-v2', device='cuda',
                                    chunk_length_s=30, return_timestamps=True)
transcript = transcriber('TL1_VO_1-2_Gleichgewicht.mp4')

# Export transcript to JSON
with open('transcript.json', 'w') as f:
    json.dump(transcript, f)

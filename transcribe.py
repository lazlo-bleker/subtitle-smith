import transformers
import json

models = {'whisper': 'openai/whisper-large-v2',
          'wav2vec2': 'facebook/wav2vec2-large-960h-lv60-self'}

transcriber = transformers.pipeline(task='automatic-speech-recognition', model=models['whisper'], device='cuda',
                                    chunk_length_s=30, return_timestamps=True)
transcript = transcriber('TL1_VO_1-2_Gleichgewicht.mp4')
print(transcript)
with open('transcript.json', 'w') as f:
    json.dump(transcript, f)

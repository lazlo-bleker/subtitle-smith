import transformers
import json

model = 'Helsinki-NLP/opus-mt-en-de'

# Read files
with open('transcript.srt', 'r', encoding='utf-8') as f:
    transcript_srt = f.read()
with open('transcript.json', 'r') as f:
    transcript = json.load(f)

# Prepare marked english text
english_text = transcript_srt.split('\n')
timestamps = english_text[1::4]
text_chunks = english_text[2::4]
english_text_marked = ''
for i in range(len(text_chunks)):
    english_text_marked += f' (T1M3STMP_{i + 1}) '
    english_text_marked += text_chunks[i]
english_text_marked = english_text_marked.split('. ')
for i in range(len(english_text_marked) - 1):
    english_text_marked[i] += '.'
english_text_marked[0] = english_text_marked[0][1:]

# Translate text
translator = transformers.pipeline('translation', model='Helsinki-NLP/opus-mt-en-de', device='cuda')
translation = translator(english_text_marked)

# Post process translated text
german_text_marked = ''
for i in range(len(translation)):
    german_text_marked += ' ' + translation[i]['translation_text']
german_text_marked = german_text_marked[1:]
german_text = german_text_marked.split('(T1M3STMP_')
german_text.pop(0)
if len(german_text) == len(timestamps):
    print(f'OK: Number of text chunks ({len(german_text)}) == number of timestamps ({len(timestamps)})\n'
          f'Manual postprocessing of translated transcript is not required.')
else:
    print(f'WARNING: Number of text chunks ({len(german_text)}) != number of timestamps ({len(timestamps)})\n'
          f'Manual postprocessing of translated transcript is required.')

# Add SRT timestamps to transcript.json
transcript['timestamps_srt'] = timestamps
with open('transcript.json', 'w') as f:
    json.dump(transcript, f)

# Export TXT files
with open('translation_raw.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(german_text))
with open('transcript.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(text_chunks))

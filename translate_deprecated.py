import json
import transformers

# Load JSON file
with open('transcript.json', 'r') as f:
    transcript = json.load(f)

# Translate full text
english_text = transcript['text'].split('. ')
for i in range(len(english_text)):
    if english_text[i][-1] != '.':
        english_text[i] += '.'
translator = transformers.pipeline('translation', model="Helsinki-NLP/opus-mt-en-de", device='cuda')
translation = translator(english_text)
german_text = ''
for i in range(len(translation)):
    german_text += ' ' + translation[i]['translation_text']
transcript['translation'] = german_text

# Add translation to JSON file
with open('transcript.json', 'w') as f:
    json.dump(transcript, f)

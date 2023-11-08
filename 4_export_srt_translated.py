import json

# Read files
with open('translation_raw.txt', 'r', encoding='utf-8') as f:
    translation_raw = f.read()
with open('transcript.json', 'r') as f:
    transcript = json.load(f)

# Remove embedded timestamps
translation = translation_raw.split('\n')
for i in range(len(translation)):
    line = translation[i]
    for j in range(len(line)):
        char = line[j]
        if char.isalpha():
            translation[i] = line[j:]
            break
if len(translation) != len(transcript['timestamps_srt']):
    raise Exception(f'Number of text chunks ({len(translation)}) != number of timestamps'
                    f'({len(transcript["timestamps_srt"])})\nManual postprocessing of translated transcript is'
                    f'required.')

# Export SRT file
with open('translation.srt', 'w', encoding='utf-8') as f:
    pass
for i in range(len(translation)):
    chunk_id = i + 1
    srt_chunk = f"{chunk_id}\n{transcript['timestamps_srt'][i]}\n{translation[i]}\n\n"
    with open('translation.srt', 'a', encoding='utf-8') as f:
        f.write(srt_chunk)

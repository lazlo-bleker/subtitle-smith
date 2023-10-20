import datetime
import json


def convert_time(s):
    time = f'0{datetime.timedelta(seconds=int(s))},{int(1000*round(s%1, 2)):03}'
    return time


with open('transcript.json', 'r') as f:
    transcript = json.load(f)

chunk_id = 1
chunks = transcript['chunks']
for i in range(len(chunks)):
    start_time = convert_time(chunks[i]['timestamp'][0])
    end_time = convert_time(chunks[i]['timestamp'][1])
    text = chunks[i]['text']
    srt_chunk = f"{chunk_id}\n{start_time} --> {end_time}\n{text[1:] if text[0] is ' ' else text}\n\n"
    chunk_id += 1

    with open('transcript.srt', 'a', encoding='utf-8') as f:
        f.write(srt_chunk)
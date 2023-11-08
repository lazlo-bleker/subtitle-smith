# SubtitleSmith

Automatic subtitle generator in SRT format from any to any language with [`Whisper`](https://openai.com/research/whisper) and [`Helsinki-NLP`](https://huggingface.co/Helsinki-NLP). Originally developed for creating automatic German subtitles of the English lectures of Tragwerkslehre/Building Structures at TUM.

## Installation Requirements

- Ensure you have [`FFmpeg`](https://www.ffmpeg.org/download.html) installed and added to your system PATH.

## File Structure

- `1_transcribe.py`: Generates a `transcript.json` file containing the transcript (in source language) of an audio file located in the main directory.
- `2_export_srt.py`: Creates a `transcript.srt` file from the `transcript.json` file generated by `transcribe.py`.
- `3_translate_srt.py`: Creates a `translation_raw.txt` file with a translation of the transcript from `transcript.srt`.
- `4_export_srt_translated.py`: Creates a `translation.srt` file from `translation_raw.txt`.

## Usage

Place an audio/video file in the main directory and run the following command to create a transcript:

```bash
python 1_transcribe.py
```

This will create a transcript.json file in the main directory.

Run the following command to create an SRT file from the transcript (in source language):

```bash
python 2_export_srt.py
```

Make sure to set a translation model with the correct source language and desired target language in `3_translate_srt.py`. Run the following command to create a translation of the transcript:

```bash
python 3_translate_srt.py
```

Occosionally the translation model misses certain timestamps merging two lines of the translated transcript. After correcting these mistakes, run the following command to create a translated transcript SRT file:

```bash
python 4_export_srt_translated.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

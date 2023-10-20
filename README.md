# Transcriber

Automatic machine transcription with Whisper. Originally develepod for automatic transcription (and German translation) of the English lectures of Tragwerkslehre/Building Structures at TUM.

## Installation Requirements

- Ensure you have [`FFmpeg`](https://www.ffmpeg.org/download.html) installed and added to your system PATH.

## File Structure

- `transcribe.py`: Generates a `transcript.json` file containing the transcript of an audio file located in the main directory.
- `export_srt.py`: Creates a `transcript.srt` file from the `transcript.json` file generated by `transcribe.py`.
- `translate.py`: Adds a German translation of the transcript to the `transcript.json` file.

## Usage

Place an audio file in the main directory and run the following command to create a transcription:

```bash
python transcribe.py
```

This will create a transcript.json file in the main directory.

Run the following command to create an SRT file from the transcript:

```bash
python export_srt.py
```

Optionally, run the following command to add a German translation to the transcript:

```bash
python translate.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

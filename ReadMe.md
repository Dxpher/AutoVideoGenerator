# Project Overview:
This Python project reads a news article, generates a summary and keywords using OpenAI's GPT-3.5 API, and converts the text summary into an audio file using Google Text-to-Speech (gTTS). It creates a short format portrait video in the form of slideshow with narration ,background music, images, and zoom effects. The final output is a video with the generated audio and keywords, along with a zoom effect applied to the images.

## Dependencies

To get started, ensure that the following Python libraries are installed:

- `moviepy`
- `opencv-python`
- `numpy`
- `openai`
- `gtts`

You can install these dependencies by running:

```bash
pip install -r requirements.txt
```
## Folder Structure:
Before running the project, ensure that you have the following folder structure. You can create these folders in your project directory:

- **text_folder**: Contains the input text files that include news articles for processing.
- **news_content**: Stores the news content files that are summarized and used for keyword extraction.
- **key_words_generated**: Folder where the extracted keyword files are stored.
- **audio_folder**: Contains the generated audio files converted from text.
- **img_folder**: Stores the images used for the video slideshow.
- **vid_folder**: The final output video is saved in this folder.
- **subtitles**: Stores the generated subtitles in SRT format.
- **bg_image_logo**: Contains background videos and logos used in the final video.

# Note that the paths used in the main code need to be customized according to the project's file structure.

## API Setup
To use OpenAI's API for generating summaries and keywords, you'll need an OpenAI API key. Set up the key as an environment variable:

Get the open Api key and save it in the running env:
```bash
setx open_ai_key "YOUR_OPENAI_API_KEY"
```
## Usage
1. Place News Article Files: Put your text files containing news articles into the `news_content` folder.
2. Place Images: Add images for the slideshow in the `img_folder`.
3. Run the Program: Execute the Python script to generate a video with audio, summaries, and keywords. The final video will be saved in the `vid_folder`.
4. Generate Subtitles (Optional): Subtitles will be generated and saved in the `subtitles` folder in SRT format.

## Output Files
- **Summary:** Summaries are saved in the `text_folder` as `.txt` files.
- **Keywords:** Keywords are generated and saved in the `key_words_generated` folder.
- **Audio:** The generated audio from the summary will be saved in the `audio_folder`.
- **Final Video:** The video combining images, audio, and effects will be saved in the `vid_folder` with a `.mp4` extension.
- **Subtitles:** If subtitles are generated, they will be saved as `.srt` files in the `subtitles` folder.


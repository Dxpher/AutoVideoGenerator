# Project Overview:
This Python project reads a news article, generates a summary and keywords using OpenAI's GPT-3.5 API, and converts the text summary into an audio file using Google Text-to-Speech (gTTS). It also creates a video slideshow with background music, images, and zoom effects. The final output is a video with the generated audio and keywords, along with a zoom effect applied to the images.

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
               ``` sample
                ├───text_folder           # Contains the input text files (news articles)
                ├───news_content          # Stores news content files for summarization
                ├───key_words_generated   # Where keyword files will be stored
                ├───audio_folder          # Stores the generated audio files
                ├───img_folder            # Contains images for the video slideshow
                ├───vid_folder            # The final output video will be saved here
                ├───subtitles             # Stores generated subtitles (SRT files)
                └───bg_image_logo         # Contains background videos and logos```
# Note that the paths to be use in the main code need to be customize according to the implementation of the File structure of the project.

## API Setup
To use OpenAI's API for generating summaries and keywords, you'll need an OpenAI API key. Set up the key as an environment variable:

Get the open Api key and save it in the running env:
```bash
setx open_ai_key "YOUR_OPENAI_API_KEY"
```
## Usage
1: Place News Article Files: Put your text files containing news articles into the news_content folder.
2: Place Images: Add images for the slideshow in the img_folder.
3: Run the Program: Execute the Python script to generate a video with audio, summaries, and keywords. The final video will be saved in the vid_folder.
4: Generate Subtitles (Optional): Subtitles will be generated and saved in the subtitles folder in SRT format.
## Output Files
-> Summary: Summaries are saved in the text_folder as .txt files.
-> Keywords: Keywords are generated and saved in the key_words_generated folder.
-> Audio: The generated audio from the summary will be saved in the audio_folder.
-> Final Video: The video combining images, audio, and effects will be saved in the vid_folder with a .mp4 extension.
-> Subtitles: If subtitles are generated, they will be saved as .srt files in the subtitles folder.

# all the libs
#Contributer: Aditya Tiwari
from moviepy.editor import *
import os,cv2,datetime,openai
import numpy as np
from gtts import gTTS
##
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
text_file = "C:\\Users\\HP\\Desktop\\sample\\text_folder"
##
# -----------------Zoom effect function---------------


#------------------summary and keyword generating function---------
openai.api_key = os.environ["open_ai_key"]
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def getting_summary_keywords(news_content_file):

    with open(news_content_file,encoding='utf-8') as file1:
     news = file1.read() 
    # Summary generation

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "user", "content" : "you are a pro summarizer, write a concise \
                and comprehensive summary of following news article not more than 50 words: News article is: \ " + news}
        ],
        max_tokens = 3000
    )
    # print(response)

    summary = response["choices"][0]["message"]["content"]
    text_folder = "C:\\Users\\HP\\Desktop\\sample\\text_folder"  #audio folder path
    output_file = os.path.join(text_folder, f"output_{timestamp}.txt")
    file2=open(output_file,"w",encoding='utf-8')
    file2.write(summary)
    file2.close()

    # Keyword Extractor

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "user", "content" : """You are a pro keyword extractor like natural language 
            processing toolkit. you have to extract keywords from news article, if two more words 
            have similar meaning like good and nice consider them same. give the keywords order 
            in most frequent to least frequent, extract just exactly 5 to 6 keywords. Just return the 
            keywords in an array separated by space.
            For example give response like: 
            Environment tree plant earth.
            The article is :""" + summary}
        ],
        max_tokens = 3000
    )
    # print(response)

    keywords = response["choices"][0]["message"]["content"]
    # print(keywords)  #Keywords

    b = str(keywords)

    keyword = b.split(", ")
    # Final Keywords
    key_folder="C:\\Users\\HP\\Desktop\\sample\\key_words_generated"
    #print("Keywords:  ")
    #print(keyword)
    output_file_keyword = os.path.join(key_folder, f"output_{timestamp}.txt")
    file3=open(output_file_keyword, "w",encoding='utf-8')
    file3.write(keywords)
    file3.close
    
    # for i in keyword:
    #     print(i)

#-----------------------------------------------------
def Zoom(clip, mode='in', position='center', speed=1):
    fps = clip.fps
    duration = clip.duration
    total_frames = int(duration * fps)
    
    def main(getframe, t):
        frame = getframe(t)
        h, w = frame.shape[:2]
        i = t * fps
        if mode == 'out':
            i = total_frames - i
        zoom = 1 + (i * ((0.1 * speed) / total_frames))
        positions = {'center': [(w - (w * zoom)) / 2, (h - (h * zoom)) / 2],
                     'left': [0, (h - (h * zoom)) / 2],
                     'right': [(w - (w * zoom)), (h - (h * zoom)) / 2],
                     'top': [(w - (w * zoom)) / 2, 0],
                     'topleft': [0, 0],
                     'topright': [(w - (w * zoom)), 0],
                     'bottom': [(w - (w * zoom)) / 2, (h - (h * zoom))],
                     'bottomleft': [0, (h - (h * zoom))],
                     'bottomright': [(w - (w * zoom)), (h - (h * zoom))]}
        tx, ty = positions[position]
        M = np.array([[zoom, 0, tx], [0, zoom, ty]])
        frame = cv2.warpAffine(frame, M, (w, h))
        return frame
    
    return clip.fl(main)
#-------------------------------------------------------



#------------------getting newest file------------------

def get_newest_file_path(directory_path):
    newest_file = None
    newest_mtime = 0

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)

            # Compare modification time with the current newest file
            if file_mtime > newest_mtime:
                newest_mtime = file_mtime
                newest_file = file_path

    return newest_file

#----------------------------------------------------------
#------------------getting the newest folder---------------

def get_newest_folder_path(directory_path):
    newest_folder = None
    newest_mtime = 0

    for root, dirs, files in os.walk(directory_path):
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            folder_mtime = os.path.getmtime(folder_path)

            if folder_mtime > newest_mtime:
                newest_mtime = folder_mtime
                newest_folder = folder_path

    return newest_folder
#--------------deleting files-----------------------------------------------------------------------------
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} has been deleted successfully.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while deleting {file_path}: {e}")
#---------------------creating summary and keywords and saving them in a folder---------------------------
getting_summary_keywords(get_newest_file_path("C:\\Users\\HP\\Desktop\\sample\\news_content"))

#------------------generating audio------------------
def voicegeneration(a):
# Reading the text from the file
 with open(a,encoding='utf-8') as file:
     text = file.read()

 # Specifying the path to the audio folder
 audio_folder = "C:\\Users\\HP\Desktop\\sample\\audio_folder"  #audio folder path
 output_file = os.path.join(audio_folder, f"output_{timestamp}.mp3")
 # Createing a gTTS object
 tts = gTTS(text, slow=False)  # Set slow=True for a slower speed
 # Saveing the speech to the audio folder with a unique name
 tts.save(output_file)
voicegeneration(get_newest_file_path(text_file))
"""

for multi language

lang_indian = {
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Telugu': 'te',
    'Marathi': 'mr',
    'Tamil': 'ta',
    'Urdu': 'ur',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Odia': 'or',
    'Punjabi': 'pa',
    'Malayalam': 'ml',
    'Assamese': 'as',
    'Maithili': 'mai',
    'Santali': 'sat'
}
"""

#----------------------text to srt file--------------------------------
def txt_to_srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.read().strip().split('\n\n')

    srt_lines = []

    for index, line in enumerate(lines, start=1):
        srt_lines.append(str(index))
        content_lines = line.strip().split('\n')
        srt_lines.extend(content_lines)

    srt_content = '\n\n'.join(srt_lines)

    with open(output_file, 'w', encoding='utf-8') as srt_file:
        srt_file.write(srt_content)
#subtitles-------------------------------------------------------------------------------------------------------------------
subtitle_folder="C:\\Users\\HP\\Desktop\\sample\\subtitles"
subtitles_file_txt=get_newest_file_path("C:\\Users\HP\\Desktop\\sample\\text_folder")
subtitle_file_srt=os.path.join(subtitle_folder, f"output_{timestamp}.srt")

txt_to_srt(subtitles_file_txt,subtitle_file_srt)

# ----------------List of file paths------------------------------------------------------------------------------------------
image_folder = get_newest_folder_path("C:\\Users\\HP\\Desktop\\sample\\img_folder")  #image folder path

output_folder = "C:\\Users\\HP\\Desktop\\sample\\vid_folder" #output folder path------------------------------<<<<<<<<o/p>>>>>>>>
# Generate a unique output video name using the current timestamp
output_video = os.path.join(output_folder, f"output_{timestamp}.mp4")
# Adding audio from "aud_folder"
audio_folder_speech = "C:\\Users\\HP\\Desktop\\sample\\audio_folder"  #audio folder path

# getting the top audio file path
audio_file_speech = get_newest_file_path(audio_folder_speech)
audio_clip_speech = AudioFileClip(audio_file_speech)

audio_path_bg_music= "C:\\Users\\HP\\Desktop\\sample\\bg_music\\audio\\dramatic-reveal-21469.mp3"
audio_clip_bg_music = AudioFileClip(audio_path_bg_music)
audio_clip_bg_music = afx.audio_loop(audio_clip_bg_music, duration=audio_clip_speech.duration).volumex(.5).audio_fadein(3).audio_fadeout(3)
#adding these bg and speech together
audio_final=CompositeAudioClip([audio_clip_speech.volumex(2),audio_clip_bg_music])
#---------------------------------------------------------------------------------------------------------

#----------------creating background template-----------------------------------------------------------------------------------
bg = "C:\\Users\\HP\\Desktop\\sample\\bg_image_logo\\vid_bg2.mp4"
bg_clip = VideoFileClip(bg)
#bg_clip = ImageClip(bg, duration=audio_final.duration)
w, h =  bg_clip.size
bg_clip=vfx.crop(bg_clip, width=(h//16)*9, height=h,  x_center=w/2, y_center=h/2).loop(duration=audio_final.duration).margin(4,color=(255,255,255))
#adding final audio to bg_clip music optional

bg_clip = bg_clip.set_audio(audio_final)
# ------------------Accessing path of each imageand making a list of imageclips-------------------------------------------------
img_clips = []
logo_duration=0
for image in os.listdir(image_folder):
    clip_duration=logo_duration=(bg_clip.duration)/(len(os.listdir(image_folder))+1)
    
    valid_extensions = (".jpg", ".jpeg", ".png")
    if image.endswith(valid_extensions):
        img_path = os.path.join(image_folder, image)
        slide = ImageClip(img_path, duration=clip_duration).margin( 6,color=(0,0,0)).set_pos(('center','center'))  
        # Each image will be displayed for equal intervals clip_duration , with margin of 6 px all diretion and center position
        a,b=slide.size
        slide=slide.resize(((h*9)/(a*16)),((h)/(b*2))).fadein(clip_duration/10,1)#.fadeout(slide_duration/10,1)
        img_clips.append(slide)
#creating logo
logo=ImageClip("C:\\Users\\HP\\Desktop\\sample\\bg_image_logo\\BPI_logo.jpg",duration=logo_duration,).margin( 6,color=(255,255,255),opacity=1.0).set_pos(('center','center'))
a,b=logo.size
logo=logo.resize(((h*9)/(a*16)),((h)/(b*2))).fadein(logo_duration/10,1)#.fadeout(logo_duration/10,1)

#adding logo to slide list
img_clips.append(logo)
# Concatenating slides
video_slides = concatenate_videoclips(img_clips ,method='compose').set_pos(('center','center'))
print(bg_clip.duration, video_slides.duration)
#composing bg tamplate and Video_slides
final_video = CompositeVideoClip([bg_clip,video_slides])

# Applying the Zoom effect to the entire video
#video_slides_with_zoom = Zoom(video_slides, mode='in', position='center', speed=10)


#adding audio to the video only file
#video_with_audio = video_slides_with_zoom.set_audio(audio_clip_speech)
#---------------increasing the volume--------------------------------------
#video_with_audio=video_with_audio.volumex(2)
#--------------------------------------------------------------------------
#---------------------extra------------------------------------------------
# Calculate the final duration of the video (1 second + audio duration)
#final_duration = 1 + audio_clip_speech.duration
# Set the duration of the video
#final_video = video_with_audio.set_duration(final_duration)
#----------------------------------------------------------------------------
# Set the aspect ratio to 9:16
#video_with_audio = video_with_audio.resize(height=720,width=1280)  # Assuming 720p resolution

# -----------------------Exporting the final video---------------------------
final_video.write_videofile(output_video, preset='ultrafast',codec='libx264', fps=30)
#----------------------------------------------------------------------------
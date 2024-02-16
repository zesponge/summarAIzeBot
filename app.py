from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from transformers import AutoTokenizer

app = Flask(__name__)

@app.get('/summary')
def summary_api():
    summarizer = pipeline('summarization')
    transcript="The soler system 8 Planets orbiting 1 sun All of the planets orbit in a counter-clockwise direction The lnner planets orbit faster than the outer planets The earth is the 3rd planet from the sun The earth takes 365 davs to complete 1 orbit THANKS FOR WACHING"
    summary = summarizer(transcript, max_length=100, min_length=30, do_sample=False)
    return summary, 200
#     print('Request received')
#     url = request.args.get('url', '')
#     video_id = url.split('=')[0]
#     print('Video ID:', video_id)
#     transcript = get_transcript(video_id)
#     print('Transcript:', transcript)
#     summary = get_summary(transcript)
#     print('Summary:', summary)
#     return summary, 200

# def get_transcript(video_id):
#     transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
#     transcript = ' '.join([d['text'] for d in transcript_list])
#     return transcript

# def get_summary(transcript):
#     summariser = pipeline('summarization')
#     summary = summariser(transcript, max_length=100, min_length=30, do_sample=False)
#     print(summary)
#     # for i in range(0, (len(transcript)//1000)+1):
#     #     summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
#     #     summary = summary + summary_text + ' '
#     return summary
    

# if __name__ == '__main__':
#     app.run()
# @app.route('/')
# def home():
#     return "<p>lebron the goat</p>"
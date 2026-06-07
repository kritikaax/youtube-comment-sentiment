from googleapiclient.discovery import build
from textblob import TextBlob

API_KEY = "AIzaSyBJk_hrKiiA11qckKs2UUy_jVMsVRRlD18"  

def get_youtube_comments(video_id, api_key, max_results=50):
    youtube = build("youtube", "v3", developerKey=api_key)
    comments = []
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(int(max_results), 100),
        textFormat="plainText"
    ).execute()

    for item in response.get("items", []):
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)
        
    return comments

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral" 
    
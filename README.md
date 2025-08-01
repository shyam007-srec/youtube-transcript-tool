
# 📺 YouTube Transcript Fetcher from Google Sheet

A Python automation tool that reads YouTube video links from a Google Sheet, fetches their English auto-generated transcripts using `yt-dlp`, and updates the transcripts back into the same Google Sheet.

---

## 🔧 Features

- ✅ Reads YouTube links from a Google Sheet
- ✅ Fetches English auto-captions using `yt-dlp`
- ✅ Cleans `.vtt` subtitle files (removes tags, timestamps)
- ✅ Writes cleaned transcripts to the same sheet
- ✅ Logs status for each video
- ✅ Skips invalid or private links

---

## 📂 Folder Structure

```
youtube_transcript_project/
├── youtube_transcript_fetcher.py   # Main script
├── requirements.txt                # Dependencies
├── credentials.json                # Google API key (keep secret!)
└── README.md                       # This file
```

---

## 📥 Setup Instructions

### 🔹 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/youtube-transcript-fetcher.git
cd youtube_transcript_fetcher
```

---

### 🔹 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Google Sheet Setup

1. Create a Google Sheet named: `YouTubeTranscriptList`
2. Paste YouTube video links into **Column A**, starting from row 2
3. Share the sheet with your service account email from `credentials.json`

---

### 🔹 4. Run the Script

```bash
python youtube_transcript_fetcher.py
```

📌 The script will:
- Process each video
- Download `.vtt` subtitles if available
- Clean them
- Paste cleaned text into **Column B**

---

## 🧪 Example

| A (YouTube URL)                                     | B (Transcript)                        |
|-----------------------------------------------------|---------------------------------------|
| `https://www.youtube.com/watch?v=abcd1234`          | `"Welcome to the course on Python..."`|

---

## 📦 Dependencies

```text
gspread
oauth2client
yt-dlp
```

---

## 🛑 Notes

- Only works with **public** videos that have **English auto-captions**
- Does **not** download full video or audio
- Does **not** support manual subtitles yet

---

## 📜 License

This project is for educational and internship evaluation purposes.  
Please do not share credentials.json publicly.

---

## 🙋‍♂️ Author

**Sham Kumar S**  
- [LinkedIn](https://www.linkedin.com/in/sham-kumar-a10037323)  
- Email: sham1309kumar@gmail.com

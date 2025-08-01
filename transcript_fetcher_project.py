import gspread
import re
import subprocess
import time
import os
import tempfile
from oauth2client.service_account import ServiceAccountCredentials

GOOGLE_SHEET_NAME = "YouTubeTranscriptList"
TRANSCRIPT_LANGUAGE = "en"
MAX_TRANSCRIPT_LENGTH = 5000
START_ROW = 2

def connect_to_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client.open(GOOGLE_SHEET_NAME).sheet1

def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

def fetch_transcript(url, lang="en"):
    video_id = extract_video_id(url)
    if not video_id:
        return "Invalid YouTube URL"

    with tempfile.TemporaryDirectory() as tmpdir:
        vtt_file = os.path.join(tmpdir, f"{video_id}.{lang}.vtt")
        cmd = [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", lang,
            "--sub-format", "vtt",
            "--skip-download",
            "-o", os.path.join(tmpdir, "%(id)s.%(ext)s"),
            url
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0 or not os.path.exists(vtt_file):
            return "Transcript not available"

        return parse_vtt(vtt_file)

def parse_vtt(vtt_path):
    lines = []
    with open(vtt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith("webvtt") or \
               re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3}", line) or \
               line == "" or \
               re.search(r"<[0-9:.]+><c>", line):
                continue
            clean_line = re.sub(r"<\/?c.*?>", "", line)
            clean_line = re.sub(r"<[0-9:.]+>", "", clean_line)
            lines.append(clean_line)
    return " ".join(lines).strip()

def main():
    sheet = connect_to_google_sheet()
    urls = sheet.col_values(1)[1:]  # Skip header

    for i, url in enumerate(urls, start=START_ROW):
        print(f"\n📺 Row {i} - {url}")
        transcript = fetch_transcript(url)
        transcript = transcript[:MAX_TRANSCRIPT_LENGTH]
        sheet.update_cell(i, 2, transcript)
        print("✅ Transcript updated")
        time.sleep(1.5)

    print("\n🎉 DONE — All transcripts processed.")

if __name__ == "__main__":
    main()

# 🎵 YouTube Playlist to MP3 Downloader (GUI)

A simple, user-friendly Python application to download entire YouTube playlists and convert them to MP3 format automatically. Built with **Tkinter** for the interface and powered by the robust **yt-dlp** library.

## 🚀 Features

- **GUI Interface:** No need to use command lines; simple graphical user interface.
- **Batch Download:** Paste a playlist link and download all videos at once.
- **Auto Conversion:** Automatically converts videos to high-quality MP3 (192kbps).
- **Clean Filenames:** Saves files with just the song title (removes playlist index numbers like "01 - ...").
- **Custom Directory:** Choose exactly where you want to save your music.
- **Live Logs:** View the download progress and status in real-time within the app.
- **Non-Blocking:** Runs on a separate thread, so the interface never freezes during downloads.

## 🛠️ Requirements

To run this application, you need:

- [Python 3.x](https://www.python.org/downloads/)
- **FFmpeg** (Required for media conversion)

## 📦 Installation

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/IlgarZaman/YouTube-playlist-downloader.git](https://github.com/IlgarZaman/YouTube-playlist-downloader.git)
    cd YouTube-playlist-downloader
    ```

2.  **Install Dependencies:**

    ```bash
    pip install yt-dlp
    ```

3.  **Setup FFmpeg (Crucial Step):**
    For the converter to work, the system needs `ffmpeg.exe` and `ffprobe.exe`.

    - **Option A (Portable - Recommended):** Download [FFmpeg Essentials](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip). Extract `ffmpeg.exe` and `ffprobe.exe` from the `bin` folder and place them **in the same folder** as the python script.
    - **Option B (System-wide):** Install FFmpeg on your system and add it to your System PATH variables.

## ▶️ Usage

1.  Run the script:

    ```bash
    python ProIndirici.py
    ```

    _(Note: Replace `ProIndirici.py` with your actual filename)_

2.  Paste the **YouTube Playlist Link** into the input field.
3.  Click **"Select Folder"** (Klasör Seç) to choose where to save MP3s.
4.  Click **"START DOWNLOAD"** (İNDİRMEYİ BAŞLAT).
5.  Watch the progress log. Enjoy your music!

## ⚠️ Disclaimer

This tool is for **educational purposes and personal archiving only**. Users are responsible for complying with YouTube's Terms of Service and copyright laws in their country. Do not use this tool to distribute copyrighted material.

---

**Author:** ILGAR ZAMANOV

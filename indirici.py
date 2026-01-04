import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import yt_dlp
import os
import threading

class YoutubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Playlist MP3 İndirici (Temiz İsim)")
        self.root.geometry("600x480")
        self.root.resizable(False, False)

        # --- 1. Link Bölümü ---
        tk.Label(root, text="YouTube Playlist Linki:", font=("Arial", 10, "bold")).pack(pady=5)
        self.url_entry = tk.Entry(root, width=70)
        self.url_entry.pack(pady=5)

        # --- 2. Klasör Seçme Bölümü ---
        tk.Label(root, text="Kaydedilecek Klasör:", font=("Arial", 10, "bold")).pack(pady=5)
        
        frame_folder = tk.Frame(root)
        frame_folder.pack(pady=5)
        
        self.folder_path = tk.StringVar()
        self.folder_entry = tk.Entry(frame_folder, textvariable=self.folder_path, width=50, state='readonly')
        self.folder_entry.pack(side=tk.LEFT, padx=5)
        
        btn_browse = tk.Button(frame_folder, text="Klasör Seç", command=self.select_folder, bg="#dddddd")
        btn_browse.pack(side=tk.LEFT)

        # --- 3. İndir Butonu ---
        self.btn_download = tk.Button(root, text="İNDİRMEYİ BAŞLAT", command=self.start_thread, 
                                      bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), height=2, width=20)
        self.btn_download.pack(pady=15)

        # --- 4. Durum Ekranı (Loglar) ---
        tk.Label(root, text="İşlem Durumu:", font=("Arial", 9)).pack(anchor="w", padx=20)
        self.log_area = scrolledtext.ScrolledText(root, width=68, height=12, state='disabled', font=("Consolas", 9))
        self.log_area.pack(pady=5)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def log(self, message):
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area.config(state='disabled')

    def start_thread(self):
        url = self.url_entry.get()
        folder = self.folder_path.get()

        if not url:
            messagebox.showerror("Hata", "Lütfen bir YouTube linki yapıştırın!")
            return
        if not folder:
            messagebox.showerror("Hata", "Lütfen dosyaların kaydedileceği klasörü seçin!")
            return

        self.btn_download.config(state='disabled', text="İndiriliyor...")
        self.log("--- İşlem Başlatılıyor ---")
        
        t = threading.Thread(target=self.run_download, args=(url, folder))
        t.start()

    def run_download(self, url, folder):
        class MyLogger:
            def __init__(self, app):
                self.app = app
            def debug(self, msg):
                if "[download] Destination" in msg:
                    # Dosya adını temizleyip gösterelim
                    filename = msg.split("Destination: ")[1].strip()
                    self.app.log(f"İndiriliyor: {filename}")
                elif "[download] 100%" in msg:
                    self.app.log("✅ İndirme bitti, dönüştürülüyor...")
            def info(self, msg): pass
            def warning(self, msg): pass
            def error(self, msg): self.app.log(f"HATA: {msg}")

        # --- AYARLAR BURADA DEĞİŞTİ ---
        ydl_opts = {
            'format': 'bestaudio/best',
            # Eski kod: f'{folder}/%(playlist_index)s - %(title)s.%(ext)s'
            # Yeni kod (Sadece başlık):
            'outtmpl': f'{folder}/%(title)s.%(ext)s', 
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(self),
            'ignoreerrors': True,
            'ffmpeg_location': os.getcwd()
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.log("\n🎉 TÜM İŞLEMLER TAMAMLANDI!")
            messagebox.showinfo("Başarılı", "Playlist indirme işlemi bitti!")
        except Exception as e:
            self.log(f"\n❌ Kritik Hata: {e}")
            messagebox.showerror("Hata", f"Beklenmedik bir hata: {e}")
        finally:
            self.btn_download.config(state='normal', text="İNDİRMEYİ BAŞLAT")

if __name__ == "__main__":
    root = tk.Tk()
    app = YoutubeApp(root)
    root.mainloop()
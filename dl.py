import yt_dlp
import sys

def download_video(url):
    # Konfigurasi download
    ydl_opts = {
        'format': 'best',  # Mengambil kualitas terbaik (video + audio)
        'outtmpl': '%(title)s.%(ext)s', # Format nama file output
        'noplaylist': True, # Hanya download single video, bukan playlist
        # Opsi tambahan agar tidak terdeteksi sebagai bot (penting untuk TikTok/FB)
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }
    }

    try:
        print(f"Sedang memproses: {url} ...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Mengambil info video tanpa download dulu (opsional, untuk cek validitas)
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', None)
            print(f"Judul Video: {video_title}")
            
            # Melakukan download
            print("Mulai mendownload...")
            ydl.download([url])
            print("\n✅ Download Selesai!")
            
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Meminta input link dari user
    print("=== Universal Video Downloader (FB, TikTok, Twitter/X) ===")
    link = input("Masukkan Link Video: ")
    
    if link:
        download_video(link)
    else:
        print("Link tidak boleh kosong.")

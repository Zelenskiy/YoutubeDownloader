import yt_dlp
import os


def download_playlist(url: str, download_audio: bool = False):
    # Базовий шаблон іменування
    output_template = "_%(playlist_title)s/Tutorial %(playlist_index)s - %(title)s.%(ext)s"

    # Формат завантаження
    if download_audio:
        ydl_format = 'bestaudio/best'
        postprocessors = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        extension = 'mp3'
    else:
        ydl_format = 'bestvideo+bestaudio/best'
        postprocessors = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
        extension = 'mp4'

    # Опції для yt-dlp
    ydl_opts = {
        'outtmpl': output_template,
        'format': ydl_format,
        'merge_output_format': extension,
        'postprocessors': postprocessors,
        'progress_hooks': [hook],
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': True,
    }

    # Запуск завантаження
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def hook(d):
    if d['status'] == 'finished':
        print(f"✅ Завантажено: {d['filename']}")


if __name__ == "__main__":
    url = input("🔗 Введіть посилання на плейлист YouTube: ").strip()
    choice = input("🎵 Завантажити тільки аудіо (mp3)? [y/N]: ").strip().lower()
    download_audio = choice == 'y'
    download_playlist(url, download_audio)

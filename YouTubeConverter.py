#!/usr/bin/env python3 

import yt_dlp
import os
from tqdm import tqdm
import pyfiglet

# Mostrar el arte ASCII de bienvenida
def show_ascii_art():
    ascii_art = pyfiglet.figlet_format("YouTubeCvt")
    print(ascii_art)

# Configuración de opciones comunes para yt-dlp
def get_common_options(output_path, external_downloader=None, extra_args=None):
    options = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'prefer_ffmpeg': True,
        'noplaylist': True,
        'concurrent_fragment_downloads': 10,  # Descargar fragmentos en paralelo
    }

    if external_downloader:
        options['external_downloader'] = external_downloader
        options['external_downloader_args'] = extra_args

    return options

# Descargar y convertir a MP3
def download_audio(video_url, output_path='downloads'):
    try:
        ydl_opts = get_common_options(output_path, external_downloader='aria2c', extra_args=['-x', '16', '-k', '1M'])
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as e:
        print(f"Error al descargar el audio: {e}")

# Descargar video en MP4 con resolución 1080p
def download_video(video_url, output_path='downloads'):
    try:
        ydl_opts = get_common_options(output_path, external_downloader='aria2c', extra_args=['-x', '16', '-k', '1M'])
        ydl_opts.update({
            'format': 'bestvideo[height=1080]+bestaudio/best',
            'merge_output_format': 'mp4',
        })

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

    except Exception as e:
        print(f"Error al descargar el video: {e}")

# Función principal para elegir y descargar
def main():
    show_ascii_art()

    # Menú para elegir entre MP3 y MP4
    print("Selecciona el formato de descarga:")
    print("1. Descargar como MP3")
    print("2. Descargar como MP4 (1080p)")
    
    choice = input("Introduce tu elección (1 o 2): ")

    if choice not in ['1', '2']:
        print("Opción no válida. Por favor, ejecuta el programa de nuevo.")
        return

    # Solicitar la URL del video de YouTube
    url = input("Introduce la URL del video de YouTube: ")

    # Descargar según la opción elegida
    if choice == '1':
        download_audio(url)
    elif choice == '2':
        download_video(url)

if __name__ == "__main__":
    main()

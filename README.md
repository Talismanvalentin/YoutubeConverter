# YouTubeConverter

YouTubeConverter es una aplicación para descargar y convertir videos de YouTube en formato MP3 o MP4 (1080p) utilizando `yt-dlp`.

## Requisitos

- Python 3.x
- yt-dlp
- aria2c
- pyfiglet
- tqdm

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd YoutubeDownload_Beta
   ```

2. Instala las dependencias:

   ```bash
   pip install yt-dlp pyfiglet tqdm
   ```

3. Asegúrate de tener `aria2c` instalado en tu sistema.

## Uso

1. Ejecuta el script:

   ```bash
   python3 YouTubeConverter.py
   ```

2. Sigue las instrucciones en pantalla para seleccionar el formato de descarga y proporcionar la URL del video de YouTube.

## Funciones

### show_ascii_art

Muestra un arte ASCII de bienvenida utilizando `pyfiglet`.

### get_common_options

Configura las opciones comunes para `yt-dlp`.

### download_audio

Descarga el audio de un video de YouTube y lo guarda como un archivo MP3.

**Args:**

- `video_url` (str): La URL del video de YouTube a descargar.
- `output_path` (str, opcional): El directorio donde se guardará el archivo de audio descargado. Por defecto es 'downloads'.

### download_video

Descarga un video de YouTube en formato MP4 con resolución 1080p.

**Args:**

- `video_url` (str): La URL del video de YouTube a descargar.
- `output_path` (str, opcional): El directorio donde se guardará el archivo de video descargado. Por defecto es 'downloads'.

### main

Función principal para elegir y descargar el formato deseado (MP3 o MP4).

## Ejemplo

Para descargar un video como MP3:

```python
download_audio('https://www.youtube.com/watch?v=example', 'my_downloads')
```

Para descargar un video como MP4:

```python
download_video('https://www.youtube.com/watch?v=example', 'my_downloads')
```

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

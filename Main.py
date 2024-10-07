import os
import yt_dlp
import whisper


url = "https://www.youtube.com/watch?v=KS8zYKcrmSY"
filename = "audio.video alemao da caravan"


if not os.path.exists(filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': filename,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download do vídeo concluído com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao baixar o vídeo: {e}")
else:
    print("O arquivo de áudio já existe.")


if os.path.exists(filename):

    model = whisper.load_model("base")


    result = model.transcribe(filename)
    transcript = result['text']

   


    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": """
            Você é um assistente que resume vídeos do YouTube.
            """
        },
        {"role": "user",
         "content": f"resuma o seguinte video {transcript}"}
        ]
    )


    try:
        print(response.choices[0].message.content)
    except AttributeError as e:
        print(f"Erro ao acessar o conteúdo da resposta: {e}")
    except IndexError as e:
        print(f"Erro ao acessar a escolha: {e}")

import os
import yt_dlp
import re

def baixar_videos_ark(username):
    # Configurações
    pasta_destino = f"ARK_Videos_{username}"
    os.makedirs(pasta_destino, exist_ok=True)

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'cookiesfrombrowser': ('firefox',),
        'matchtitle': r'(?i)ARK|Survival Evolved',  # Filtra por termos no título
        'ignoreerrors': True,
        'quiet': False,
    }

    try:
        print(f"🔍 Procurando vídeos de ARK em @{username}...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.tiktok.com/@{username}'])
        
        # Pós-processamento: verificar arquivos baixados
        print("\n📂 Arquivos baixados:")
        for file in os.listdir(pasta_destino):
            if re.search(r'(?i)ark', file):  # Confirma se é sobre ARK
                print(f"✔ {file}")
            else:
                os.remove(f"{pasta_destino}/{file}")  # Remove não-ARK
                
        print("✅ Download concluído!")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    baixar_videos_ark("")  # Altere para o perfil desejado

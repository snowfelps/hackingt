# -*- coding: utf-8 -*-

import os
import shutil

# Caminho do diretório a ser excluído
diretorio_whatsapp = '/sdcard/Android/media/com.whatsapp'

try:
    # Remover todos os arquivos no diretório
    for filename in os.listdir(diretorio_whatsapp):
        file_path = os.path.join(diretorio_whatsapp, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Erro ao excluir {file_path}: {e}")

    # Tentar excluir o diretório agora
    os.rmdir(diretorio_whatsapp)
    print(f"Diretório {diretorio_whatsapp} excluído com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro {diretorio_whatsapp}: {e}")

# -*- coding: utf-8 -*-
from PIL import Image

def extrair_mensagem_lsb(caminho_imagem):
    try:
        # Abre a imagem e garante que está no modo RGB
        img = Image.open(caminho_imagem).convert("RGB")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")
        return None

    bits = []
    
    # Percorre todos os pixels na ordem original
    for r, g, b in img.getdata():
        # Pega o último bit de cada canal (R, G, B) e guarda na lista
        bits.append(r & 1)
        bits.append(g & 1)
        bits.append(b & 1)

    bytes_lista = []
    # Agrupa os bits de 8 em 8
    for i in range(0, len(bits), 8):
        grupo_bits = bits[i:i+8]
        if len(grupo_bits) < 8:
            break  # Ignora bits incompletos no final da imagem
        
        # Converte a lista de 8 bits (0s e 1s) para uma string binária e depois para inteiro
        string_binaria = "".join(str(b) for b in grupo_bits)
        byte_num = int(string_binaria, 2)
        bytes_lista.append(byte_num)

    # Converte os bytes para caracteres e monta a string completa
    texto_completo = ""
    for b in bytes_lista:
        try:
            texto_completo += chr(b)
        except ValueError:
            continue

    # Define o marcador de parada
    marcador = "<<<FIM_DA_MENSAGEM>>>"
    
    if marcador in texto_completo:
        # Isola tudo o que vem antes do marcador
        mensagem_cifrada = texto_completo.split(marcador)[0]
        return mensagem_cifrada
    else:
        print("Aviso: O marcador de fim de mensagem não foi encontrado.")
        # Retorna um pedaço do texto extraído para conferência caso queira
        return texto_completo[:200] 

if __name__ == "__main__":
    # Substitua pelo nome exato do arquivo de imagem que você recebeu
    nome_arquivo_imagem = "2023102306_ENZO_LUIZ_BERLESI_SALLES.png" 
    
    print("Extraindo mensagem oculta da imagem...")
    mensagem_escondida = extrair_mensagem_lsb(nome_arquivo_imagem)
    
    if mensagem_escondida:
        print("\n--- MENSAGEM CIFRADA ENCONTRADA ---")
        print(mensagem_escondida)
        print("-----------------------------------")
        print("\nCopie o texto acima para usar no decifrador.")
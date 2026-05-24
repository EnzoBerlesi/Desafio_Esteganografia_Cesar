# -*- coding: utf-8 -*-

ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MODULO = 62

def decifrar_cesar_forca_bruta(mensagem_cifrada):
    print("\n--- TESTANDO DESLOCAMENTOS (FORÇA BRUTA) ---\n")
    
    # Testa os deslocamentos de 0 a 61
    for deslocamento in range(MODULO):
        texto_decifrado = ""
        
        for caractere in mensagem_cifrada:
            if caractere in ALFABETO:
                # Encontra a posição atual no alfabeto customizado
                posicao = ALFABETO.index(caractere)
                # Voltas as posições aplicando o módulo 62
                nova_posicao = (posicao - deslocamento) % MODULO
                texto_decifrado += ALFABETO[nova_posicao]
            else:
                # Caracteres de fora (espaço, pontos, etc.) permanecem iguais
                texto_decifrado += caractere
                
        # Exibe o resultado do deslocamento atual
        print(f"Deslocamento {deslocamento:02d}: {texto_decifrado}")

if __name__ == "__main__":
    # COLE AQUI dentro das aspas a mensagem cifrada que o primeiro programa extrair
    mensagem_para_testar = "tfYg2: o 0f6dhc4fY36Y dfch242 Y 6b3cfaY0Yc | o9ibc: sBNC zIwN psFzsGw GozzsG | Fo: QOQRPOQROU | G2b5Y: VOUO | HifaY: VsGoB"
    
    # Executa a força bruta
    decifrar_cesar_forca_bruta(mensagem_para_testar)
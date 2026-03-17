# =========================================
# [creeper criado em paint apartir do robô]
# =========================================
import pyautogui as py
import time as tm

py.FAILSAFE = True

# Velocidade do desenho (0.3 é mais seguro para o Paint não falhar o risco)
velocidade = 0.3

# --- FUNÇÃO PARA DESENHAR RETÂNGULOS ---
def desenhar_retangulo(largura, altura):
    py.drag(largura, 0, duration=velocidade, button='left')   # Direita
    py.drag(0, altura, duration=velocidade, button='left')    # Baixo
    py.drag(-largura, 0, duration=velocidade, button='left')  # Esquerda
    py.drag(0, -altura, duration=velocidade, button='left')   # Cima

py.alert('ATENÇÃO! Vou desenhar o rosto do Creeper. Solte o mouse!')

# 1. Abrir o Paint / comandos do teclado 
py.press('win')
tm.sleep(1)
py.write('paint', interval=0.1)
tm.sleep(1)
py.press('enter')
tm.sleep(3)


# 2. Achar o meio da tela e focar no papel
largura_tela, altura_tela = py.size()
centro_x = largura_tela / 2
centro_y = altura_tela / 2

py.click(centro_x, centro_y)
tm.sleep(0.5)

# 3. Configurar a Escala para saber como vai desenhar 
escala = 60
x_inicial = centro_x - (4 * escala) #aqui sera desenhado com eixos x, y
y_inicial = centro_y - (4 * escala)

# Primeira parte desenhando o contorno
py.moveTo(x_inicial, y_inicial, duration=velocidade)
desenhar_retangulo(8 * escala, 8 * escala)

# Olho Esquerdo
py.moveTo(x_inicial + (1 * escala), y_inicial + (2 * escala), duration=velocidade)
desenhar_retangulo(2 * escala, 2 * escala)

# Olho Direito
py.moveTo(x_inicial + (5 * escala), y_inicial + (2 * escala), duration=velocidade)
desenhar_retangulo(2 * escala, 2 * escala)

# Nariz / Centro da Boca
py.moveTo(x_inicial + (3 * escala), y_inicial + (4 * escala), duration=velocidade)
desenhar_retangulo(2 * escala, 2 * escala)

# Canto Esquerdo da Boca
py.moveTo(x_inicial + (2 * escala), y_inicial + (5 * escala), duration=velocidade)
desenhar_retangulo(1 * escala, 2 * escala)

# Canto Direito da Boca
py.moveTo(x_inicial + (5 * escala), y_inicial + (5 * escala), duration=velocidade)
desenhar_retangulo(1 * escala, 2 * escala)


# segunda

# Pausa para você preparar a ferramenta
py.alert('Clique no BALDE DE TINTA no Paint.\n2. Escolha a cor PRETA.\n3. Depois clique em OK aqui para pintar!')

# O robô vai clicar exatamente no centro geométrico de cada parte:

# Pintar Olho Esquerdo
py.click(int(x_inicial + 2 * escala), int(y_inicial + 3 * escala)) #vai achar os pontos e vai clicar no local para pintar
tm.sleep(0.3)

# Pintar Olho Direito
py.click(int(x_inicial + 6 * escala), int(y_inicial + 3 * escala))
tm.sleep(0.3)

# Pintar Nariz / Centro da boca
py.click(int(x_inicial + 4 * escala), int(y_inicial + 5 * escala))
tm.sleep(0.3)

# Pintar Canto Esquerdo da boca
py.click(int(x_inicial + 2.5 * escala), int(y_inicial + 6 * escala))
tm.sleep(0.3)

# Pintar Canto Direito da boca
py.click(int(x_inicial + 5.5 * escala), int(y_inicial + 6 * escala))
tm.sleep(0.3)

py.alert('Clique no BALDE DE TINTA no Paint.\n2. Escolha a cor verde.\n3. Depois clique em OK aqui para pintar!')
py.click(int(x_inicial + 2 * escala), int(y_inicial + 1 * escala))
tm.sleep(0.3)

#  Desenhado a palavra "MINECRAFT"
py.alert('Rosto do Creeper finalizado! \n\n1. Escolha a ferramenta PINCEL (ou Lápis).\n2. Escolha a cor PRETA (ou a que preferir).\n3. Clique em OK para escrever MINECRAFT!')

# Ajustando a escala do texto para caber abaixo do desenho
escala_texto = escala * 0.5 
h = 2 * escala_texto      # altura da letra
w = 1.5 * escala_texto    # largura da letra
espaco = 0.5 * escala_texto # espaço entre as letras

# Calculando para centralizar o texto (9 letras no total)
largura_total_texto = (9 * w) + (8 * espaco)
x_letra = centro_x - (largura_total_texto / 2)
y_letra = y_inicial + (9 * escala) # Fica um pouco abaixo do rosto

# Função auxiliar para encurtar os comandos de arrastar, aqui neste caso ele desenhara as letras.
def arrastar(dx, dy):
    py.drag(dx, dy, duration=velocidade, button='left')

# M
py.moveTo(x_letra, y_letra + h) #automaiza a escrita de texto para escrita em desenho.
arrastar(0, -h)
arrastar(w/2, h/2)
arrastar(w/2, -h/2)
arrastar(0, h)
x_letra += w + espaco

# I
py.moveTo(x_letra + w/2, y_letra)
arrastar(0, h)
x_letra += w + espaco

# N
py.moveTo(x_letra, y_letra + h)
arrastar(0, -h)
arrastar(w, h)
arrastar(0, -h)
x_letra += w + espaco

# E
py.moveTo(x_letra + w, y_letra)
arrastar(-w, 0)
arrastar(0, h/2)
arrastar(w, 0)
py.moveTo(x_letra, y_letra + h/2)
arrastar(0, h/2)
arrastar(w, 0)
x_letra += w + espaco

# C
py.moveTo(x_letra + w, y_letra)
arrastar(-w, 0)
arrastar(0, h)
arrastar(w, 0)
x_letra += w + espaco

# R
py.moveTo(x_letra, y_letra + h)
arrastar(0, -h)
arrastar(w, 0)
arrastar(0, h/2)
arrastar(-w, 0)
py.moveTo(x_letra + w/2, y_letra + h/2)
arrastar(w/2, h/2)
x_letra += w + espaco

# A
py.moveTo(x_letra, y_letra + h)
arrastar(0, -h)
arrastar(w, 0)
arrastar(0, h)
py.moveTo(x_letra, y_letra + h/2)
arrastar(w, 0)
x_letra += w + espaco

# F
py.moveTo(x_letra, y_letra + h)
arrastar(0, -h)
arrastar(w, 0)
py.moveTo(x_letra, y_letra + h/2)
arrastar(w*0.8, 0)
x_letra += w + espaco

# T
py.moveTo(x_letra, y_letra)
arrastar(w, 0)
py.moveTo(x_letra + w/2, y_letra)
arrastar(0, h)

# Move o mouse para fora e finaliza
py.moveTo(10, 10, duration=velocidade)
py.alert('Creeper do Minecraft Finalizada!')

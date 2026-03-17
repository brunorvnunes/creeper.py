import pyautogui as py
import time as tm

py.FAILSAFE = True

# Velocidade do desenho (0.3 é mais seguro para o Paint não falhar o risco)
velocidade = 0.3

#-- função--

def desenhar_triangulo(base, altura):
    py.drag(base /2, altura, duration=velocidade, button='left')
    py.drag(-base, 0, duration=velocidade, button='left')
    py.drag(base /2, -altura, duration=velocidade, button='left')

def desenhar_retangulo(largura, altura):
    py.drag(largura, 0, duration=velocidade, button='left')   # Direita
    py.drag(0, altura, duration=velocidade, button='left')    # Baixo
    py.drag(-largura, 0, duration=velocidade, button='left')  # Esquerda
    py.drag(0, -altura, duration=velocidade, button='left')   # Cima
py.alert('ATENÇÃO')
py.press('win')
tm.sleep(1)
py.write('paint', interval=0.1)
tm.sleep(1)
py.press('enter')
tm.sleep(4)

largura_tela, altura_tela= py.size()
centro_x = largura_tela / 2
centro_y = altura_tela  / 2

py.click(centro_x, centro_y)
tm.sleep(0.5)

escala=20

# --- 1. DESENHA O TELHADO (Uma vez só!) ---
py.moveTo(centro_x, centro_y - (3 * escala), duration=velocidade)
desenhar_triangulo(6 * escala, 4 * escala)


# --- 2. PREPARA E DESENHA AS PAREDES ---
x_parede = centro_x - (2 * escala)
y_parede = centro_y + (1 * escala)

py.moveTo(x_parede, y_parede, duration=velocidade)
desenhar_retangulo(4 * escala, 4 * escala)

# Desenhando um quadrado do mesmo tamanho da base do telhado
desenhar_retangulo(6 * escala, 4 * escala)
py.moveTo(10, 10, duration=velocidade)
py.alert('triangulo :D')


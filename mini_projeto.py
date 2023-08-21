# Feito por Arthur Nº:04 e Guilherme Nº:14
import PySimpleGUI as sg

sg.theme('LightBrown11')  # Tema

# Segunda lei de newton
def calcular_forca_resultante(massa, aceleracao):
    forca_resultante = massa * aceleracao
    return forca_resultante


# Layout do programa
layout = [ 
    [sg.Text("Cálculo da Força Resultante", font=("Helvetica", 12))],
    [sg.Text("Massa:", size=(9, 1)), sg.InputText(key="massa")],
    [sg.Text("Aceleração:", size=(9, 1)), sg.InputText(key="aceleracao")],
    [sg.Button("Calcular"), sg.Button("Sair")],
    [sg.Text("Força Resultante Anterior:", size=(22, 1)), sg.Text("", size=(14, 1), key="resultado")]
    ]


window = sg.Window('Segunda lei de Newton', layout)
while True:
    evento, valores = window.read()

    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break

    if evento == "Calcular":
        try:
            massa = float(valores["massa"])#fala pro programa que o text é o mesmo do calculo
            aceleracao = float(valores["aceleracao"])
            forca_resultante = calcular_forca_resultante(massa, aceleracao)
            window["resultado"].update(f"{forca_resultante:.1f} N")
            sg.popup("O resultado é", f"{forca_resultante:.1f}N")
        except ValueError:
            sg.popup_error("Digite valores numéricos válidos.")

window.close()
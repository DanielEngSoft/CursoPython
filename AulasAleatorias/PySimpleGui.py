from PySimpleGUI import Window, Button

janela = Window(
    'Título da janela',
    size=(300, 300),
    layout=[
        [Button('B1'),Button('B2')]
    ]
)
janela.read()
janela.close()
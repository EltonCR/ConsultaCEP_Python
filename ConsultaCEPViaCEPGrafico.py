import requests
import tkinter as tk
import sys
from PIL import Image, ImageTk

'''
Linguagem: Python
Desenvolvedor: Elton da Costa Ramos
Data: 19/04/2021
Comentário: Consulta de CEP consumindo uma API via interface gráfica TKinter.
            Utilizando tutoriais no Youtube e Google.
'''


root = tk.Tk()
canvas = tk.Canvas((root), width=600, height=300)
canvas.grid(columnspan=3, rowspan=10)


logo = Image.open('ConsultaCEP_Canvas.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image =  logo
logo_label.grid(column=1, row=0)



entrada_caixa = tk.Entry(root, bg="#ffffff", fg="black")
entrada_caixa.grid(column=1, row=2)


instruções = tk.Label(root, text="Digite o CEP (somente números)", font="Arial")
instruções.grid(columnspan=3,column=0, row=1)


buscar_cep = tk.StringVar()

browser_btn = tk.Button(root, textvariable=buscar_cep, command=lambda:busca_cep(), font="Arial", bg="#000000", fg="white", height=1,width=15)
buscar_cep.set("Buscar")
browser_btn.grid(column=1, row=4)

assinatura = tk.Label(root, text="Elton C. Ramos", font="Arial")
assinatura.grid(columnspan=3,column=0, row=10)

def busca_cep():
    buscar_cep.set("Buscar novamente")

    cep_invalido = ''
    valor_dados = ''

    cep_input = entrada_caixa.get() 
    if len(cep_input) != 8:
        cep_invalido = 'Quantidade de dígitos inválida.'
        print('Quantidade de dígitos inválida.')

        text_box = tk.Text(root, height=5, width=50, padx=15, pady=15)
        text_box.insert(1.0, cep_invalido)
        text_box.grid(column=1, row=3)

    else:

        requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
        valor_dados = requisicao.json()
    
    if valor_dados != '':
    
        if 'erro' not in valor_dados:
            
            print(valor_dados)
            print('CEP Encontrado')
            
            Logradouro = "Logradouro: {}".format(valor_dados['logradouro'])
            Complemento = Logradouro + "\nComplemento: {}".format(valor_dados['complemento'])
            Bairro = Complemento + "\nBairro: {}".format(valor_dados['bairro'])
            Localidade = Bairro + "\nLocalidade: {}".format(valor_dados['localidade'])
            End_Completo = Localidade + "\nUF: {}".format(valor_dados['uf'])
            
            text_box = tk.Text(root, height=5, width=50, padx=15, pady=15)
            text_box.insert(1.0, End_Completo)
            text_box.grid(column=1, row=3)
        else:
            cep_invalido = 'CEP Inválido'
            print('CEP Inválido')
            text_box = tk.Text(root, height=5, width=50, padx=15, pady=15)
            text_box.insert(1.0, cep_invalido)
            text_box.grid(column=1, row=3)
            

root.mainloop()


if __name__ == '__main__':
    busca_cep()

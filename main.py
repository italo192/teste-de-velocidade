from tkinter import*
from PIL import Image, ImageTk
import speedtest

# cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Blue

#janela
janela = Tk ()
janela.title ("")
janela.geometry('350x200')
janela.config(background=co1)
janela.resizable(width=FALSE, height=FALSE)



#divisão da janela
frame_logo = Frame(janela, width=350, height=60, bg=co1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# parte de cima

imagem = Image.open('velocimetro.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem.place(x=20, y=0)

l_logo_nome = Label(frame_logo,text='Teste de Velocidade', padx=10, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
l_logo_nome.place(x=75, y=10)

l_logo_linha = Label(frame_logo, width=350 ,padx=10, anchor=NW, font=('Ivy 1'), bg=co2)
l_logo_linha.place(x=0, y=57)


#funçao
def main():
    seepd = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(seepd.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(seepd.upload()/1024/1024)}"

    l_download['text'] = download
    l_upload['text'] = upload




# parte de baixo

l_download = Label(frame_corpo,text='', anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_download.place(x=30, y=25)

l_download_mb = Label(frame_corpo,text='Mbps download', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_download_mb.place(x=30, y=70)


imagem_down = Image.open('desce.png')
imagem_down = imagem_down.resize((50,50))
imagem_down = ImageTk.PhotoImage(imagem_down)

l_logo_imagem_down = Label(frame_corpo, height=60, image=imagem_down, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem_down.place(x=130, y=35)



l_upload = Label(frame_corpo,text='', anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_upload.place(x=240, y=25)

l_upload_mb = Label(frame_corpo,text='Mbps download', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_upload_mb.place(x=235, y=70)



imagem_up = Image.open('sobe.png')
imagem_up = imagem_up.resize((50,50))
imagem_up = ImageTk.PhotoImage(imagem_up)

l_logo_imagem_up = Label(frame_corpo, height=60, image=imagem_up, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=co1, fg=co3)
l_logo_imagem_up.place(x=180, y=35)


botao_testar = Button(frame_corpo,command= main, text='Iniciar teste ', font=('Ivy 10 bold'),relief=RAISED, overrelief=RIDGE, bg=co5, fg=co1)
botao_testar.place(x=135, y=100)



janela.mainloop()

from Tkinter import*
import pyttsx
main = Tk()
main.title('TTS')
main.geometry("450x300+350+50")
main['bg']='#000066'
texte=Label(main,text="entrez votre texte : ")
texte['bg']='#000066'
texte['fg']='#ffffff'
texte.place(x='0',y='30')

var_texte = StringVar()
ligne_texte = Entry(main, textvariable=var_texte, width=70)
ligne_texte.place(x='10',y='80')

def Lire():
    engine=pyttsx.init()
    lebel['text']=var_texte.get()
    engine.say(var_texte.get())
    engine.runAndWait()
    

def volume_pl():
    engine1=pyttsx.init()
    lebel['text']=var_texte.get()+" avec volume "
    volume = engine1.getProperty('volume')
    engine1.setProperty('volume', volume+text_v.get())
    engine1.say(var_texte.get())
    engine1.runAndWait()
    
def rate():
    engine2=pyttsx.init()
    lebel['text']=var_texte.get()+" avec rate"
    rate = engine2.getProperty('rate')
    engine2.setProperty('rate', rate+text_r.get())
    engine2.say(var_texte.get())
    engine2.runAndWait()
    

def quitter():
    main.quit()

text_v=DoubleVar()
textv=Entry(main,textvariable=text_v,width=8).place(x='80',y='150')

boutton1=Button(main,text="lire",command=Lire)
boutton1['bg']='#809fff'
boutton1['fg']='#ffffff'
boutton1.place(x='30',y='150')


boutton3=Button(main,text="volume+",command=volume_pl)
boutton3['bg']='#809fff'
boutton3['fg']='#ffffff'
boutton3.place(x='  140',y='150')

text_r=IntVar()
textr=Entry(main,textvariable=text_r,width=5).place(x='220',y='150')

boutton5=Button(main,text="rate",command=rate)
boutton5['bg']='#809fff'
boutton5['fg']='#ffffff'
boutton5.place(x='  260',y='150')

boutton6=Button(main,text="Quitter",command=quitter)
boutton6['bg']='#809fff'
boutton6['fg']='#ffffff'
boutton6.place(x='330',y='150')

lebel=Label(main)
lebel['bg']='#000066'
lebel.place(x='30',y='200')

main.mainloop()

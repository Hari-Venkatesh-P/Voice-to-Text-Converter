import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
global result
def speech():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
	try:
		print("System Predicts:"+r.recognize_google(audio))
		result = str(r.recognize_google(audio))
		label.config(text=str(result))
		with open("test.txt", "a") as myfile:
    			myfile.write(result)
    			myfile.write("\n")
	except Exception:
		print("Exception")

def audio():
	global answer
	filename = "trim.wav"
	r = sr.Recognizer()
	with sr.AudioFile(filename) as source:
		audio=r.listen(source)
	try:
		print("System Predicts:"+r.recognize_google(audio))
		#global result
		result = str(r.recognize_google(audio))
		with open("test.txt", "a") as myfile:
    			myfile.write(result)
    			myfile.write("\n")
		#l.config(text="answer = %s" % result)
		label.config(text=str(result))
		#myScrolledText.config(text=str(result))
		#myScrolledText.insert(INSERT, "Some text")
		#changeText(result)
	except Exception:
		print("Unable to hear")

def close():
	try:
		root.destroy()
	except Exception:
		print("Exception")

def nextf():
	result=""
	try:
		label.config(text=str(result))
	except Exception:
		print("Exception")


#window = Tk()
#window.title("Audio To Speech Converter")
#window.geometry("300x250")
#window.configure(background='skyblue')

#label = Label(window, text="Speech To Text..!!",fg = "red",bg = "skyblue",font ="Times 20 bold italic").place(x=50,y=20)


#button_login = Button(window,text="Audio File",command=audio).place(x=70,y=150)
#button_signup = Button(window,text="Speech",command =speech).place(x=200,y=150)

#myScrolledText = scrolledtext.ScrolledText(window, font=("Courier",25, "bold"),width=10, height=2, state='disabled').place(x=50,y=60)
#l = Label(window).place(x=50,y=60)
#l.pack()

 
root = tk.Tk()
root.title("Voice To Text Converter")
root.geometry("615x200")
root.wm_iconbitmap('3xhumed-Mega-Games-Pack-32-Wolfenstein-5.ico')

root.configure(background='black')

caption = tk.Label(root, text="Voice To Text..!!",fg = "light green",bg = "black",font ="Times 25 bold italic")
caption.pack()
caption.place(x=50,y=20)

label = tk.Label(root, fg="white",bg = "black",font=("Courier",15, "bold"))
label.pack()
label.place(x=60,y=80)

audio = tk.Button(root,text="Audio File",command=audio)#.place(x=70,y=150)
audio.pack()
audio.place(x=70,y=130)

speech = tk.Button(root,text="Live Speech",command =speech)
speech.pack()
speech.place(x=200,y=130)


nextb = tk.Button(root,text="Clear",command = nextf)
nextb.pack()
nextb.place(x=330,y=130)

close = tk.Button(root,text="Exit App",command =exit)
close.pack()
close.place(x=460,y=130)

mylabel = tk.Label(root,text="Developed By Hari V @2K19",fg="light green",bg = "black",font=("Times",10, "bold"))
mylabel.pack()
mylabel.place(x=60,y=180)
#def changeText(result):
#		print("2nd method")
#		print(result)
#		global answer
#		answer = result
#		l.config(text="answer = %s" % result)

root.mainloop()
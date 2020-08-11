from gtts import gTTS
import os
import PyPDF2

pdffileobj = open('1.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
x = pdfreader.numPages

pageobj = pdfreader.getPage(x-1)
text = pageobj.extractText()

file1 = open(r"C:/Python/gtts//1.txt","a")
file1.writelines(text)
file1.close

f = open('1.txt')
x = f.read()

language = 'en'
audio = gTTS(text = x, lang = language, slow = False)

audio.save('1.wav')
os.system('1.wav')
import pyttsx3
import PyPDF2
book = open('Goodfile.pdf', 'rb')
readr = PyPDF2.PdfFileReader(book)
pages = readr.numPages
# print(pages)
speaker = pyttsx3.init()
for num in range(7 , pages):
    page = readr.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

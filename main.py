# PDF to Audio

#Set up Virtual Environment
#In terminal type
#Python -m .venv
#.\.venv\Scripts\Activate

#Install dependencies pyttsx3 and PyPDF2
#In Terminal type 
#python.exe pip install pyttsx3
#python.exe pip install PyPDF2
import pyttsx3,PyPDF2

pdfreader = PyPDF2.PdfReader(open('book2.pdf', 'rb'))



# Initialize text variable to srore the entire content
text = ""

#Extract text from each page
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', '')
    print(clean_text)

#Initialize the text-to-speech engine
speaker = pyttsx3.init()

speaker.setProperty('rate', 150) #speed os speech

speaker.save_to_file(clean_text, 'book2.mp3')
speaker.runAndWait()

speaker.stop()
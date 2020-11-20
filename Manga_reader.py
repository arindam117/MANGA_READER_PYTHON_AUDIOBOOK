# PYTHON TEXT TO SPEECH READER (AUDIO BOOK ALTERNATIVE)

# IMPORTANT LIBRARIES TO LOAD
import pyttsx3
import PyPDF2


# THIS READS THE FILE FORM THE GIVEN PATH
op_summary = open("text.pdf",'rb')


# THIS LIBRARY READS THE PDF FOR USE WITH PROPER FORMATTING
manga_reader = PyPDF2.PdfFileReader(op_summary)


# THIS WILL GIVE THE NUMBER OF PAGES
pages = manga_reader.numPages


# THIS IS JUST A TEST TO CHECK THE NUMBER OF PAGES IN THE PDF
print(pages)


# SINCE THERE IS ONLY ONE PAGE HERE SO THE PARAMETER IS 0 == page 1
content = manga_reader.getPage(0)

# THIS EXTRACTS THE RAW TEXT CONTENT
text = content.extractText()

# THIS INITIALISES THE PYTHON TEXT TO SPEECH (THIS IS BETTER THAN GOOGLE TEXT_TO_SPEECH)
novel_read = pyttsx3.init()
novel_read.say(text)

# THIS PASUES THE READING AT THE END OF SENTENCE FOR A BRIEF TIME
novel_read.runAndWait()
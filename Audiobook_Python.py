import pdfplumber
from gtts import gTTS
article = """

"""
language = 'en'
gtts_transformer = gTTS(text=article, lang=language)
gtts_transformer.save("Rich_Dad_Poor_Dad_summary.mp3")
print("WORK DONE")
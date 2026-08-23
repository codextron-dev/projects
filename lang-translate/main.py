from googletrans import Translator

translator = Translator()

text = input("Enter text to translate: ")
result = translator.translate(text, dest="es")

print(f"Translated: {result.text}")
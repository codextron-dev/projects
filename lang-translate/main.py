# pip install googletrans
from googletrans import Translator

translator = Translator()

text = input("Enter text to translate: ")
target_lang = "es"

result = translator.translate(text, dest=target_lang)

print(f"\nOriginal ({result.src}): {text}")
print(f"Translated ({target_lang}): {result.text}")

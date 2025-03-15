from googletrans import Translator

def translate_text(text, target_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

if __name__ == "__main__":
    input_text = input("Enter text to translate: ")
    target_language = input("Enter target language code (e.g., 'fr' for French, 'es' for Spanish): ")

    translated_text = translate_text(input_text, target_language)
    print(f"Translated Text: {translated_text}")

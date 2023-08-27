from googletrans import Translator

def get_gujarati_meaning(word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='gu')
    return translation.text
    
english_word = "dog"
gujarati_meaning = get_gujarati_meaning(english_word)
print(f"Gujarati meaning of '{english_word}': {gujarati_meaning}")

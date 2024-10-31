
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        
        words = self.phrase.split()
        translated_words = []
        
        for word in words:
            if any(c in word for c in "!?,;:()'"):
                translated_words.append(self.translate_word_with_punctuation(word))
            elif '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_subword(subword) for subword in subwords]
                translated_words.append('-'.join(translated_subwords))
            else:
                translated_words.append(self.translate_subword(word))

        return ' '.join(translated_words)

    def translate_word_with_punctuation(self, word):
        punctuation = ''.join(c for c in word if c in "!?,;:()'")
        clean_word = ''.join(c for c in word if c not in "!?,;:()'")
        translated = self.translate_subword(clean_word)
        return translated + punctuation

    def translate_subword(self, word):
        ay = 'ay'
        yay = 'yay'
        nay = 'nay'
        if word.isupper():
            ay = 'AY'
            yay = 'YAY'
            nay = 'NAY'


        if word[0] in 'aeiouAEIOU':
            if word[-1] in 'aeiouAEIOU':
                return word + yay
            elif word[-1] == 'y':
                return word + nay
            else:
                return word + ay
        else:
            consonant_cluster = ''
            rest_of_word = word
            while rest_of_word and rest_of_word[0] not in 'aeiouAEIOU':
                consonant_cluster += rest_of_word[0]
                rest_of_word = rest_of_word[1:]
            return rest_of_word + consonant_cluster + 'ay'


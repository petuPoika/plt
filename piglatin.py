from os.path import split


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
        mark = ''
        
        for word in words:
            if '!' in word:
                mark = '!'
                parts = word.replace('!', '')
                translated_words.append(self.translate_subword(parts))
            elif '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_subword(subword) for subword in subwords]
                translated_words.append('-'.join(translated_subwords))
            else:
                translated_words.append(self.translate_subword(word))

        if mark:
            translated = ' '.join(translated_words)
            return translated + mark
        return ' '.join(translated_words)

    def translate_subword(self, word):
        if word[0] in 'aeiouAEIOU':
            if word[-1] in 'aeiouAEIOU':
                return word + 'yay'
            elif word[-1] == 'y':
                return word + 'nay'
            else:
                return word + 'ay'
        else:
            consonant_cluster = ''
            rest_of_word = word
            while rest_of_word and rest_of_word[0] not in 'aeiouAEIOU':
                consonant_cluster += rest_of_word[0]
                rest_of_word = rest_of_word[1:]
            return rest_of_word + consonant_cluster + 'ay'


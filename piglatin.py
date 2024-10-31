
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
            if word[0] in 'aeiouAEIOU':
                if word[-1] in 'aeiouAEIOU':
                    translated_words.append(word + 'yay')
                elif word[-1] == 'y':
                    translated_words.append(word + 'nay')
                else:
                    translated_words.append(word + 'ay')
            else:
                consonant_cluster = ''
                rest_of_word = word
                while rest_of_word and rest_of_word[0] not in 'aeiouAEIOU':
                    consonant_cluster += rest_of_word[0]
                    rest_of_word = rest_of_word[1:]
                translated_words.append(rest_of_word + consonant_cluster + 'ay')
        
        return ' '.join(translated_words)


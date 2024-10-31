
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        first_letter = self.phrase[0]
        last_letter = self.phrase[-1]
        if last_letter == 'y' and first_letter in 'aeiouAEIOU':
            return self.phrase + 'nay'
        if last_letter in 'aeiouAEIOU' and first_letter in 'aeiouAEIOU':
            return self.phrase + 'yay'
        if last_letter in 'kK':
            return self.phrase + 'ay'
        if first_letter not in 'aeiouAEIOU':
            consonant_cluster_end = 0
            for char in self.phrase:
                if char.lower() not in 'aeiou':
                    consonant_cluster_end += 1
                else:
                    break
            return self.phrase[consonant_cluster_end:] + self.phrase[:consonant_cluster_end] + 'ay'
        return ""


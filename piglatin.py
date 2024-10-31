
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        first_letter = self.phrase[0]
        second_letter = self.phrase[1]
        last_letter = self.phrase[-1]
        if last_letter == 'y' and first_letter in 'aeiouAEIOU':
            return self.phrase + 'nay'
        if last_letter in 'aeiouAEIOU' and first_letter in 'aeiouAEIOU':
            return self.phrase + 'yay'
        if last_letter in 'kK':
            return self.phrase + 'ay'
        if first_letter not in 'aeiouAEIOU':
            modified_phrase = self.phrase[1:] + first_letter
            if second_letter not in "aeiouAEIOU":
                modified_phrase = modified_phrase[1:] + second_letter
            return modified_phrase + 'ay'
        return ""



class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        if self.phrase[-1] == 'y' and self.phrase[0] in 'aeiouAEIOU':
            return self.phrase + 'nay'
        if self.phrase[-1] in 'aeiouAEIOU' and self.phrase[0] in 'aeiouAEIOU':
            return self.phrase + 'yay'
        if self.phrase[0] in 'aeiouAEIOU':
            return self.phrase + 'ay'
        return ""


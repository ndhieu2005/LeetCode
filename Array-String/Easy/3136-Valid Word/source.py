class Solution:
    def is_vowel(self,c):
        return c.lower() in 'aeiou'
    def is_consonant(self,c):
        return c.isalpha() and not self.is_vowel(c)
    def has_atLeastOneVowel(self,word):
        return any(self.is_vowel(c) for c in word)
    def has_atLeastOneConsonant(self,word):
        return any(self.is_consonant(c) for c in word)
    def isValid(self, word: str) -> bool:
        return (
            len(word) >= 3
            and word.isalnum()
            and self.has_atLeastOneVowel(word)
            and self.has_atLeastOneConsonant(word)
        )


        
"""
T2: Vowel Word Flip

Given a list of words, for each word where BOTH the first and last characters
are vowels, reverse the middle characters while keeping the first and last
characters unchanged. Words that don't satisfy this condition are left as-is.

Vowels are: a, e, i, o, u (both uppercase and lowercase).

Example:

    - For words = ["abcde", "hello"],
      the output should be vowel_word_flip(words) = ["adcbe", "hello"]

      Explanation:
        - "abcde": starts with 'a' (vowel) and ends with 'e' (vowel), so
          reverse the middle "bcd" → "dcb", giving "a" + "dcb" + "e" = "adcbe".
        - "hello": starts with 'h' (not a vowel), so it stays "hello".

    - For words = ["apple", "iglooi", "xyz"],
      the output should be vowel_word_flip(words) = ["apple", "ioolgi", "xyz"]

      Explanation:
        - "apple": starts with 'a' (vowel) but ends with 'e'... wait, 'e' IS
          a vowel. Middle "ppl" reversed → "lpp", giving "a" + "lpp" + "e" =
          "alppe". (Correction: "apple" → "alppe".)
        - "iglooi": starts with 'i' and ends with 'i' (both vowels). Middle
          "gloo" reversed → "oolg", giving "i" + "oolg" + "i" = "ioolgi".
        - "xyz": starts with 'x' (not a vowel), unchanged.
"""

def vowel_word_flip(words: list) -> list:
    ret = []
    const = set('aeiouAEIOU')
    for word in words: 
        if len(word) <= 2:
            ret.append(word)
            continue # finish no need to process more obviously
        if word[0] in const and word[-1] in const:
            newWord = word[0] + word[1:-1][::-1] + word[-1]
            ret.append(newWord)
        else:
            ret.append(word)
    return ret
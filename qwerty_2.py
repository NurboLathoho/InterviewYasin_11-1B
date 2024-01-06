def find_word(text, word):
    text_lower = text.lower()
    word_lower = word.lower()

    count = text_lower.count(word_lower)
    return count

text = "Hello world, hello Python"
word_to_find = "hello"
result = find_word(text, word_to_find)
print(result)  

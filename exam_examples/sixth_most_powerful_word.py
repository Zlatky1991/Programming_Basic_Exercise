the_most_powerful_word_text = ""
the_most_powerful_word_counter = 0
while True:
    word = input()

    if word == "End of words":
        break

    current_word_counter = 0
    for ch in word: #всяка дума ще разглеждам буква по буква и всяка буква ще взимам от ASCI таблицата и ще сумирам
        current_word_counter += ord(ch) # ord иска да върне кода който се крие зад буквата в ASCI таблицата
        #ако използваме chr вместо ord тогава като добавим число ти връща буквата според ASCI таблицата
        #ASCI таблицата се работи със ord и chr
    if word[0].lower() in "aeiouy":#lower - без значение дали буквата е голяма или малка аз я приравнявам винаги към малка
        current_word_counter *= len(word)
    else:
        current_word_counter = int(current_word_counter / len(word))

    if current_word_counter > the_most_powerful_word_counter:
        the_most_powerful_word_text = word
        the_most_powerful_word_counter = current_word_counter

print(f"The most powerful word is {the_most_powerful_word_text} - {the_most_powerful_word_counter}")

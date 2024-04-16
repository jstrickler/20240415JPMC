FILE_PATH = "DATA/words.txt"  #  174K words, one per line

FIRST_CHAR = "v"

OUTPUT_PATH = f"{FIRST_CHAR}_words.txt"

word_count = 0

with open(FILE_PATH) as words_in:
    with open(OUTPUT_PATH, "w") as words_out:
        for word in words_in:
            if word.startswith(FIRST_CHAR):
                word_count += 1
                words_out.write(word)

print(f"{word_count} words start with {FIRST_CHAR}")

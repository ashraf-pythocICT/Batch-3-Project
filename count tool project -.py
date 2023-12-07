def count_words_lines_chars(text):
    word_count = 0
    line_count = 0
    char_count = 0

    for line in text:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)

    return word_count, line_count, char_count

if __name__ == "__main__":
    text = []
    print("Enter text (type 'END' on a new line to finish input):")

    while True:
        line = input()
        if line == 'END':
            break
        text.append(line)

    word_count, line_count, char_count = count_words_lines_chars(text)

    print(f"Word count: {word_count}")
    print(f"Line count: {line_count}")
    print(f"Character count: {char_count}")



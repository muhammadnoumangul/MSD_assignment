from collections import Counter
import string

def get_successive_word_pairs(text):
    # Split the text into words using whitespace or punctuation as delimiters
    words = text.split()
    #print("I am printing words")
    #print(words)

    # Generate successive word pairs
    pairs = [(words[i], words[i + 1]) for i in range(len(words) - 1)]

    #print("I am printing pairs")
    #print(pairs)
    return pairs

def main():
    file_path = input("Enter the file path ")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            print(text)
            translator = str.maketrans('', '', string.punctuation)
            text = text.translate(translator)
            #print(text)
    except FileNotFoundError:
        print("File not found.")
        return

    word_pairs = get_successive_word_pairs(text)
    word_pair_counts = Counter(word_pairs)
    #print("i am printing word_pair_counts")
    #print(word_pair_counts)

    # Print the top 10 most frequently occurring word pairs
    for pair, count in word_pair_counts.most_common(10):
        print(pair, "-", count)

if __name__ == "__main__":
    main()

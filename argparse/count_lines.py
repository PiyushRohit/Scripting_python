import argparse

def count_lines_words(filename):
    line_count = 0
    word_count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
        print(f"File: {filename}")
        print(f"Total Lines: {line_count}")
        print(f"Total Words: {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines and words in a file.")
    parser.add_argument("filename", help="The name of the file to analyze")
    args = parser.parse_args()

    count_lines_words(args.filename)

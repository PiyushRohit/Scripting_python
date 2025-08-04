import re

# Open and read the file
with open('sample_test_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Find all matches of the word 'vlsi' (case-insensitive)
matches = re.findall(r'\bvlsi\b', content, flags=re.IGNORECASE)

# Print the count
print(f"The word 'vlsi' appears {len(matches)} times.")

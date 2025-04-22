word_per_page = 0
pages = int(input("Number of pages: "))

# This statement was not an assignment but a comparison. The Print statement returns a boolean value and shows this.
# word_per_page == int(input("Number of words per page: "))
# print(word_per_page == int(input("Number of words per page: ")))

# Corrected
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

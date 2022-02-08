def print_upper_words(words):
	"""print each word on separate line, uppercased"""

	for word in words:
		print(word.upper())


def print_upper_words2(words):
	"""print each word that starts with letter 'e' on separate line, uppercased"""

	for word in words:
         if word.startswith("e") or word.startswith("E"):
        	 print(word.upper())

def print_upper_words3(words, must_start_with):
	"""print each word that starts with one of given letters on sep line, uppercased"""

	for word in words:
     	 for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
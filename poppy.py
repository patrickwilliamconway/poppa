from english_words import english_words_lower_alpha_set as ew

def len_word(w, l): return len(w) == l
assert len_word("1" * 9, 9) == True
assert len_word("1", 9) == False

def remove_i_char(w, index): return w[:index] + w[index+1:]
assert remove_i_char("cat", 0) == "at"
assert remove_i_char("cat", 1) == "ct"
assert remove_i_char("cat", 2) == "ca"
assert remove_i_char("a", 0) == ""

word_sets = [
	set(filter(lambda word: len_word(word, 1), ew)),
	set(filter(lambda word: len_word(word, 2), ew)),
	set(filter(lambda word: len_word(word, 3), ew)),
	set(filter(lambda word: len_word(word, 4), ew)),
	set(filter(lambda word: len_word(word, 5), ew)),
	set(filter(lambda word: len_word(word, 6), ew)),
	set(filter(lambda word: len_word(word, 7), ew)),
	set(filter(lambda word: len_word(word, 8), ew)),
	set(filter(lambda word: len_word(word, 9), ew)),
]

def is_word(w, depth):
	indent = "  " * depth
	length_check = 8 - depth
	if len(w) == 0:
		print("we've found a word!")
	else:
		for idx, letter in enumerate(w):
			sub_word = remove_i_char(w, idx)
			if sub_word in word_sets[length_check]:
				if depth == 1:
					print(f"{w}")
				print(f"{indent}{sub_word}")
				return is_word(sub_word, depth + 1)

def iterate_set(words):
	for w in words:
		is_word(w, 1)

iterate_set(word_sets[8])
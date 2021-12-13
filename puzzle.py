def len_word(w, l): return len(w) == l
assert len_word("1" * 9, 9) == True
assert len_word("1", 9) == False

def remove_i_char(w, index): return w[:index] + w[index+1:]
assert remove_i_char("cat", 0) == "at"
assert remove_i_char("cat", 1) == "ct"
assert remove_i_char("cat", 2) == "ca"
assert remove_i_char("a", 0) == ""

def word_sets(length, dictionary):
	l = list()
	for i in range(1, length + 1):
		s = set(filter(lambda word: len_word(word, i), dictionary))
		l.append(s)
	return l


def is_word(w, depth, dicts, running, ans_dict):
	indent = "  " * depth
	length_check = 8 - depth
	if len(w) == 1:
		ans_dict[running[0]] = running
	else:
		for idx, letter in enumerate(w):
			sub_word = remove_i_char(w, idx)
			if sub_word in dicts[length_check]:
				# if depth == 1:
				# 	print(f"{w}")
				# print(f"{indent}{sub_word}")
				new_running = running.copy()
				new_running.append(sub_word)
				return is_word(sub_word, depth + 1, dicts, new_running, ans_dict)

def iterate_set(word_len, dicts, ans_dict):
	for w in dicts[word_len - 1]:
		is_word(w, 1, dicts, list([w]), ans_dict)

# turns out unix has a list of words at:
# wc -l /usr/share/dict/words
# 235886 /usr/share/dict/words
with open("/usr/share/dict/words", "r") as word_file:
	english_words = set(word.strip().lower() for word in word_file)
b = word_sets(9, english_words)
for l in b:
	assert len(l) > 0
ans_dict = dict()
iterate_set(9, b, ans_dict)

for v in ans_dict.values():
	if v[-1] == "a" or v[-1] == "i":
		print(v)
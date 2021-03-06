# The Riddle
9 letter word:
remove one letter at a time: each letter removed still
leaves you with a
common english word, down to the last letter Poppa

# Approach
From a dictionary of english words:
1. find subsets of words of length 1 - 9
2. for each word of length N, check each subword of length N-1 for membership in word subset of length N-1
3. resurse until we have an empty string

# Data
I'm pulling the words from `/usr/share/dict/words`. 

# Answer(s)

<details open>
<summary>Using the unix words, I got all these results:</summary>
<br>

- ['branchery', 'brancher', 'rancher', 'rancer', 'racer', 'acer', 'aer', 'er', 'r']

- ['millioner', 'milliner', 'milline', 'millie', 'mille', 'mile', 'mil', 'mi', 'i']

- ['concreate', 'cocreate', 'ocreate', 'create', 'crate', 'rate', 'ate', 'te', 'e']

- ['camphoryl', 'camphory', 'camphor', 'campho', 'campo', 'camp', 'cap', 'ca', 'a']

- ['ampullary', 'ampullar', 'ampulla', 'amulla', 'mulla', 'ulla', 'ula', 'la', 'a']

- ['emendable', 'mendable', 'endable', 'enable', 'nable', 'able', 'ale', 'ae', 'e']

- ['coronated', 'coronate', 'coronae', 'corona', 'coroa', 'cora', 'ora', 'ra', 'a']

- ['brahmanda', 'brahmana', 'brahman', 'brahma', 'brahm', 'bram', 'ram', 'am', 'm']

- ['secretory', 'secretor', 'secreto', 'secret', 'secre', 'sere', 'ere', 're', 'e']

- ['gnomology', 'nomology', 'noology', 'oology', 'ology', 'logy', 'loy', 'ly', 'y']

- ['uparching', 'parching', 'arching', 'aching', 'ching', 'hing', 'ing', 'in', 'n']

- ['acalycine', 'calycine', 'calcine', 'alcine', 'aline', 'line', 'lie', 'ie', 'e']

- ['prelation', 'relation', 'elation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['brahmanic', 'brahmaic', 'brahmic', 'brahmi', 'brahm', 'bram', 'ram', 'am', 'm']

- ['picketeer', 'picketer', 'pickeer', 'picker', 'piker', 'pier', 'per', 'er', 'r']

- ['palmation', 'palation', 'alation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['floridean', 'floridan', 'florian', 'floran', 'loran', 'loan', 'lan', 'an', 'n']

- ['teaseller', 'teaseler', 'teasler', 'teaser', 'easer', 'ease', 'ase', 'se', 'e']

- ['shameable', 'shamable', 'shamble', 'hamble', 'amble', 'able', 'ale', 'ae', 'e']

- ['affronted', 'affronte', 'affront', 'afront', 'front', 'font', 'fot', 'fo', 'o']

- ['probeable', 'probable', 'probabl', 'probal', 'proal', 'proa', 'poa', 'pa', 'a']

- ['tambouret', 'tabouret', 'taboret', 'tabret', 'abret', 'bret', 'ret', 're', 'e']

- ['millinery', 'milliner', 'milline', 'millie', 'mille', 'mile', 'mil', 'mi', 'i']

- ['expalpate', 'epalpate', 'palpate', 'palate', 'alate', 'late', 'ate', 'te', 'e']

- ['amendable', 'mendable', 'endable', 'enable', 'nable', 'able', 'ale', 'ae', 'e']

- ['palpation', 'palation', 'alation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['scrabbler', 'scabbler', 'cabbler', 'cabler', 'abler', 'able', 'ale', 'ae', 'e']

- ['guttulate', 'guttulae', 'guttule', 'guttle', 'gutte', 'gutt', 'gut', 'ut', 't']

- ['laureated', 'laureate', 'aureate', 'aurate', 'urate', 'rate', 'ate', 'te', 'e']

- ['foresweat', 'foreseat', 'foreset', 'forset', 'forst', 'fort', 'ort', 'or', 'r']

- ['shallowly', 'shallowy', 'sallowy', 'sallow', 'allow', 'alow', 'low', 'ow', 'w']

- ['scrabbled', 'scrabble', 'scabble', 'cabble', 'cable', 'able', 'ale', 'ae', 'e']

- ['lacerated', 'lacerate', 'acerate', 'cerate', 'crate', 'rate', 'ate', 'te', 'e']

- ['reflation', 'relation', 'elation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['estranger', 'stranger', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['deltation', 'delation', 'elation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['affronter', 'affronte', 'affront', 'afront', 'front', 'font', 'fot', 'fo', 'o']

- ['teacherly', 'teachery', 'teacher', 'teache', 'tache', 'ache', 'che', 'he', 'e']

- ['phorology', 'horology', 'orology', 'oology', 'ology', 'logy', 'loy', 'ly', 'y']

- ['replaster', 'relaster', 'relater', 'elater', 'later', 'late', 'ate', 'te', 'e']

- ['chorology', 'horology', 'orology', 'oology', 'ology', 'logy', 'loy', 'ly', 'y']

- ['treachery', 'teachery', 'teacher', 'teache', 'tache', 'ache', 'che', 'he', 'e']

- ['barrabora', 'barabora', 'barabra', 'barbra', 'barra', 'bara', 'ara', 'ra', 'a']

- ['romagnese', 'romanese', 'romanes', 'romane', 'roman', 'oman', 'man', 'an', 'n']

- ['silverily', 'silverly', 'silvery', 'silver', 'siver', 'sier', 'ser', 'er', 'r']

- ['floriated', 'floriate', 'florate', 'lorate', 'orate', 'rate', 'ate', 'te', 'e']

- ['spendable', 'sendable', 'endable', 'enable', 'nable', 'able', 'ale', 'ae', 'e']

- ['casemated', 'casemate', 'caseate', 'casate', 'caste', 'cate', 'ate', 'te', 'e']

- ['chelation', 'celation', 'elation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['strangler', 'stranger', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['machinery', 'machiner', 'machine', 'machin', 'machi', 'mahi', 'mah', 'ah', 'h']

- ['macerater', 'macerate', 'acerate', 'cerate', 'crate', 'rate', 'ate', 'te', 'e']

- ['darklings', 'darkling', 'darling', 'daring', 'darin', 'dain', 'din', 'in', 'n']

- ['cabriolet', 'cabriole', 'cariole', 'carole', 'carol', 'carl', 'cal', 'al', 'l']

- ['floridian', 'floridan', 'florian', 'floran', 'loran', 'loan', 'lan', 'an', 'n']

- ['acaridean', 'caridean', 'caridea', 'carida', 'carid', 'arid', 'rid', 'id', 'd']

- ['tabularly', 'tabulary', 'tabular', 'tabula', 'taula', 'aula', 'ula', 'la', 'a']

- ['precourse', 'recourse', 'recurse', 'recuse', 'reuse', 'ruse', 'use', 'se', 'e']

- ['coronaled', 'coronale', 'coronae', 'corona', 'coroa', 'cora', 'ora', 'ra', 'a']

- ['ghostlily', 'ghostily', 'ghostly', 'hostly', 'hotly', 'holy', 'hoy', 'hy', 'y']

- ['espantoon', 'spantoon', 'pantoon', 'panton', 'anton', 'anon', 'non', 'on', 'n']

- ['strengthy', 'strength', 'strenth', 'strent', 'trent', 'rent', 'ret', 're', 'e']

- ['haughtily', 'haughtly', 'haughty', 'haught', 'aught', 'augh', 'ugh', 'ug', 'g']

- ['nostology', 'nosology', 'noology', 'oology', 'ology', 'logy', 'loy', 'ly', 'y']

- ['stamineal', 'staminal', 'stamina', 'stamin', 'stain', 'tain', 'tin', 'in', 'n']

- ['strapping', 'trapping', 'rapping', 'raping', 'aping', 'ping', 'ing', 'in', 'n']

- ['remigrate', 'emigrate', 'migrate', 'mirate', 'irate', 'rate', 'ate', 'te', 'e']

- ['strickler', 'stickler', 'tickler', 'ticker', 'ticer', 'tier', 'tie', 'ie', 'e']

- ['deflation', 'delation', 'elation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['jatrophic', 'atrophic', 'trophic', 'tropic', 'topic', 'topi', 'toi', 'ti', 'i']

- ['strippler', 'trippler', 'rippler', 'ripper', 'riper', 'rier', 'rie', 'ie', 'e']

- ['strophaic', 'strophic', 'trophic', 'tropic', 'topic', 'topi', 'toi', 'ti', 'i']

- ['externals', 'external', 'eternal', 'ternal', 'terna', 'tera', 'era', 'ra', 'a']

- ['strangles', 'strangle', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['turntable', 'turnable', 'tunable', 'unable', 'nable', 'able', 'ale', 'ae', 'e']

- ['dealation', 'delation', 'elation', 'lation', 'latin', 'lain', 'lin', 'in', 'n']

- ['shearsman', 'shearman', 'sherman', 'herman', 'herma', 'erma', 'era', 'ra', 'a']

</details>

But if we're being real, the last "word" needs to be "a" or "i", right? That is the only single letter work that makes sense in common english.

<details open>
<summary>That leaves us with:</summary>
<br>

- ['millinery', 'milliner', 'milline', 'millie', 'mille', 'mile', 'mil', 'mi', 'i']

- ['estranger', 'stranger', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['strangles', 'strangle', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['camphoryl', 'camphory', 'camphor', 'campho', 'campo', 'camp', 'cap', 'ca', 'a']

- ['tabularly', 'tabulary', 'tabular', 'tabula', 'taula', 'aula', 'ula', 'la', 'a']

- ['strangler', 'stranger', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['shearsman', 'shearman', 'sherman', 'herman', 'herma', 'erma', 'era', 'ra', 'a']

- ['probeable', 'probable', 'probabl', 'probal', 'proal', 'proa', 'poa', 'pa', 'a']

- ['externals', 'external', 'eternal', 'ternal', 'terna', 'tera', 'era', 'ra', 'a']

- ['strophaic', 'strophic', 'trophic', 'tropic', 'topic', 'topi', 'toi', 'ti', 'i']

- ['coronated', 'coronate', 'coronae', 'corona', 'coroa', 'cora', 'ora', 'ra', 'a']

- ['coronaled', 'coronale', 'coronae', 'corona', 'coroa', 'cora', 'ora', 'ra', 'a']

- ['barrabora', 'barabora', 'barabra', 'barbra', 'barra', 'bara', 'ara', 'ra', 'a']

- ['ampullary', 'ampullar', 'ampulla', 'amulla', 'mulla', 'ulla', 'ula', 'la', 'a']

- ['jatrophic', 'atrophic', 'trophic', 'tropic', 'topic', 'topi', 'toi', 'ti', 'i']

- ['millioner', 'milliner', 'milline', 'millie', 'mille', 'mile', 'mil', 'mi', 'i']

</details>


But of these words, the two letter words are a stretch.
<details open>
<summary>I think the most likely options are:</summary>
<br>

- ['estranger', 'stranger', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['strangles', 'strangle', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

- ['strangler', 'stranger', 'strange', 'strang', 'stang', 'tang', 'tag', 'ta', 'a']

</details>

 
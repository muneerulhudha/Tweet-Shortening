import re
#getting the input from the user

tweets=raw_input("Enter your tweet to be shortened:\n\n")
#tweets="wru now wru now"
#tweets=" now"

vowels = 'a', 'e', 'i', 'o', 'u'


def remove_vowels_case1(word):
    
	for letter in word:	
		#if   letter[0]  == ['a','e','i','o','u']:
		#	letter=letter[1:]
		print letter
	#	if   letter  in ['a','e','i','o','u']:
	#		word=word.replace(letter,'')
	#print word


#putting each words into a list

def put_in_a_list(sentence):  #removes vowels except if first character is a vowel
	words=sentence.split()
	#print words
	abbr_set=make_abbr_set("/home/siv/Dev/word-short/common_abbr.txt")
	#print abbr_set
#	for item in words:
#		for vowel in vowels:
	#remove_vowels_case1(words)	
#			words=item.replace(vowel,'')
			#print item	
#	w[0].replace('e', 'e').replace('a','a').replace('i','i').replace('o','o').replace('u','u') and 
	#aa = set(abbr_set)
	#aa.intersection(b)
	#l1=list(set(words).intersection(set(abbr_set)))
	#for w in l1:
	#	words=['*'+w]
	#	print words

#	matches = [item for item in words if item in abbr_set]
#	print matches
#	print "matched"
#	q=[([int(item1 == item2) for item2 in abbr_set], [n for n, item2 in enumerate(abbr_set) if item1 == item2]) for item1 in words]
#	print q

	for idx,w in enumerate(words) :
		
		if len(w)>2:
			if w in abbr_set:
#				print "its THERE"
				w='*'+w
				words[idx]=w
				#idx=idx+1
			if w[0] is not '*':
				#print w
				w=w.replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u','*']) else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','')
				words[idx]=w	
	#	words = [w.replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u','*']) else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','') for w in words] #for w in words] 
		#else: 
		#words= [w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','') for w in words]
	return words
#	print words

#put_in_a_list(tweets)
#remove_vowels_case1(tweets)	





#print tweets


def remove_rep_consonants(words):
#	words=tweets.split()
	#words=["".join(OrderedDict.fromkeys(w)) for w in words]
	#for i in words:
	words=[	re.sub(r'(\w)\1+', r'\1', e ) for e in words]
	for idx,w in enumerate(words) :
		if w[0] == '*':
			words[idx]=w[1:]	
	print '%s ' % ' '.join(map(str, words))#print "%s" % words



def make_abbr_set(file):
	fileName=open(file)
	lines =[i.strip() for i in open(file).readlines()]
	return lines


remove_rep_consonants(put_in_a_list(tweets))

import re
#getting the input from the user

tweets=raw_input("emter your tweet to be shortened:")
#tweets="order food"

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
												print words
													
													#	for item in words:
													#		for vowel in vowels:
														#remove_vowels_case1(words)	
														#			words=item.replace(vowel,'')
																	#print item	
																	#	w[0].replace('e', 'e').replace('a','a').replace('i','i').replace('o','o').replace('u','u') and 

																		words = [w.replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','') if (w[0] not in ['a','e','i','o','u']) else w[:1]+w[1:].replace('e', '').replace('a','').replace('i','').replace('o','').replace('u','') for w in words]
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
																							print '%s ' % ' '.join(map(str, words))#print "%s" % words

																							remove_rep_consonants(put_in_a_list(tweets))


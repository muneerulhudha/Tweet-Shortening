Text shortening tool for twitter v1.0

Programming language: Python.

Implementation.

1. Get input as a sentence.
2. Split the sentence into words. Each word is an array by itself.
3. If the first character is not a vowel, we remove the vowels from the words.
4. If it is a vowel, we leave the first character unchanged.
	(The first character holds the greater meaning. Eg: 'Egg' getting replaced by 'gg' doesn't make sense. Whereas 'year' replaced by 'yr' makes sense)
5. Replace repeated consonants by a single occurence.
	(Eg: 'Egg' will become 'Eg')
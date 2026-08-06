#Count how many times a specific word appears in a sentence. 
text=input("Enter a string :")
word=input("enter a word to count :")
count=0
words=text.split()
count=words.count(word)
print("number of ", word,"word is",count)

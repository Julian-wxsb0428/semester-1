# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
word_count=0
# open and read the file
with open("glasses.txt","r") as infile:
    for line in infile:
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings
        words=line.split()
        word_count+= len(words)
# display the wordcount
print(word_count)
# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
import os

#open the file input and read the file into contents
f = open("input.txt", 'r')
contents = f.read().splitlines()
#close the input file 
f.close()

#Open the file output 
f = open("output.txt", 'w')

#loop through the contents and for every line, and write each to the output file
for currentLine in contents:
	final = (currentLine[0:10] + "\n") #cuts off the words after ten characters, and new line 	
	#Write the final message to output 
	f.write(final) 

#Close the output file (outside of the loop)
f.close()


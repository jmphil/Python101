# from previous homework
# Given a word as a string, print the result of extending any long vowels to the length of 5.

dblvwl = input("Give me a word to double its long vowels: ")
result = dblvwl

for i in range(0, len(dblvwl) - 1):
    if dblvwl[i] == dblvwl[i+1] :
        result = dblvwl[0:i] + dblvwl[i]*3 + dblvwl[i:]
        # break
    
print(result)
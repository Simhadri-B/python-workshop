A = ["abba", "bbaa", "abbaba", "bbaabb"]
for x in A:
    rev = ""
    for ch in x:
        rev = ch + rev  
    if x == rev:
        print(x, "Palindrome")
    else:
        print(x, " Not Palindrome")

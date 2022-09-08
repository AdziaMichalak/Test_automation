def palindrome(txt):
    txt = str(txt)
    txt = txt.lower()
    txt = txt.replace(" ", "")
    txt = "".join(l for l in txt if l.isalnum())
    return txt == txt[::-1]

#print(palindrome(12344321))
#print(palindrome("kaja"))


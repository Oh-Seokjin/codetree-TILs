text = input()
for tok in text:
    if tok.isupper():
        print(tok.lower(), end="")
    elif tok.islower():
        print(tok.upper(), end='')
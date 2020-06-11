#changesto be tested
s=input()


def palin(s):
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1] and palin(s[1:-1]):
            return True


c=palin(s)
if c==True:
    print(s,"is palindrome")
else:
    print("not a palindrome")

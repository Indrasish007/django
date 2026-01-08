#string palindrome
n=input("Enter a string  : ")
rev=n[: : -1]
print(rev)
if n==rev:
    print("palindrome")
else:
    print("Not pali")
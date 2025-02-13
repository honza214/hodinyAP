print("zadejte prvni cislo")
y = int(input())
print("zadejte druhy cislo")
x = int(input())
if x > y:
    print(str(x) + " je vetsi nez " + str(y))
elif x==y:
    print("cisla jsou stejna")
else: 
    print(str(x) + " je mensi nez " + str(y))
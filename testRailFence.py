from railFence import decryptRailFence

ciphertext = str(raw_input("Send the cipher text: "))
ciphertext = ciphertext.replace(" ", "%")
print "Brute forcing all rails and offsets:"

rails = range(2,10)
offsets = range(0,10)
print(rails)
print(offsets)
for i in rails:
    for j in offsets:
        tempciphertext = " " * j + ciphertext
        print decryptRailFence(tempciphertext, i,0)


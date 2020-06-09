from railFence import decryptRailFence
import sys
# CHANGE THIS
# THE LAST NUMBER DOES NOT GET USED
rails = range(2,11)
offsets = range(0,11)

# DONT CHANGE THIS

if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " [ciphertext]")
    print("You may need to use quotes around the ciphertext if it contains spaces")
    exit(1)
ciphertext = sys.argv[1]
print("-----------------------------")
ciphertext = ciphertext.replace(" ", "%")
print "Brute forcing all rails and offsets:"


print(rails)
print(offsets)
for i in rails:
    for j in offsets:
        tempciphertext = "*" * j + ciphertext
        print decryptRailFence(tempciphertext, i, 0).replace("*", "").replace("%", " ")


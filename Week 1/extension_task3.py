name = input("Enter your name: ")
print("(H)ello"+"\n"+"(G)oodbye"+"\n"+"(Q)uit"+"\n")
letter = input('>>>').upper()

if letter == "H":
    print("Hello ", name)
elif letter == "G":
    print("Goodbye ", name)
elif letter == "Q":
    print("Finished")
else:
    print("Invalid Choice")


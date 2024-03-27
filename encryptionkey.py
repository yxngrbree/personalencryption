 # Fepo Encryption Key

f = "error"  # testues
y = "success"  # testues

wlc = "Welcome to the Fepo encryption software, please choose an option from the list below:"
print(wlc)
opt1 = "1. Encrypt"
print(opt1)
opt2 = "2. Decrypt"
print(opt2)
choice = int(input("Enter the number of your desired option: "))

decmessage = ""

if choice == 1:
    print("You have chosen Encryption.")
    print("Enter your message you want to encrypt")

    message = str(input("Here: "))  # per testim
    wordlist = [chr(ord('A') + i) for i in range(26)] + [chr(ord('a') + i) for i in range(26)]  # per testim
    numlis = [int(0 + i) for i in range(10)]  # per testim

    for number in range(17):
        for numberj in range(number):
            print("*", end=" ")
        print()

    enclsit = []
    for char in message:
        enclsit.append(char)

    newlist = []
    for item in enclsit:
        if item == "a":
            newlist.append("0@£$%£*&")
        if item == "b":
            newlist.append("0!%^^!$)")
        if item == "c":
            newlist.append("0+^%^%^")
        if item == "d":
            newlist.append("0?%^&*!$")
        if item == "e":
            newlist.append("0[%^&&^&")
        if item == "f":
            newlist.append("0]!!!!!!")
        if item == "g":
            newlist.append("0{^&%$££")
        if item == "h":
            newlist.append("0($%^*&!")
        if item == "i":
            newlist.append("0}!^&*)$")
        if item == "j":
            newlist.append("0)!£!$%^")
        if item == "k":
            newlist.append("0£&&&*")
        if item == "l":
            newlist.append("0%$^$^^^")
        if item == "m":
            newlist.append("0^%^&*%$")
        if item == "n":
            newlist.append("0&!££$&^")
        if item == "o":
            newlist.append("0*£££££^")
        if item == "p":
            newlist.append("0-@L:@}~")
        if item == "q":
            newlist.append("0=##}:")
        if item == "r":
            newlist.append("0.?@}@##")
        if item == "s":
            newlist.append("0`><?}~@")
        if item == "t":
            newlist.append("0'<<><><")
        if item == "u":
            newlist.append("0/><><><")
        if item == "v":
            newlist.append("0>¬`¬#].")
        if item == "w":
            newlist.append("0<^^^&*")
        if item == "x":
            newlist.append("0|¬¬¬¬!/")
        if item == "y":
            newlist.append("0¬/?????")
        if item == "z":
            newlist.append("0:::@}~")
        if item == "A":
            newlist.append(",@@£$%££")
        if item == "B":
            newlist.append(",!!^&*!£")
        if item == "C":
            newlist.append(",++!£$%^")
        if item == "D":
            newlist.append(",??&%^&*")
        if item == "E":
            newlist.append(",[[]{]#'")
        if item == "F":
            newlist.append(",]]``%^&")
        if item == "G":
            newlist.append(",{@{&^$%")
        if item == "H":
            newlist.append(",(()))))")
        if item == "I":
            newlist.append(",}+}~@@}")
        if item == "J":
            newlist.append(",))£$$£%")
        if item == "K":
            newlist.append(",££@@::}")
        if item == "L":
            newlist.append(",%++_%^^")
        if item == "M":
            newlist.append(",^^^&*()")
        if item == "N":
            newlist.append(",&&[[!]]")
        if item == "O":
            newlist.append(",[?]!!")
        if item == "P":
            newlist.append(",--??><>")
        if item == "Q":
            newlist.append(",==<><?>")
        if item == "R":
            newlist.append(",..|||>.")
        if item == "S":
            newlist.append(",`¬###")
        if item == "T":
            newlist.append(",''#||..")
        if item == "U":
            newlist.append(",//>£$%^")
        if item == "V":
            newlist.append(",>>>>?<<")
        if item == "W":
            newlist.append(",<<>><<<")
        if item == "X":
            newlist.append(",||,,..;")
        if item == "Y":
            newlist.append(",¬¬``@:>")
        if item == "Z":
            newlist.append(",::*&&^%")
        if item == " ":
            newlist.append("#--=#!£$")
        if item == "0":
            newlist.append(".&^^%^&)")
        if item == "1":
            newlist.append(".£!$@~><")
        if item == "2":
            newlist.append(".$%$!£$%")
        if item == "3":
            newlist.append(".*^$))))")
        if item == "4":
            newlist.append(".!%$£)_!")
        if item == "5":
            newlist.append(".£^^*£$%")
        if item == "6":
            newlist.append(".*()!><|")
        if item == "8":
            newlist.append(".,.£$/:;")
        if item == "9":
            newlist.append(".&&*).?@")

    enkprn = "".join(newlist)
    print(f"Copy the following message ------> {enkprn}")

# decryption part
if choice == 2:
    print("You have chosen Decryption.")  # eshte ok deri posht
    print("Enter your message you want to decrypt")
    decmessage = str(input("Here: "))

decod = {
    "0@£$%£*&": "a",  
    "0!%^^!$)": "b",
    "0+^%^%^": "c",
    "0?%^&*!$": "d",
    "0[%^&&^&": "e",
    "0]!!!!!!": "f",
    "0{^&%$££": "g",
    "0($%^*&!": "h",
    "0}!^&*)$": "i",
    "0)!£!$%^": "j",
    "0£&&&*": "k",
    "0%$^$^^^": "l",
    "0^%^&*%$": "m",
    "0&!££$&^": "n",
    "0*£££££^": "o",
    "0-@L:@}~": "p",
    "0=##}:": "q",
    "0.?@}@##": "r",
    "0`><?}~@": "s",
    "0'<<><><": "t",
    "0/><><><": "u",
    "0>¬`¬#].": "v",
    "0<^^^&*": "w",
    "0|¬¬¬¬!/": "x",
    "0¬/?????": "y",
    "0:::@}~": "z",
    ",@@£$%££": "A",
    ",!!^&*!£": "B",
    ",++!£$%^": "C",
    ",??&%^&*": "D",
    ",[[]{]#'": "E",
    ",]]``%^&": "F",
    ",{@{&^$%": "G",
    ",(()))))": "H",
    ",}+}~@@}": "I",
    ",))£$$£%": "J",
    ",££@@::}": "K",
    ",%++_%^^": "L",
    ",^^^&*()": "M",
    ",&&[[!]]": "N",
    ",[?]!!": "O",
    ",--??><>": "P",
    ",==<><?>": "Q",
    ",..|||>.": "R",
    ",`¬###": "S",
    ",''#||..": "T",
    ",//>£$%^": "U",
    ",>>>>?<<": "V",
    ",<<>><<<": "W",
    ",||,,..;": "X",
    ",¬¬``@:>": "Y",
    ",::*&&^%": "Z",
    "#--=#!£$": " ",
    ".&^^%^&)": "0",
    ".£!$@~><": "1",
    ".$%$!£$%": "2",
    ".*^$))))": "3",
    ".!%$£)_!": "4",
    ".£^^*£$%": "5",
    ".*()!><|": "6",
    ".,.£$/:;": "8",
    ".&&*).?@": "9",
}

def decrypt_message(enc_message):
    dec_message = []
    key_length = len(list(decod.keys())[0])  # length of a key in the dictionary
    for i in range(0, len(enc_message), key_length):
        enc_word = enc_message[i:i+key_length]
        if enc_word in decod:
            dec_message.append(decod[enc_word])
    return ''.join(dec_message)

decrypted_message = decrypt_message(decmessage)
print(f"Decrypted message: {decrypted_message}")



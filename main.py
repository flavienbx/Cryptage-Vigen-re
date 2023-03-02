def lettre(c):
    car = ord(c.upper())
    return car>64 and car<91

def decalage(c,k):
    car = ord(c.upper())
    if lettre(c):
        car += k
        while car>90:
            car -= 26
        while car<65:
            car += 26
        return chr(car)
    else:
        return ""

def cryptage(text, text_key, boolean):
    n = 0
    chiffre=''
    for c in text:
        if lettre(c):
            k = ord(text_key[n%len(text_key)])-65
            if boolean:
                chiffre += decalage(c,k)
            else:
                chiffre += decalage(c,-k)
            n+=1
        else:
            chiffre += c
    return chiffre

def main():
    texte = str(input("\nTexte : "))
    key = str(input("Clé de cryptage : "))
    select_action = 0
    while (select_action == 0):
        try:
            print(f"\nText : {texte}\nKey : {key}\n")
            select_action = int(input("Crypter le message : [1] \nDécrypter le message : [2]\nAction : "))
            if (select_action == 1):
                return_text = cryptage(texte, key, True)
            elif (select_action == 2):
                return_text = cryptage(texte, key, False)
        except:
            pass
    print(f"Message : {return_text.lower()}")

if __name__ == "__main__":
    while True:
        main()

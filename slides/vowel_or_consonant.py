input_letter = input("Type here a letter: ")
vowels = "a","e","i","o","u"
consonants = "b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"
input_letter = input_letter.lower()
if input_letter in vowels:
    print("Your letter is a vowel!")
elif input_letter in consonants:
    print("Your letter is a consonant!")
else:
    print("Your letter isn't on consonants or vowels group.")
#Des
def translate (str):
    Translater = ""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                Translater=Translater + "Z"
            else:
                 Translater=Translater+"z"

        else:
            Translater=Translater+letter
    return Translater
print(translate(input("Please Enter a phase :")))
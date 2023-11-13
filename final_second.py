import random

password = ""
buffer = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+*/\|"
)

choice = input("Do You Want To Generate A new Password ? (y/n): ").strip().lower()

while True:
    if choice == "y" or choice == "yes":
        length_of_password = int(
            input("Please Enter Length Of Password You Want: ").strip()
        )
        while len(password) < length_of_password:
            password += buffer[random.randint(0, len(buffer) - 1)]

        print(f"Your Generated Password: {password}")
        print("=" * 50)
        choice2 = input("Do You Want To Generate Password Again ? (y/n)").strip()

        if choice2 == "n" or choice2 == "no":
            print("Okay, Thank You. 😚")
            break
        elif choice2 == "y" or choice2 == "yes":
            pass
        else:
            print("Invalid Choice! 🤨🤔🙄")
            break

    elif choice == "n":
        print("Okay, Thank You. 😚")
        break

    else:
        print("Invalid Choice! 🤨🤔🙄")
        break

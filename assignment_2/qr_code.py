import qrcode
import random
import string
from PIL import Image

def generate_random_string(length=6):
    """Generate a random string of uppercase letters and digits."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def create_qr_code(data):
    """Generate a QR code from the given string."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    return img

def qr_code_game():
    """The QR code guessing game."""
    print("Welcome to the QR Code Generator Game!")
    
    # Generate a random string that the user needs to guess
    correct_string = generate_random_string()
    
    # Generate a QR code for that string
    qr_image = create_qr_code(correct_string)
    
    # Show the QR code to the user (in a real game, you might hide it)
    qr_image.show()

    print("\nA QR code has been generated. Try to guess the string embedded in it.")
    
    # Game loop for guessing the string
    attempts = 3
    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Enter your guess: ").strip()
        
        if guess == correct_string:
            print("Congratulations! You guessed the correct string!")
            break
        else:
            attempts -= 1
            print("Incorrect! Try again.")

    if attempts == 0:
        print(f"\nSorry, you've run out of attempts. The correct string was: {correct_string}")

qr_code_game()

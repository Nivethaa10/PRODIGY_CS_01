def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Main program
print("Caesar Cipher Program")
message = input("Enter your message: ")
shift = int(input("Enter shift value (integer): "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode selected.")
else:
    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")

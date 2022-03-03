def rot13_cipher(text):
    result = ""
    result_m = ""
    resultado = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text    
        if (char.isupper()):
            resultado += chr((ord(char) + 13 - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
        else:
            resultado += chr((ord(char) + 13 - 97) % 26 + 97)

    return resultado

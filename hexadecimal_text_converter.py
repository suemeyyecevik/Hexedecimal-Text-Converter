# -*- coding: utf-8 -*-
"""Hexadecimal_Text_Converter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N48e4a4TFMF7Joth3BHbuz1uw69pPSl8
"""

def text_to_hex(text):
    """Convert text to hexadecimal."""
    return text.encode("utf-8").hex()

def hex_to_text(hex_string):
    """Convert hexadecimal to text."""
    return bytes.fromhex(hex_string).decode("utf-8")

while True:
    print("\nHexadecimal Text Converter")
    print("1. Convert text to hex")
    print("2. Convert hex to text")
    print("3. Exit")
    choice = input("Make your choice: ")

    if choice == "1":
        text = input("Enter the text: ")
        hex_result = text_to_hex(text)
        print("Hexadecimal representation:", hex_result)
    elif choice == "2":
        hex_string = input("Enter the hexadecimal text: ")
        try:
            original_text = hex_to_text(hex_string)
            print("Original text:", original_text)
        except:
            print("Invalid hexadecimal text!")
    elif choice == "3":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again!")
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):

  if cipher_direction == "decode":
    shift_amount *= -1

  end_text = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift_amount) % 26
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"The {cipher_direction}d text is: {end_text}")
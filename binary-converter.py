def text_to_binary(text):
    binary_list = [format(ord(char), '08b') for char in text]
    return ' '.join(binary_list)

def binary_to_text(binary):
    binary_values = binary.split()
    text = ''.join(chr(int(bin_val, 2)) for bin_val in binary_values)
    return text

while True:
    choice = input("What do you wanna do?\n1. Turn text to binary\n2. Turn binary to text\n3. Quit\n")

    if choice == '1':
        user_text = input("Type the text you wanna convert to binary: ")
        binary_output = text_to_binary(user_text)
        print(f"Binary version: {binary_output}")
    elif choice == '2':
        user_binary = input("Type the binary you wanna convert to text: ")
        text_output = binary_to_text(user_binary)
        print(f"Text version: {text_output}")
    elif choice == '3':
        print("Alright, see ya!")
        break
    else:
        print("Didn't get that. Just type 1, 2, or 3.")



print ("Github : 0xq1")

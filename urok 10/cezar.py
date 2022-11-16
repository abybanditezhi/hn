alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False
while not should_end:
    text = input('vvedi slovo: ')
    text = list(text)
    shift = int(input('sdvig: '))

    cipher_text = ''
    for i in text:
        if i == ' ':
            cipher_text += i
        else:
            pos = alphabet.index(i)
            if pos + shift > len(alphabet):
                new_pos = pos + shift - len(alphabet)
            elif pos + shift < 0:
                new_pos = pos + shift + len(alphabet)
            else:
                new_pos = pos + shift
            cipher_text += alphabet[new_pos]

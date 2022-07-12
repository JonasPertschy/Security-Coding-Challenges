import string
import emoji


translation_forward = {}
translation_backward = {}
counter = 0
emoji_list = emoji.UNICODE_EMOJI['en'].keys()

emoji_list_true = []
for value in emoji_list:
    emoji_list_true.append(value)


for ascii_char in string.printable:
    translation_forward[ascii_char] = emoji_list_true[counter]
    translation_backward[emoji_list_true[counter]] = ascii_char
    counter += 1



def emoji_encoder(text):
    result = []
    for character in text:
        if character in translation_forward:
            result.append(translation_forward[character])
        else:
            result.append(character)
    return result

def emoji_decoder(cipher):
    result = []
    for character in cipher:
        if character in translation_backward:
            result.append(translation_backward[character])
        else:
            result.append(character)
    return ''.join(result)

encode_me = "Example Text"

encoded = emoji_encoder(encode_me)
print("Encoded:",encoded)

decoded = emoji_decoder(encoded)
print("Decoded:",decoded)
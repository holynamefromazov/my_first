text2 = input()
is_decryption = False
leng = "en"


def crypto_cesar(text, offset):

    new_text = ""
    start_up_chr = ord("A")
    end_up_chr = ord("Z")
    start_low_chr = ord("a")
    end_low_chr = ord("z")

    if leng == "ru":
        start_up_chr = ord("А")
        end_up_chr = ord("Я")
        start_low_chr = ord("а")
        end_low_chr = ord("я")
    char_range = end_up_chr - start_up_chr + 1

    for c in text:
        if c.isalpha():
            index_chr = ord(c)
            if is_decryption:
                if (start_up_chr + offset <= index_chr <= end_up_chr) or (
                    start_low_chr + offset <= index_chr <= end_low_chr
                ):
                    new_text += chr(index_chr - offset)
                else:
                    new_text += chr(index_chr - offset + char_range)
            else:
                if (start_up_chr <= index_chr <= end_up_chr - offset) or (
                    start_low_chr <= index_chr <= end_low_chr - offset
                ):
                    new_text += chr(index_chr + offset)
                else:
                    new_text += chr(index_chr + offset - char_range)
        else:
            new_text += c
    return new_text


string = ""
for c in text2:
    if c.isalpha():
        string += c
    else:
        text2 = text2.replace(string, crypto_cesar(string, len(string)), 1)
        string = ""
if string != "":
    text2 = text2.replace(string, crypto_cesar(string, len(string)), 1)
print(text2)

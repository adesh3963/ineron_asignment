
## function to replace a word

def replace_placement_word(value):
    try:
        # reading content from text
        with open("./example.txt", 'r') as file:
            content = file.read()
        if "placement" in content:
            new_text = content.replace("placement", value)
            # replacing content of text
            with open('example.txt', "w") as f:
                f.write(new_text)
        else:
            print("text contains no word as 'placement'")
    except Exception as e:
        raise e


if __name__ == "__main__":
    replace_placement_word("screening")




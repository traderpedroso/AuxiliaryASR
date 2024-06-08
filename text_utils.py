_pad = "$"
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

dicts = {}
for i in range(len((symbols))):
    dicts[symbols[i]] = i


class TextCleaner:
    def __init__(self):
        self.word_index_dictionary = dicts
        print(len(dicts))

    def __call__(self, text):
        indexes = []
        text = text.replace("(", "“")
        text = text.replace(")", "”")
        for char in text:
            try:
                indexes.append(self.word_index_dictionary[char])
            except KeyError:
                save_to_txt("ouput.txt", char)
        return indexes


def save_to_txt(file_path, content):
    try:
        # Ler o conteúdo existente do arquivo
        with open(file_path, 'r', encoding='utf-8') as file:
            existing_content = file.readlines()
        
        # Verificar se o conteúdo já está presente
        if f"{content}\n" in existing_content:
            pass
        else:
            # Adicionar o novo conteúdo ao arquivo
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(f"{content}\n")
            print(f"Conteúdo '{content}' adicionado com sucesso.")
    except FileNotFoundError:
        # Se o arquivo não existir, criar e adicionar o conteúdo
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{content}\n")
        print(f"Arquivo criado e conteúdo '{content}' adicionado com sucesso.")

def process_train_list(file_path, text_cleaner):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    second_column_texts = [line.split('|')[1].strip() for line in lines]

    for text in second_column_texts:
        text_cleaner(text)

from tkinter import W
import markovify as mk
import pandas as pd
import re
import glob


def df_for_text(data):
    text = ""
    for w in data:
        w = re.sub(r"[【】≪≫「」『』＠（）～＿・]", "", w)
        w = re.sub(r"[()\[\]@_~\"\'|]", "", w)
        w = re.sub(r"\u3000", "", w)
        w = re.sub(r" ", "", w)
        w = re.sub(r"。", "。\n", w)
        w += " "
        text += w
    return text


def markoving(text):
    current_model = ""
    with open("markolesson/model/text_model.json") as f:
        current_model = mk.NewlineText.from_json(f.read())

    text_model = mk.NewlineText(text, state_size=3)
    new_model = mk.combine([current_model, text_model])

    print(" ", "", new_model.make_short_sentence(100, tries=100))

    with open("markolesson/model/text_model.json", "w") as f:
        f.write(new_model.to_json())


while True:
    files = glob.glob("markolesson/csv/*.csv")
    for file in files:
        df = pd.read_csv(file)
        text = df_for_text(df.iloc[:, 3])
        markoving(text)
    f_name = input("続けますか?>>")
    if f_name == "end":
        break
    # df = pd.read_csv(f"markolesson/csv/{f_name}.csv")
    # text = df_for_text(df.iloc[:, 3])
    # markoving(text)

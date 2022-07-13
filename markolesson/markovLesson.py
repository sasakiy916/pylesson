import markovify

text1 = "僕 は カレー が 好き 。"
text2 = "彼 は 焼肉定食 が 食べ たい 。"
text3 = "徹夜 は 好き じゃ ない 。"

model1 = markovify.Text(text1, state_size=1)
model2 = markovify.Text(text2, state_size=1)
model3 = markovify.Text(text3, state_size=1)

models = [model1, model2, model3]

new_model = markovify.combine(models)

# print(new_model.make_sentence(tries=100))

text4 = "僕 は カレー が 好き 。\n" \
        "彼 は 焼肉定食 が 食べ たい 。\n" \
        "徹夜 は 好き じゃ ない 。"

model4 = markovify.NewlineText(text4, state_size=1)
# print(model4.make_sentence(tries=100))
for n in range(10):
    #     print(model4.make_short_sentence(10, tries=100))
    print(model4.make_sentence_with_start(beginning="徹夜"))

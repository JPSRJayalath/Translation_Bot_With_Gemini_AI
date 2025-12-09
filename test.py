from deep_translator import GoogleTranslator

text1 = GoogleTranslator(source="en", target="ja").translate("why")
text2 = GoogleTranslator(source="ja", target="en").translate("なぜ")

print(text1)
print(text2)
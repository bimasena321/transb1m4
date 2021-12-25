from googletrans import Translator, LANGUAGES

translator = Translator()
text = input("masukan text: ")
bahasa = input("terjemahkan ke bahasa: ")
hasil = trannslator.translate(text, dest = bahasa)

print("dari",LANGUAGES[hasil.src],":".text)
print("ke",LANGUAGES[hasil.dest],":",hasil.text)
print("hasil",hasil.pronuncitation)

import joblib
from veri import veri
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

cumleler = [cumle for cumle, niyet in veri]
niyetler = [niyet for cumle, niyet in veri]

model = make_pipeline(
    TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4)),
    LogisticRegression(max_iter=1000),
)
model.fit(cumleler, niyetler)

joblib.dump(model, "model.joblib")
print("Model kaydedildi:", len(cumleler), "örnekle eğitildi")

for deneme in ["merhabalar", "rezervasyonumu değiştirmek istiyorum",
               "hafta sonu açık mısınız", "eve getirir misiniz"]:
    print(deneme, "->", model.predict([deneme])[0])

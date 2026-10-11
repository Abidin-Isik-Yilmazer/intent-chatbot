from veri import veri
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

cumleler = [cumle for cumle, niyet in veri]
niyetler = [niyet for cumle, niyet in veri]

X_egitim, X_test, y_egitim, y_test = train_test_split(
    cumleler, niyetler, test_size=0.2, random_state=42, stratify=niyetler
)

model = make_pipeline(
    TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4)),
    LogisticRegression(max_iter=1000),
)
model.fit(X_egitim, y_egitim)

tahminler = model.predict(X_test)
print("Doğruluk:", accuracy_score(y_test, tahminler))

print()
print("Yanlış bilinenler:")
for cumle, gercek, tahmin in zip(X_test, y_test, tahminler):
    if gercek != tahmin:
        print(f"  '{cumle}' -> gerçek: {gercek}, model dedi ki: {tahmin}")
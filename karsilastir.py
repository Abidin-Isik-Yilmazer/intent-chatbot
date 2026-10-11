from veri import veri
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

cumleler = [cumle for cumle, niyet in veri]
niyetler = [niyet for cumle, niyet in veri]

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

kelime_modeli = make_pipeline(
    TfidfVectorizer(), LogisticRegression(max_iter=1000)
)
harf_modeli = make_pipeline(
    TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4)),
    LogisticRegression(max_iter=1000),
)

for ad, model in [("kelime modeli", kelime_modeli), ("harf parçası modeli", harf_modeli)]:
    skorlar = cross_val_score(model, cumleler, niyetler, cv=kfold)
    print(ad, "-> ortalama:", skorlar.mean().round(3), "| tek tek:", skorlar.round(2))
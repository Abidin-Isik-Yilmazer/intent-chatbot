import random
import joblib

model = joblib.load("model.joblib")

cevaplar = {
    "selamlama": [
        "Merhaba! Size nasıl yardımcı olabilirim?",
        "Selam, hoş geldiniz!",
    ],
    "menu": [
        "Menümüzde pizza, hamburger, makarna, kebap, salata ve tatlı çeşitleri var.",
    ],
    "siparis": [
        "Siparişiniz için ne istediğinizi yazar mısınız? Adresinizi de alalım.",
    ],
    "rezervasyon": [
        "Rezervasyon için kaç kişi olduğunuzu, günü ve saati yazar mısınız?",
    ],
    "calisma_saati": [
        "Her gün 11:00 ile 23:00 arası açığız.",
    ],
    "vedalasma": [
        "Rica ederim, iyi günler dileriz!",
        "Görüşmek üzere, afiyet olsun!",
    ],
}

ESIK = 0.40

print("Restoran botu hazır. Çıkmak için q yazın.")

while True:
    mesaj = input("Siz: ").strip().lower()

    if mesaj == "q":
        break
    if not mesaj:
        continue

    olasiliklar = model.predict_proba([mesaj])[0]
    guven = olasiliklar.max()
    niyet = model.classes_[olasiliklar.argmax()]

    if guven < ESIK:
        print(f"Bot: Üzgünüm, tam anlayamadım. (güven: {guven:.2f})")
        continue

    print(f"Bot: {random.choice(cevaplar[niyet])}  [{niyet}, güven: {guven:.2f}]")

    if niyet == "vedalasma":
        break
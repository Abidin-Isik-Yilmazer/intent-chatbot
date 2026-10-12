# Restoran Niyet Sınıflandırma Botu

Türkçe mesajların niyetini (selamlama, menü, sipariş, rezervasyon,
çalışma saati, vedalaşma) tahmin eden ve hazır cevaplarla yanıt veren bir sohbet botu.

## Nasıl çalışır
1. Mesaj, TF-IDF ile sayılara çevrilir (2-4 harflik parçalar, Türkçe ekleri tolere eder).
2. Logistic Regression mesajın niyetini tahmin eder.
3. Model emin değilse (güven < 0.40) bot "anlayamadım" der.
4. Tahmin edilen niyete ait hazır cevaplardan biri verilir.

## Sonuçlar
210 cümlelik elle hazırlanmış veri, 5 katlı çapraz doğrulama:

| Yöntem | Ortalama doğruluk |
|---|---|
| TF-IDF (kelime) | %84,3 |
| TF-IDF (karakter n-gram) | %88,6 |

Veri 90 cümleden 210 cümleye çıkarılınca doğruluk yaklaşık 11-12 puan arttı.

## Kurulum ve çalıştırma
```bash
pip install -r requirements.txt
python egit.py
python bot.py
```

## Dosyalar
- `veri.py`: örnek cümleler ve niyetleri
- `karsilastir.py`: yöntemleri çapraz doğrulama ile karşılaştırır
- `egit.py`: son modeli eğitir ve `model.joblib` olarak kaydeder
- `bot.py`: terminalde sohbet botu

## Sınırlılıklar
- Veri küçük ve elle yazıldı.
- Bot yalnızca 6 niyeti biliyor (örneğin fiyat ve ödeme sorularını anlayamıyor).
- Cevaplar hazır, bot yeni cümle üretmiyor.

## Geliştirme fikirleri
- "fiyat" ve "ödeme" niyetlerini eklemek
- Web arayüzü
- Cevap üretimi için bir dil modeli API'si
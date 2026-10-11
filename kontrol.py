from veri import veri
from collections import Counter

print("Toplam örnek:", len(veri))
print(Counter(niyet for _, niyet in veri))
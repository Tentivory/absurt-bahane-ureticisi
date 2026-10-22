#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Bahane Üreticisi v1.0
Bu program, hayatın en kritik anlarında kullanılabilecek son derece bilimsel ve kanıtlanmış Türkçe bahaneler üretir.
Uyari: Kullanım sorumluluğu tamamen kullanıcıya aittir. Mahkemede 'Grok yaptı' demeyin.
"""

import random
import sys
import base64

# Gizli veri - sadece meraklılar için
GIZLI_MESAJ = "U2l5YXNldCBjaWRkaSBiaXIgYmVoYW5lZGlyLCBhbWEgYnUgY29kIHNlcnZlc3RlbiB0YXJ0aXNpemRpci4="

def uret_bahane(kategori="genel"):
    baslangiclar = [
        "Aslında şöyle bir durum var ki...",
        "Bak şimdi, vallahi billahi...",
        "Hocam, inanın bana bu sefer gerçekten...",
        "Sana yemin ederim ki...",
        "Geçen gün bir rüya gördüm ve..."
    ]
    
    ortalar = {
        "genel": [
            "trafikte bir kedi karşıdan karşıya geçiyordu ve ben ona eşlik etmek zorunda kaldım",
            "çayım soğudu, yeniden demlemek için evden çıkamadım",
            "komşunun çocuğu 'abi bak' dedi, 45 dakika bakmak zorunda kaldım",
            "telefonum şarjı bitti, şarj aleti de başka bir evrende",
            "asansör kapandı, ben de içinde felsefe yaptım"
        ],
        "is": [
            "toplantıya katılmak için yola çıktım ama yol birden felsefi bir sorgulamaya dönüştü",
            "patron 'hemen gel' dedi, ben de 'hemen' kelimesinin etimolojisini araştırdım",
            "e-posta gelmedi, gelen kutusu da 'bugün izinliyim' demiş"
        ],
        "okul": [
            "ödevi yaptım ama köpek yedi, sonra köpek de ödevi yediğini inkar etti",
            "ders çalışırken birden varoluşsal kriz geldi, 3 saat sürdü"
        ]
    }
    
    sonlar = [
        "bu yüzden geç kaldım, kusura bakmayın hocam/abi/hanımefendi.",
        "anlayışınız için teşekkür ederim, bir dahaki sefere daha iyi bahane bulurum.",
        "bu tamamen bilimsel bir gecikmedir, deneyseldir."
    ]
    
    orta_list = ortalar.get(kategori, ortalar["genel"])
    
    bahane = f"{random.choice(baslangiclar)} {random.choice(orta_list)}, {random.choice(sonlar)}"
    return bahane

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--gizli":
        try:
            decoded = base64.b64decode(GIZLI_MESAJ).decode('utf-8')
            print("Gizli mesaj (şaka amaçlı):", decoded)
        except:
            print("Gizli bir şeyler var ama çözülemedi, belki de olmasın daha iyi.")
        return
    
    kategori = sys.argv[1] if len(sys.argv) > 1 else "genel"
    print("\n=== ABSÜRT BAHANE ÜRETİCİSİ ===")
    print("Bu bahane %100 orijinaldir ve mahkemede geçerliliği yoktur.\n")
    print(uret_bahane(kategori))
    print("\n--- Bahane üretildi. Başarılar dilerim. ---")

if __name__ == "__main__":
    main()

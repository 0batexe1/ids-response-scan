import requests # type: ignore
import time
import re
from colorama import Fore, Style # type: ignore

def bilgi_sizintisi_kontrolu(response_text):
    # Geliştirilmiş sızıntı patternleri
    patternler = {
        "E-posta": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "IP Adresi": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
        "Kredi Kartı": r"\b(?:\d[ -]*?){13,16}\b",
        "Telefon Numarası": r"\b(?:\+?(\d{1,3}))?[-.\s]?(\d{2,4})[-.\s]?(\d{2,4})[-.\s]?(\d{4,9})\b",
        "SSN (ABD)": r"\b\d{3}-\d{2}-\d{4}\b",
        "URL": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        "Veritabanı Hataları": r"(?i)(select .* from|insert into|sql syntax|mysql_fetch_array|Warning: mysqli_)",
        "API Anahtarı": r"\b[A-Za-z0-9._%+-]+[A-Za-z0-9.-]+/.*?\b",
        "JWT Token": r"eyJ[A-Za-z0-9_-]+",
        "Base64 Şifreleme": r"[A-Za-z0-9+/=]{20,}"
    }
    sızıntılar = []
    for bilgi, pattern in patternler.items():
        matches = list(re.finditer(pattern, response_text))
        if matches:
            sızıntılar.append((bilgi, matches))
    return sızıntılar

def format_sızıntı(matcher):
    if matcher.group():
        return matcher.group()
    return ""

def tarama_yap(dosya_adi):
    with open(dosya_adi, 'r') as file:
        urller = file.readlines()
    
    baslangic_zamani = time.time()
    
    for url in urller:
        url = url.strip()
        if url:
            protokoller = ['http://', 'https://'] if not url.startswith(('http://', 'https://')) else [url.split('://')[0] + '://']
            for protokol in protokoller:
                tam_url = protokol + url if not url.startswith(('http://', 'https://')) else url
                try:
                    response = requests.get(tam_url)
                    response_text = response.text  # response_text'i burada tanımlıyoruz
                    sızıntılar = bilgi_sizintisi_kontrolu(response_text)
                    if sızıntılar:
                        print(Fore.RED + f"[SIZINTI TESPIT EDILDI] {tam_url}")
                        for bilgi_turu, matches in sızıntılar:
                            print(Fore.YELLOW + f"Bilgi Türü: {bilgi_turu}")
                            for match in matches:
                                sızıntı_veri = format_sızıntı(match)
                                if bilgi_turu == "Telefon Numarası":
                                    # Telefon numarası için basit bir doğrulama
                                    if re.match(r"\b(?:\+?(\d{1,3}))?[-.\s]?(\d{2,4})[-.\s]?(\d{2,4})[-.\s]?(\d{4,9})\b", sızıntı_veri):
                                        print(Fore.CYAN + f"Sızan Bilgi: {sızıntı_veri}")
                                        print(Fore.CYAN + f"Bulunduğu Kısım: {response_text[max(0, match.start()-50):match.end()+50]}") # type: ignore
                                else:
                                    print(Fore.CYAN + f"Sızan Bilgi: {sızıntı_veri}")
                                    print(Fore.CYAN + f"Bulunduğu Kısım: {response_text[max(0, match.start()-50):match.end()+50]}") # type: ignore
                            print(Fore.GREEN + f"Çözüm Önerisi: Sızdırılan bilgileri maskeleyin veya kaldırın.")
                            print(Style.RESET_ALL)
                    break  # Bir protokolde başarılı olursa diğerini deneme
                except requests.RequestException as e:
                    print(Fore.RED + f"[HATA] {tam_url} adresine erişilemedi. Hata: {str(e)}")
    
    bitis_zamani = time.time()
    gecen_sure = bitis_zamani - baslangic_zamani
    print(Fore.BLUE + f"Tarama tamamlandı. Toplam süre: {gecen_sure:.2f} saniye.")
    print(Style.RESET_ALL)

if __name__ == "__main__":
    print("Hoş geldiniz! Lütfen taramak istediğiniz txt dosyasının ismini giriniz:")
    dosya_adi = input("Dosya adı: ")
    tarama_yap(dosya_adi)

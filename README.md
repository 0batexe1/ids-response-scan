Proje Hakkında

Bu Python script'i, belirtilen URL'leri tarayarak olası bilgi sızıntılarını tespit etmek amacıyla geliştirilmiştir. Web sayfalarının içeriğinde gizlenmiş e-posta adresleri, IP adresleri, kredi kartı numaraları, telefon numaraları, API anahtarları, JWT token'lar ve veritabanı hata mesajları gibi hassas verileri regex desenleri kullanarak arar. Amacı, geliştiricilerin ve güvenlik araştırmacılarının web uygulamalarındaki yanlışlıkla sızdırılan bilgileri kolayca bulmasına yardımcı olmaktır.

Amaç ve Hedef Kitle

Bu projenin temel amacı, geliştiricilerin ve güvenlik uzmanlarının web depolarındaki hassas veri sızıntılarını daha etkili bir şekilde tespit etmelerine yardımcı olmaktır. Özellikle şu kitlelere hitap eder:

    Bug Bounty Avcıları: Hedef programlarda gizli kalmış sırları bulmak için.
    Güvenlik Araştırmacıları: Açık kaynak projelerde veya dahili kod tabanlarında zafiyet avlamak için.
    DevOps ve Geliştiriciler: CI/CD süreçlerine entegre ederek kendi kod tabanlarındaki yanlışlıkla sızdırılmış sırları proaktif olarak tespit etmek için.

Özellikler

    Çok Yönlü Sızıntı Tespiti: E-posta, IP adresi, kredi kartı, telefon numarası, SSN (ABD), URL, veritabanı hataları, API anahtarları, JWT token'lar ve potansiyel Base64 şifrelemeleri dahil olmak üzere geniş bir yelpazedeki bilgi türlerini tarar.
    Renkli Çıktı: Bulguları ve hata mesajlarını terminalde kolayca ayırt etmek için renkli çıktılar kullanır.
    Esnek URL Girişi: URL'leri içeren bir .txt dosyasını girdi olarak kabul eder. URL'lerin başında http:// veya https:// olmasa bile otomatik olarak hem HTTP hem de HTTPS protokollerini dener.
    Detaylı Bulgular: Tespit edilen sızıntının türünü, sızan veriyi ve ilgili metin parçasını (bağlamı) gösterir.
    Çözüm Önerisi: Her sızıntı bulgusu için genel bir çözüm önerisi sunar.
    Tarama Süresi Bilgisi: Taramanın toplam ne kadar sürdüğünü belirtir.

Gereklilikler

Bu aracı kullanmak için sisteminizde aşağıdaki yazılımların kurulu olması gerekir:

    Python 3: Script Python 3 ile yazılmıştır.
    requests kütüphanesi: HTTP istekleri yapmak için kullanılır. pip install requests komutu ile kurulabilir.
    colorama kütüphanesi: Terminal çıktılarını renklendirmek için kullanılır. pip install colorama komutu ile kurulabilir.

Kurulum ve Kullanım

    Gerekli Kütüphaneleri Kurun:
    Script'i çalıştırmadan önce, Python ortamınızda requests ve colorama kütüphanelerinin kurulu olduğundan emin olun:
    pip install requests colorama

    Script'i İndirin:
    Bu projenin GitHub deposundan 'idsresponsescan.py' dosyasını indirin veya kopyalayın.

    URL Listesi Hazırlayın:
    Taramak istediğiniz URL'leri her satıra bir tane gelecek şekilde bir metin dosyasına kaydedin (örneğin: 'urls.txt').

Örnek urls.txt:
example.com
sub.example.com/path
https://another-site.net/page

    Script'i Çalıştırın: Terminalinizde script'in bulunduğu dizine gidin ve aşağıdaki komutu çalıştırın. Script sizden URL'lerin bulunduğu dosyanın adını isteyecektir. python idsresponsescan.py

İstendiğinde dosya adını girin:
Hoş geldiniz! Lütfen taramak istediğiniz txt dosyasının ismini giriniz:
Dosya adı: urls.txt

Bulguları Değerlendirme

Tarama tamamlandığında, terminalde tespit edilen tüm bilgi sızıntılarını renkli olarak göreceksiniz. Her bulgu için:

    [SIZINTI TESPIT EDILDI]: Sızıntının bulunduğu URL.
    Bilgi Türü: Sızan bilginin kategorisi (E-posta, IP Adresi vb.).
    Sızan Bilgi: Regex deseniyle eşleşen gerçek veri.
    Bulunduğu Kısım: Sızan bilginin geçtiği HTML/metin içeriğinin etrafındaki kısa bir bağlam.
    Çözüm Önerisi: Genel bir düzeltme önerisi.

Önemli Not: Regex desenleri her zaman %100 doğru sonuç vermeyebilir. Bazı eşleşmeler hatalı pozitif (false positive) olabilir. Tespit edilen her bulguyu manuel olarak doğrulamanız ve hassasiyetini teyit etmeniz kritik öneme sahiptir. Örneğin, bir API Anahtarı deseni, gerçek bir anahtar yerine rastgele bir diziyi de eşleştirebilir.

Katkıda Bulunma

Proje daha fazla geliştirmeye açık! Yeni regex desenleri eklemek, hata yönetimi iyileştirmeleri yapmak veya yeni özellikler önermek isterseniz, geri bildirimleriniz, hata raporlarınız ve katkılarınız her zaman açığız. Bir çekme isteği (pull request) göndermeden önce lütfen mevcut sorunları kontrol edin veya yeni bir sorun açın.

Lisans

Bu proje MIT Lisansı altında yayınlanmıştır. Daha fazla bilgi için 'LICENSE' dosyasına bakın.

İletişim

Sorularınız, önerileriniz veya işbirliği talepleriniz için bana [github.com/0batexe1] üzerinden ulaşabilirsiniz.

English Version

Web Information Leak Scanner

About The Project

This Python script is designed to scan specified URLs and detect potential information leaks. It uses regex patterns to search for sensitive data such as email addresses, IP addresses, credit card numbers, phone numbers, API keys, JWT tokens, and database error messages hidden within the content of web pages. Its purpose is to help developers and security researchers easily find inadvertently leaked information in web applications.

Purpose and Target Audience

The primary goal of this project is to help developers and security professionals more effectively identify sensitive data leaks in web repositories. It specifically targets the following audiences:

    Bug Bounty Hunters: To find hidden secrets in target programs.
    Security Researchers: To discover vulnerabilities in open-source projects or internal codebases.
    DevOps and Developers: To integrate into CI/CD pipelines for proactive detection of accidentally leaked secrets in their own codebases.

Features

    Versatile Leak Detection: Scans for a wide range of information types, including email, IP address, credit card, phone number, SSN (US), URL, database errors, API keys, JWT tokens, and potential Base64 encodings.
    Colored Output: Uses colored output in the terminal for easy distinction of findings and error messages.
    Flexible URL Input: Accepts a .txt file containing URLs as input. Automatically attempts both HTTP and HTTPS protocols even if URLs don't explicitly start with http:// or https://.
    Detailed Findings: Shows the type of leak detected, the leaked data, and a short context (surrounding text) where it was found.
    Remediation Suggestion: Provides a general remediation suggestion for each detected leak.
    Scan Duration Info: Displays the total time taken for the scan.

Requirements

To use this tool, the following software must be installed on your system:

    Python 3: The script is written in Python 3.
    requests library: Used for making HTTP requests. Can be installed with the command pip install requests.
    colorama library: Used for coloring terminal output. Can be installed with the command pip install colorama.

Installation and Usage

    Install Required Libraries:
    Before running the script, ensure that the requests and colorama libraries are installed in your Python environment:
    pip install requests colorama

    Download the Script:
    Download or copy the 'idsresponsescan.py' file from this project's GitHub repository.

    Prepare Your URL List:
    Save the URLs you want to scan in a text file, with one URL per line (e.g., 'urls.txt').

Example urls.txt:
example.com
sub.example.com/path
https://another-site.net/page

    Run the Script: Navigate to the directory where you saved the script in your terminal and run the following command. The script will prompt you for the name of the file containing your URLs. python idsresponsescan.py

Enter the file name when prompted:
Welcome! Please enter the name of the txt file you want to scan:
File name: urls.txt

Evaluating Findings

Once the scan is complete, you will see all detected information leaks highlighted in color in your terminal. For each finding:

    [LEAK DETECTED]: The URL where the leak was found.
    Information Type: The category of the leaked information (Email, IP Address, etc.).
    Leaked Information: The actual data matched by the regex pattern.
    Location: A short context from the HTML/text content surrounding the leaked information.
    Remediation Suggestion: A general recommendation for fixing the issue.

Important Note: Regex patterns may not always yield 100% accurate results. Some matches might be false positives. It is crucial to manually verify each detected finding and confirm its sensitivity. For example, an API Key pattern might match a random string instead of a genuine key.

Contributing

The project is open for further development! If you'd like to add new regex patterns, improve error handling, or suggest new features, your feedback, bug reports, and contributions are always welcome. Please check for existing issues or open a new one before submitting a pull request.

License

This project is licensed under the MIT License. See the 'LICENSE' file for more details.

Contact

For any questions, suggestions, or collaboration inquiries, feel free to reach out to me via [github.com/0batexe1].

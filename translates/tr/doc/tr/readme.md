# Kullanım Kılavuzu: NVDA için Gelişmiş Çeviri

<h2 id="İçindekiler">İçindekiler</h2>

- [1 - Giriş](#Giriş)
  - [1.1 - Gereksinimler](#Gereksinimler)
  - [1.2 - Sınırlamalar ve uyarılar](#Sınırlamalar ve uyarılar)
  - [1.3 - Yazar bilgileri](#Yazar bilgileri)
- [2 - Açıklamalar ve yapılandırma](#Açıklamalar ve yapılandırma)
  - [2.1 - Çeviri Hizmetleri](#Çeviri Hizmetleri)
    - [Google](#Google)
    - [DeepL](#DeepL)
    - [LibreTranslate](#LibreTranslate)
    - [Microsoft Translate](#Microsoft Translate)
  - [2.2 - Yapılandırma](#Yapılandırma)
    - [Eklenti Menüsü](#Eklenti Menüsü)
    - [Eklenti Kısayol Tuşları](#Eklenti Kısayol Tuşları)
- [3 - Sorun giderme](#Sorun giderme)
  - [Yaygın Sorunlar ve Çözümleri](#Yaygın Sorunlar ve Çözümleri)
  - [NVDA Günlüğüne Nasıl Bakılır?](#NVDA Günlüğüne Nasıl Bakılır?)
- [4 - Teşekkürler](#Teşekkürler)
  - [Çevirmenler](#Çevirmenler)
- [5 - Sürüm Geçmişi](#Sürüm Geçmişi)
  - [Sürüm 2024.06.06](#Sürüm 2024.06.06)
  - [Sürüm 2024.06.16](#Sürüm 2024.06.16)
  - [Sürüm 2024.06.23](#Sürüm 2024.06.23)
  - [Sürüm 2024.09.07](#Sürüm 2024.09.07)

<h2 id="Giriş">1 - Giriş</h2>

**NVDA için Gelişmiş Çeviri**, Google Çeviri, DeepL, LibreTranslate ve Microsoft Translator gibi çeşitli çevrimiçi çeviri hizmetlerini kullanarak metinleri çevirmenize olanak tanıyan bir eklentidir.  
Bu eklenti, eşzamanlı çeviri, çeviri geçmişi, seçilen öğelerin çevirisi, birden fazla dil desteği ve daha fazlası gibi gelişmiş işlevler sunar.  

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Gereksinimler">1.1 - Gereksinimler</h3>

- NVDA (NonVisual Desktop Access) 2024.1 ve sonrası.
- internet bağlantısı.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Sınırlamalar ve uyarılar">1.2 - Sınırlamalar ve uyarılar</h3>

Eklenti, eşzamanlı çeviriyi gerçekleştirmek için İnternet üzerinden ilgili hizmetlere bilgi gönderir. Çevrilen bilgilerin gizli ve hassas veriler içerebileceğini unutmamak önemlidir. Eklentinin kullanımı, gönderilen bilgilerin niteliğini değerlendirmesi gereken kullanıcının sorumluluğundadır. Eklentinin geliştiricisi, eklentinin kullandığı hizmetlere gönderilen verilerle ilgili hiçbir sorumluluk kabul etmez.  

Bir geliştirici olarak eklentinin kullanımından doğabilecek herhangi bir sorumluluğu kabul etmiyorum. Tüm sorumluluk kullanıcıya aittir.  

Ayrıca eklentinin çalışması için İnternet bağlantısı gerekir. Eklentinin yanıt hızı aşağıdakiler gibi çeşitli faktörlere bağlıdır:

- İnternet bağlantımızın kalitesi.
- Kullanılan çeviri hizmetlerinde olası gecikme (gecikme).
- Kullanıcının ağ altyapısıyla ilgili faktörler.

Kullanıcıların bu hususlara dikkat etmeleri, eklentinin beklentilerini ve güvenlik gereksinimlerini karşıladığından emin olmak için gerekli testleri yapmaları önerilir.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Yazar bilgileri">1.3 - Yazar bilgileri</h3>

**NVDA Eklentisinin Teknik Bilgileri ve Güvenlik Önlemleri**

Eklentiyi olabildiğince sağlam hale getirmek, olası hataları hesaba katmak ve bunları ele almak için çok çalıştım.  
Tüm hatalar yakalanıp NVDA günlüğüne kaydedilir; bu da sorunların izlenmesini ve hızla çözülmesini kolaylaştırır.  

**Windows Sertifikalarıyla ilgili sorunlar**

Son zamanlarda, yeni yüklenen Windows bilgisayarların sertifikalarla ilgili sorunlar yaşayabileceğini ve bunun sinir bozucu olabileceğini fark ettim.  
Bu nedenle eklentinin başlangıcında bir kontrol oluşturdum.  
Sertifikalarla ilgili bir hata tespit edilirse eklenti bunları otomatik olarak yeniden oluşturarak hem Windows'un hem de eklentinin kendisinin doğru çalışmasını sağlar.  

**Güvenlik önlemleri**

Eklenti çeşitli güvenlik önlemleri içerir:

- Güvenli ekranlarda çalışmasına izin verilmez.
- İnternet bağlantısı algılanmazsa başlamaz.

Bazen NVDA, Bilgisayarın Wi-Fi ağına bağlanmasından  daha önce başlayabilir. Bu gibi durumlarda, eklentiyi doğru şekilde kullanabilmek için bağlantı kurulduktan sonra NVDA'yı yeniden başlatmak gerekecektir.

**API Anahtar Yönetimi**

Eklenti, gerektiren hizmetler için istenen API anahtarlarını saklayan bir JSON dosyası oluşturur.  
'apis.json' adı verilen bu dosya Windows kullanıcı klasöründe bulunur.  

**Arşivlemeyle İlgili Önemli Hususlar**

Bu dosyanın hassas bilgiler içermesi nedeniyle yanlışlıkla NVDA'nın taşınabilir bir kopyasıyla veya başka durumlarda paylaşılmasını önlemek amacıyla eklenti ortamı dışında saklanmasına karar verilmiştir.  
Kullanıcı eklentiyi kullanmayı bırakmaya karar verirse bu dosyayı manuel olarak silmelidir.  

Bu önlemler, eklentinin daha iyi yönetilmesini ve güvenliğini sağlayarak kullanımını ve bakımını kolaylaştırır.  

[İçindekiler'e Dön](#İçindekiler)

<h2 id="Açıklamalar ve yapılandırma">2 - Açıklamalar ve yapılandırma</h2>

<h3 id="Çeviri Hizmetleri">2.1 - Çeviri Hizmetleri</h3>

Eklenti ilk sürümünde 7 çeviri hizmeti sunuyor:

<h4 id="Google">Google</h4>

**4 Google Hizmeti**

- **2 Web kazıma hizmeti:** Her hizmet aynı işlevi farklı bir şekilde yerine getirir ve içlerinden birinin arızalanması durumunda her zaman bir alternatifin mevcut olmasını sağlar.
- **API aracılığıyla 2 Hizmet:** Bu hizmetler de sınırsız ve ücretsizdir, ancak bunların kötüye kullanılması, IP'nin birkaç saat süreyle geçici olarak yasaklanmasıyla sonuçlanabilir, ardından hizmet yeniden kurulacaktır.
- Bu Google hizmetlerinin tümü API anahtarları gerektirmez, sınırsız ve ücretsizdir.

<h4 id="DeepL">DeepL</h4>

**2 DeepL Hizmeti**

- **Ücretsiz API:** Bu seçenek, ayda 500.000 karakter sunan DeepL sayfasından Ücretsiz API anahtarının alınmasını gerektirir.
- **API Pro:** Bu seçenek aynı zamanda DeepL web sitesinden alınan bir API anahtarını da gerektirir. Kullanımı kullanıcının DeepL hesabındaki bakiyeye ve sözleşmeli plana bağlıdır.
- DeepL API'nin kullanım koşulları [web sitesinde](https://www.deepl.com/tr/pro/change-plan#developer) yer almaktadır ve eklenti bu koşullarla sınırlıdır.

<h4 id="LibreTranslate">LibreTranslate</h4>

**1 LibreTranslate Hizmeti**

- Bu hizmet, sürekli nöral öğrenme sayesinde daima gelişmektedir. Şu anda Google kadar iyi olmasa da, mükemmel bir şekilde kullanılabilir.
- Argos Translate teknolojisine dayanmaktadır.
- Bu hizmeti kullanmak için, [NVDA.es](https://nvda.es/donaciones/) topluluğuna bağış yaparak elde edilebilecek bir API anahtarı gereklidir.
  - Bağış yaptıktan sonra, [Bu sayfada](https://nvda.es/contacto/) bulunan formu kullanarak, konuyu "API anahtarı isteği" olarak belirterek ve PayPal referansını, aktarımını vb. sağlayarak API anahtarını talep edebilirsiniz.
- Ek olarak, API anahtarını ekleyerek ve eklenti yapılandırma bölümünde hizmet Bağlantısını değiştirerek diğer LibreTranslate hizmetlerini yapılandırmak mümkündür.

<h4 id="Microsoft Translate">Microsoft Translate</h4>

**1 Microsoft Çeviri Hizmeti**

- Bu hizmetin, sürekli kullanımın birkaç dakikalığına geçici IP yasağıyla sonuçlanabileceği sınırlaması vardır.
- Bu yasak ancak çok yoğun kullanımda ve uzun metinlerin çevrilmesinde ortaya çıkar.
- Hizmet oldukça iyi çalışıyor ancak kesinti yaşamamak için sürekli kullanılmaması tavsiye ediliyor.

Bu seçenekler, kullanıcıların çeşitli çeviri hizmetleri arasında seçim yapmasına olanak tanıyarak, bireysel ihtiyaçlara ve tercihlere göre eklentinin kullanılabilirliğini ve esnekliğini sağlar.  

Eklenti güncellendikçe hizmetler eklenebilir veya kaldırılabilir. Değişiklikler güncellemeler bölümünde bildirilecektir.  

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Yapılandırma">2.2 - Yapılandırma</h3>

**Eklenti Ayarları**

Bu bölümde, API anahtarlarının nasıl ekleneceği, hizmet bağlantılarının nasıl değiştirileceği ve eklentinin kullanımını kullanıcının ihtiyaçlarına göre özelleştirmek için gerekli diğer ayarlar da dahil olmak üzere, eklentide bulunan her bir hizmetin nasıl yapılandırılacağı ayrıntılı olarak açıklanmaktadır.

<h4 id="Eklenti Menüsü">Eklenti Menüsü</h4>

NVDA > Tercihler > Gelişmiş Çeviri alt menüsünde, aşağıdakileri içeren bir menü bulunur:

- **Gelişmiş Çeviri Ayarları**  
  Bu seçeneğe tıklarsak eklenti yapılandırma penceresi açılacaktır. Bu pencerede 2 alan vardır:
  - **Genel**  
    Bu sekmede eklentinin genel seçenekleri eklenecektir. Şu anda eklenti önbelleğini etkinleştirmek veya devre dışı bırakmak için yalnızca bir onay kutusu bulunur.  
    Eklenti, her uygulama için bu çevirilerin önbelleğini kaydedebilir; bu, gelecekteki çevirilerde çevirinin daha kolay ve daha hızlı olmasını sağlayacaktır. Ayrıca artık her dil için bir önbellek oluşturuyor ve farklı diller için önbelleğe sahip birden fazla uygulama olabilir.
  - **Çeviri modülleri**  
    Bu sekmede çeviri yapmak istediğimiz hizmeti seçebiliriz. API anahtarı gerektiren hizmetlerde API anahtar yöneticisi de gösterilecektir.  
    Aynı hizmet için birden fazla API anahtarımız olabilir; Örneğin, LibreTranslate'te bağlanmak için farklı anahtarlara ve bağlantılara sahip olabiliriz. Mevcut hizmet için istediğimiz varsayılan API anahtarını ekleyebilir, düzenleyebilir, silebilir ve ayarlayabiliriz.  
    API anahtar yönetimi alanı sahip olduğumuz hizmete göre değişmektedir. Hangi API'den bahsettiğimizi hızlı bir şekilde anlamak için her API anahtarına tanımlayıcı bir ad verebiliriz. Bir hizmet için birden fazla API anahtarımız olduğunda, listede yıldız işareti olan öğe varsayılan öğe olacaktır. Bu, "Varsayılan" butonu ile değiştirilebilir ve söz konusu hizmet için tanımlanan anahtar, o anda odaklandığımız anahtar haline gelir.
    Seçtiğimiz çeviri hizmeti API anahtarı gerektirmiyorsa Anahtar yöneticisi görüntülenmez.  
    Daha sonra "Tamam" ve "İptal" düğmelerimiz var. Tüm seçeneklerin, NVDA'nın bize bildireceği kendi kısayol tuşları vardır.
- **Yardım**  
  Yardım seçeneğine tıklarsak, okumakta olduğumuz bu belge açılır.
- **İşimi beğendiysen bana bir kahve ısmarla**  
  Bu seçeneğe basarsak "Gönder" yazan bir bağlantının bulunduğu PayPal sayfası açılacaktır. Bu bağlantıya tıkladığımızda hesabımıza giriş yapıp bizi bağış sayfasına bırakmamızı isteyecektir.  
  Sadece bu eklentiyi yaparken çok fazla kahve içtiğimi söyleyeceğim.

[İçindekiler'e Dön](#İçindekiler)

<h4 id="Eklenti Kısayol Tuşları">Eklenti Kısayol Tuşları</h4>

NVDA > Tercihler > Girdi Hareketleri> Gelişmiş Çeviri dalı altında yapılandırabileceğimiz aşağıdaki seçenekler bulunur.  

Kullanıcının en iyi düzeni seçebilmesi için varsayılan tuşlar atanmamış olarak gelir. Bu hareketler aşağıdaki gibidir:

- **Eklenti ayarlarını açar**  
  Bu hareket, eklenti Ayarları penceresini hızlı bir şekilde açacaktır.
- **Çeviri önbelleğini etkinleştirir veya devre dışı bırakır**  
  Bu hareket, ayarlara girmeye gerek kalmadan önbelleği etkinleştirecek veya devre dışı bırakacaktır.
- **Çevrimiçi eşzamanlı çeviriyi etkinleştirir veya devre dışı bırakır**  
  Bu hareket çeviriyi etkinleştirir veya devre dışı bırakır. Yön tuşlarıyla hareket ettiğimizde Üzerine geldiğimiz her şey çevrilmeye başlar. Sorun yoksa çeviriyi dinleyeceğiz; Orijinal metni duyarsak NVDA günlüğüne bakıp ne olduğunu görmemiz gerekecek.
- **Çeviri modülünü değiştirir**  
  Bu hareket, mevcut tüm çeviri hizmetlerinin bulunduğu bir pencere açacaktır. Ok tuşları ile hareket edip "Enter" tuşu ile seçim yapabiliriz. Seçtiğimiz hizmet, varsayılan olarak sahip olduğumuz hizmet olacaktır.
- **Hedef dili değiştirir**  
  Bu hareket, seçtiğimiz hizmette mevcut olan hedef dillerin bulunduğu bir pencere açacaktır. Her hizmetin farklı dilleri vardır. Örneğin Rusça bir metni çeviriyorsak ve onu İngilizce olarak duymak istiyorsak, bu iletişim kutusunda İngilizce'yi seçmemiz gerekecektir. İstediğimiz dili seçmek için yön tuşlarını ve onaylamak için de "Enter" tuşunu kullanıyoruz.  
  Dil adları, NVDA'nın desteklediği dillerden elde edilmiştir. Bu nedenle, NVDA tarafından desteklenmeyen diller  listede İngilizce görülebilir. Dilin ISO kodu her dil adının yanına eklenmiştir.
- **Kaynak dili değiştirir**  
  Öncekiyle aynıdır. Ancak bu iletişim kutusu yalnızca Microsoft Translator için geçerlidir. Microsoft hizmeti, kaynak dili otomatik olarak algılayamaz. Bu nedenle onu kendimiz seçmek zorunda kalacağız.  
  Diğer hizmetler varsayılan olarak dili otomatik algıladığından, bu pencerede yer almazlar.
- **Son çevrilen metni panoya kopyalar**  
  Bu hareket, çevrilen son metni panoya kopyalayacaktır.
- **Şu anda odaklanılan uygulamanın çeviri önbelleğini siler**  
  Bu harekete bir kere basarsak bize bilgi verecektir; Hızlı bir şekilde iki kez basarsak o anda odaklanılan uygulamanın önbelleğini temizleyecek ve sonucu bildirecektir.
- **Tüm uygulamalar için önbelleğe alınmış bütün çevirileri siler**  
  Bir kez basıldığında bu hareket bize bilgi verecektir; Hızlı bir şekilde iki kez basıldığında eklenti önbelleğinin tamamı temizlenir ve ayrıca bilgi sunulur.
- **Çeviri geçmişini görüntüler**  
  Listedeki son 500 çeviriyi içeren bir pencere görüntüleyecektir. Kaynak metni ve çevrilmiş metni salt okunur kutularda arayabilir ve inceleyebiliriz. Bu iletişim kutusu tüm geçmişi aramamıza, hem kaynak metni hem de çevrilmiş metni panoya veya her ikisine birden kopyalamamıza olanak tanır.  
  Ayrıca kaynak metin ile çevrilmiş metin arasında geçiş yapmamıza ve her iki şekilde de çalışmamıza olanak tanır. Sıfırdan başlamak için tüm geçmişi silebiliriz.  
  NVDA her yeniden başlatıldığında geçmişin silindiğini fark ettim.
- **Seçilen metni çevirir**  
  Bu hareket, seçtiğimiz ve odaklandığımız metni çevirecektir. Büyük bir metinse çevirinin ilerleme yüzdesini gösteren bir iletişim kutusu açılacaktır. Söz konusu iletişim kutusu iptal edilebilir ve bu durum çeviriyi de iptal eder.  
  Çeviri tamamlandıktan sonra metin bir pencerede görüntülenecek, böylece onu inceleyebiliriz.  
  Bu seçenek Google Çeviri hizmetini kullanır. Bu hizmet, uzun metinler için en iyi sonuçları veren hizmettir. Varsayılan olarak  tanımlandığından dolayı değiştirilemez.

[İçindekiler'e Dön](#İçindekiler)

<h2 id="Sorun giderme">3 - Sorun giderme</h2>

<h3 id="Yaygın Sorunlar ve Çözümleri">Yaygın Sorunlar ve Çözümleri</h3>

**internet bağlantısı**

- İnternet bağlantınızın aktif olduğundan ve düzgün çalıştığından emin olun.
- Gerekirse yönlendiricinizi veya modeminizi yeniden başlatın.

**Sertifika Hataları**

- Sertifika hataları yaşıyorsanız sisteminizin tarih ve saatinin doğru olduğundan emin olun.
- Gerekli sertifikaların yüklendiğinden ve güncellendiğinden emin olun.

**Performans sorunları**
- Bilgisayarınızın minimum sistem gereksinimlerini karşıladığından emin olun.
- Çok fazla kaynak tüketebilecek diğer uygulamaları kapatın.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="NVDA Günlüğüne Nasıl Bakılır?">NVDA Günlüğüne Nasıl Bakılır?</h3>

1. NVDA'yı açın.
2. 'NVDA > Araçlar > Log dosyasını göster' seçeneğine gidin.
3. Log dosyasında Gelişmiş Çeviri ile ilgili hataları veya mesajları arayın.

[İçindekiler'e Dön](#İçindekiler)

<h2 id="Teşekkürler">4 - Teşekkürler</h2>

Mükemmel çalışmalarından dolayı tüm NVDA programcılarına teşekkür ederiz.  

Ayrıca, bu eklentinin prensibinin, bazı işlevlerini öğrendiğim ve kullandığım Yannick PLASSIARD'ın eklentisi (TRANSLATE) olduğunu söylemeyi unutmak istemiyorum.  

Ayrıca Alexy Sadovoy aka Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino ve diğer NVDA katılımcılarına, yöntemlerden birinin Google için elde edildiği ve Gelişmiş Çeviri'de uygulanmak üzere değiştirildiği eklenti (Anında Çeviri) için de teşekkür ederiz.  

Bu eklenti, birkaç yıllık resmi olmayan sürümlerin ve çevrimdışı çevirileri kullanma çalışmasının eseridir.  

Öğrenme, gelecekte şaşırtıcı yenilikler getireceğini bilerek bu tamamlayıcının sonucudur.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Çevirmenler">Çevirmenler</h3>

- **Portekizce:** Angelo Abrantes.
- **Türkçe:** Umut Korkmaz.
- **Rusça:** Valentin Kupriyanov.
- **İngilizce:** Samuel Proulx.
- **Ukraynaca:** Heorhii Halas y Volodymyr Pyrih.
- **Fransızca:** Rémy Ruiz.

[İçindekiler'e Dön](#İçindekiler)

<h2 id="Sürüm Geçmişi">5 - Sürüm Geçmişi</h2>

Bu bölümde, Eklentinin yeni sürümlerinin ekleneceği bir sürüm günlüğü eklenecektir.  

Kılavuz ilk sürüme dayalı olduğundan temel olarak güncellenmeyecektir.  

Yeni gelişmeler bu başlık altına eklenecektir.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Sürüm 2024.06.06">Sürüm 2024.06.06</h3>

- Eklentinin ilk sürümü.
- 7 çeviri hizmeti desteği.
- Temel eşzamanlı çeviri ve API anahtar yönetimi işlevleri.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Sürüm 2024.06.16">Sürüm 2024.06.16</h3>

- **Çevrilen metni bir iletişim kutusunda göstermek yerine, istenirse panoya kopyalama seçeneği eklendi:**
Bu işlev seçildiğinde çevrilmiş metni otomatik olarak panoya kopyalamak için bir seçenek eklendi ve ek bir iletişim kutusu görüntüleme ihtiyacı ortadan kaldırıldı.  
Bu seçenek, eklenti yapılandırma iletişim kutusunda Genel içerisine eklendi.  
Bu seçenek işaretlenirse, seçilen metni çevirdiğimizde artık bir iletişim kutusu görüntülenmez, bunun yerine doğrudan panoya kopyalanır.  
- **Panoda bulunan metni çevirin:**
Kopyalanan metinleri çevirmenin hızlı ve etkili bir yolunu sağlayarak, panoda bulunan içeriği doğrudan çevirmek artık mümkün.  
Pano boş ise veya çevrilecek bir metin yoksa bizi bilgilendirir.  
- **Sentezleyicinin son söylediğini çevirin:**
Sentezleyici tarafından söylenen son cümleyi veya metni çevirmek için yeni bir özellik eklendi, eklentinin erişilebilirliği ve kullanılabilirliği artırıldı.  
Eğer son konuşulan şey çevrilemiyorsa, bize kaynak dilde son konuşulan şeyi söyleyecektir.
- **Çevirileri Braille satırlarında görüntüleyin:**
Yeni sürüm, çevirilerin braille görüntüleme cihazlarında görüntülenmesine yönelik destek sağlayarak çevirilere erişimi kolaylaştırıyor.  
Yalnızca braille ekranı yapılandırılmış cihazlarda çalışır.  
Bu özellik test aşamasındadır.
- **Eklenti dil güncelleyici:**
Eklenti dillerini her zaman güncel tutmak, en yeni ve doğru dillerin kullanılabilirliğini sağlamak için bir güncelleyici eklendi..  
Şimdi NVDA menüsü > Tercihler > Gelişmiş Çeviri'de:  
Eklenti dillerini güncelle (Güncelleme yok) adında yeni bir seçenek bulunuyor.  
Bu öğe, güncellemeler olup olmadığını bize bildirebilir, örneğin:  
Eklenti dillerini güncelle (3 güncelleme mevcut)  
Bu seçeneği kullanırsak, yeni dillerle, güncellemelerle veya her ikisi de yoksa ikisinden biriyle ilgili bir diyalog göreceğiz.  
Dilleri, yükleyebilir veya atlayabiliriz.  
Kur'a tıklarsak diller indirilip kurulacak ve NVDA yeniden başlatılacaktır.  
Bu Menü öğesi, her 30 dakikada bir veya NVDA her başlatıldığında güncellemeleri denetler.  
Bu kontrolün veri yükü, veri sorunları olan yerler için önemsizdir, kontrol etmeniz gereken 1kb'den azdır.  
Bu güncelleyici, eklenti için dil güncellemelerini, yeni dilleri içeren yeni bir sürüm yayınlamaya gerek kalmadan, kullanıcılarla hızlı bir şekilde paylaşmayı kolaylaştıracaktır.  
Eklentinin her yeni sürümü, gelen tüm yeni ve güncellenmiş dillerle birlikte gelecektir.
- **Sürekli okuma hatası düzeltildi:**
Sürekli okuma hatalarına neden olan ve uzun süreli kullanım sırasında eklenti kararlılığını ve performansını artıran bir sorun düzeltildi.
- **Yazarın notları:**
Panoyu çevirmek, sentezleyici tarafından söylenen son sözcükleri çevirmek veya dil güncellemelerini kontrol etmek gibi tüm yeni işlevlere hareketler atanabilir.  
Herhangi bir seçeneği kullanmayacaksak, diğer eklentilerde de kullanabilmemiz için giriş hareketi eklemememizi öneririm. Bize faydalı olabilecekleri ekleyelim.  
Daha fazla eklenti eklendikçe, daha çok harekete ihtiyaç duyulacaktır ve bir yardımcı program biri için çalışmazken diğeri için çalışabilir, bu nedenle yalnızca kullanacaklarınızı atayın.

[İçindekiler'e Dön](#İçindekiler)

<h3 id="Sürüm 2024.06.23">Sürüm 2024.06.23</h3>

* Yeni DeepL Çeviri modülü eklendi (Ücretsiz)
Bu yeni modül bir API anahtarına ihtiyaç duymaz ve simültane çeviri için kullanılır.
* Hata düzeltmeleri

[İçindekiler'e Dön](#İçindekiler)


<h3 id="Sürüm 2024.09.07">Sürüm 2024.09.07</h3>

#### Çeviri Arayüzü:

**Çeviri Arayüzü**, NVDA için **Gelişmiş Çeviri** eklentisinin ana bileşenidir. Bu arayüz, kullanıcının metni farklı diller arasında verimli bir şekilde çevirmesine, orijinal ve çevrilmiş metni görüntülemesine ve çeşitli özelleştirme seçenekleri sunmasına olanak tanır.  

Bu iletişim kutusunu, Girdi hareketleri içerisinde atanacak bir kısayol tuşu ile veya Sanal menü içerisinden açabiliyoruz.  
Sanal menüye aşağıda deyinilecektir.

##### Ana özellikler:

1. **Kaynak metin girişi**: Kullanıcının çevirmek istediği metni yazmasına veya yapıştırmasına olanak tanır. 'Alt+1' tuş kombinasyonuyla hızlı bir şekilde erişilebilir.
   2. **Hedef metin (sonuç)**: Çevrilmiş metnin görüntülendiği alan. Bu alan salt okunur durumdadır ve 'Alt+2' ile odaklanılabilir.
3. **Kaynak dil seçimi**: Kaynak metnin dilini seçmenizi sağlar. Varsayılan dil, sistemin metnin dilini otomatik olarak algılamasını sağlayan "Otomatik Algıla" seçeneğidir. 'Alt+3' ile erişilir.
4. **Hedef dil seçimi**: Metni çevirmek istediğiniz dili seçmenizi sağlar. 'Alt+4' ile odaklanılabilir.
5. **Karakter Sayacı**: Kaynak metin alanındaki karakter sayısını görüntüler. Çevrilecek metin miktarını bilmek faydalıdır. 'Alt+5' ile erişilir.
6. **Eylem düğmeleri**:
   - **Çevir**: Girilen metnin çevirisini başlatır.
   - **Dinle**: Çevirinin ses dosyasını oluşturur ve dahili bir oynatıcı ile oynatılmasına imkan verir. (aşağıdaki bölüme bakın).
   - **Değiştir**: Kaynak dili hedef dille değiştirir; çeviri dillerini tersine çevirmek istiyorsanız kullanışlıdır.
   - **Temizle**: Hem kaynak hem de hedef metin alanlarını temizler.
   - **Odağa Yapıştır**: Çevrilen metni arayüzün arkasındaki etkin pencereye veya metin alanına yapıştırır. 'F3' ile de etkinleştirilebilir.
   - **Kapat**: Çeviri penceresini kapatır.

##### Klavye kısayolları:

- `Alt+1`: Kaynak metin kutusuna odaklanır.
- `Alt+2`: Hedef metin kutusuna odaklanır.
- `Alt+3`: Kaynak dili seçer.
- `Alt+4`: Hedef dili seçer.
- `Alt+5`: Karakter sayacına odaklanır.
- `F3`: Çevrilen metni etkin pencereye yapıştırır.
- `Esc`: Çeviri iletişim kutusunu kapatır.

##### Alınan hatalarda eklentinin davranışları:

- İnternet bağlantısı yoksa, sistem size bağlantı eksikliğini bildiren bir mesaj görüntüleyecektir.
- Kaynak metin kutusu boşsa kullanıcı, çeviriyi gerçekleştirmeden önce metin girmesini isteyen bir uyarı alacaktır.
- Kaynak ve hedef dillerin aynı olması durumunda metnin aynı dile çevrilmesine gerek olmadığını belirten bir uyarı görüntülenecektir.

##### Ek Özellikler:

- **Dil otomatik algılama**: Kaynak dilde "Otomatik Algıla" seçilirse eklenti, çevrilecek metnin dilini otomatik olarak tanımlamaya çalışacaktır.
- **Dil Değişimi**: Bu özellik, bir metni orijinal dile geri çevirmek istediğinizde kullanışlıdır.

#### Ses Oynatıcı:

Kullanıcı bir çeviri yaptıktan sonra **Dinle** seçeneğini kullandığında eklenti, çevrilmiş metni bir ses dosyasına dönüştürür ve dahili bir oynatıcı aracılığıyla oynatır. Bu oynatıcı, ses oynatmayı yönetmek için temel ve gelişmiş kontroller içerir.

##### Oynatıcı özellikleri:

1. **Kontrol düğmeleri**:
   - **Geri Sar(F1)**: Seçilen zamana göre oynatmayı geri sarar. Kullanıcı bu zamanı yapılandırabilir.
   - **Oynat/Duraklat (F2)**: Ses dosyasının oynatılmasını başlatır veya duraklatır.
   - **İleri Sar (F3)**: Kullanıcı tarafından ayarlanan süreye göre oynatmayı ileri sarar.
   - **Durdur (F4)**: Oynatmayı tamamen durdurur.
2. **Ses seviyesi ve hız**:
   - **Ses seviyesi (F5/F6)**: Kaydırıcıyı kullanarak oynatma ses seviyesini ayarlar.
   - **Hız (F7/F8)**: Normal hızın 0,50 katı ile 2,0 katı arasındaki seçeneklerle oynatma hızını değiştirir.
3. **İlişkili metin**: Çevrilen metni salt okunur bir kutuda görüntüleyerek kullanıcının oynatılan metni görüntülemesine imkan verir.
4. **Kaydet**: Oluşturulan ses dosyasını kullanıcının sistemine WAV formatında kaydedilmesini sağlar.
5. **Kapat**: Oynatıcıyı kapatır ve ilgili kaynakları serbest bırakır.

##### Klavye kısayolları:

- `F1`: Oynatmayı geri sarar.
- `F2`: Sesi Oynatır veya duraklatır.
- `F3`: Oynatmayı ileri sarar.
- `F4`: Oynatmayı durdurur.
- `F5/F6`: Ses seviyesini azaltır/arttırır.
- `F7/F8`: Oynatma hızını değiştirir.
- `F9`: Oynatma süre bilgisini verir.
- `Shift+F10 veya Uygulama Tuşu`: Geri ve ileri sarma süresini seçebleceğimiz bir içerik menüsü açar.

##### Ek Özellikler:

- **Kaydet**: Kullanıcılar, daha sonra kullanmak üzere ses dosyasını cihazlarına WAV formatında kaydetmeyi seçebilir.
- **Gelişmiş seçenekler menüsü**: Oynatıcı, bağlamsal menü ('Shift+F10' tuşuyla erişilir) veya uygulamalar tuşu aracılığıyla oynatmayı geri veya ileri sarmak için tam zamanı seçmenize olanak tanır.

#### Sanal menü

Eklentinin sahip olduğu tüm seçenekleri içeren sanal bir menü eklendi.

Girdi hareketlerinde atayabileceğimiz tüm seçenekleri sanal menüden kullanabiliriz, bu şekilde eklentiye daha fazla tuş atanmasına gerek kalmadan sanal menüden eklenti tamamen kullanılabilir.  

Bu kullanıcıya bağlıdır.

Sanal menüyü açmak için girdi hareketlerinde ona bir tuş atamamız gerekir.  

Sanal menüyü kullanmak basittir; bir kez açıldığında, yürütmek istediğimiz eylem için ilgili tuşa basmamız gerekir.  

Herhangi bir tuşa basıldığında, ilgili eylem çalışır ve eklenti bilgi mesajını seslendirir.  
Eğer, basılan tuş herhangi bir eylem içermiyorsa sanal menü kapanır. Escape ile de menü kapatılabilir.

##### Sanal Menü Klavye Kısayolları:

Gelişmiş Çeviri sanal menüsü, eklentinin en kullanışlı işlevlerine hızlı bir şekilde erişmenizi sağlar. Aşağıda çeşitli eylemleri gerçekleştirmek için kullanabileceğiniz kısayollar verilmiştir:

- **`P`**: **Ayarları Açar**  
  Dilleri ve çeviri hizmetlerini ayarlayabileceğimiz Gelişmiş Çeviri ayarlarını açar.

- **`U`**: **Dil güncellemelerini denetler**  
  Eklenti dilleri için güncellemeleri denetler ve varsa indirir.

- **`O`**: **Kaynak dili değiştirir**  
  Çevirmek istediğimiz metnin dilini (kaynak dil) değiştirir.

- **`D`**: **Hedef dili değiştirir**  
  Metni çevirmek istediğimiz dili (hedef dil) değiştirir.

- **`C`**: **Çeviri hizmetini değiştirir**  
  Diğerlerinin yanı sıra Google, DeepL, Microsoft gibi mevcut çeviri hizmetleri arasında geçiş yapmamıza imkan verir.

- **`A`**: **Tüm çeviri önbelleğini siler**  
  Önbelleğe alınmış tüm çevirileri temizler.

- **`X`**: **Geçerli uygulamanın çeviri önbelleğini siler**  
  Yalnızca açtığımız uygulama için önbelleğe alınmış çevirileri temizler.

- **`G`**: **Çeviri önbelleğini etkinleştir/devre dışı bırakır**  
  Çevirileri geçici olarak kaydeden önbellek özelliğini etkinleştirir veya devre dışı bırakır.

- **`L`**: **Son çeviriyi panoya kopyalar**  
  Yapılan son çeviriyi panoya kopyalar. Böylece ihtiyaç duyulan yere yapıştırılabilir.

- **`B`**: **Panodaki metni çevirir**  
  Panoda bulunan metni çevirir.

- **`V`**: **Son konuşulan metni çevirir**  
  NVDA'nın yüksek sesle okuduğu son metni çevirir.

- **`T`**: **Gerçek zamanlı çeviriyi etkinleştirir/devre dışı bırakır**  
  Metinlere göz atarken otomatik çeviriyi açar veya kapatır.

- **`S`**: **Seçili metni çevirir**  
  Seçili metni çevirir.

- **`Z`**: **Tarayıcı nesnesinden metni çevirir**  
  Tarayıcıdaki düğme veya metin kutusu gibi belirli bir nesnenin metnini çevirir.

- **`W`**: **Çeviri arayüzünü açar**  
  Çevirmek istediğimiz metni manuel olarak girebileceğimiz grafik penceresini açar.

- **`I`**: **Seçili dili algılar**  
  Seçilen metnin dilini otomatik olarak algılar.

- **`J`**: **Otomatik dil değişimini etkinleştirir/devre dışı bırakır**  
  Algılanan kaynak dilin hedef dille eşleşmesi durumunda otomatik geçişi açar veya kapatır.

- **`K`**: **Birincil ve alternatif dilleri değiştirir**  
  Çevirmen ayarlarında birincil dili alternatif dille değiştirir.

- **`H`**: **Çeviri geçmişini gösterir**  
  Gerçekleştirilen son çevirilerin bulunduğu geçmişi gösterir.

- **`F1`**: **Komutların listesini gösterir**  
  Gelişmiş Çeviri için tek tuşlu komutları listeleyen bir iletişim kutusu açar.

#### Dil algılama

Bu seçenek herhangi bir uygulamada seçmiş olduğunuz metnin dilini otomatik olarak algılamanızı sağlar. Bu özelliği kullanmak için:
1. Dilini öğrenmek istediğiniz metni seçin.
2. Dil algılamayı etkinleştirmek için girdi hareketlerinde (veya sanal menüde) yapılandırılan klavye kısayolunu kullanın.
3. Sistem seçilen metnin yazıldığı dili algılayacak ve size bilgi verecektir.
Bu özellik, bir metnin dilinden emin olmadığınız ve onu çevirmeden veya başka bir işlem yapmadan önce bilmeniz gerektiğinde kullanışlıdır.

#### NVDA Gelişmiş Çeviri'de Otomatik Dil Değişimi

  1. İlgili klavye kısayoluna basarak veya sanal menüden erişerek otomatik değiştiri etkinleştirin.
  2. Seçtiğiniz metnin hedef dille aynı dilde olması durumunda sistem, gereksiz çevirileri önlemek için hedef dili otomatik olarak alternatif dile geçirecektir.
  3. Aynı kısayolu kullanarak bu seçeneği istediğiniz zaman devre dışı bırakabilirsiniz.

##### Eklentideki Dil Ayarları

- **Genel** bölümünde **Eklenti Ayarları**'na erişerek **hedef dilleri** ve **alternatif dilleri** yapılandırabilirsiniz. Buradan otomatik değişim için kullanılacak dilleri seçebilirsiniz.

Bu özellik, kaynak dilin hedef dille aynı olduğu metinleri çevirirken karışıklığı önlemek için kullanışlıdır ve otomatik olarak yapılandırılmış bir alternatif dile geçiş yapar.

#### Eklenti İletişim Kutusu Yardımı

Eklenti iletişim kutularında bağlamsal yardımı görüntülemek için işlevsellik eklendi. 'Ctrl+H' tuş kombinasyonuna basıldığında, o anda odakta olan widget'ın işlevinin küçük bir açıklaması görüntülenecektir.

Eklentinin iletişim kutularının herhangi bir bölümünde, bir düğmenin, metin kutusunun, kaydırıcının veya başka bir kontrolün işlevi hakkında bilgiye ihtiyaç duyarsanız, 'Ctrl+H' tuşlarına basmanız yeterlidir. Bu, odaklanılan widget'ın kısa bir açıklamasını görüntüleyecek ve kullanımıyla ilgili hızlı bir kılavuz sağlayacaktır.

#### Tarayıcı nesnesinden metni çevirme:

Bu işlevsellik, tarayıcı veya NVDA'nın kullandığı herhangi bir uygulama içindeki belirli bir nesnenin metnini çevirmenize imkan verir. Sanal menü aracılığıyla veya eklentinin girdi hareketlerine atanan tuş kombinasyonu aracılığıyla etkinleştirilebilir.

1. İmleci çevirmek istediğiniz nesnenin üzerine getirin (bu bir düğme, metin kutusu vb. olabilir).
2. Atanan tuş kombinasyonuna basarak veya sanal menü aracılığıyla işlevselliği etkinleştirin.
3. Eklenti, o nesnenin içerdiği metni çevirecek ve yapılandırmaya bağlı olarak onu görüntüleyecek veya duyuracaktır.

- Bir web sayfası, uygulama veya NVDA'nın etkileşimde bulunduğu herhangi bir arayüzde seçilen nesnede bulunan herhangi bir metni çevirir.
- Menüler, düğmeler veya etiketler gibi bir sayfanın veya uygulamanın ana gövdesinin parçası olmayan küçük metin parçalarını çevirmek için kullanışlıdır.
- Nesne metin içermiyorsa veya erişilemiyorsa eklenti, çevrilecek metin olmadığını belirten bir mesaj görüntüler.
- Bu işlevselliğe hem eklentinin sanal menüsünden hem de NVDA'nın "Girdi Hareketleri"nde bir kısayol tuşu ayarlayarak erişebilirsiniz.

#### OpenAI modülü

En ucuz ve en hızlı olan chatGPT-4o-mini modeli ile OpenAI ile çeviri yapmak için yeni bir modül eklenmiştir.  

Bu modül test aşamasındadır, bazen biraz gecikme yaşanmaktadır, ancak gelecek sürümlerde gelişecektir.  

Bu modül, yapılandırma penceresinde/Çeviri modüllerinde bir API anahtarının atanmasını gerektirir.  

OpenAI ücretli olduğundan harcamalarını kontrol etmek kullanıcıya kalmıştır.  

Aşağıdaki linkte yaptığımız masrafı görebilirsiniz:  

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Microsoft modülünde iyileştirme:

Microsoft çevirmen modülü sıfırdan yazılmıştır ve hız, kararlılık ve kullanım nedeniyle bloke olana ve tekrar çeviri yapmak için birkaç dakika beklememiz gerekene kadar daha fazla çeviri süresine sahip olma yeteneği geliştirilmiştir.  

Şimdi yapılan testlerde, aynı anda birçok metni normal kullanımın ötesinde çevirdiğimde herhangi bir kısıtlamayla karşılaşmadım.  

Yani şu anda çalışıyor ve önceki modüle göre geliştirildi.

#### Diğer:

* Bazı mesajların sözlü olarak ifade edilmesiyle ilgili sorun düzeltildi.
* İnternet bağlantısını denetleme yöntemi değiştirildi.
* Hata düzeltmeleri.
* Resmi olarak Fransızca dili eklendi.

[İçindekiler'e Dön](#İçindekiler)

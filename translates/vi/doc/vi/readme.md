# Hướng dẫn sử dụng: Trình dịch nâng cao cho NVDA

<h2 id="index">Mục lục</h2>

- [1 - Giới thiệu](#introduction)
  - [1.1 - Yêu cầu](#requirements)
  - [1.2 - Hạn chế và cảnh báo](#limitations-and-warnings)
  - [1.3 - Thông tin tác giả](#author-information)
- [2 - Mô tả và cấu hình](#description-configuration)
  - [2.1 - Mô tả mô-đun](#module-description)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Translate](#microsoft-translate)
  - [2.2 - Cấu hình](#configuration)
    - [Menu Tiện ích](#addon-menu)
    - [Phím tắt Tiện ích](#addon-hotkeys)
- [3 - Khắc phục sự cố](#troubleshooting)
  - [Các vấn đề thường gặp và giải pháp](#common-problems-and-solutions)
  - [Cách tham khảo nhật ký NVDA](#how-to-consult-the-nvda-log)
- [4 - Lời cảm ơn](#acknowledgments)
  - [Người dịch](#translators)
- [5 - Nhật ký thay đổi phiên bản](#version-changelog)
  - [Phiên bản 1.0](#version-1-0)
  - [Phiên bản 2024.06.16](#version-2024-06-16)
  - [Phiên bản 2024.06.23](#version-2024-06-23)
  - [Phiên bản 2024.09.07](#version-2024-09-07)

<h2 id="introduction">1 - Giới thiệu</h2>

**Trình dịch nâng cao cho NVDA** là một tiện ích bổ sung cho phép bạn dịch văn bản bằng nhiều dịch vụ dịch thuật trực tuyến khác nhau, chẳng hạn như Google Translate, DeepL, LibreTranslate và Microsoft Translator. Tiện ích này cung cấp các tính năng nâng cao như dịch thời gian thực, lịch sử dịch, dịch văn bản đã chọn, hỗ trợ nhiều ngôn ngữ và nhiều hơn nữa.

[Quay lại mục lục](#index)

<h3 id="requirements">1.1 - Yêu cầu</h3>

- NVDA (NonVisual Desktop Access) 2024.1 hoặc cao hơn
- Kết nối Internet

[Quay lại mục lục](#index)

<h3 id="limitations-and-warnings">1.2 - Hạn chế và cảnh báo</h3>

Tiện ích gửi thông tin qua Internet đến từng dịch vụ để thực hiện dịch thời gian thực. Điều quan trọng cần lưu ý là thông tin đang được dịch có thể bao gồm dữ liệu bí mật và nhạy cảm. Việc sử dụng plugin hoàn toàn thuộc trách nhiệm của người dùng, người phải đánh giá bản chất của thông tin được gửi. Nhà phát triển plugin không chịu trách nhiệm về dữ liệu được gửi đến các dịch vụ mà plugin sử dụng.

Là một nhà phát triển, tôi từ chối mọi trách nhiệm đối với bất kỳ sự cố nào có thể phát sinh từ việc sử dụng plugin. Hoàn toàn chịu trách nhiệm thuộc về người dùng.

Ngoài ra, plugin yêu cầu kết nối Internet để hoạt động. Tốc độ phản hồi của plugin phụ thuộc vào một số yếu tố, chẳng hạn như:
- Chất lượng kết nối Internet của bạn.
- Độ trễ (lag) có thể có của các dịch vụ dịch thuật được sử dụng.
- Các yếu tố liên quan đến cơ sở hạ tầng mạng của người dùng.

Người dùng nên biết những khía cạnh này và thực hiện các bài kiểm tra cần thiết để đảm bảo rằng plugin đáp ứng mong đợi và yêu cầu bảo mật của họ.[Quay lại mục lục](#index)

<h3 id="author-information">1.3 - Thông tin tác giả</h3>

**Thông tin kỹ thuật và các biện pháp bảo mật của Tiện ích cho NVDA**

Tôi đã làm việc chăm chỉ để làm cho plugin trở nên mạnh mẽ nhất có thể, tính toán và xử lý mọi lỗi tiềm ẩn. Tất cả các lỗi đều được ghi lại và ghi vào nhật ký NVDA, giúp dễ dàng theo dõi và giải quyết nhanh chóng các vấn đề.

**Vấn đề với Chứng chỉ Windows**

Gần đây, tôi nhận thấy rằng các bản cài đặt Windows mới có thể gặp sự cố với chứng chỉ, điều này có thể gây khó chịu. Vì lý do này, tôi đã tích hợp sẵn một kiểm tra khi tiện ích khởi động. Nếu phát hiện lỗi liên quan đến các chứng chỉ, tiện ích sẽ tự động tạo lại chúng, đảm bảo hoạt động chính xác của cả Windows và chính tiện ích.

**Các biện pháp bảo mật**

Tiện ích bao gồm một số biện pháp bảo mật:
- Không được phép chạy trên màn hình an toàn.
- Nó không khởi động nếu không phát hiện thấy kết nối Internet.

Đôi khi NVDA có thể khởi động nhanh hơn kết nối mạng wi-fi. Trong trường hợp như vậy, cần khởi động lại NVDA sau khi kết nối được thiết lập để sử dụng tiện ích một cách chính xác.

**Quản lý Khóa API**

Tiện ích tạo ra một tệp JSON lưu trữ các khóa API cần thiết cho các dịch vụ yêu cầu chúng. Tệp này, được gọi là `apis.json`, nằm trong thư mục người dùng Windows.

**Cân nhắc về Tệp Khóa**

Đã quyết định lưu trữ tệp này bên ngoài thư mục tiện ích, vì nó chứa thông tin nhạy cảm. Điều này là để ngăn thông tin này vô tình được chia sẻ với một bản sao di động của NVDA hoặc trong các tình huống khác. Nếu người dùng quyết định ngừng sử dụng tiện ích, họ phải xóa thủ công tệp này.

Các biện pháp này đảm bảo quản lý và bảo mật tốt hơn cho tiện ích, tạo điều kiện thuận lợi cho việc sử dụng và bảo trì.

[Quay lại mục lục](#index)

<h2 id="description-configuration">2 - Mô tả và cấu hình</h2>

<h3 id="description-modules">2.1 - Mô tả các mô-đun</h3>

Trong phiên bản đầu tiên, plugin cung cấp 7 mô-đun dịch:

<h4 id="google">Google</h4>

**4 Mô-đun Google**

- **2 Mô-đun Web Scraping:** Mỗi mô-đun thực hiện cùng một chức năng, nhưng theo một cách khác nhau, đảm bảo rằng luôn có sẵn một giải pháp thay thế trong trường hợp một trong số chúng bị lỗi.
- **2 Mô-đun qua API:** Các mô-đun này cũng không giới hạn và miễn phí, nhưng việc lạm dụng chúng có thể dẫn đến việc cấm IP tạm thời trong vài giờ, sau đó mô-đun sẽ khả dụng trở lại.
- Tất cả các mô-đun Google này không yêu cầu khóa API và không giới hạn và miễn phí.

<h4 id="deepl">DeepL</h4>

**2 Mô-đun DeepL**

- **API Miễn phí:** Tùy chọn này yêu cầu lấy khóa API Miễn phí từ trang DeepL, cung cấp 500.000 ký tự mỗi tháng.
- **API Pro:** Tùy chọn này cũng yêu cầu khóa API lấy từ trang web DeepL. Việc sử dụng nó phụ thuộc vào số dư và gói hợp đồng của tài khoản DeepL của người dùng.
- Các điều khoản sử dụng của API DeepL được tìm thấy trên [trang web](https://www.deepl.com/en/pro/change-plan#developer) của họ, và tiện ích bị giới hạn bởi các điều khoản này.

<h4 id="libretranslate">LibreTranslate</h4>

**1 Mô-đun LibreTranslate**

- Dịch vụ này liên tục được cải thiện nhờ quá trình học tập liên tục của nơ-ron thần kinh. Mặc dù hiện tại nó không đạt chất lượng Google, nhưng nó hoàn toàn có thể sử dụng được.
- Dựa trên công nghệ Argos Translate.
- Để sử dụng mô-đun này, cần có khóa API, có thể nhận được bằng cách đóng góp cho cộng đồng [NVDA.es](https://nvda.es/donaciones/).
  - Sau khi quyên góp, bạn có thể yêu cầu khóa API bằng cách sử dụng biểu mẫu trên [trang](https://nvda.es/contacto/) sau, cho biết trong chủ đề "solicitud de clave API" và cung cấp tham chiếu PayPal, chuyển khoản, v.v.
- Ngoài ra, có thể cấu hình các dịch vụ LibreTranslate khác bằng cách thêm khóa API và sửa đổi URL dịch vụ trong phần cấu hình tiện ích.

<h4 id="microsoft-translate">Microsoft Translate</h4>

**1 Mô-đun Microsoft Translate**

- Mô-đun này có hạn chế là sử dụng liên tục có thể dẫn đến việc cấm IP tạm thời trong vài phút.
- Lệnh cấm này chỉ xảy ra khi sử dụng rất nhiều và trong các bản dịch văn bản dài.
- Dịch vụ hoạt động rất tốt, nhưng khuyên bạn không nên sử dụng liên tục để tránh gián đoạn.

Các tùy chọn này cho phép người dùng lựa chọn giữa các mô-đun dịch khác nhau, đảm bảo tính khả dụng và linh hoạt của tiện ích dựa trên nhu cầu và sở thích cá nhân.

Khi tiện ích nhận được các bản cập nhật, các dịch vụ có thể được thêm hoặc xóa. Các thay đổi sẽ được báo cáo trong phần cập nhật.

[Quay lại mục lục](#index)

<h3 id="configuration">2.2 - Cấu hình</h3>

**Cài đặt Tiện ích**

Phần này nêu chi tiết cách cấu hình từng mô-đun có sẵn trong tiện ích, bao gồm cách thêm khóa API, sửa đổi URL dịch vụ và các cài đặt khác cần thiết để tùy chỉnh việc sử dụng tiện ích theo nhu cầu của người dùng.

<h4 id="plugin-menu">Menu Tiện ích</h4>

Trong NVDA > Thiết lập > Advanced Translator có một menu chứa những điều sau:

- **Cấu hình Advanced Translator**

  Nếu bạn nhấp vào tùy chọn này, cửa sổ cấu hình tiện ích sẽ mở ra. Cửa sổ này có 2 phần:

  - **Chung**

    Trong tab này, các tùy chọn chung của tiện ích được hiển thị. Hiện tại chỉ có một hộp kiểm để bật hoặc tắt bộ nhớ cache tiện ích.

    Tiện ích có thể lưu bộ nhớ cache các bản dịch cho từng ứng dụng, điều này sẽ giúp quá trình dịch dễ dàng và nhanh hơn cho các bản dịch trong tương lai. Ngoài ra, giờ đây nó tạo bộ nhớ cache cho từng ngôn ngữ và có thể có nhiều hơn một ứng dụng có bộ nhớ cache cho các ngôn ngữ khác nhau.

  - **Các mô-đun dịch**

    Trong tab này, bạn có thể chọn dịch vụ bạn muốn sử dụng để dịch. Đối với các dịch vụ yêu cầu khóa API, trình quản lý khóa API cũng sẽ được hiển thị.

    Bạn có thể có nhiều hơn một khóa API cho cùng một dịch vụ; Ví dụ: trong LibreTranslate, bạn có thể có các khóa và URL khác nhau để kết nối. Bạn có thể thêm, sửa, xóa và đặt khóa API mặc định mà bạn muốn cho dịch vụ hiện tại.

    Phần quản lý khóa API thay đổi tùy thuộc vào dịch vụ bạn đã chọn. Bạn có thể đặt tên định danh cho mỗi khóa API để biết nhanh bạn đang đề cập đến API nào. Khi bạn có nhiều hơn một khóa API cho một dịch vụ, mục có dấu hoa thị trong danh sách sẽ là mục mặc định. Điều này có thể được thay đổi bằng nút "Mặc định", biến khóa được xác định cho dịch vụ thành khóa bạn đang tập trung vào thời điểm đó.

    Nếu dịch vụ dịch thuật bạn chọn không yêu cầu khóa API, trình quản lý API sẽ không được hiển thị.

    Sau đó, bạn có các nút "Chấp nhận" và "Hủy". Tất cả các tùy chọn đều có phím tắt mà NVDA sẽ thông báo cho bạn.

- **Tài liệu Tiện ích**

  Nếu bạn nhấp vào "Tài liệu Tiện ích", tài liệu này sẽ mở ra.

- **Tặng một tách cà phê nếu bạn thích công việc của tôi**

  Nếu bạn nhấn tùy chọn này, trang PayPal sẽ mở ra nơi có liên kết ghi "Gửi". Nếu bạn nhấp vào liên kết này, nó sẽ yêu cầu bạn đăng nhập vào tài khoản của mình và để bạn ở trang quyên góp.

  Tôi chỉ nói rằng tôi đã uống rất nhiều cà phê trong khi làm tiện ích này.

[Quay lại mục lục](#index)

<h4 id="addon-hotkeys">Phím tắt Tiện ích</h4>

Trong NVDA > Thiết lập > Cử chỉ đầu vào... > Advanced Translator có các phím sau mà bạn có thể cấu hình.

Các phím mặc định chưa được gán để người dùng có thể chọn bố cục tốt nhất cho họ. Chúng bao gồm:

- **Mở cấu hình tiện ích**

  Thao tác này sẽ mở nhanh cấu hình plugin.

- **Bật hoặc tắt bộ nhớ cache dịch**

  Thao tác này sẽ kích hoạt hoặc hủy kích hoạt bộ nhớ cache mà không cần phải vào cấu hình.

- **Kích hoạt hoặc hủy kích hoạt dịch thời gian thực trực tuyến**

  Điều này kích hoạt hoặc hủy kích hoạt dịch thời gian thực. Đây là chức năng chính sẽ bắt đầu dịch khi bạn di chuyển bằng các mũi tên con trỏ. Nếu mọi thứ đều chính xác, bạn sẽ nghe thấy bản dịch; Nếu bạn nghe thấy văn bản gốc, bạn sẽ phải xem nhật ký NVDA và xem điều gì đã xảy ra.

- **Thay đổi mô-đun dịch**

  Thao tác này sẽ mở một cửa sổ với tất cả các mô-đun dịch có sẵn. Bạn có thể di chuyển bằng các mũi tên và chọn bằng "Enter". Mô-đun bạn chọn sẽ là mô-đun bạn có theo mặc định.

- **Thay đổi ngôn ngữ đích**

  Thao tác này sẽ mở một cửa sổ với các ngôn ngữ đích có sẵn trong mô-đun mà chúng ta đã chọn. Mỗi dịch vụ có các ngôn ngữ khác nhau và ví dụ, nếu bạn đang dịch một văn bản bằng tiếng Nga và bạn muốn nghe nó bằng tiếng Anh, trong hộp thoại này bạn sẽ phải chọn tiếng Anh. Bạn di chuyển qua hộp thoại bằng các mũi tên con trỏ và "Enter" để chọn ngôn ngữ bạn muốn.

- **Thay đổi ngôn ngữ nguồn**

  Tương tự như chức năng trước, nhưng hộp thoại này chỉ khả dụng cho trình dịch Microsoft. Dịch vụ Microsoft không cho phép bạn đặt ngôn ngữ nguồn là tự động để nó phát hiện ngôn ngữ nào được gửi đến bạn, vì vậy bạn sẽ phải tự chọn.

  Các dịch vụ còn lại sẽ không thể sử dụng hộp thoại này vì tùy chọn mặc định của chúng là phát hiện ngôn ngữ đang được gửi.

- **Sao chép văn bản đã dịch cuối cùng vào khay nhớ tạm**

  Thao tác này sẽ sao chép văn bản cuối cùng đã được dịch vào khay nhớ tạm.

- **Xóa bộ nhớ cache dịch cho ứng dụng hiện đang được tiêu điểm**

  Nếu chúng ta nhấn nút này một lần, nó sẽ cung cấp thông tin cho chúng ta; Nếu chúng ta nhấn nút này hai lần nhanh chóng, nó sẽ xóa bộ nhớ cache cho ứng dụng hiện đang có tiêu điểm và sẽ thông báo cho chúng ta kết quả.

- **Xóa tất cả các bản dịch đã lưu trong bộ nhớ cache cho tất cả các ứng dụng**

  Nếu nhấn nút này một lần, nó sẽ cung cấp thông tin cho chúng ta; Nhấn hai lần nhanh chóng, nó sẽ xóa toàn bộ bộ nhớ cache của plugin, cũng cung cấp thông tin.

- **Hiển thị lịch sử dịch**

  Nó sẽ hiển thị một hộp thoại với 500 bản dịch gần đây nhất trong một danh sách. Bạn có thể tìm kiếm và xem lại văn bản nguồn và văn bản đã dịch trong các hộp chỉ đọc. Hộp thoại này sẽ cho phép bạn tìm kiếm toàn bộ lịch sử, sao chép cả văn bản nguồn và văn bản đã dịch vào khay nhớ tạm, hoặc cả hai.

  Nó cũng cho phép bạn chuyển đổi giữa văn bản nguồn và văn bản đã dịch và làm việc theo cả hai cách. Ngoài ra, bạn có thể xóa tất cả lịch sử để bắt đầu lại từ đầu.

  Lưu ý rằng lịch sử bị xóa mỗi khi NVDA khởi động lại.

- **Dịch văn bản đã chọn**

  Hành động này sẽ dịch văn bản mà bạn đã chọn và tập trung. Nếu đó là một văn bản lớn, một hộp thoại sẽ mở ra với phần trăm dịch. Hộp thoại này có thể bị hủy, điều này cũng sẽ hủy bỏ quá trình dịch.

  Sau khi quá trình dịch hoàn tất, văn bản sẽ được hiển thị trong một hộp thoại để bạn có thể khám phá.

  Tùy chọn này sử dụng dịch vụ Google Translate và dịch vụ này không thể thay đổi, được chọn nội bộ vì nó là dịch vụ mang lại kết quả tốt nhất cho các văn bản dài.

[Quay lại mục lục](#index)

<h2 id="troubleshooting">3 - Khắc phục sự cố</h2>

<h3 id="common-problems-and-solutions">Các vấn đề thường gặp và giải pháp</h3>

**Kết nối Internet**
- Kiểm tra xem kết nối Internet của bạn có đang hoạt động và hoạt động bình thường không.
- Khởi động lại bộ định tuyến hoặc modem nếu cần.

**Lỗi Chứng chỉ**
- Nếu bạn gặp lỗi chứng chỉ, hãy đảm bảo ngày và giờ hệ thống của bạn là chính xác.
- Xác minh rằng các chứng chỉ cần thiết đã được cài đặt và cập nhật.

**Vấn đề Hiệu suất**
- Đảm bảo máy tính của bạn đáp ứng các yêu cầu hệ thống tối thiểu.
- Đóng các ứng dụng khác có thể đang tiêu tốn nhiều tài nguyên.

[Quay lại mục lục](#index)

<h3 id="how-to-consult-the-nvda-log">Cách tham khảo nhật ký NVDA</h3>

1. Mở NVDA.
2. Đi tới `NVDA > Công cụ > Xem nhật ký`.
3. Trong cửa sổ nhật ký, hãy tìm bất kỳ lỗi hoặc thông báo nào liên quan đến Advanced Translator.

[Quay lại mục lục](#index)

<h2 id="acknowledgments">4 - Lời cảm ơn</h2>

Cảm ơn tất cả các lập trình viên NVDA vì công việc tuyệt vời của họ.

Và tôi không muốn quên nói rằng sự khởi đầu của plugin này đến từ plugin của Yannick PLASSIARD (TRANSLATE), từ đó tôi đã học và sử dụng một số chức năng.

Cũng cảm ơn Alexy Sadovoy aka Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino và những người đóng góp NVDA khác cho plugin Instant Translate mà từ đó một trong các phương pháp cho Google đã được lấy và sửa đổi để triển khai trong Advanced Translator.

Plugin này là công trình của vài năm phát hành các phiên bản không chính thức và nghiên cứu sử dụng các bản dịch ngoại tuyến.

Tiện ích này là kết quả của quá trình học tập này, hãy ghi nhớ rằng trong tương lai nó sẽ mang đến những tính năng mới đáng ngạc nhiên.

[Quay lại mục lục](#index)
<h3 id="translators">Người dịch</h3>

- **Tiếng Bồ Đào Nha:** Ângelo Abrantes.
- **Tiếng Thổ Nhĩ Kỳ:** Umut Korkmaz.
- **Tiếng Nga:** Valentin Kupriyanov.
- **Tiếng Anh:** Samuel Proulx.
- **Tiếng Ukraina:** Heorhii Halas và Volodymyr Pyrih.
- **Tiếng Việt:** Đào Đức Trung.

[Quay lại mục lục](#index)

<h2 id="version-changelog">5 - Nhật ký thay đổi</h2>

Trong phần này, nhật ký thay đổi sẽ được thêm vào, nơi các tính năng mới của mỗi phiên bản sẽ được đăng.

Hướng dẫn dựa trên phiên bản đầu tiên nên nó sẽ không được cập nhật đóng vai trò làm cơ sở.

Tin tức sẽ được thêm vào trong phần này.

[Quay lại mục lục](#index)

<h3 id="version-1-0">Phiên bản 2024.06.06</h3>

- Phát hành ban đầu của plugin.
- Hỗ trợ 7 dịch vụ dịch thuật.
- Các chức năng cơ bản của dịch thời gian thực và quản lý khóa API.

<h3 id="version-2024-06-16">Phiên bản 2024.06.16</h3>

- **Thêm khả năng sao chép bản dịch của văn bản đã chọn vào khay nhớ tạm thay vì hiển thị trong hộp thoại:**

Một tùy chọn đã được thêm vào để tự động sao chép văn bản đã dịch vào khay nhớ tạm khi chức năng này được chọn, tránh cần phải hiển thị thêm một hộp thoại.

Tùy chọn này đã được thêm vào trong hộp thoại cấu hình plugin ở phần Chung.

Nếu tùy chọn này được chọn, nó sẽ không còn hiển thị hộp thoại khi bạn dịch một văn bản đã chọn, thay vào đó nó sẽ trực tiếp sao chép vào khay nhớ tạm.

- **Dịch bất cứ thứ gì có trên khay nhớ tạm:**

Giờ đây, có thể dịch trực tiếp nội dung nằm trên khay nhớ tạm, cung cấp một cách nhanh chóng và hiệu quả để dịch các văn bản đã sao chép.

Nếu không có gì được dịch, nó sẽ cho bạn biết những gì có trên khay nhớ tạm hoặc nếu không có gì trên khay nhớ tạm, nó sẽ thông báo cho bạn bằng một tin nhắn.

- **Dịch nội dung cuối cùng được nói bởi trình tổng hợp giọng nói:**

Một chức năng đã được thêm vào cho phép bạn dịch cụm từ hoặc văn bản cuối cùng được nói bởi trình tổng hợp giọng nói, cải thiện khả năng truy cập và khả năng sử dụng của tiện ích.

Nếu nội dung cuối cùng được nói không thể dịch được, nó sẽ cho bạn biết nội dung cuối cùng được nói bằng ngôn ngữ gốc.

- **Hiển thị bản dịch bằng chữ nổi:**

Phiên bản mới bao gồm hỗ trợ hiển thị bản dịch trên các thiết bị hiển thị chữ nổi, giúp các bản dịch dễ tiếp cận hơn.

Nó sẽ chỉ hoạt động trên các thiết bị có cấu hình hiển thị chữ nổi.

Chức năng này đang trong giai đoạn thử nghiệm.

- **Trình cập nhật ngôn ngữ plugin:**

Một trình cập nhật đã được triển khai để giữ cho ngôn ngữ plugin luôn cập nhật, đảm bảo tính khả dụng của các ngôn ngữ mới nhất và chính xác nhất.

Bây giờ trong menu NVDA > Thiết lập > Advanced Translator

Bạn sẽ có một mục mới gọi là Cập nhật ngôn ngữ plugin (Không có cập nhật).

Mục này sẽ thông báo cho bạn nếu có bản cập nhật, ví dụ:

Cập nhật ngôn ngữ plugin (3 bản cập nhật có sẵn)

Nếu bạn nhấn nó, một hộp thoại sẽ xuất hiện với các ngôn ngữ mới, với các bản cập nhật của các ngôn ngữ hiện có hoặc cả hai.

Bạn có thể cài đặt hoặc bỏ qua.

Nếu bạn nhấp vào cài đặt, các ngôn ngữ sẽ được tải xuống và cài đặt và NVDA sẽ khởi động lại.

Mục menu được cập nhật mỗi 30 phút kiểm tra các bản cập nhật hoặc mỗi khi khởi động lại.

Chi phí dữ liệu của việc kiểm tra này là nhỏ vì đối với những nơi có vấn đề về dữ liệu, nó ít hơn 1kb mà bạn phải kiểm tra.

Trình cập nhật này sẽ giúp chia sẻ các bản cập nhật ngôn ngữ cho tiện ích với người dùng nhanh chóng khi chúng đến và không cần phải phát hành phiên bản mới với các ngôn ngữ mới.

Mỗi phiên bản mới của tiện ích sẽ đi kèm với tất cả các ngôn ngữ mới và cập nhật đã đến.

- **Sửa lỗi đọc liên tục:**

Đã khắc phục sự cố gây ra lỗi đọc liên tục, cải thiện độ ổn định và hiệu suất của tiện ích trong thời gian sử dụng kéo dài.

- **Ghi chú của tác giả:**

Tất cả các chức năng mới như dịch khay nhớ tạm, dịch các từ cuối cùng được nói bởi trình tổng hợp hoặc kiểm tra cập nhật ngôn ngữ, đều có thể được gán cử chỉ.

Tôi khuyên rằng nếu bạn không sử dụng bất kỳ tùy chọn nào, bạn không nên thêm cử chỉ đầu vào để bạn có thể rảnh tay cho các tiện ích khác. Chỉ thêm những cái sẽ hữu ích cho bạn.

Khi các tính năng được thêm vào, sẽ cần nhiều cử chỉ hơn và một tính năng có thể không hoạt động với một người và có thể hoạt động tốt với người khác, vì vậy chỉ gán những cái bạn sẽ sử dụng.

[Quay lại mục lục](#index)

<h3 id="version-2024-06-23">Phiên bản 2024.06.23</h3>

* Thêm mô-đun Dịch giả DeepL mới (Miễn phí)

Mô-đun mới này không cần khóa API và được sử dụng để dịch thời gian thực

* Sửa lỗi

[Quay lại mục lục](#index)

<h3 id="version-2024-09-07">Phiên bản 2024.09.07</h3>

#### Giao diện dịch

**Giao diện dịch** là thành phần chính của tiện ích **Advanced Translator** cho NVDA. Giao diện này cho phép người dùng dịch văn bản giữa các ngôn ngữ khác nhau một cách hiệu quả, hiển thị văn bản gốc và bản dịch, và cung cấp nhiều tùy chọn tùy chỉnh khác nhau.

Để gọi nó, bạn sẽ phải gán một tổ hợp phím trong cử chỉ đầu vào hoặc từ menu ảo (được giải thích bên dưới).

##### Các tính năng chính:

1. **Nhập văn bản nguồn**: Cho phép người dùng viết hoặc dán văn bản họ muốn dịch. Có thể truy cập nhanh bằng tổ hợp phím `Alt+1`.
   
2. **Văn bản đích (kết quả)**: Khu vực hiển thị văn bản đã dịch. Trường này là chỉ đọc và có thể được tập trung với `Alt+2`.

3. **Chọn ngôn ngữ nguồn**: Cho phép bạn chọn ngôn ngữ của văn bản nguồn. Ngôn ngữ mặc định là tùy chọn "Tự động phát hiện", cho phép hệ thống tự động phát hiện ngôn ngữ của văn bản. Truy cập nó bằng `Alt+3`.

4. **Chọn ngôn ngữ đích**: Cho phép bạn chọn ngôn ngữ mà bạn muốn dịch văn bản sang. Có thể tập trung với `Alt+4`.

5. **Bộ đếm ký tự**: Hiển thị số lượng ký tự trong trường văn bản nguồn. Hữu ích để biết lượng văn bản sẽ được dịch. Truy cập nó bằng `Alt+5`.

6. **Các nút hành động**:
   - **Dịch**: Bắt đầu dịch văn bản đã nhập.
   - **Nghe**: Lấy âm thanh của bản dịch và cho phép phát qua trình phát tích hợp (xem phần bên dưới).
   - **Hoán đổi**: Hoán đổi ngôn ngữ nguồn với ngôn ngữ đích, hữu ích nếu bạn muốn đảo ngược ngôn ngữ dịch.
   - **Xóa**: Xóa cả trường văn bản nguồn và đích.
   - **Dán vào tiêu điểm**: Dán văn bản đã dịch vào cửa sổ hoạt động hoặc trường văn bản phía sau giao diện. Cũng có thể được kích hoạt bằng `F3`.
   - **Đóng**: Đóng cửa sổ dịch.

##### Phím tắt bàn phím:

- `Alt+1`: Tập trung vào hộp văn bản nguồn.
- `Alt+2`: Tập trung vào hộp văn bản đích.
- `Alt+3`: Chọn ngôn ngữ nguồn.
- `Alt+4`: Chọn ngôn ngữ đích.
- `Alt+5`: Tập trung vào bộ đếm ký tự.
- `F3`: Dán văn bản đã dịch vào cửa sổ hoạt động.
- `Esc`: Đóng hộp thoại dịch.

##### Hành vi trong trường hợp có lỗi:

- Nếu không có kết nối Internet, hệ thống sẽ hiển thị thông báo thông báo về việc thiếu kết nối.
- Nếu hộp văn bản nguồn trống, người dùng sẽ nhận được cảnh báo yêu cầu nhập văn bản trước khi thực hiện dịch.
- Nếu ngôn ngữ nguồn và đích giống nhau, một cảnh báo sẽ được hiển thị cho biết rằng văn bản không cần phải được dịch sang cùng một ngôn ngữ.

##### Các tính năng bổ sung:

- **Tự động phát hiện ngôn ngữ**: Nếu "Tự động phát hiện" được chọn trong ngôn ngữ nguồn, Plugin sẽ cố gắng tự động xác định ngôn ngữ của văn bản cần dịch.
- **Trao đổi ngôn ngữ**: Chức năng này hữu ích khi bạn muốn dịch một văn bản trở lại ngôn ngữ gốc.

#### Trình phát âm thanh

Khi người dùng sử dụng tùy chọn **Nghe** sau khi thực hiện dịch, plugin chuyển đổi văn bản đã dịch thành tệp âm thanh và phát qua trình phát tích hợp. Trình phát này bao gồm các điều khiển cơ bản và nâng cao để quản lý phát lại âm thanh.

##### Các tính năng của trình phát:

1. **Các nút điều khiển**:
   - **Lùi lại (F1)**: Tua lại phát lại theo thời gian đã chọn. Người dùng có thể cấu hình thời gian này.
   - **Phát/Tạm dừng (F2)**: Bắt đầu hoặc tạm dừng phát tệp âm thanh.
   - **Tua tới (F3)**: Tua nhanh phát lại theo thời gian do người dùng thiết lập.
   - **Dừng (F4)**: Dừng phát lại hoàn toàn.

2. **Âm lượng và tốc độ**:
   - **Âm lượng (F5/F6)**: Điều chỉnh âm lượng phát lại bằng thanh trượt.
   - **Tốc độ (F7/F8)**: Thay đổi tốc độ phát lại, với các tùy chọn từ 0.50x đến 2.0x tốc độ bình thường.

3. **Văn bản liên kết**: Hiển thị văn bản đã dịch trong một hộp chỉ đọc, cho phép người dùng xem những gì đang được phát.

4. **Lưu**: Cho phép bạn lưu tệp âm thanh đã tạo ở định dạng WAV trên hệ thống của bạn.

5. **Đóng**: Đóng trình phát và giải phóng các tài nguyên liên quan.

##### Phím tắt bàn phím:

- `F1`: Tua lại phát lại.
- `F2`: Phát hoặc tạm dừng âm thanh.
- `F3`: Tua nhanh phát lại.
- `F4`: Dừng phát lại.
- `F5/F6`: Điều chỉnh âm lượng.
- `F7/F8`: Thay đổi tốc độ phát lại.
- `F9`: Thông tin thời gian phát lại.
- `Shift+F10/Ứng dụng`: sẽ hiển thị menu ngữ cảnh để chọn khoảng thời gian của các nút tua lại và tua tới.

##### Các tính năng bổ sung:

- **Lưu âm thanh**: Người dùng có thể chọn lưu tệp âm thanh vào thiết bị của họ ở định dạng WAV để sử dụng sau.
- **Menu tùy chọn nâng cao**: Trình phát cho phép bạn chọn thời gian chính xác để tua lại hoặc tiến phát lại thông qua menu ngữ cảnh (truy cập bằng phím `Shift+F10`) hoặc phím ứng dụng.

#### Menu ảo

Một menu ảo đã được thêm vào chứa tất cả các tùy chọn của tiện ích.

Bạn có thể gọi tất cả các tùy chọn từ menu ảo mà bạn có thể gán trong cử chỉ đầu vào. Bằng cách này, tất cả các tính năng của tiện ích có thể được sử dụng mà không cần phải có thêm phím nào được gán cho tiện ích.

Điều này tùy thuộc vào người dùng.

Để gọi menu ảo, bạn sẽ phải gán một phím cho nó trong cử chỉ đầu vào.

Sử dụng menu ảo rất đơn giản, sau khi gọi, bạn sẽ phải nhấn phím tương ứng cho hành động bạn muốn thực hiện. Sau khi nhấn, hành động sẽ được thực hiện và bạn sẽ luôn được thông báo về những gì đã được thực hiện. Nếu bạn nhấn một phím không được gán, menu ảo sẽ đóng và bạn cũng có thể đóng nó bằng escape.

##### Phím tắt Bàn phím Menu Ảo

Menu ảo Advanced Translator cho phép bạn truy cập nhanh các chức năng hữu ích nhất của plugin. Dưới đây là các phím tắt mà bạn có thể sử dụng để thực hiện các hành động khác nhau:

- **`P`**: **Mở cấu hình**  
  Mở cài đặt Advanced Translator nơi bạn có thể điều chỉnh ngôn ngữ và dịch vụ dịch thuật.

- **`U`**: **Kiểm tra cập nhật ngôn ngữ**  
  Kiểm tra và tải xuống các bản cập nhật có sẵn cho ngôn ngữ plugin.

- **`O`**: **Thay đổi ngôn ngữ nguồn**  
  Thay đổi ngôn ngữ của văn bản bạn muốn dịch (ngôn ngữ nguồn).

- **`D`**: **Thay đổi ngôn ngữ đích**  
  Thay đổi ngôn ngữ bạn muốn dịch văn bản sang (ngôn ngữ đích).

- **`C`**: **Thay đổi dịch vụ dịch thuật**  
  Cho phép bạn chuyển đổi giữa các dịch vụ dịch thuật có sẵn, chẳng hạn như Google, DeepL, Microsoft, cùng những người khác.

- **`A`**: **Xóa tất cả bộ nhớ cache dịch**  
  Xóa tất cả các bản dịch đã lưu trong bộ nhớ cache.

- **`X`**: **Xóa bộ nhớ cache dịch của ứng dụng hiện tại**  
  Xóa các bản dịch đã lưu trong bộ nhớ cache chỉ cho ứng dụng bạn đang mở.

- **`G`**: **Bật/Tắt bộ nhớ cache dịch**  
  Bật hoặc tắt tính năng bộ nhớ cache lưu tạm thời các bản dịch.

- **`L`**: **Sao chép bản dịch cuối cùng vào khay nhớ tạm**  
  Sao chép bản dịch cuối cùng được thực hiện vào khay nhớ tạm để bạn có thể dán nó ở bất cứ đâu bạn cần.

- **`B`**: **Dịch văn bản khay nhớ tạm**  
  Dịch nội dung hiện tại của khay nhớ tạm.

- **`V`**: **Dịch văn bản được nói cuối cùng**  
  Dịch văn bản cuối cùng mà NVDA đọc to.

- **`T`**: **Bật/Tắt dịch thời gian thực**  
  Bật hoặc tắt dịch tự động trong khi duyệt văn bản.

- **`S`**: **Dịch văn bản đã chọn**  
  Dịch văn bản bạn đã chọn trong ứng dụng.

- **`Z`**: **Dịch văn bản từ đối tượng trình duyệt**  
  Dịch văn bản của một đối tượng cụ thể trong trình duyệt, chẳng hạn như nút hoặc hộp văn bản.

- **`W`**: **Mở giao diện dịch**  
  Mở cửa sổ đồ họa nơi bạn có thể nhập thủ công văn bản bạn muốn dịch.

- **`I`**: **Phát hiện ngôn ngữ đã chọn**  
  Tự động phát hiện ngôn ngữ của văn bản đã chọn.

- **`J`**: **Bật/Tắt trao đổi ngôn ngữ tự động**  
  Bật hoặc tắt chuyển đổi tự động nếu ngôn ngữ nguồn được phát hiện khớp với ngôn ngữ đích.

- **`K`**: **Hoán đổi ngôn ngữ chính và thay thế**  
  Hoán đổi ngôn ngữ chính với ngôn ngữ thay thế trong cài đặt trình dịch.

- **`H`**: **Hiển thị lịch sử dịch**  
  Hiển thị lịch sử các bản dịch gần đây đã thực hiện.

- **`F1`**:**Hiển thị danh sách lệnh**  
  Hiển thị hộp thoại liệt kê các lệnh đơn phím cho Advanced Translator.

#### Phát hiện ngôn ngữ

Tùy chọn này cho phép bạn tự động phát hiện ngôn ngữ của văn bản bạn đã chọn trong bất kỳ ứng dụng nào. Để sử dụng tính năng này:
1. Chọn văn bản mà bạn muốn biết ngôn ngữ.
2. Sử dụng phím tắt bàn phím được cấu hình trong cử chỉ đầu vào (hoặc menu ảo) để kích hoạt phát hiện ngôn ngữ.
3. Hệ thống sẽ phát hiện và thông báo cho bạn ngôn ngữ mà văn bản đã chọn được viết.
Tính năng này hữu ích khi bạn không chắc chắn về ngôn ngữ của một văn bản và cần biết nó trước khi dịch nó hoặc thực hiện bất kỳ hành động nào khác.

#### Trao đổi ngôn ngữ tự động trong NVDA Advanced Translator

  1. Kích hoạt trao đổi tự động bằng cách nhấn phím tắt bàn phím tương ứng hoặc truy cập nó từ menu ảo.
  2. Nếu văn bản bạn chọn cùng ngôn ngữ với ngôn ngữ đích, hệ thống sẽ tự động chuyển ngôn ngữ đích sang ngôn ngữ thay thế để tránh các bản dịch không cần thiết.
  3. Bạn có thể tắt tùy chọn này bất cứ lúc nào bằng cách sử dụng cùng một phím tắt.

##### Cài đặt ngôn ngữ trong Tiện ích

- Bạn có thể cấu hình **ngôn ngữ đích** và **ngôn ngữ thay thế** bằng cách truy cập **Cấu hình Tiện ích** trong phần **Chung**. Từ đó bạn có thể chọn các ngôn ngữ sẽ được sử dụng cho trao đổi tự động.

Chức năng này hữu ích để tránh nhầm lẫn khi dịch các văn bản trong đó ngôn ngữ nguồn giống với ngôn ngữ đích, tự động chuyển sang ngôn ngữ thay thế đã được cấu hình.

#### Trợ giúp trong Hộp thoại Tiện ích

Đã thêm chức năng hiển thị trợ giúp theo ngữ cảnh trong các hộp thoại tiện ích. Nhấn tổ hợp phím `Ctrl+H` sẽ hiển thị một mô tả nhỏ về chức năng của widget hiện đang được tập trung.

Ở bất cứ đâu trong các hộp thoại tiện ích, nếu bạn cần thông tin về chức năng của một nút, hộp văn bản, thanh trượt hoặc điều khiển khác, bạn chỉ cần nhấn `Ctrl+H`. Điều này sẽ hiển thị một mô tả ngắn gọn về widget được tập trung, cung cấp hướng dẫn nhanh về việc sử dụng nó.

#### Dịch văn bản từ đối tượng trình duyệt

Chức năng này cho phép bạn dịch văn bản của một đối tượng cụ thể trong trình duyệt hoặc bất kỳ ứng dụng nào khác mà NVDA đang sử dụng. Nó có thể được kích hoạt thông qua menu ảo hoặc thông qua tổ hợp phím được gán trong cử chỉ đầu vào của tiện ích.

1. Đặt con trỏ lên đối tượng bạn muốn dịch (có thể là một nút, hộp văn bản, v.v.).
2. Kích hoạt chức năng bằng cách nhấn tổ hợp phím được gán hoặc thông qua menu ảo.
3. Tiện ích sẽ dịch văn bản chứa trong đối tượng đó và hiển thị hoặc nói nó, tùy thuộc vào cấu hình.

- Dịch bất kỳ văn bản nào chứa trong đối tượng đã chọn trong trang web, ứng dụng hoặc bất kỳ giao diện nào khác nơi NVDA tương tác.
- Hữu ích để dịch các đoạn văn bản nhỏ không phải là một phần của nội dung chính của trang hoặc ứng dụng, chẳng hạn như menu, nút hoặc nhãn.
- Nếu đối tượng không chứa văn bản hoặc không thể truy cập, plugin sẽ hiển thị thông báo cho biết không có văn bản nào để dịch.

- Bạn có thể truy cập chức năng này cả từ menu ảo của tiện ích và bằng cách thiết lập phím nóng trong "Cử chỉ đầu vào" của NVDA.

#### Mô-đun OpenAI

Một mô-đun mới đã được thêm vào để dịch với OpenAI với mô hình chatGPT-4º-mini, là mô hình rẻ nhất và nhanh nhất.

Mô-đun này đang trong quá trình thử nghiệm, đôi khi gặp một chút độ trễ, nhưng nó sẽ cải thiện trong các phiên bản tương lai.

Mô-đun này yêu cầu khóa API được gán trong cấu hình / các mô-đun.

OpenAI được trả tiền vì vậy việc kiểm tra chi tiêu của họ là tùy thuộc vào người dùng.

Trong liên kết sau, bạn có thể xem chi phí bạn đã sử dụng:

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Cải tiến trong mô-đun Microsoft

Mô-đun trình dịch Microsoft đã được viết lại từ đầu để cải thiện tốc độ, độ ổn định và cho phép thời gian dịch nhiều hơn cho đến khi họ chặn bạn do sử dụng và bạn phải đợi vài phút để dịch lại.

Bây giờ trong các bài kiểm tra của tôi được thực hiện bằng cách dịch đồng thời rất nhiều văn bản, thậm chí nhiều hơn mức sử dụng bình thường, tôi đã không chịu bất kỳ hạn chế nào.

Vì vậy, hiện tại nó hoạt động và đã được cải thiện so với mô-đun trước đó.

#### Khác

* Đã sửa lỗi với việc nói một số tin nhắn.
* Đã thay đổi cách kiểm tra xem có internet hay không.
* Sửa lỗi
* Chính thức thêm tiếng Pháp.

[Quay lại mục lục](#index)


# Руководство пользователя: TranslateAdvanced (Продвинутый переводчик для NVDA)

<h2 id="#index">Оглавление</h2>

- [1 - Введение](#introduction)
- [1.1 - Требования](#requirements)
- [1.2 - Ограничения и предупреждения](#limitations-and-warnings)
- [1.3 - Информация об авторе](#author-information)
- [2 - Описание и конфигурация](#description-configuration)
- [2.1 - Описание сервисов](#description-services)
 - [Google](#google)
 - [DeepL](#deepl)
 - [LibreTranslate](#libretranslate)
 - [Microsoft Translate](#microsoft-translate)
- [2.2 - Конфигурация](#configuration)
 - [Добавочное меню](#add-in-menu)
 - [Горячие клавиши](#add-in-key-quick-keys)
- [3 - Устранение неполадок](#trouble-shooting)
- [Общие проблемы и решения](#common-problems-and-solutions)
- [Как обращаться к журналу NVDA](#how-to-consult-the-nvda-log)
- [4 - Благодарности](#acknowledgements)
- [Переводчики](#translators)
- [5 - Журнал версий](#version-log)
- [Версия 1.0](#version-1-0)

<h2 id=«introduction»>1 - Введение</h2>

**TranslateAdvanced** - это дополнение, которое позволяет переводить тексты с помощью различных онлайн-сервисов перевода, таких как Google Translate, DeepL, LibreTranslate и Microsoft Translator. Дополнение предлагает расширенные возможности, такие как одновременный перевод, история переводов, перевод выделенного текста, поддержка нескольких языков и многое другое.

[Вернуться к оглавлению](#index)

<h3 id=«требования»>1.1 - Требования</h3>

- NVDA (Невизуальный доступ к рабочему столу) 2024.1 или новее
- Интернет-соединение

[Вернуться к оглавлению](#index)

<h3 id=«ограничения и предупреждения»>1.2 - Ограничения и предупреждения</h3>

Дополнение отправляет информацию в Интернет каждому соответствующему сервису для выполнения синхронного перевода. Важно отметить, что переводимая информация может содержать конфиденциальные и чувствительные данные. Ответственность за использование дополнения несет исключительно пользователь, который должен оценивать характер отправляемой информации. Разработчик дополнения не несет никакой ответственности за данные, отправляемые сервисам, используемым дополнением.

Как разработчик, я снимаю с себя всю ответственность за любые события, которые могут возникнуть в результате использования дополнения. Вся ответственность лежит на пользователе.

Кроме того, для работы дополнения необходимо подключение к Интернету. Скорость отклика дополнения зависит от нескольких факторов, таких как:
- Качество нашего интернет-соединения.
- Возможная задержка (лаг) используемых служб перевода.
- Факторы, связанные с сетевой инфраструктурой пользователя.

Пользователям рекомендуется ознакомиться с этими аспектами и провести необходимые тесты, чтобы убедиться, что дополнение соответствует их ожиданиям и требованиям безопасности.

[Вернуться к оглавлению](#index)

<h3 id=«author-information»>1.3 - Информация об авторе</h3>.

**Техническая информация и меры безопасности дополнения NVDA**.

Я приложил все усилия, чтобы сделать дополнение как можно более надежным, предусмотреть и устранить все возможные ошибки. Все ошибки фиксируются и записываются в журнал NVDA, что позволяет легко отслеживать и быстро устранять проблемы.

**Проблемы с сертификатами Windows

Недавно я заметил, что на недавно установленных компьютерах с Windows могут возникать проблемы с сертификатами, что может быть неприятно. По этой причине я включил проверку при запуске дополнения. Если обнаружен сбой, связанный с сертификатами, дополнение автоматически регенерирует сертификаты, обеспечивая нормальную работу как Windows, так и самого дополнения.

**Меры безопасности

Дополнение включает в себя несколько мер безопасности:
- Оно запрещено для запуска на защищенных экранах.
- Оно не запускается, если не обнаружено подключение к Интернету.

Иногда NVDA может запускаться быстрее, чем Wi-Fi соединение. В таких случаях NVDA необходимо перезапустить после установления соединения, чтобы использовать дополнение должным образом.

Управление ключами **API

Дополнение генерирует JSON-файл, в котором хранятся API-ключи, необходимые для тех сервисов, которые их требуют. Этот файл, называемый `apis.json`, размещается в папке пользователя Windows.

**Файл ключей

Было решено хранить этот файл вне среды дополнения, чтобы избежать того, что, поскольку он содержит конфиденциальную информацию, он может быть случайно передан портативной копии NVDA или в других ситуациях. Если пользователь решит прекратить использование дополнения, этот файл должен быть удален вручную.

Эти меры обеспечивают более эффективное управление и безопасность дополнения, упрощая его использование и обслуживание.

[Вернуться к оглавлению](#index)

<h2 id=«description-configuration»>2 - Описание и конфигурация</h2>.

<h3 id=«description-services»>2.1 - Описание услуг</h3>.

В первой версии дополнение предлагает 7 сервисов перевода:

<h4 id=«google»>Google</h4>

**4 сервиса Google

- **2 сервиса веб-скреппинга:** Каждый сервис выполняет одну и ту же функцию, но по-разному, что гарантирует наличие альтернативы в случае отказа одного из них.
- **2 сервиса через API:** Эти сервисы также неограниченны и бесплатны, но злоупотребление ими может привести к временному запрету IP-адреса на несколько часов, после чего сервис будет восстановлен.
- Все эти сервисы Google не требуют ключей API и являются неограниченными и бесплатными.

<h4 id=«deepl»>DeepL</h4>

**2 сервиса с сайта DeepL**

- **API Free:** Этот вариант требует получения ключа API Free на сайте DeepL, который предлагает 500 000 символов в месяц.
- API Pro:** Для этой опции также требуется ключ API, полученный на сайте DeepL. Его использование зависит от баланса и тарифного плана, заключенного на аккаунте пользователя DeepL.
- Условия использования API DeepL можно найти на его [сайте](https://www.deepl.com/es/pro/change-plan#developer), и данное дополнение ограничено этими условиями.

<h4 id=«libretranslate»>LibreTranslate</h4>

**1 Сервис LibreTranslate

- Этот сервис постоянно совершенствуется благодаря непрерывному нейронному обучению. Хотя в настоящее время он не дотягивает до качества Google, его вполне можно использовать.
- Основан на технологии Argos Translate.
- Для использования этого сервиса требуется API-ключ, который можно получить, пожертвовав на сообщество [NVDA.es] (https://nvda.es/donaciones/).
- После пожертвования ключ API можно запросить через форму на следующей [странице](https://nvda.es/contacto/), указав в теме письма «Запрос ключа API» и предоставив ссылку на PayPal, банковский перевод и т. д.
- Также можно настроить другие сервисы LibreTranslate, добавив API-ключ и изменив URL-адрес сервиса в разделе конфигурации дополнения.

<h4 id=«microsoft-translate»>Microsoft Translate</h4>

**1 Служба Microsoft Translate

- Эта служба имеет ограничение, согласно которому ее дальнейшее использование может привести к временному запрету IP-адреса на несколько минут.
- Такой запрет происходит только при очень интенсивном использовании и переводе длинных текстов.
- Служба работает очень хорошо, но рекомендуется не использовать ее постоянно, чтобы избежать перебоев.

Эти опции позволяют пользователям выбирать между несколькими сервисами перевода, обеспечивая доступность и гибкость дополнения в соответствии с индивидуальными потребностями и предпочтениями.

По мере обновления дополнения сервисы могут быть добавлены или удалены. Об изменениях будет сообщаться в разделе обновлений.

[Вернуться к оглавлению](#index)

<h3 id=«configuration»>2.2 - Конфигурация</h3>.

**Конфигурация дополнения

В этом разделе подробно описано, как настроить каждый из сервисов, доступных в дополнении, включая добавление API-ключей, изменение URL-адресов сервисов и другие настройки, необходимые для адаптации использования дополнения к потребностям пользователя.

<h4 id=«add-on-menu»>Меню дополнения</h4>

В NVDA > Параметры > Продвинутый переводчик есть меню, содержащее следующее:

- **Настройки Продвинутого переводчика**.

  При нажатии на эту опцию откроется окно настроек дополнения. В этом окне есть 2 области:

- **Общие**.

    В этой вкладке будут добавлены те опции, которые носят общий характер для дополнения. В настоящее время здесь есть только флажок для включения или отключения кэша дополнения.

    Дополнение может кэшировать переводы для каждого приложения, что облегчит и ускорит перевод в будущем. Кроме того, теперь оно создает кэш для каждого языка, так что несколько приложений могут иметь кэш для разных языков.

- Модули перевода

    На этой вкладке мы можем выбрать сервис, который мы хотим использовать для перевода. Для тех сервисов, которые требуют API-ключ, также будет показан менеджер API-ключей.

    У нас может быть несколько API-ключей для одного и того же сервиса; например, в LibreTranslate у нас могут быть разные ключи и URL-адреса для подключения. Вы можете добавлять, редактировать, удалять и использовать по умолчанию нужный вам API-ключ для текущего сервиса.

    Область управления ключами API меняется в зависимости от используемого сервиса. Мы можем присвоить идентификационное имя каждому ключу API, чтобы быстро понять, к какому API мы обращаемся. Если у нас есть несколько API-ключей для сервиса, элемент со звездочкой в списке будет использоваться по умолчанию. Это можно изменить, нажав на кнопку «По умолчанию», и в этот момент в фокусе будет ключ, определенный для данного сервиса.

    Если выбранный нами сервис перевода не требует ключа API, менеджер не будет отображаться.

    Далее имеются кнопки «ОК» и «Отмена». Все опции имеют свою клавишу быстрого доступа, которую нам сообщит NVDA.

- Документация дополнения

  Если мы нажмем на «Документация по дополнению», откроется эта документация.

- Пригласите меня на чашечку кофе, если вам нравится моя работа**.

  Если мы нажмем на эту опцию, откроется страница PayPal, где есть ссылка «Отправить». Если мы нажмем на эту ссылку, нас попросят войти в наш аккаунт и переведут на страницу пожертвований.

  Скажу лишь, что я выпил много кофе, создавая это дополнение.

[Вернуться к оглавлению](#index)

<h4 id=«add-on-fast-keys»>Дополнительные горячие клавиши</h4>.

В NVDA > Параметры > Жесты ввода... > Продвинутый переводчик у нас есть следующие клавиши, которые мы можем настроить.

Клавиши по умолчанию не назначены, чтобы пользователь мог выбрать оптимальное расположение. К ним относятся:

- **Открыть настройки дополнения**.

  Этот доступ быстро откроет настройки дополнения.

- Включить или выключить кэш переводов**.

  Этот доступ позволяет включать или выключать кэш без необходимости заходить в настройки.

- Включение или выключение синхронного перевода онлайн**.

  Этот доступ включает или выключает перевод. Это основной доступ, который начнет переводить, когда мы будем двигаться с помощью клавиш со стрелками. Если все правильно, мы услышим перевод; если же мы услышим оригинальный текст, нам придется заглянуть в журнал NVDA и посмотреть, что произошло.

- Изменить модуль перевода

  Этот доступ откроет окно со всеми доступными службами перевода. Мы сможем перемещаться с помощью стрелок и выбирать с помощью «Enter». Выбранная нами служба будет той, которая установлена по умолчанию.

- Изменить язык перевода

  Этот пункт открывает окно с языками перевода, доступными в выбранном сервисе. В каждом сервисе есть разные языки, и, например, если мы переводим текст на русский, а хотим услышать его на английском, в этом диалоге нужно выбрать английский. Перемещаемся по диалогу с помощью курсорных стрелок и «Enter», чтобы выбрать нужный язык.

  Названия языков получены на нашем языке от NVDA и поддерживают те языки, которые поддерживает NVDA. По этой причине список может содержать названия языков на английском языке, так как NVDA их не переводит. Рядом с названием каждого языка указан его ISO-код.

- Изменить исходный язык

  То же самое, что и выше, но этот диалог действителен только для переводчика Microsoft. Служба Microsoft не позволяет установить язык источника как автоматический, чтобы определить, какой язык отправляется в нее, поэтому нам придется выбрать его самостоятельно.

  Остальные службы не смогут использовать этот диалог, так как по умолчанию они определяют, какой язык отправляется.

- **Копировать последний переведенный текст в буфер обмена**.

  Этот доступ скопирует последний переведенный текст в буфер обмена.

- Удалить кэш перевода для текущего сфокусированного приложения**.

  Если мы нажмем на этот доступ один раз, он выдаст нам информацию; если мы быстро нажмем на него два раза, он очистит кэш для приложения, находящегося в фокусе, и сообщит нам о результате.

- **Удалить все кэшированные переводы для всех приложений**.

  При однократном нажатии эта кнопка предоставит информацию; при двукратном быстром нажатии она очистит весь кэш дополнения и также предоставит информацию.

- Показать историю переводов**.

  Отобразится диалог со списком последних 500 переводов. Мы сможем искать и просматривать в окнах «только для чтения» исходный и переведенный текст. Этот диалог позволяет искать по всей истории, копировать в буфер обмена либо исходный, либо переведенный текст, либо оба.

  Он также позволяет переключаться между исходным и переведенным текстом и работать с любым из них. Кроме того, мы можем удалить всю историю, чтобы начать работу с нуля.

  Обратите внимание, что история очищается при каждом перезапуске NVDA.

- Перевести выделенный текст

  Это действие переведет текст, который мы выделили и на котором сфокусировались. Если это большой текст, откроется диалог с процентом перевода. Этот диалог можно отменить, что также приведет к отмене перевода.

  После завершения перевода текст будет отображен в диалоговом окне, чтобы мы могли его изучить.

  Эта опция использует сервис Google Translate и не может быть изменена, так как она выбрана внутренне, поскольку дает наилучшие результаты для длинных текстов.

[Вернуться к оглавлению](#index)

<h2 id=«устранение неполадок»>3 - Устранение неполадок</h2>

<h3 id=«problem-common-problems-and-solutions»>Общие проблемы и решения</h3>

**Подключение к Интернету
- Убедитесь, что подключение к Интернету активно и работает должным образом.
- При необходимости перезапустите маршрутизатор или модем.

**Ошибки сертификата
- Если возникают ошибки сертификатов, убедитесь, что дата и время в системе верны.
- Убедитесь, что необходимые сертификаты установлены и обновлены.

**Проблемы с производительностью**.
- Убедитесь, что ваш компьютер соответствует минимальным системным требованиям.
- Закройте другие приложения, которые могут потреблять много ресурсов.

[Вернуться к оглавлению](#index)

<h3 id=«how-to-query-nvda-log»>Как запрашивать журнал NVDA</h3> 1.

1. Откройте NVDA.
2. Перейдите в меню `NVDA > Сервис > Просмотр журнала`.
3. В окне журнала найдите все ошибки и сообщения, связанные с Advanced Translator.

[Вернуться к оглавлению](#index)

<h2 id=«благодарности»>4 - Благодарности</h2>

Спасибо всем программистам NVDA за их отличную работу.

Не хочу забыть сказать, что начало этому дополнению положило дополнение Yannick PLASSIARD (TRANSLATE), из которого я почерпнул и использовал некоторые функции.

Также Alexy Sadovoy aka Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino и другие участники NVDA за дополнение (Instant Translate), из которого был взят один из методов для Google и модифицирован для внедрения его в Advanced Translator.

Это дополнение - результат нескольких лет неофициальных релизов и изучения использования автономных переводов.

Мы учимся на этом дополнении, зная, что в будущем оно принесет новые удивительные возможности.

[Вернуться к оглавлению](#index)

<h3 id=«переводчики»>Переводчики</h3>

- Валентин Куприянов:** Перевод на русский.

[Вернуться к оглавлению](#index)

<h2 id=«version-log»>5 - Журнал версий</h2>

В этом разделе мы добавим журнал версий, в котором будем публиковать новые релизы каждой версии.

Руководство основано на первой версии, поэтому оно не будет обновляться и будет служить базой.

Новые версии будут добавляться в этот раздел.

[Вернуться к оглавлению](#index)

<h3 id=«version-1-0»>Версия 2024.06.06</h3>

- Начальный релиз дополнения.
- Поддержка 7 сервисов перевода.
- Базовый синхронный перевод и функциональность управления ключами API.

[Вернуться к оглавлению](#index)
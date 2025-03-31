# Benutzerhandbuch: Erweiterter Übersetzer für NVDA

<h2 id="Inhaltsverzeichnis">Inhaltsverzeichnis</h2>

- [1 - Einleitung](#introduction)
  - [1.1 - Anforderungen](#requirements)
  - [1.2 - Einschränkungen und Warnungen](#limitations-und-Warnungen)
  - [1.3 - Informationen zum Autor](#author-Informationen)
- [2 - Beschreibung und Konfiguration](#description-Konfiguration)
  - [2.1 - Modulbeschreibung](#module-Beschreibung)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Übersetzer](#microsoft-Übersetzer)
  - [2.2 - Konfiguration](#configuration)
    - [Addon-Menü](#addon-Menü)
    - [Addon Hotkeys](#addon-Hotkeys)
- [3 - Fehlerbehebung](#troubleshooting)
  - [Häufige Probleme und Lösungen](#common-Probleme-und-Lösungen)
  - [Wie man das NVDA-Protokoll konsultiert](#how-to-consult-the-nvda-log)
- [4 - Danksagung](#acknowledgments)
  - [Übersetzer](#translators)
- [5 - Versionsänderungsprotokoll](#version-Änderungsprotokoll)
  - [Version 1.0](#version-1-0)
  - [Fassung 2024.06.16](#version-2024-06-16)
  - [Fassung 2024.06.23](#version-2024-06-23)
  - [Fassung 2024.09.07](#version-2024-09-07)

<h2 id="Einführung">1 - Einführung</h2>

**Erweiterter Übersetzer für NVDA** ist ein Addon, mit dem Sie Texte mit verschiedenen Online-Übersetzungsdiensten wie Google Translate, DeepL, LibreTranslate und Microsoft Translator übersetzen können. Dieses Addon bietet erweiterte Funktionen wie Echtzeitübersetzung, Übersetzungsverlauf, Übersetzung des ausgewählten Textes, Unterstützung für mehrere Sprachen und mehr.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Anforderungen">1.1 - Anforderungen</h3>

- NVDA (NonVisual Desktop Access) 2024.1 oder höher
- Internetverbindung

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Einschränkungen-und-Warnungen">1.2 - Einschränkungen und Warnungen</h3>

Das Addon sendet Informationen über das Internet an jeden Dienst, um eine Echtzeitübersetzung durchzuführen. Es ist wichtig zu beachten, dass die zu übersetzenden Informationen vertrauliche und sensible Daten enthalten können. Die Nutzung des Plugins liegt in der alleinigen Verantwortung des Nutzers, der die Art der gesendeten Informationen bewerten muss. Der Entwickler des Plugins übernimmt keine Verantwortung für die Daten, die an die Dienste gesendet werden, die das Plugin verwendet.

Als Entwickler lehne ich jede Verantwortung für Eventualitäten ab, die sich aus der Nutzung des Plugins ergeben können. Die volle Verantwortung liegt beim Nutzer.

Darüber hinaus benötigt das Plugin eine Internetverbindung, um zu funktionieren. Die Reaktionsgeschwindigkeit des Plugins hängt von mehreren Faktoren ab, wie zum Beispiel:
- Die Qualität Ihrer Internetverbindung.
- Die mögliche Verzögerung (Verzögerung) der in Anspruch genommenen Übersetzungsdienste.
- Faktoren, die sich auf die Netzwerkinfrastruktur des Benutzers beziehen.

Es wird empfohlen, dass sich die Benutzer dieser Aspekte bewusst sind und die notwendigen Tests durchführen, um sicherzustellen, dass das Plugin ihren Erwartungen und Sicherheitsanforderungen entspricht. 
[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Autoreninformationen">1.3 - Informationen zum Autor</h3>

**Technische Informationen und Sicherheitsmaßnahmen des Addons für NVDA**

Ich habe hart daran gearbeitet, das Plugin so robust wie möglich zu machen und mögliche Fehler zu berücksichtigen und zu behandeln. Alle Fehler werden erfasst und im NVDA-Protokoll aufgezeichnet, was die Nachverfolgung und schnelle Behebung von Problemen erleichtert.

**Probleme mit Windows-Zertifikaten**

In letzter Zeit ist mir aufgefallen, dass neue Installationen von Windows Probleme mit Zertifikaten haben können, was frustrierend sein kann. Aus diesem Grund habe ich einen Check eingebaut, wenn das Addon startet. Wenn ein Fehler im Zusammenhang mit den Zertifikaten erkannt wird, generiert das Addon diese automatisch neu, um den korrekten Betrieb von Windows und dem Addon selbst sicherzustellen.

**Sicherheitsmaßnahmen**

Das Addon beinhaltet mehrere Sicherheitsmaßnahmen:
- Es ist nicht erlaubt, auf sicheren Bildschirmen zu laufen.
- Es wird nicht gestartet, wenn keine Internetverbindung erkannt wird.

Manchmal kann NVDA schneller gestartet werden, als das Wi-Fi-Netzwerk eine Verbindung herstellt. In solchen Fällen ist es notwendig, NVDA nach dem Verbindungsaufbau neu zu starten, um das Addon korrekt zu verwenden.

**API-Schlüsselverwaltung**

Das Addon generiert eine JSON-Datei, in der die notwendigen API-Schlüssel für die Dienste gespeichert sind, die sie benötigen. Diese Datei mit dem Namen "apis.json" befindet sich im Windows-Benutzerordner.

**Überlegungen zu wichtigen Dateien**

Es wurde beschlossen, diese Datei außerhalb des Addon-Ordners zu speichern, da sie vertrauliche Informationen enthält.  Dies soll verhindern, dass diese Informationen versehentlich mit einer portablen Kopie von NVDA oder in anderen Situationen geteilt werden. Wenn der Benutzer beschließt, das Addon nicht mehr zu verwenden, muss er diese Datei manuell löschen.

Diese Maßnahmen sorgen für eine bessere Verwaltung und Sicherheit des Addons und erleichtern seine Nutzung und Wartung.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h2 id="description-configuration">2 - Beschreibung und Konfiguration</h2>

<h3 id="Beschreibung-Module">2.1 - Beschreibung der Module</h3>

In seiner ersten Version bietet das Plugin 7 Übersetzungsmodule:

<h4 id="google">Google</h4>

**4 Google-Module**

- **2 Web Scraping Module:** Jedes Modul führt die gleiche Funktion aus, jedoch auf eine andere Weise, um sicherzustellen, dass immer eine Alternative verfügbar ist, falls eines von ihnen ausfällt.
- **2 Module über API:** Diese Module sind ebenfalls unbegrenzt und kostenlos, aber ein Missbrauch kann zu einer vorübergehenden IP-Sperre für einige Stunden führen, danach ist das Modul wieder verfügbar.
- Alle diese Google-Module benötigen keine API-Schlüssel und sind unbegrenzt und kostenlos.

<h4 id="deepl">DeepL</h4>

**2 DeepL-Module**

- **Kostenlose API:** Für diese Option muss ein kostenloser API-Schlüssel von der DeepL-Seite bezogen werden, die 500.000 Zeichen pro Monat bietet.
- **Pro API:** Auch für diese Option ist ein API-Schlüssel erforderlich, den Sie von der DeepL-Website bezogen haben. Die Nutzung ist abhängig vom Guthaben und dem vertraglich vereinbarten Plan des DeepL-Kontos des Nutzers.
- Die Nutzungsbedingungen der DeepL-API sind auf ihrer [Website](https://www.deepl.com/en/pro/change-plan#developer) zu finden, und das Addon ist durch diese Bedingungen eingeschränkt.

<h4 id="libretranslate">LibreTranslate</h4>

**1 LibreTranslate-Modul**

- Dieser Dienst wird dank seines kontinuierlichen neuronalen Lernens ständig verbessert. Obwohl es derzeit nicht die Qualität von Google erreicht, ist es perfekt nutzbar.
- Basierend auf der Argos Translate-Technologie.
- Um dieses Modul nutzen zu können, ist ein API-Key erforderlich, den Sie durch eine Spende an die [NVDA.es](https://nvda.es/donaciones/)-Community erhalten können.
  - Nach der Spende können Sie den API-Schlüssel über das Formular auf der folgenden [Seite](https://nvda.es/contacto/) anfordern, indem Sie im Betreff "solicitud de clave API" angeben und die PayPal Referenz, Überweisung usw. angeben.
- Darüber hinaus ist es möglich, andere LibreTranslate-Dienste zu konfigurieren, indem Sie den API-Schlüssel hinzufügen und die Dienst-URL im Addon-Konfigurationsbereich ändern.

<h4 id="microsoft-translate">Microsoft Translate</h4>

**1 Microsoft Übersetzer-Modul**

- Dieses Modul hat die Einschränkung, dass die Dauernutzung zu einer vorübergehenden IP-Sperre für einige Minuten führen kann.
- Dieses Verbot tritt nur bei sehr intensiver Nutzung und bei Übersetzungen langer Texte auf.
- Der Dienst funktioniert sehr gut, aber es wird empfohlen, ihn nicht ständig zu nutzen, um Unterbrechungen zu vermeiden.

Diese Optionen ermöglichen es den Nutzern, zwischen verschiedenen Übersetzungsmodulen zu wählen, um die Verfügbarkeit und Flexibilität des Addons basierend auf individuellen Bedürfnissen und Vorlieben zu gewährleisten.

Wenn das Addon Updates erhält, können Dienste hinzugefügt oder entfernt werden. Änderungen werden im Abschnitt "Updates" gemeldet.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Konfiguration">2.2 - Konfiguration</h3>

**Addon-Einstellungen**

In diesem Abschnitt wird beschrieben, wie Sie jedes der im Addon verfügbaren Module konfigurieren, einschließlich des Hinzufügens von API-Schlüsseln, des Änderns von Dienst-URLs und anderer Einstellungen, die erforderlich sind, um die Verwendung des Addons an die Bedürfnisse des Benutzers anzupassen.

<h4 id="plugin-menu">Addon menu</h4>

In NVDA > Optionen  > Erweiterter Übersetzer gibt es ein Menü, das Folgendes enthält:

- **Erweiterte Übersetzerkonfiguration**

  Wenn Sie auf diese Option klicken, öffnet sich das Addon-Konfigurationsfenster. Dieses Fenster besteht aus 2 Abschnitten:

  -**Allgemein**

    In diesem Tab werden die allgemeinen Optionen des Addons angezeigt. Derzeit gibt es nur eine Checkbox, um den Addon-Cache ein- oder auszuschalten.

    Das Addon kann für jede Anwendung einen Cache mit den Übersetzungen speichern, was die Übersetzung für zukünftige Übersetzungen einfacher und schneller macht. Darüber hinaus wird jetzt für jede Sprache ein Cache erstellt, und es kann mehr als eine Anwendung geben, die über einen Cache für verschiedene Sprachen verfügt.

  - **Übersetzungs-Module**

    Auf dieser Registerkarte können Sie den Dienst auswählen, den Sie zum Übersetzen verwenden möchten. Für die Dienste, die einen API-Schlüssel benötigen, wird auch der API-Schlüssel-Manager angezeigt.

    Sie können mehr als einen API-Schlüssel für denselben Dienst haben. In LibreTranslate können Sie beispielsweise verschiedene Schlüssel und URLs für die Verbindung verwenden. Sie können den Standard-API-Schlüssel, den Sie für den aktuellen Dienst wünschen, hinzufügen, bearbeiten, löschen und festlegen.

    Der Abschnitt API-Schlüsselverwaltung ändert sich je nach ausgewähltem Dienst. Sie können jedem API-Schlüssel einen identifizierenden Namen geben, um schnell zu wissen, auf welche API Sie sich beziehen. Wenn Sie mehr als einen API-Schlüssel für einen Dienst haben, ist das Element mit einem Sternchen in der Liste das Standardelement. Dies kann mit der Schaltfläche "Standard" geändert werden, so dass der für den Dienst definierte Schlüssel der Schlüssel ist, auf den Sie sich in diesem Moment konzentriert haben.

    Wenn für den von Ihnen gewählten Übersetzungsdienst kein API-Schlüssel erforderlich ist, wird der API-Manager nicht angezeigt.

    Dann haben Sie die Schaltflächen "OK" und "Abbrechen". Alle Optionen verfügen über eine Tastenkombination, über die Sie von NVDA informiert werden.

- **Addon-Dokumentation**

  Wenn Sie auf "Plugin-Dokumentation" klicken, öffnet sich diese Dokumentation.

- **Spende einen Kaffee, wenn dir meine Arbeit gefällt**

  Wenn Sie auf diese Option klicken, öffnet sich die PayPal-Seite, auf der sich ein Link mit der Aufschrift "Senden" befindet. Wenn Sie auf diesen Link klicken, werden Sie aufgefordert, sich in Ihr Konto einzuloggen und auf der Spendenseite zu bleiben.

  Ich sage nur, dass ich viel Kaffee getrunken habe, während ich dieses Addon gemacht habe.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h4 id="addon-hotkeys">Addon-hotkeys</h4>

In den NVDA-Optionen > Tastenbefehle ... > Erweiterter Übersetzer gibt es die folgenden Schlüssel, die Sie konfigurieren können.

Die Standardtasten sind nicht zugewiesen, sodass der Benutzer das beste Layout für sie auswählen kann. Es handelt sich um die folgenden:

- **Öffnet die Addon-Konfiguration**

  Dadurch wird die Plugin-Konfiguration schnell geöffnet.

- **Übersetzungscache aktivieren oder deaktivieren**

  Dadurch wird der Cache aktiviert oder deaktiviert, ohne dass die Konfiguration eingegeben werden muss.

- **Aktivieren oder Deaktivieren der Online-Echtzeitübersetzung**

  Dadurch wird die Echtzeitübersetzung aktiviert oder deaktiviert. Es ist die Hauptfunktion, die zu übersetzen beginnt, wenn Sie sich mit den Cursorpfeilen bewegen. Wenn alles korrekt ist, hören Sie die Übersetzung; Wenn Sie den Originaltext hören, müssen Sie sich das NVDA-Protokoll ansehen und sehen, was passiert ist.

- **Ändern des Übersetzungsmoduls**

  Daraufhin öffnet sich ein Fenster mit allen verfügbaren Übersetzungsmodulen. Sie können sich mit den Pfeilen bewegen und mit "Enter" auswählen. Das Modul, das Sie auswählen, ist dasjenige, das Sie standardmäßig haben.

- **Zielsprache ändern**

  Daraufhin öffnet sich ein Fenster mit den Zielsprachen, die in dem von uns ausgewählten Modul verfügbar sind. Jeder Dienst hat unterschiedliche Sprachen, und wenn Sie beispielsweise einen Text übersetzen, der auf Russisch ist und Sie ihn auf Englisch hören möchten, müssen Sie in diesem Dialogfeld Englisch auswählen. Sie bewegen sich mit Cursorpfeilen und "Enter" durch den Dialog, um die gewünschte Sprache auszuwählen.

- **Quellsprache ändern**

  Ähnlich wie die vorherige Funktion, aber dieser Dialog ist nur für den Microsoft-Übersetzer verfügbar. Der Microsoft-Dienst erlaubt es Ihnen nicht, die Ausgangssprache auf automatisch einzustellen, damit er erkennt, welche Sprache an Sie gesendet wird, sodass Sie sie selbst auswählen müssen.

  Die übrigen Dienste können dieses Dialogfeld nicht verwenden, da ihre Standardoption darin besteht, zu erkennen, welche Sprache gesendet wird.

- **Kopieren Sie den zuletzt übersetzten Text in die Zwischenablage**

  Dadurch wird der letzte Text, der in die Zwischenablage übersetzt wurde, kopiert.

- **Löschen des Übersetzungscaches für die aktuell fokussierte Anwendung**

  Wenn wir diese Taste einmal drücken, erhalten wir Informationen; Wenn wir es zweimal schnell drücken, wird der Cache für die Anwendung geleert, die gerade den Fokus hat, und wir werden über das Ergebnis informiert.

- **Alle zwischengespeicherten Übersetzungen für alle Apps löschen**

  Wenn diese einmal gedrückt wird, erhalten wir Informationen; Zweimal schnell gedrückt, löscht es den gesamten Plugin-Cache und bietet auch Informationen an.

- **Zeigt die Übersetzungshistorie an**

  Es wird ein Dialog mit den letzten 500 Übersetzungen in einer Liste angezeigt. Sie können den Ausgangstext und den übersetzten Text in schreibgeschützten Feldern suchen und überprüfen. In diesem Dialogfeld können Sie die gesamte Historie durchsuchen, sowohl den Ausgangstext als auch den übersetzten Text in die Zwischenablage kopieren oder beides.

  Es ermöglicht Ihnen auch, zwischen Ausgangstext und übersetztem Text zu wechseln und in beide Richtungen zu arbeiten. Darüber hinaus können Sie den gesamten Verlauf löschen, um von vorne zu beginnen.

  Beachten Sie, dass der Verlauf bei jedem Neustart von NVDA gelöscht wird.

- **Den ausgewählten Text übersetzen**

  Diese Aktion übersetzt den Text, den Sie ausgewählt und fokussiert haben. Wenn es sich um einen großen Text handelt, öffnet sich ein Dialog mit dem Prozentsatz der Übersetzung. Dieser Dialog kann abgebrochen werden, wodurch auch die Übersetzung abgebrochen wird.

  Sobald die Übersetzung abgeschlossen ist, wird der Text in einem Dialogfeld angezeigt, damit Sie ihn erkunden können.

  Diese Option verwendet den Google Übersetzer-Dienst und dieser Dienst kann nicht geändert werden, da er intern ausgewählt wird, da er die besten Ergebnisse für lange Texte liefert.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h2 id="Fehlerbehebung">3 - Fehlerbehebung</h2>

<h3 id="häufige-probleme-und-lösungen">häufige probleme und lösungen</h3>

**Internetverbindung**
- Überprüfen Sie, ob Ihre Internetverbindung aktiv ist und ordnungsgemäß funktioniert.
- Starten Sie bei Bedarf Ihren Router oder Ihr Modem neu.

**Zertifikatsfehler**
- Wenn Zertifikatfehler auftreten, stellen Sie sicher, dass Datum und Uhrzeit des Systems korrekt sind.
- Stellen Sie sicher, dass die erforderlichen Zertifikate installiert und aktualisiert wurden.

**Leistungsprobleme**
- Stellen Sie sicher, dass Ihr Computer die Mindestsystemanforderungen erfüllt.
- Schließen Sie andere Anwendungen, die möglicherweise viele Ressourcen verbrauchen.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="how-to-consult-the-nvda-log">Wie konsultiert man das NVDA-Log</h3>

1. Öffnen Sie NVDA.
2. Gehen Sie zu "NVDA > Werkzeuge > Protokoll anzeigen".
3. Suchen Sie im Protokollfenster nach Fehlern oder Meldungen im Zusammenhang mit Advanced Translator.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h2 id="Danksagung">4 - Danksagung</h2>

Vielen Dank an alle NVDA-Programmierer für ihre hervorragende Arbeit.

Und ich möchte nicht versäumen zu sagen, dass der Anfang dieses Plugins von Yannick PLASSIARDs Plugin (TRANSLATE) kam, von dem ich einige Funktionen gelernt und verwendet habe.

Vielen Dank auch an Alexy Sadovoy aka Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino und andere NVDA-Mitwirkende für das Plugin Instant Translate, von dem eine der Methoden für Google abgerufen und geändert wurde, um sie in Advanced Translator zu implementieren.

Dieses Plugin ist das Ergebnis mehrerer Jahre der Veröffentlichung inoffizieller Versionen und der Untersuchung der Verwendung von Offline-Übersetzungen.

Dieses Addon ist das Ergebnis dieses Lernens, wobei zu bedenken ist, dass es in Zukunft überraschende neue Funktionen mit sich bringen wird.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Übersetzer">Übersetzer</h3>

- **Portugiesisch:** Ângelo Abrantes.
- **Türkisch:** Umut Korkmaz.
- **Russisch:** Walentin Kuprianov.
- **Englisch:** Samuel Proulx.
- **Ukrainisch:** Heorhii Halas und Volodymyr Pyrih.
- **Deutsch:** BFW Würzburg

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h2 id="version-changelog">5 - Änderungsprotokoll</h2>

In diesem Abschnitt wird ein Was-ist-neu hinzugefügt, in dem die neuen Funktionen jeder Version veröffentlicht werden.

Das Handbuch basiert auf der ersten Version, so dass es nicht als Basis aktualisiert wird.

Neuigkeiten werden in dieser Rubrik hinzugefügt.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="version-1-0">Version 2024.06.06</h3>

- Erste Veröffentlichung des Plugins.
- Unterstützung für 7 Übersetzungsdienste.
- Grundlegende Funktionen der Echtzeit-Übersetzung und der API-Schlüsselverwaltung.

<h3 id="Version-2024-06-16">Version 2024.06.16</h3>

- **Es wurde die Möglichkeit hinzugefügt, die Übersetzung des markierten Textes in die Zwischenablage zu kopieren, anstatt ihn in einem Dialog anzuzeigen:**

Es wurde eine Option hinzugefügt, mit der übersetzter Text automatisch in die Zwischenablage kopiert werden kann, wenn diese Funktion ausgewählt ist, sodass kein zusätzliches Dialogfeld angezeigt werden muss.

Diese Option wurde im Plugin-Konfigurationsdialog unter Allgemein hinzugefügt.

Wenn diese Option aktiviert ist, wird beim Übersetzen eines markierten Textes kein Dialog mehr angezeigt, sondern direkt in die Zwischenablage kopiert.

- **Übersetzen Sie, was sich in der Zwischenablage befindet:**

Es ist jetzt möglich, Inhalte, die sich in der Zwischenablage befinden, direkt zu übersetzen, was eine schnelle und effiziente Möglichkeit bietet, kopierte Texte zu übersetzen.

Wenn nichts übersetzt ist, wird es Ihnen mitteilen, was sich in der Zwischenablage befindet, oder wenn sich nichts in der Zwischenablage befindet, werden Sie mit einer Nachricht benachrichtigt.

- **Übersetze das Letzte, was der Synthesizer gesprochen hat:**

Es wurde eine Funktion hinzugefügt, mit der Sie die letzte Phrase oder den letzten vom Sprachsynthesizer gesprochenen Text übersetzen können, um die Zugänglichkeit und Benutzerfreundlichkeit des Addons zu verbessern.

Wenn das zuletzt Gesprochene nicht übersetzt werden kann, wird Ihnen das Letzte mitgeteilt, was in der Ausgangssprache gesprochen wurde.

- **Übersetzungen in Blindenschrift anzeigen:**

Die neue Version unterstützt die Anzeige von Übersetzungen auf Braille-Anzeigegeräten, um den Zugriff auf Übersetzungen zu erleichtern.

Es funktioniert nur auf Geräten, auf denen eine Braillezeile konfiguriert ist.

Diese Funktion befindet sich in der Testphase.

- **Sprach-Updater des Plugins:**

Es wurde ein Updater implementiert, um die Plugin-Sprachen immer auf dem neuesten Stand zu halten und die Verfügbarkeit der neuesten und genauesten Sprachen zu gewährleisten.

Jetzt im NVDA-Menü > Optionen > Erweiterter Übersetzer

Sie erhalten ein neues Element mit dem Namen Plug-in-Sprachen aktualisieren (keine Updates).

Dieser Punkt informiert Sie, wenn es Aktualisierungen gibt, zum Beispiel:

Update-Plugin-Sprachen (3 Updates verfügbar)

Wenn Sie diese Taste drücken, erscheint ein Dialogfeld mit den neuen Sprachen, mit den Aktualisierungen der vorhandenen Sprachen oder mit beiden.

Sie können diese installieren oder überspringen.

Wenn Sie auf Installieren klicken, werden die Sprachen heruntergeladen und installiert, und NVDA wird neu gestartet.

Der Menüpunkt wird alle 30 Minuten aktualisiert, wobei nach Updates gesucht wird, oder bei jedem Neustart.

Der Datenaufwand für diese Prüfung ist gering, da Sie an den Orten, an denen Datenprobleme auftreten, weniger als 1 KB überprüfen müssen.

Dieser Updater wird es einfacher machen, Sprachupdates für das Addon schnell mit Benutzern zu teilen, sobald sie ankommen und ohne dass eine neue Version mit den neuen Sprachen veröffentlicht werden muss.

Jede neue Version des Addons wird mit allen neuen und aktualisierten Sprachen geliefert, die eingetroffen sind.

- **Fehler beim kontinuierlichen Lesen behoben:**

Es wurde ein Problem behoben, das zu Fehlern beim kontinuierlichen Lesen führte, wodurch die Stabilität und Leistung des Addons bei längerer Nutzung verbessert wurde.

- **Anmerkungen des Autors:**

Alle neuen Funktionen wie das Übersetzen der Zwischenablage, das Übersetzen der letzten vom Synthesizer gesprochenen Wörter oder das Überprüfen von Sprachupdates können mit Gesten belegt werden.

Ich empfehle, dass Sie, wenn Sie keine Option verwenden, keine Eingabegeste hinzufügen, damit Sie sie für andere Addons frei haben können. Fügen Sie nur diejenigen hinzu, die für Sie nützlich sind.

Wenn Funktionen hinzugefügt werden, werden mehr Gesten benötigt, und eine Funktion funktioniert möglicherweise nicht für eine Person und möglicherweise gut für eine andere, also weisen Sie nur die zu, die Sie verwenden werden.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Version-2024-06-23">Version 2024.06.23</h3>

* Neues DeepL Translator Modul hinzugefügt (kostenlos)

Dieses neue Modul benötigt keinen API-Schlüssel und wird für die Echtzeit-Übersetzung verwendet

*Fehlerkorrektur

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)

<h3 id="Version-2024-09-07">Version 2024.09.07</h3>

#### Übersetzungsschnittstelle

Die **Übersetzungsschnittstelle** ist die Hauptkomponente des **Erweiterter Übersetzer** Addons für NVDA. Diese Schnittstelle ermöglicht es dem Benutzer, Text effizient zwischen verschiedenen Sprachen zu übersetzen, den ursprünglichen und den übersetzten Text anzuzeigen und verschiedene Anpassungsoptionen bereitzustellen.

Um es aufzurufen, müssen Sie eine Tastenkombination in tastenbefehle  oder aus dem virtuellen Menü zuweisen (siehe unten).

##### Hauptmerkmale:

1. **Quelltexteingabe**: Ermöglicht es dem Benutzer, den Text, den er übersetzen möchte, zu schreiben oder einzufügen. Er kann mit der Tastenkombination 'Alt+1' schnell aufgerufen werden.
   
2. **Zieltext (Ergebnis)**: Der Bereich, in dem der übersetzte Text angezeigt wird. Dieses Feld ist schreibgeschützt und kann mit 'Alt+2' fokussiert werden.

3. **Auswahl der Ausgangssprache**: Ermöglicht die Auswahl der Sprache des Ausgangstextes. Die Standardsprache ist die Option "Automatische Erkennung", mit der das System die Sprache des Textes automatisch erkennen kann. Der Zugriff erfolgt mit 'Alt+3'.

4. **Auswahl der Zielsprache**: Hier können Sie die Sprache auswählen, in die Sie den Text übersetzen möchten. Es kann mit 'Alt+4' fokussiert werden.

5. **Zeichenzähler**: Zeigt die Anzahl der Zeichen im Quelltextfeld an. Es ist nützlich, die Menge des zu übersetzenden Textes zu kennen. Der Zugriff erfolgt mit 'Alt+5'.

6. **Aktionstasten**:
   - **Übersetzen**: Startet die Übersetzung des eingegebenen Textes.
   - **Hören**: Ruft das Audio der Übersetzung ab und ermöglicht die Wiedergabe über einen integrierten Player (siehe Abschnitt unten).
   - **Tauschen**: Tauschen Sie die Ausgangssprache mit der Zielsprache aus, was nützlich ist, wenn Sie die Übersetzungssprachen umkehren möchten.
   - **Löschen**: Löscht sowohl die Quell- als auch die Zieltextfelder.
   - **In Fokus einfügen**: Fügt den übersetzten Text in das aktive Fenster oder Textfeld hinter der Benutzeroberfläche ein. Es kann auch mit 'F3' aktiviert werden.
   - **Schließen**: Schließen Sie das Übersetzungsfenster.

##### Tastenkombinationen:

- 'Alt+1': Fokussieren Sie das Quelltextfeld.
- 'Alt+2': Fokussieren Sie das Zieltextfeld.
- 'Alt+3': Wählen Sie die Ausgangssprache aus.
- 'Alt+4': Wählen Sie die Zielsprache aus.
- 'Alt+5': Fokussiert den Zeichenzähler.
- 'F3': Fügt den übersetzten Text in das aktive Fenster ein.
- 'Esc': Schließt den Übersetzungsdialog.

##### Verhalten bei Fehlern:

- Wenn keine Internetverbindung besteht, zeigt das System eine Meldung an, die über das Fehlen einer Verbindung informiert.
- Wenn das Feld für den Ausgangstext leer ist, erhält der Benutzer eine Warnung, in der er aufgefordert wird, Text einzugeben, bevor er die Übersetzung durchführt.
- Wenn die Ausgangs- und Zielsprache identisch sind, wird eine Warnung angezeigt, die darauf hinweist, dass der Text nicht in dieselbe Sprache übersetzt werden muss.

##### Zusätzliche Funktionen:

- **Automatische Spracherkennung**: Wenn "Automatische Erkennung" in der Ausgangssprache ausgewählt ist, versucht das Plugin automatisch, die Sprache des zu übersetzenden Textes zu identifizieren.
- **Sprachaustausch**: Diese Funktion ist nützlich, wenn Sie einen Text in die Originalsprache zurückübersetzen möchten.

#### Audioplayer

Wenn der Benutzer nach einer Übersetzung die Option **Hören** verwendet, wandelt das Plugin den übersetzten Text in eine Audiodatei um und spielt sie über einen integrierten Player ab. Dieser Player enthält grundlegende und erweiterte Steuerelemente zur Verwaltung der Audiowiedergabe.

##### Player-Funktionen:

1. **Bedientasten**:
   - **Rückwärts (F1)**: Spult die Wiedergabe entsprechend der ausgewählten Zeit zurück. Der Benutzer kann diese Zeit konfigurieren.
   - **Wiedergabe/Pause (F2)**: Starten oder pausieren Sie die Wiedergabe der Audiodatei.
   - **Schneller Vorlauf (F3)**: Spulen Sie die Wiedergabe entsprechend der vom Benutzer eingestellten Zeit vor.
   - **Stopp (F4)**: Stoppt die Wiedergabe vollständig.

2. **Lautstärke und Geschwindigkeit**:
   - **Lautstärke (F5/F6)**: Stellen Sie die Wiedergabelautstärke mit einem Schieberegler ein.
   - **Geschwindigkeit (F7/F8)**: Ändern Sie die Wiedergabegeschwindigkeit mit Optionen von 0,50x bis 2,0x der normalen Geschwindigkeit.

3. **Zugeordneter Text**: Zeigt den übersetzten Text in einem schreibgeschützten Feld an, sodass der Benutzer sehen kann, was gerade abgespielt wird.

4. **Speichern**: Ermöglicht es Ihnen, die generierte Audiodatei im WAV-Format auf Ihrem System zu speichern.

5. **Schließen**: Schließt den Player und gibt die zugehörigen Ressourcen frei.

##### Tastenkombinationen:

- 'F1': Wiedergabe zurückspulen.
- 'F2': Wiedergabe oder Pause des Audios.
- 'F3': Schneller Vorlauf der Wiedergabe.
- 'F4': Stoppen Sie die Wiedergabe.
- 'F5/F6': Stellen Sie die Lautstärke ein.
- 'F7/F8': Ändern Sie die Wiedergabegeschwindigkeit.
- 'F9': Informationen zur Wiedergabezeit.
- 'Umschalt+F10/Anwendungen': Zeigt ein Kontextmenü an, in dem Sie die Zeitintervalle der Tasten zum Zurückspulen und Vorspulen auswählen können.

##### Zusätzliche Funktionen:

- **Audio speichern**: Benutzer können die Audiodatei zur späteren Verwendung im WAV-Format auf ihrem Gerät speichern.
- **Menü "Erweiterte Optionen": Mit dem Player können Sie die genaue Zeit zum Zurück- oder Zurückspulen der Wiedergabe über ein Kontextmenü (Zugriff mit der Taste "Umschalt+F10") oder die Anwendungstaste auswählen.

#### Virtuelles menü

Es wurde ein virtuelles Menü hinzugefügt, das alle Optionen des Addons enthält.

Sie können alle Optionen aus dem virtuellen Menü aufrufen, die Sie in Eingabegesten zuweisen können. Auf diese Weise können alle Funktionen des Addons genutzt werden, ohne dass dem Addon weitere Tasten zugewiesen werden müssen.

Dies ist dem Benutzer überlassen.

Um das virtuelle Menü aufzurufen, müssen Sie ihm in Tastenbefehle  eine Taste zuweisen.

Die Verwendung des virtuellen Menüs ist einfach, sobald es aufgerufen ist, müssen Sie die entsprechende Taste für die Aktion drücken, die Sie ausführen möchten. Sobald Sie gedrückt haben, wird die Aktion ausgeführt und Sie werden immer darüber informiert, was getan wurde. Wenn Sie eine Taste drücken, die nicht zugewiesen ist, wird das virtuelle Menü geschlossen und Sie können es auch mit der Escape-Taste schließen.

##### Tastaturkürzel für virtuelle Menüs

Über das virtuelle Menü des erweiterten Übersetzers können Sie schnell auf die nützlichsten Funktionen des Plugins zugreifen. Im Folgenden finden Sie Tastenkombinationen, mit denen Sie verschiedene Aktionen ausführen können:

- **'P'**: **Konfiguration öffnen**  
  Öffnen Sie die Einstellungen für den erweiterten Übersetzer, in denen Sie die Sprachen und Übersetzungsdienste anpassen können.

- **'U'**: **Nach Sprachupdates suchen**  
  Suchen Sie nach verfügbaren Updates für die Plugin-Sprachen und laden Sie sie herunter.

- **'O'**: **Quellsprache ändern**  
  Ändern Sie die Sprache des Textes, den Sie übersetzen möchten (Ausgangssprache).

- **'D'**: **Zielsprache ändern**  
  Ändern Sie die Sprache, in die Sie den Text übersetzen möchten (Zielsprache).

- **'C'**: **Übersetzungsdienst ändern**  
  Ermöglicht es Ihnen, zwischen verfügbaren Übersetzungsdiensten wie Google, DeepL, Microsoft und anderen zu wechseln.

- **'A'**: **Den gesamten Übersetzungscache löschen**  
  Löscht alle zwischengespeicherten Übersetzungen.

- **'X'**: **Übersetzungscache der aktuellen Anwendung löschen**  
  Löschen Sie zwischengespeicherte Übersetzungen nur für die App, die Sie geöffnet haben.

- **'G'**: **Übersetzungscache aktivieren/deaktivieren**  
  Aktivieren oder deaktivieren Sie die Cache-Funktion, die Übersetzungen vorübergehend speichert.

- **'L'**: **Letzte Übersetzung in die Zwischenablage kopieren**  
  Kopieren Sie die letzte Übersetzung in die Zwischenablage, damit Sie sie an der gewünschten Stelle einfügen können.

- **'B'**: **Text aus der Zwischenablage übersetzen**  
  Übersetzt den aktuellen Inhalt der Zwischenablage.

- **'V'**: **Den zuletzt gesprochenen Text übersetzen**  
  Übersetzt den letzten Text, den NVDA vorgelesen hat.

- **'T'**: **Echtzeit-Übersetzung aktivieren/deaktivieren**  
  Aktivieren oder deaktivieren Sie die automatische Übersetzung beim Durchsuchen von Texten.

- **'S'**: **Den ausgewählten Text übersetzen**  
  Übersetzen Sie den Text, den Sie in der Anwendung ausgewählt haben.

- **'Z'**: **Text aus Browserobjekt übersetzen**  
  Übersetzt den Text eines bestimmten Objekts in der Übersicht, z. B. einer Schaltfläche oder eines Textfelds.

- **'W'**: **Übersetzungsschnittstelle öffnen**  
  Öffnet das grafische Fenster, in dem Sie den Text, den Sie übersetzen möchten, manuell eingeben können.

- **'I'**: **Ausgewählte Sprache erkennen**  
  Erkennt automatisch die Sprache des markierten Textes.

- **'J'**: **Aktivieren/Deaktivieren des automatischen Sprachaustauschs**  
  Schaltet die automatische Ein- oder Ausschaltung ein, wenn die erkannte Ausgangssprache mit der Zielsprache übereinstimmt.

- **'K'**: **Primäre und alternative Sprachen tauschen**  
  Tauschen Sie die Hauptsprache in den Übersetzereinstellungen gegen die alternative Sprache aus.

- **'H'**: **Übersetzungshistorie anzeigen**  
  Zeigt einen Verlauf der kürzlich durchgeführten Übersetzungen an.

- **'F1'**:**Liste der Befehle anzeigen**  
  Zeigt ein Dialogfeld an, in dem Befehle mit einer Taste für den erweiterten Übersetzer aufgelistet sind.

#### Spracherkennung

Mit dieser Option können Sie die Sprache des Textes, den Sie in einer beliebigen Anwendung ausgewählt haben, automatisch erkennen. So verwenden Sie diese Funktion:

1. Wählen Sie den Text aus, dessen Sprache Sie wissen möchten.
2. Verwenden Sie die Tastenkombination, die in den Eingabegesten (oder im virtuellen Menü) konfiguriert ist, um die Spracherkennung zu aktivieren.
3. Das System erkennt und informiert Sie über die Sprache, in der der ausgewählte Text verfasst ist.

Diese Funktion ist nützlich, wenn Sie sich über die Sprache eines Textes nicht sicher sind und diese kennen müssen, bevor Sie ihn übersetzen oder andere Maßnahmen ergreifen.

#### Automatischer Sprachaustausch in NVDA erweiterter Übersetzer

  1. Aktivieren Sie den automatischen Austausch, indem Sie die entsprechende Tastenkombination drücken oder über das virtuelle Menü darauf zugreifen.
  2. Wenn der von Ihnen ausgewählte Text in der gleichen Sprache wie die Zielsprache vorliegt, wechselt das System automatisch die Zielsprache in die alternative Sprache, um unnötige Übersetzungen zu vermeiden.
  3. Sie können diese Option jederzeit mit derselben Tastenkombination deaktivieren.

##### Spracheinstellungen im Addon

- Sie können **Zielsprachen** und **alternative Sprachen** konfigurieren, indem Sie auf **Addon-Einstellungen** im Abschnitt **Allgemein** zugreifen. Von dort aus können Sie die Sprachen auswählen, die für den automatischen Austausch verwendet werden sollen.

Diese Funktion ist nützlich, um Verwirrung bei der Übersetzung von Texten zu vermeiden, bei denen die Ausgangssprache mit der Zielsprache übereinstimmt, und automatisch auf eine konfigurierte alternative Sprache umzuschalten.

#### Hilfe in Addon-Dialogen

Es wurde eine Funktion hinzugefügt, um kontextbezogene Hilfe in Addon-Dialogen anzuzeigen. Durch Drücken der Tastenkombination 'Strg+H' wird eine kleine Beschreibung der Funktion des Widgets angezeigt, das sich gerade im Fokus befindet.

Wenn Sie an einer beliebigen Stelle in den Addon-Dialogen Informationen über die Funktion einer Schaltfläche, eines Textfelds, eines Schiebereglers oder eines anderen Steuerelements benötigen, können Sie einfach "Strg+H" drücken. Daraufhin wird eine kurze Beschreibung des fokussierten Widgets mit einer Kurzanleitung zu seiner Verwendung angezeigt.

#### Text aus Browserobjekt übersetzen

Diese Funktion ermöglicht es Ihnen, den Text eines bestimmten Objekts innerhalb des Browsers oder einer anderen Anwendung, die NVDA verwendet, zu übersetzen. Sie kann über das virtuelle Menü oder über eine Tastenkombination aktiviert werden, die in den Eingabegesten des Addons zugewiesen ist.

1. Platzieren Sie den Cursor über dem Objekt, das Sie übersetzen möchten (es kann sich um eine Schaltfläche, ein Textfeld usw. handeln).
2. Aktivieren Sie die Funktionalität durch Drücken der zugewiesenen Tastenkombination oder über das virtuelle Menü.
3. Das Addon übersetzt den in diesem Objekt enthaltenen Text und zeigt ihn je nach Konfiguration an oder liest ihn.

- Übersetzen Sie jeden Text, der im ausgewählten Objekt enthalten ist, innerhalb einer Webseite, Anwendung oder einer anderen Schnittstelle, an der NVDA interagiert.
- Nützlich zum Übersetzen kleiner Textabschnitte, die nicht Teil des Hauptteils einer Seite oder Anwendung sind, z. B. Menüs, Schaltflächen oder Beschriftungen.
- Wenn das Objekt keinen Text enthält oder nicht zugänglich ist, zeigt das Plugin eine Meldung an, die darüber informiert, dass kein Text zum Übersetzen vorhanden ist.

- Sie können auf diese Funktionalität sowohl über das virtuelle Menü des Addons als auch durch Festlegen eines Hotkeys in den "Eingabegesten" von NVDA zugreifen.

#### OpenAI-Modul

Es wurde ein neues Modul hinzugefügt, um mit OpenAI mit dem chatGPT-4º-mini-Modell zu übersetzen, das am billigsten und schnellsten ist.

Dieses Modul befindet sich in der Testphase und tritt manchmal mit einer kleinen Verzögerung auf, wird sich aber in zukünftigen Versionen verbessern.

Für dieses Modul muss ein API-Schlüssel in der Konfiguration / Module zugewiesen werden.

OpenAI wird bezahlt, so dass es dem Benutzer überlassen ist, seine Ausgaben zu überprüfen.

Unter dem folgenden Link können Sie die Ausgabe sehen, die Sie verwendet haben:

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Verbesserung im Microsoft-Modul

Das Microsoft-Übersetzermodul wurde von Grund auf neu geschrieben, um die Geschwindigkeit und Stabilität zu verbessern und mehr Übersetzungszeit zu ermöglichen, bis Sie aufgrund der Verwendung blockiert werden und Sie einige Minuten warten müssen, um erneut zu übersetzen.

In meinen Tests, bei denen ich gleichzeitig viel Text übersetzt habe, auch mehr als bei normalem Gebrauch, habe ich keine Einschränkungen erlitten.

Im Moment funktioniert es also und wurde im Vergleich zum vorherigen Modul verbessert.

#### Sonstiges

* Problem mit der Verbalisierung einiger Nachrichten behoben.
* Die Methode zur Überprüfung, ob Internet vorhanden ist, wurde geändert.
* Fehlerbehebungen
* Offiziell französische Sprache hinzugefügt.

[Zurück zum Inhaltsverzeichnis](#Inhaltsverzeichnis)
# User Manual: Advanced Translator for NVDA

<h2 id="index">Index</h2>

- [1 - Introduction](#introduction)
  - [1.1 - Requirements](#requirements)
  - [1.2 - Limitations and warnings](#limitations-and-warnings)
  - [1.3 - Author information](#author-information)
- [2 - Description and configuration](#description-configuration)
  - [2.1 - Module description](#module-description)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Translate](#microsoft-translate)
  - [2.2 - Configuration](#configuration)
    - [Addon Menu](#addon-menu)
    - [Addon Hotkeys](#addon-hotkeys)
- [3 - Troubleshooting](#troubleshooting)
  - [Common Problems and Solutions](#common-problems-and-solutions)
  - [How to Consult the NVDA Log](#how-to-consult-the-nvda-log)
- [4 - Acknowledgments](#acknowledgments)
  - [Translators](#translators)
- [5 - Version Changelog](#version-changelog)
  - [Version 1.0](#version-1-0)
  - [Version 2024.06.16](#version-2024-06-16)
  - [Version 2024.06.23](#version-2024-06-23)
  - [Version 2024.09.07](#version-2024-09-07)

<h2 id="introduction">1 - Introduction</h2>

**Advanced Translator for NVDA** is an addon that allows you to translate texts using various online translation services, such as Google Translate, DeepL, LibreTranslate and Microsoft Translator. This addon offers advanced features such as real time translation, translation history, translation of the selected text, support for multiple languages, and more.

[Back to index](#index)

<h3 id="requirements">1.1 - Requirements</h3>

- NVDA (NonVisual Desktop Access) 2024.1 or higher
- Internet connection

[Back to index](#index)

<h3 id="limitations-and-warnings">1.2 - Limitations and warnings</h3>

The addon sends information over the Internet to each service to perform real time translation. It is important to note that the information being translated may include confidential and sensitive data. The use of the plugin is the sole responsibility of the user, who must evaluate the nature of the information sent. The developer of the plugin takes no responsibility for the data sent to the services that the plugin uses.

As a developer, I decline all responsibility for any eventuality that may arise from the use of the plugin. Complete responsibility lies with the user.

Additionally, the plugin requires an Internet connection to function. The response speed of the plugin depends on several factors, such as:
- The quality of your Internet connection.
- The possible delay (lag) of the translation services used.
- Factors related to the user's network infrastructure.

It is recommended that users be aware of these aspects and perform the necessary tests to ensure that the plugin meets their expectations and security requirements.[Back to index](#index)

<h3 id="author-information">1.3 - Author information</h3>

**Technical Information and Security Measures of the Addon for NVDA**

I've worked hard to make the plugin as robust as possible, accounting for and handling any potential bugs. All errors are captured and recorded in the NVDA log, making it easy to track and quickly resolve issues.

**Problems with Windows Certificates**

Recently, I have noticed that new installations of Windows can have issues with certificates, which can be frustrating. For this reason, I have built in a check when the addon starts. If a failure related to the certificates is detected, the addon will automatically regenerate them, ensuring correct operation of both Windows and the addon itself.

**Security measures**

The addon includes several security measures:
- It is not allowed to run on secure screens.
- It does not start if an Internet connection is not detected.

Sometimes NVDA can start faster than the wi-fi network connects. In such cases, it will be necessary to restart NVDA after the connection is established in order to use the addon correctly.

**API Key Management**

The addon generates a JSON file that stores the necessary API keys for those services that require them. This file, called `apis.json`, is located in the Windows user folder.

**Key File Considerations**

It has been decided to store this file outside the addon folder, as it contains sensitive information.  This is to prevent this information from being inadvertently shared with a portable copy of NVDA or in other situations. If the user decides to stop using the addon, they must manually delete this file.

These measures ensure better management and security of the addon, facilitating its use and maintenance.

[Back to index](#index)

<h2 id="description-configuration">2 - Description and configuration</h2>

<h3 id="description-modules">2.1 - Description of modules</h3>

In its first version, the plugin offers 7 translation modules:

<h4 id="google">Google</h4>

**4 Google Modules**

- **2 Web Scraping Modules:** Each module performs the same function, but in a different way, ensuring that there is always an alternative available in case one of them fails.
- **2 Modules via API:** These modules are also unlimited and free, but abuse of them may result in a temporary IP ban for a few hours, after which the module will be available again.
- All these Google modules do not require API keys and are unlimited and free.

<h4 id="deepl">DeepL</h4>

**2 DeepL Modules**

- **Free API:** This option requires obtaining a Free API key from the DeepL page, which offers 500,000 characters per month.
- **Pro API:** This option also requires an API key obtained from the DeepL website. Its use is conditional on the balance and the contracted plan of the user's DeepL account.
- The terms of use of the DeepL API are found on its [website](https://www.deepl.com/en/pro/change-plan#developer), and the addon is limited by these terms.

<h4 id="libretranslate">LibreTranslate</h4>

**1 LibreTranslate Module**

- This service is constantly improving thanks to its continuous neural learning. Although it currently does not reach Google quality, it is perfectly usable.
- Based on Argos Translate technology.
- To use this module an API key is required, which can be obtained by making a donation to the [NVDA.es](https://nvda.es/donaciones/) community.
  - After donating, you can request the API key using the form on the following [page](https://nvda.es/contacto/), indicating in the subject "solicitud de clave API" and providing the PayPal reference, transfer , etc.
- Additionally, it is possible to configure other LibreTranslate services by adding the API key and modifying the service URL in the addon configuration section.

<h4 id="microsoft-translate">Microsoft Translate</h4>

**1 Microsoft Translate Module**

- This module has the limitation that continuous use may result in a temporary IP ban for a few minutes.
- This ban only occurs with very intensive use and in translations of long texts.
- The service works very well, but it is recommended not to use it continuously to avoid interruptions.

These options allow users to choose between various translation modules, ensuring availability and flexibility of the addon based on individual needs and preferences.

As the addon receives updates, services may be added or removed. Changes will be reported in the updates section.

[Back to index](#index)

<h3 id="configuration">2.2 - Configuration</h3>

**Addon Settings**

This section details how to configure each of the modules available in the addon, including how to add API keys, modify service URLs, and other settings necessary to customize the use of the addon to the user's needs.

<h4 id="plugin-menu">Addon menu</h4>

In NVDA > Preferences > Advanced Translator there is a menu that contains the following:

- **Advanced Translator Configuration**

  If you click this option, the addon configuration window will open. This window has 2 sections:

  - **General**

    In this tab, the general options of the addon are shown. Currently there is only one checkbox to turn the addon cache on or off.

    The addon can save a cache of the translations for each application, which will make the translation easier and faster for future translations. In addition, it now creates a cache for each language, and there may be more than one application that has a cache for different languages.

  - **Translation modules**

    In this tab you can choose the service you want to use to translate. For those services that require an API key, the API key manager will also be shown.

    You can have more than one API key for the same service; For example, in LibreTranslate you can have different keys and URLs to connect. You can add, edit, delete and set the default API key that you want for the current service.

    The API key management section changes depending on the service you have selected. You can give each API key an identifying name to quickly know which API you are referring to. When you have more than one API key for a service, the item that has an asterisk in the list will be the default one. This can be changed with the "Default" button, making the key defined for the service the key you have focused on at that moment.

    If the translation service you choose does not require an API key, the API manager will not be displayed.

    Then you have the "OK" and "Cancel" buttons. All options have a shortcut key that NVDA will inform you about.

- **Addon Documentation**

  If you click "Plugin Documentation" this documentation will open.

- **Donate a coffee if you like my work**

  If you press this option, the PayPal page will open where there is a link that says "Send". If you click on this link, it will ask you to log in to your account and leave you on the donation page.

  I'll just say that I've had a lot of coffee while making this addon.

[Back to index](#index)

<h4 id="addon-hotkeys">Addon-hotkeys</h4>

In NVDA > Preferences > Input Gestures... > Advanced Translator there are the following keys that you can configure.

The default keys come unassigned so that the user can choose the best layout for them. They are the following:

- **Opens addon configuration**

  This will quickly open the plugin configuration.

- **Enable or disable translation cache**

  This will activate or deactivate the cache without having to enter the configuration.

- **Activate or deactivate online real time translation**

  This activates or deactivates the real time translation. It is the main function that will begin to translate as you move with the cursor arrows. If everything is correct, you will hear the translation; If you hear the original text, you will have to look at the NVDA log and see what happened.

- **Change the translation module**

  This will open a window with all the translation modules available. You can move with the arrows and select with "Enter". The module you select will be the one you have by default.

- **Change target language**

  This will open a window with the target languages available in the module we have selected. Each service has different languages, and, for example, if you are translating a text that is in Russian and you want to hear it in English, in this dialog you will have to select English. You move through the dialog with cursor arrows and "Enter" to select the language you want.

- **Change source language**

  Similar to the previous function, but this dialog is only available for the Microsoft translator. The Microsoft service does not allow you to set the source language as auto so that it detects which language is sent to you, so you will have to choose it yourself.

  The rest of the services will not be able to use this dialog since their default option is to detect which language is being sent.

- **Copy the last translated text to the clipboard**

  This will copy the last text that has been translated to the clipboard.

- **Delete the translation cache for the currently focused application**

  If we press this once, it will give us information; If we press it twice quickly, it will clear the cache for the application that currently has focus and will inform us of the result.

- **Delete all cached translations for all apps**

  If this is pressed once, it will give us information; Pressed twice quickly, it will clear the entire plugin cache, also offering information.

- **Shows translation history**

  It will show a dialog with the last 500 translations in a list. You can search and review the source text and the translated text in read-only boxes. This dialog will allow you to search the entire history, copy both the source text and the translated text to the clipboard, or both.

  It also allows you to switch between source text and translated text and work in either way. In addition, you can delete all history to start from scratch.

  Notice that the history is cleared every time NVDA restarts.

- **Translate the selected text**

  This action will translate the text that you have selected and focused. If it is a large text, a dialog will open with the percentage of the translation. Said dialogue can be canceled, which will also cancel the translation.

  Once the translation is complete, the text will be displayed in a dialog so you can explore it.

  This option uses the Google Translate service and this service cannot be changed, being chosen internally since it is the one that gives the best results for long texts.

[Back to index](#index)

<h2 id="troubleshooting">3 - Troubleshooting</h2>

<h3 id="common-problems-and-solutions">Common Problems and Solutions</h3>

**Internet connection**
- Check that your Internet connection is active and working properly.
- Restart your router or modem if necessary.

**Certificate Errors**
- If you experience certificate errors, make sure your system date and time are correct.
- Verify that the necessary certificates are installed and updated.

**Performance Issues**
- Make sure your computer meets the minimum system requirements.
- Close other applications that may be consuming a lot of resources.

[Back to index](#index)

<h3 id="how-to-consult-the-nvda-log">How to Consult the NVDA Log</h3>

1. Open NVDA.
2. Go to `NVDA > Tools > View Log`.
3. In the log window, look for any errors or messages related to Advanced Translator.

[Back to index](#index)

<h2 id="acknowledgments">4 - Acknowledgments</h2>

Thanks to all the NVDA programmers for their excellent work.

And I don't want to fail to say that the beginning of this plugin came from Yannick PLASSIARD's plugin (TRANSLATE), from which I have learned and used some functions.

Also thanks to Alexy Sadovoy aka Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino, and other NVDA contributors for the plugin Instant Translate from which one of the methods for Google was obtained and modified to implement it in Advanced Translator.

This plugin is the work of several years of releasing unofficial versions and the study of using offline translations.

This addon is the result of this learning, keeping in mind that in the future it will bring surprising new features.

[Back to index](#index)
<h3 id="translators">Translators</h3>

- **Portuguese:** Ângelo Abrantes.
- **Turkish:** Umut Korkmaz.
- **Russian:** Valentin Kupriyanov.
- **English:** Samuel Proulx.
- **Ukrainian:** Heorhii Halas and Volodymyr Pyrih.

[Back to index](#index)

<h2 id="version-changelog">5 - changelog</h2>

In this section a changelog will be added, where the new features of each version will be posted.

The manual is based on the first version so it will not be updated serving as a base.

News will be added in this section.

[Back to index](#index)

<h3 id="version-1-0">Version 2024.06.06</h3>

- Initial release of the plugin.
- Support for 7 translation services.
- Basic functions of real time translation and API key management.

<h3 id="version-2024-06-16">Version 2024.06.16</h3>

- **Add the ability to copy the translation of selected text to the clipboard instead of showing it in a dialog:**

An option has been added to automatically copy translated text to the clipboard when this function is selected, avoiding the need to display an additional dialog box.

This option was added in the plugin configuration dialog in General.

If this option is checked, it will no longer display a dialog when you translate a selected text, but rather it will directly copy it to the clipboard.

- **Translate whatever is on the clipboard:**

It is now possible to directly translate content located on the clipboard, providing a fast and efficient way to translate copied texts.

If nothing is translated it will tell you what is on the clipboard or if there is nothing on the clipboard it will notify you with a message.

- **Translate the last thing spoken by the synthesizer:**

A function has been added that allows you to translate the last phrase or text spoken by the voice synthesizer, improving the accessibility and usability of the addon.

If the last thing spoken cannot be translated, it will tell you the last thing that was spoken in the source language.

- **Show translations in Braille:**

The new version includes support for displaying translations on Braille display devices, making translations easier to access.

It will only work on devices that have a Braille display configured.

This function is in the testing phase.

- **Plugin language updater:**

An updater has been implemented to keep the plugin languages always up to date, ensuring the availability of the most recent and accurate languages.

Now in the NVDA menu > Preferences > Advanced Translator

You will have a new item called Update plugin languages (No updates).

This item will inform you if there are updates, for example:

Update plugin languages (3 updates available)

If you press it, a dialog will appear with the new languages, with the updates of existing languages, or with both.

You can install or skip.

If you click install, the languages will be downloaded and installed and NVDA will restart.

The menu item is updated every 30 minutes checking for updates or on every restart.

The data expense of this check is small because for those places that have data problems, it is less than 1kb that you have to check.

This updater will make it easier to share language updates for the addon with users quickly as they arrive and without the need to release a new version with the new languages.

Each new version of the addon will come with all the new and updated languages that have arrived.

- **Continuous reading bug fixed:**

Fixed an issue that caused continuous reading errors, improving addon stability and performance during extended use.

- **Author's Notes:**

All new functions such as translating the clipboard, translating the last words spoken by the synthesizer or checking language updates, can be assigned gestures.

I recommend that if you are not going to use any option, you do not add an input gesture so that you can have it free for other addons. Only add those that will be useful to you.

As features are added, more gestures will be needed and a feature may not work for one person and it may work well for another, so assign only the ones you are going to use.

[Back to index](#index)

<h3 id="version-2024-06-23">Version 2024.06.23</h3>

* Added new DeepL Translator module (Free)

This new module does not need an API key and is used for real time translation

* Error correction

[Back to index](#index)

<h3 id="version-2024-09-07">Version 2024.09.07</h3>

#### Translation Interface

The **Translation Interface** is the main component of the **Advanced Translator** addon for NVDA. This interface allows the user to translate text between different languages efficiently, displaying the original and translated text, and providing various customization options.

To invoke it you will have to assign a key combination in input gestures or from the virtual menu (explained below).

##### Main features:

1. **Source text entry**: Allows the user to write or paste the text they want to translate. It can be accessed quickly with the key combination `Alt+1`.
   
2. **Target text (result)**: The area where the translated text is displayed. This field is read-only and can be focused with `Alt+2`.

3. **Source language selection**: Allows you to select the language of the source text. The default language is the "Auto Detect" option, which allows the system to automatically detect the language of the text. It is accessed with `Alt+3`.

4. **Target language selection**: Allows you to select the language to which you want to translate the text. It can be focused with `Alt+4`.

5. **Character Counter**: Displays the number of characters in the source text field. It is useful to know the amount of text that will be translated. It is accessed with `Alt+5`.

6. **Action Buttons**:
   - **Translate**: Starts the translation of the entered text.
   - **Listen**: Obtains the audio of the translation and allows it to be played through an integrated player (see section below).
   - **Swap**: Swap the source language with the target language, useful if you want to reverse translation languages.
   - **Clear**: Clears both the source and destination text fields.
   - **Paste to Focus**: Pastes the translated text into the active window or text field behind the interface. It can also be activated with `F3`.
   - **Close**: Close the translation window.

##### Keyboard shortcuts:

- `Alt+1`: Focus the source text box.
- `Alt+2`: Focus the target text box.
- `Alt+3`: Select the source language.
- `Alt+4`: Select the target language.
- `Alt+5`: Focus the character counter.
- `F3`: Paste the translated text into the active window.
- `Esc`: Close the translation dialog.

##### Behavior in case of errors:

- If there is no Internet connection, the system will display a message informing of the lack of connection.
- If the source text box is empty, the user will receive a warning asking to enter text before performing the translation.
- If the source and target languages are the same, a warning will be displayed indicating that the text does not need to be translated into the same language.

##### Additional Features:

- **Language auto-detect**: If "Auto Detect" is selected in the source language,The plugin will try to automatically identify the language of the text to be translated.
- **Language Exchange**: This function is useful when you want to translate a text back to the original language.

#### Audio Player

When the user uses the **Listen** option after performing a translation, the plugin converts the translated text into an audio file and plays it through an integrated player. This player includes basic and advanced controls to manage audio playback.

##### Player Features:

1. **Control buttons**:
   - **Backward (F1)**: Rewinds playback according to the selected time. The user can configure this time.
   - **Play/Pause (F2)**: Start or pause playback of the audio file.
   - **Fast forward (F3)**: Fast forward the playback according to the time set by the user.
   - **Stop (F4)**: Stops playback completely.

2. **Volume and speed**:
   - **Volume (F5/F6)**: Adjust the playback volume using a slider.
   - **Speed (F7/F8)**: Change the playback speed, with options from 0.50x to 2.0x the normal speed.

3. **Associated text**: Displays the translated text in a read-only box, allowing the user to view what is being played.

4. **Save**: Allows you to save the generated audio file in WAV format on your system.

5. **Close**: Closes the player and releases the associated resources.

##### Keyboard shortcuts:

- `F1`: Rewind playback.
- `F2`: Play or pause the audio.
- `F3`: Fast forward playback.
- `F4`: Stop playback.
- `F5/F6`: Adjust the volume.
- `F7/F8`: Change the playback speed.
- `F9`: Playback time information.
- `Shift+F10/Applications`: will display a contextual menu to choose the time intervals of the rewind and fast forward buttons.

##### Additional Features:

- **Save Audio**: Users can choose to save the audio file to their device in WAV format for later use.
- **Advanced options menu**: The player allows you to choose the exact time to rewind or advance playback through a contextual menu (accessed with the `Shift+F10` key) or applications key.

#### Virtual menu

A virtual menu has been added which contains all the options of the addon.

You can invoke all the options from the virtual menu that you can assign in input gestures. In this way, all of the features of the addon can be used without having to have more keys assigned to the addon.

This is up to the user.

In order to invoke the virtual menu you will have to assign a key to it in input gestures.

Using the virtual menu is simple, once invoked you will have to press the corresponding key for the action you want to perform. Once pressed, the action will be performed and you will always be informed of what has been done. If you press a key that is not assigned, the virtual menu will close and you can also close it with escape.

##### Virtual Menu Keyboard Shortcuts

The Advanced Translator virtual menu allows you to quickly access the most useful functions of the plugin. Below are shortcuts that you can use to perform various actions:

- **`P`**: **Open configuration**  
  Open the Advanced Translator settings where you can adjust the languages and translation services.

- **`U`**: **Check for language updates**  
  Check for and download available updates for the plugin languages.

- **`O`**: **Change source language**  
  Change the language of the text you want to translate (source language).

- **`D`**: **Change target language**  
  Change the language you want to translate the text to (target language).

- **`C`**: **Change translation service**  
  Allows you to switch between available translation services, such as Google, DeepL, Microsoft, among others.

- **`A`**: **Delete all translation cache**  
  Clears all cached translations.

- **`X`**: **Delete translation cache of the current application**  
  Clear cached translations only for the app you have open.

- **`G`**: **Enable/Disable translation cache**  
  Enable or disable the cache feature that temporarily saves translations.

- **`L`**: **Copy last translation to clipboard**  
  Copy the last translation made to the clipboard so you can paste it wherever you need it.

- **`B`**: **Translate clipboard text**  
  Translates the current contents of the clipboard.

- **`V`**: **Translate the last spoken text**  
  Translates the last text that NVDA read aloud.

- **`T`**: **Enable/Disable real-time translation**  
  Turn automatic translation on or off while browsing texts.

- **`S`**: **Translate the selected text**  
  Translate the text you have selected in the application.

- **`Z`**: **Translate text from browser object**  
  Translates the text of a specific object within the browser, such as a button or text box.

- **`W`**: **Open translation interface**  
  Opens the graphical window where you can manually enter the text you want to translate.

- **`I`**: **Detect selected language**  
  Automatically detects the language of the selected text.

- **`J`**: **Enable/Disable automatic language exchange**  
  Turns automatic switching on or off if the detected source language matches the target language.

- **`K`**: **Swap primary and alternate languages**  
  Swap the primary language with the alternate language in the translator settings.

- **`H`**: **Show translation history**  
  Shows a history of recent translations performed.

- **`F1`**:**Show list of commands**  
  Displays a dialog listing single-key commands for the Advanced Translator.

#### Language detection

This option allows you to automatically detect the language of the text you have selected in any application. To use this feature:
1. Select the text of which you want to know the language.
2. Use the keyboard shortcut configured in the input gestures (or virtual menu) to activate language detection.
3. The system will detect and inform you of the language in which the selected text is written.
This feature is useful when you are not sure of the language of a text and need to know it before translating it or taking any other action.

#### Automatic Language Exchange in NVDA Advanced Translator

  1. Activate automatic exchange by pressing the corresponding keyboard shortcut or accessing it from the virtual menu.
  2. If the text you select is in the same language as the target language, the system will automatically switch the target language to the alternative language to avoid unnecessary translations.
  3. You can disable this option at any time using the same shortcut.

##### Language Settings in the Addon

- You can configure **target languages** and **alternative languages** by accessing **Addon Settings** in the **General** section. From there you can select the languages that will be used for automatic exchange.

This feature is useful to avoid confusion when translating texts in which the source language is the same as the target language, automatically switching to a configured alternative language.

#### Help in Addon Dialogs

Added functionality to display contextual help in addon dialogs. Pressing the key combination `Ctrl+H` will display a small description of the function of the widget that is currently in focus.

Anywhere in the addon dialogs, if you need information about the function of a button, text box, slider, or other control, you can simply press `Ctrl+H`. This will display a brief description of the focused widget, providing a quick guide to its use.

#### Translate text from browser object

This functionality allows you to translate the text of a specific object within the browser or any other application that NVDA is using. It can be activated via the virtual menu or via a key combination assigned in the addon's input gestures.

1. Place the cursor over the object you want to translate (it can be a button, a text box, etc.).
2. Activate the functionality by pressing the assigned key combination or through the virtual menu.
3. The addon will translate the text contained in that object and display or speak it, depending on the configuration.

- Translate any text contained in the selected object within a web page,application or any other interface where NVDA interacts.
- Useful for translating small pieces of text that are not part of the main body of a page or application, such as menus, buttons, or labels.
- If the object does not contain text or is inaccessible, the plugin will display a message informing that there is no text to translate.

- You can access this functionality both from the addon's virtual menu and by setting a hotkey in NVDA's "Input Gestures".

#### OpenAI module

A new module has been added to translate with OpenAI with the chatGPT-4º-mini model, which is the cheapest and fastest.

This module is in testing, sometimes experiencing a bit of lag, but it will improve in future versions.

This module requires an API key to be assigned in configuration / modules.

OpenAI is paid so it is up to the user to check their spending.

In the following link you can see the expense you have used:

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Improvement in the Microsoft module

The Microsoft translator module has been rewritten from scratch to improve speed, stability and allow more translation time until they block you due to use and you have to wait a few minutes to translate again.

Now in my tests carried out by simultaneously translating a lot of text, even more than normal use, I have not suffered any restrictions.

So at the moment it works and has been improved compared to the previous module.

#### Others

* Fixed problem with the verbalization of some messages.
* Changed way to check if there is internet.
*Bug fixes
* Officially added French language.

[Back to index](#index)
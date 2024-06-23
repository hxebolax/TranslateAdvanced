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
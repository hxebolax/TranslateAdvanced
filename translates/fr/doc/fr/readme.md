# Manuel de l'utilisateur : Traducteur Avancé pour NVDA

<h2 id="sommaire">Sommaire</h2>

- [1 - Introduction](#introduction)
  - [1.1 - Exigences](#exigences)
  - [1.2 - Limites et avertissements](#limites-et-avertissements)
  - [1.3 - Informations de l'auteur](#informations-auteur)
- [2 - Description et configuration](#description-configuration)
  - [2.1 - Description des services](#description-services)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Translate](#microsoft-translate)
  - [2.2 - Configuration](#configuration)
    - [Menu de l'extension](#menu-extension)
    - [Touches ou gestes de commandes de l'extension](#touches-ou-gestes-de-commandes-extension)
- [3 - Solution de problèmes](#solution-de-problemes)
  - [Problèmes courants et solutions](#problemes-courants-et-solutions)
  - [Comment consulter le journal de NVDA](#comment-consulter-le-journal-de-nvda)
- [4 - Remerciements à](#remerciements-a)
  - [Traducteurs](#traducteurs)
- [5 - Journal des versions](#journal-des-versions)
  - [Version 2024.06.06](#version-2024-06-06)
  - [Version 2024.06.16](#version-2024-06-16)
  - [Version 2024.06.23](#version-2024-06-23)

<h2 id="introduction">1 - Introduction</h2>

Le **Traducteur Avancé pour NVDA** est une extension qui facilite la traduction de textes à l'aide de divers services de traduction en ligne, tels que Google Translate, DeepL, LibreTranslate et Microsoft Translator. Cette extension offre des fonctionnalités avancées telles que la traduction simultanée, l'historique des traductions, traduction de ce qui est sélectionné, prise en charge de plusieurs langues et encore plus.

[Retour au sommaire](#sommaire)

<h3 id="exigences">1.1 - Exigences</h3>

- NVDA (NonVisual Desktop Access) 2024.1 ou supérieur
- Connexion Internet

[Retour au sommaire](#sommaire)

<h3 id="limites-et-avertissements">1.2 - Limites et avertissements</h3>

L'extension envoie des informations sur Internet à chaque service correspondant pour effectuer une traduction simultanée. Il est important de noter que les informations traduites peuvent inclure des données confidentielles et sensibles. L'utilisation de l'extension relève de la responsabilité exclusive de l'utilisateur, qui doit évaluer la nature des informations envoyées. Le développeur de l'extension n'assume aucune responsabilité quant aux données envoyées aux services utilisés par l'extension.

En tant que développeur, je décline toute responsabilité quant à toute éventualité pouvant découler de l'utilisation de l'extension. L'entière responsabilité incombe à l'utilisateur.

De plus, l'extension nécessite une connexion Internet pour son fonctionnement. La vitesse de réponse de l'extension dépend de plusieurs facteurs, tels que :
- La qualité de notre connexion Internet.
- Le retard éventuel (lag) des services de traduction utilisés.
- Facteurs liés à l'infrastructure réseau de l'utilisateur.

Il est recommandé aux utilisateurs de prendre connaissance de ces aspects et d'effectuer les tests nécessaires pour s'assurer que l'extension répond à leurs attentes et exigences de sécurité.

[Retour au sommaire](#sommaire)

<h3 id="informations-auteur">1.3 - Informations de l'auteur</h3>

**Informations techniques et mesures de sécurité de l'extension pour NVDA**

J'ai travaillé dur pour rendre l'extension aussi robuste que possible, en tenant compte et en gérant les bogues potentiels. Toutes les erreurs sont capturées et enregistrées dans le journal NVDA, ce qui facilite le suivi et la résolution rapide des problèmes.

**Problèmes avec les certificats Windows**

Récemment, j'ai remarqué que les ordinateurs Windows nouvellement installés peuvent avoir des problèmes avec les certificats, ce qui peut être frustrant. Pour cette raison, j'ai incorporé une vérification au démarrage de l'extension. Si une défaillance liée aux certificats est détectée, l'extension les régénérera automatiquement, garantissant ainsi le bon fonctionnement de Windows et de l'extension elle-même.

**Mesure de sécurité**

L'extension comprend plusieurs mesures de sécurité :
- Son exécution n'est pas autorisée sur des écrans sécurisés.
- Elle ne démarre pas si aucune connexion Internet n'est détectée.

Parfois, NVDA peut démarrer plus rapidement que la connexion au réseau Wi-Fi. Dans de tels cas, il sera nécessaire de redémarrer NVDA une fois la connexion établie afin d'utiliser correctement l'extension.

**Gestion des clés API**

L'extension génère un fichier JSON qui stocke les clés API nécessaires pour les services qui les nécessitent. Ce fichier, appelé `apis.json`, se trouve dans le dossier utilisateur Windows.

**Considérations sur le fichier de clés**

Il a été décidé de stocker ce fichier en dehors de l'environnement de l'extension pour éviter un désagrément, car il contient des informations sensibles, et qu'il ne puissent pas être partagé par inadvertance dans une copie portable de NVDA ou dans d'autres situations. Si l'utilisateur décide de cesser d'utiliser l'extension, il doit supprimer manuellement ce fichier.

Ces mesures assurent une meilleure gestion et sécurité de l’extension, facilitant son utilisation et sa maintenance.

[Retour au sommaire](#sommaire)

<h2 id="description-configuration">2 - Description et configuration</h2>

<h3 id="description-services">2.1 - Description des services</h3>

Dans sa première version, l'extension propose 7 services de traduction :

<h4 id="google">Google</h4>

**4 Services de Google**

- **2 Services de grattage Web:** Chaque service remplit la même fonction, mais de manière différente, garantissant qu'il existe toujours une alternative disponible en cas de panne de l'un d'entre eux.
- **2 Services via une API:** Ces services sont également illimités et gratuits, mais leur abus peut entraîner une interdiction temporaire de l'IP pendant quelques heures, après quoi le service sera rétabli.
- Tous ces services de Google ne nécessitent pas de clés API et sont illimités et gratuits.

<h4 id="deepl">DeepL</h4>

**2 Services de DeepL**

- **API Free:** Cette option nécessite l'obtention d'une clé API gratuite sur la page DeepL, qui propose 500 000 caractères par mois.
- **API Pro:** Cette option nécessite également une clé API obtenue sur le site Web de DeepL. Son utilisation est conditionnelle au solde et au forfait souscrit dans le compte DeepL de l'utilisateur.
- Les conditions d’utilisation de l’API de DeepL sont disponibles à partir de sa [page Web](https://www.deepl.com/fr/pro/change-plan#developer), et l'extension est limitée par lesdites conditions.

<h4 id="libretranslate">LibreTranslate</h4>

**1 Service de LibreTranslate**

- Ce service s’améliore constamment grâce à son apprentissage neuronal continu. Même s’il n’atteint pas actuellement la qualité de Google, il est parfaitement utilisable.
- Basé sur la technologie de Argos Translate.
- Pour utiliser ce service, une clé API est requise, qui peut être obtenue en faisant un don à la communauté [NVDA.es (page en espagnol)](https://nvda.es/donaciones/).
  - Après avoir fait un don, vous pouvez demander la clé API en utilisant le formulaire à partir de la [page (en espagnol)](https://nvda.es/contacto/), indiquant dans l'objet "<span lang="es">solicitud de clave API</span>" et en fournissant la référence PayPal, le virement, etc.
- De plus, il est possible de configurer d'autres services de LibreTranslate en ajoutant la clé API et en modifiant l'URL du service dans la section Configuration de l'extension.

<h4 id="microsoft-translate">Microsoft Translate</h4>

**1 Service de Microsoft Translate**

- Ce service a la limitation qu'une utilisation continue peut entraîner une interdiction temporaire de l'adresse IP pendant quelques minutes.
- Cette interdiction n'intervient qu'en cas d'usage très intensif et dans les traductions de textes longs.
- Le service fonctionne très bien, mais il est recommandé de ne pas l'utiliser en continu pour éviter les interruptions.

Ces options permettent aux utilisateurs de choisir entre différents services de traduction, garantissant la disponibilité et la flexibilité de l'extension en fonction des besoins et préférences individuels.

Au fur et à mesure que l'extension reçoit des mises à jour, des services peuvent être ajoutés ou supprimés. Les modifications seront signalées dans la section mises à jour.

[Retour au sommaire](#sommaire)

<h3 id="configuration">2.2 - Configuration</h3>

**Configuration de l'extension**

Cette section explique comment configurer chacun des services disponibles dans l'extension, notamment comment ajouter des clés API, modifier les URL des services et d'autres paramètres nécessaires pour personnaliser l'utilisation de l'extension en fonction des besoins de l'utilisateur.

<h4 id="menu-extension">Menu de l'extension</h4>

Dans NVDA > Préférences > Traducteur Avancé nous avons un menu qui contient les éléments suivants :

- **Configuration de Traducteur Avancé**

  Si nous appuyons sur cette option, la fenêtre de configuration de l'extension s'ouvrira. Cette fenêtre comporte 2 zones :

  - **Général**

    Dans cet onglet les options générales de l'extension seront ajoutées. Actuellement, vous ne disposez que d'une seule case à cocher pour activer ou désactiver le cache de l'extension.

    L'extension peut enregistrer un cache de ces traductions pour chaque application, ce qui rendra la traduction plus facile et plus rapide dans les traductions futures. De plus, il crée désormais un cache pour chaque langue, et il peut y avoir plusieurs applications disposant d'un cache pour différentes langues.

  - **Modules de traduction**

    Dans cet onglet, nous pouvons choisir le service que nous voulons utiliser pour traduire. Dans les services qui nécessitent une clé API, le gestionnaire de clés API sera également affiché.

    Nous pouvons avoir plusieurs clés API pour le même service ; Par exemple, dans LibreTranslate, nous pouvons avoir différentes clés et URL pour nous connecter. Nous pouvons ajouter, modifier, supprimer et définir la clé API par défaut que nous souhaitons pour le service actuel.

    La zone du  gestionnaire des clés API change en fonction du service dont nous disposons. Nous pouvons donner à chaque clé API un nom d'identification pour savoir rapidement à quelle API nous faisons référence. Lorsque nous avons plusieurs clés API pour un service, l'élément qui comporte un astérisque dans la liste sera celui par défaut. Cela peut être modifié avec le bouton "Par défaut", c'est-à-dire que la clé dont nous disposons devient celle définie pour ledit service actuellement en focus.

    Si le service de traduction que nous choisissons ne nécessite pas de clé API, le gestionnaire ne sera pas affiché.

    Ensuite, nous avons les boutons "OK" et "Annuler". Toutes les options ont leur touche de raccourci dont NVDA nous informera.

- **Documentation de l'extension**

  Si nous appuyons sur l'option "Documentation de l'extension" cette documentation s'ouvrira.

- **Invite-moi un café si tu aimes mon travail**

  Si nous appuyons sur cette option, la page PayPal s'ouvrira où se trouve un lien indiquant "Envoyer". Si nous appuyons sur ce lien, il nous demandera de nous connecter à notre compte et et nous laissera sur la page de don.

  Je dirai juste que j'ai bu beaucoup de café en faisant cette extension.

[Retour au sommaire](#sommaire)

<h4 id="touches-ou-gestes-de-commandes-extension">Touches ou gestes de commandes de l'extension</h4>

Dans NVDA > Préférences > Gestes de commandes... > Traducteur Avancé nous avons les touches ou gestes de commandes  suivantes que nous pouvons configurer à notre guise.

Les touches ou gestes de commandes par défaut ne sont pas attribuées afin que l'utilisateur puisse choisir sa meilleure disposition. Ce sont les suivantes :

- **Ouvre la configuration de l'extension**

  Cet accès ouvrira rapidement la configuration de l'extension.

- **Active ou désactive le cache de traduction**

  Cet accès activera ou désactivera le cache sans avoir à entrer dans la configuration.

- **Active ou désactive la traduction simultanée en ligne**

  Cet accès active ou désactive la traduction. C'est l'accès principal qui commencera à traduire au fur et à mesure que nous nous déplacerons avec les flèches du curseur. Si tout est correct, nous entendrons la traduction ; Si nous entendons le texte source, nous devrons consulter le journal NVDA et voir ce qui s'est passé.

- **Changer le module de traduction**

  Cet accès ouvrira une fenêtre avec tous les services de traduction disponibles. Nous pouvons nous déplacer avec les flèches et sélectionner avec "Entrée". Le service que nous sélectionnerons sera celui que nous avons par défaut.

- **Changer la langue cible**

  Cet accès ouvrira une fenêtre avec les langues cibles disponibles dans le service que nous avons sélectionné. Chaque service a des langues et, par exemple, si nous traduisons un texte en russe et que nous voulons l'entendre en anglais, dans ce dialogue, nous devrons sélectionner l'anglais. Nous nous déplaçons dans le dialogue avec les flèches du curseur et "Entrée" pour sélectionner la langue souhaitée.

  Les noms des langues sont obtenus dans notre langue auprès de NVDA, y compris celles prises en charge par NVDA. Pour cette raison, les noms des langues en anglais peuvent apparaître dans la liste, puisque NVDA ne les traduit pas. Le code ISO de la langue est ajouté à côté de chaque nom de la langue.

- **Changer la langue source**

  Identique à la précédente, mais ce dialogue n'est valable que pour le traducteur Microsoft. Le service Microsoft ne vous permet pas de définir la langue source sur auto afin qu'il détecte quelle langue vous est envoyée, nous devrons donc la choisir nous-mêmes.

  Les autres services ne pourront pas utiliser ce dialogue puisque leur option par défaut est de détecter la langue envoyée.

- **Copier le dernier texte traduit dans le Presse-papiers**

  Cet accès copiera le dernier texte traduit dans le presse-papiers.

- **Supprimer le cache de traduction pour l'application actuellement focalisée**

  Si nous appuyons une fois sur cet accès, il nous donnera des informations ; Si nous appuyons dessus deux fois rapidement, cela effacera le cache de l'application qui a actuellement le focus et nous informera du résultat.

- **Supprimer toutes les traductions en cache pour toutes les applications**

  Cet accès, en appuyant une fois, nous donnera des informations ; En appuyant deux fois rapidement, il supprimera tout le cache de l'extension, offrant également des informations.

- **Afficher l'historique de la traduction**

  Il affichera un dialogue avec les 500 dernières traductions dans une liste. Nous pouvons rechercher et réviser le texte source et le texte traduit dans des zones en lecture seule. Ce dialogue nous permettra de rechercher dans tout l'historique, de copier à la fois le texte source et le texte traduit dans le presse-papiers ou les deux.

  Il vous permet également de basculer entre le texte source et le texte traduit et de travailler dans les deux sens. De plus, nous pouvons supprimer tout l’historique pour repartir de zéro.

  J'avertis que l'historique est effacé à chaque redémarrage de NVDA.

- **Traduire le texte sélectionné**

  Cette action traduira le texte que nous avons sélectionné et focalisé. S'il s'agit d'un texte volumineux, un dialogue s'ouvrira avec le pourcentage de la traduction. Ce dialogue peut être annulé, ce qui annulera également la traduction.

  Une fois la traduction terminée, le texte sera affiché dans un dialogue afin que nous puissions l'explorer.

  Cette option utilise le service Google Translate et ce service ne peut pas être modifié, étant choisi en interne puisque c'est celui qui donne les meilleurs résultats pour les textes longs.

[Retour au sommaire](#sommaire)

<h2 id="solution-de-problemes">3 - Solution de problèmes</h2>

<h3 id="problemes-courants-et-solutions">Problèmes courants et solutions</h3>

**Connexion Internet**
- Vérifiez que votre connexion Internet est active et fonctionne correctement.
- Redémarrez votre routeur ou modem si nécessaire.

**Erreurs de certificat**
- Si vous rencontrez des erreurs de certificat, assurez-vous que la date et l'heure de votre système sont correctes.
- Vérifiez que les certificats requis sont installés et mis à jour.

**Problèmes de performance**
- Assurez-vous que votre ordinateur répond à la configuration minimale requise.
- Fermez les autres applications susceptibles de consommer beaucoup de ressources.

[Retour au sommaire](#sommaire)

<h3 id="comment-consulter-le-journal-de-nvda">Comment consulter le journal de NVDA</h3>

1. Ouvrir NVDA.
2. Aller à `NVDA > Outils > Voir le journal`.
3. Dans la fenêtre du journal, recherchez les erreurs ou les messages liés au Traducteur Avancé.

[Retour au sommaire](#sommaire)

<h2 id="remerciements-a">4 - Remerciements à</h2>

Merci à tous les programmeurs NVDA pour leur excellent travail.

Et je ne veux pas manquer de préciser que la source  de cette extension est celle de l'extension (TRANSLATE) de Yannick PLASSIARD, à partir de laquelle j'ai appris et utilisé certaines fonctions.

Également à Alexy Sadovoy alias Lex, Ruslan, Beqa, Mesar Hameed, Alberto Buffolino et d'autres contributeurs de NVDA également pour l'extension (Instant Translate) à partir de laquelle l'une des méthodes de Google a été obtenue et a été modifiée pour l'implémenter dans l'extension Traducteur Avancé.

Cette extension est le fruit de plusieurs années de publication de versions non officielles et d'étude de l'utilisation de traductions hors ligne.

L'apprentissage est le résultat de cette extension, en gardant à l'esprit que à l'avenir apportera de nouvelles fonctionnalités surprenantes.

[Retour au sommaire](#sommaire)

<h3 id="traducteurs">Traducteurs</h3>

- **Portugais:** Ângelo Abrantes.
- **Turc:** Umut Korkmaz.
- **Russe:** Valentin Kupriyanov.
- **Anglais:** Samuel Proulx.
- **Ukrainien:** Heorhii Halas et Volodymyr Pyrih.

[Retour au sommaire](#sommaire)

<h2 id="journal-des-versions">5 - Journal des versions</h2>

Dans cette section, un journal des versions sera ajouté, où les nouvelles fonctionnalités de chaque version seront publiées.

Le manuel est basé sur la première version, il ne sera donc pas mis à jour et servira de base pour l'utilisateur.

Des nouveautés seront ajoutées dans cette section.

[Retour au sommaire](#sommaire)

<h3 id="version-2024-06-06">Version 2024.06.06</h3>

- Version initiale de l'extension.
- Prise en charge de 7 services de traduction.
- Fonctionnalités de base de traduction simultanée et de gestion des clés API.

[Retour au sommaire](#sommaire)

<h3 id="version-2024-06-16">Version 2024.06.16</h3>

- **Ajout de la possibilité de copier la traduction traduite dans le presse-papiers par sélection au lieu de l'afficher dans un dialogue:**

Une option a été ajoutée pour copier automatiquement le texte traduit dans le presse-papiers lorsque cette fonction est sélectionnée, évitant ainsi d'avoir à afficher un dialogue supplémentaire.

Cette option a été ajoutée dans le dialogue de configuration de l'extension dans Général.

Si cette option est cochée, il n'affichera plus le dialogue lorsque l'on traduira un texte sélectionné, mais le copiera directement dans le presse-papiers.

- **Traduire le contenu du presse-papiers:**

Il est désormais possible de traduire directement le contenu situé dans le presse-papiers, offrant ainsi un moyen rapide et efficace de traduire les textes copiés.

Si rien n'est traduit, il nous dira ce qu'il y a dans le presse-papiers ou s'il n'y a rien dans le presse-papiers, il nous en informera avec un message.

- **Traduire la dernière chose verbalisée par le synthétiseur:**

Une fonctionnalité a été incorporée qui vous permet de traduire la dernière phrase ou le dernier texte verbalisé par le synthétiseur vocal, améliorant ainsi l'accessibilité et la convivialité de l'extension.

Si la dernière chose verbalisée ne peut pas être traduite, il nous dira la dernière chose verbalisée dans la langue source.

- **Afficher les traductions sur les afficheurs braille:**

La nouvelle version inclut la prise en charge de l'affichage des traductions sur les afficheurs braille, ce qui facilite l'accès aux traductions.

Cela ne fonctionnera que sur les ordinateurs sur lesquels un afficheur braille est configuré.

Cette fonction est en phase de test.

- **Assistant de mise à jour de la langue de l'extension:**

Un assistant de mise à jour a été implémenté pour maintenir les langues de l'extension toujours à jour, garantissant ainsi la disponibilité des langues les plus récentes et plus précises.

Maintenant dans le menu NVDA > Préférences > Traducteur Avancé

Nous aurons un nouvel élément appelé Mettre à jour les langues de l'extension (Pas de mise à jour).

Cet élément peut nous informer s'il y a des mises à jour, par exemple :

Mettre à jour les langues de l'extension  (3 mises à jour disponibles)

Si nous appuyons dessus, un dialogue apparaîtra avec les nouvelles langues, avec les mises à jour ou avec l'une des deux s'il n'y en a pas dans les deux.

Nous pouvons installer ou ignorer.

Si nous appuyons sur Installer, les langues seront téléchargées et installées et NVDA redémarrera.

L'élément du menu est mis à jour toutes les 30 minutes en vérifiant les mises à jour ou à chaque redémarrage.

La dépense en données de cette vérification est ridicule car pour les endroits qui ont des problèmes de données, c'est moins de 1 Ko que vous devez vérifier.

Cet assistant de mise à jour facilitera le partage des mises à jour linguistiques de l'extension avec les utilisateurs, dès leur arrivée et sans qu'il soit nécessaire de publier une nouvelle version avec les nouvelles langues.

Chaque nouvelle version de l'extension sera accompagnée de toutes les nouvelles langues et mises à jour arrivées.

- **Bug de lecture continue corrigé:**

Correction d'un problème qui provoquait des erreurs de lecture continues, améliorant la stabilité et les performances de l'extension lors d'une utilisation prolongée.

- **Notes de l'auteur:**

Toutes les nouvelles fonctions telles que traduire dans le presse-papier, traduire le dernier texte verbalisé par le synthétiseur ou la vérification des mises à jour linguistiques peuvent se voir attribuer des gestes de commandes.

Je recommande que si nous n'utilisons aucune option, nous n'ajoutons pas de geste de commande afin de pouvoir l'avoir dans d'autres extensions. Ajoutons ceux qui peuvent nous être utiles.

Au fur et à mesure que des utilitaires sont ajoutés, davantage de gestes de commandes seront nécessaires et un utilitaire peut ne pas fonctionner pour l'un ou pour un autre geste de commande, nous attribuons donc uniquement ceux que nous allons utiliser.

[Retour au sommaire](#sommaire)

<h3 id="version-2024-06-23">Version 2024.06.23</h3>

* Ajout d'un nouveau module Traducteur DeepL (Free)

Ce nouveau module n'a pas besoin de clé API et est utilisé pour la traduction simultanée

* Corrections d'erreurs

[Retour au sommaire](#sommaire)

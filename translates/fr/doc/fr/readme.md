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
  - [Version 2024.09.07](#version-2024-09-07)
  - [Version 2024.09.19](#version-2024-09-19)

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

- **Ouvrir la configuration de l'extension**

  Cet accès ouvrira rapidement la configuration de l'extension.

- **Activer ou désactiver le cache de traduction**

  Cet accès activera ou désactivera le cache sans avoir à entrer dans la configuration.

- **Activer ou désactiver la traduction simultanée en ligne**

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

- **Afficher l'historique des traductions**

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
- **Français:** Rémy Ruiz.

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

Cette option a été ajoutée dans le dialogue Configuration de l'extension dans la section Général.

Si cette option est cochée, il n'affichera plus le dialogue lorsque l'on traduira un texte sélectionné, mais le copiera directement dans le presse-papiers.

- **Traduire ce qu'il y a dans le presse-papiers:**

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

<h3 id="version-2024-09-07">Version 2024.09.07</h3>
#### Interface de traduction

**L'Interface de traduction** est le composant principal de l'extension **Traducteur Avancé** pour NVDA. Cette interface permet à l'utilisateur de traduire efficacement du texte entre différentes langues, en affichant le texte source et traduit et en offrant diverses options de personnalisation.

Pour l'invoquer, nous devrons attribuer une combinaison de touches dans le dialogue "Gestes de commandes" ou depuis le menu virtuel (expliqué ci-dessous).

##### Principales caractéristiques:

1. **Introduire du texte source**: Permet à l'utilisateur de taper ou de coller le texte qu'il souhaite traduire. Il est accessible rapidement avec la combinaison de touches `Alt+1`.
   
2. **Texte cible (résultat)**: La zone où le texte traduit est affiché. Ce champ est en lecture seule et peut être focalisé avec `Alt+2`.

3. **Sélection de la langue source**: Permet de sélectionner la langue du texte source. La langue par défaut est l'option "Détection automatique", ce qui permet au système de détecter automatiquement la langue du texte. Accessible avec `Alt+3`.

4. **Sélection de la langue cible**: Vous permet de sélectionner la langue dans laquelle vous souhaitez traduire le texte. Il peut être focalisé avec `Alt+4`.

5. **Compteur de caractères**: Affiche le nombre de caractères dans le champ de texte source. Il est utile de connaître la quantité de texte qui sera traduite. Accessible avec `Alt+5`.

6. **Boutons d'action**:
   - **Traduire**: Démarre la traduction du texte tapé.
   - **Écouter**: Obtient l'audio de la traduction et permet de le lire via un lecteur intégré (voir la section ci-dessous).
   - **Intervertir**: Échange la langue source avec la langue cible, utile si vous souhaitez inverser les langues de traduction.
   - **Effacer**: Efface les champs de texte source et sible.
   - **Coller au focus**: Colle le texte traduit dans la fenêtre active ou le champ de texte derrière l'interface. Il peut également être activé avec `F3`.
   - **Fermer**: Ferme la fenêtre de traduction.

##### Raccourcis clavier:

- `Alt+1`: Focaliser la zone de texte source.
- `Alt+2`: Focaliser la zone de texte cible.
- `Alt+3`: Sélectionner la langue source.
- `Alt+4`: Sélectionner la langue sible.
- `Alt+5`: Focaliser le compteur de caractères.
- `F3`: Coller le texte traduit dans la fenêtre active.
- `Échap`: Fermer le dialogue de traduction.

##### Comportement en cas d'erreurs:

- S'il n'y a pas de connexion Internet, le système affichera un message vous informant de l'absence de connexion.
- Si la zone de texte source est vide, l'utilisateur recevra un avertissement lui demandant d'écrire du texte avant que la traduction ne soit effectuée.
- Si les langues source et cible sont les mêmes, un avertissement s'affichera indiquant que le texte n'a pas besoin d'être traduit dans la même langue.

##### Fonctionnalités supplémentaires:

- **Détection automatique de la langue**: Si la "Détection automatique"  est sélectionnée dans la langue source, l'extension tentera d'identifier automatiquement la langue du texte à traduire.
- **Intervertir  les langues**: Cette fonctionnalité est utile lorsque vous souhaitez traduire en retour un texte dans la langue source.

#### Lecteur audio

Lorsque l'utilisateur utilise l'option **Écouter** Après avoir effectué une traduction, l'extension convertit le texte traduit en fichier audio et le lit via un lecteur intégré. Ce lecteur comprend des commandes de base et avancées pour gérer la lecture audio.

##### Caractéristiques du lecteur:

1. **Boutons de contrôle**:
   - **Reculer (F1)**: Recule la lecture en fonction du temps sélectionnée. L'utilisateur peut configurer cette durée.
   - **Lire/Pause (F2)**: Démarrer ou mettre en pause la lecture du fichier audio.
   - **Avancer (F3)**: Avance la lecture en fonction de la durée définie par l'utilisateur.
   - **Arrêter (F4)**: Arrête complètement la lecture.

2. **Volume et vitesse**:
   - **Volume (F5/F6)**: Ajuste le volume de lecture à l’aide d’un curseur.
   - **Vitesse (F7/F8)**: Modifie la vitesse de lecture, avec des options de 0,50x à 2,0x la vitesse normale.

3. **Texte associé**: Affiche le texte traduit dans une zone en lecture seule, permettant à l'utilisateur de voir ce qui est en cours de lecture.

4. **Enregistrer**: Permet d'enregistrer le fichier audio généré au format WAV sur le système de l'utilisateur.

5. **Fermer**: Ferme le lecteur et libère les ressources associées.

##### Raccourcis clavier:

- `F1`: Reculer la lecture.
- `F2`: Lire ou mettre en pause l'audio.
- `F3`: Avancer la lecture.
- `F4`: Arrêter la lecture.
- `F5/F6`: Ajuster le volume de lecture.
- `F7/F8`: Changer la vitesse de lecture.
- `F9`: Informations sur la durée de lecture.
- `Maj+F10/Applications`: Sur les boutons Reculer et Avancer, un menu contextuel s'affichera pour choisir la durée correspondante.

##### Fonctionnalités supplémentaires:

- **Enregistrer l'audio**: Les utilisateurs peuvent choisir d'enregistrer le fichier audio sur leur appareil au format WAV pour une utilisation ultérieure.
- **Menu d'options avancés**: Le lecteur permet de choisir la durée exacte pour reculer ou avancer la lecture grâce à un menu contextuel (accessible avec la touche `Maj+F10`) ou touche applications.

#### Menu virtuel

Un menu virtuel a été ajouté qui contient toutes les options dont dispose l'extension.

Nous pouvons invoquer depuis le menu virtuel toutes les options que nous pouvons attribuer dans le dialogue "Gestes de commandes", De cette façon, à partir du menu virtuel, l'extension peut être utilisée complètement sans avoir à attribuer davantage de touches à l'extension.

Ce qui reste au goût de l'utilisateur.

Pour appeler le menu virtuel, nous devrons lui attribuer une touche dans le dialogue "Gestes de commandes".

L'utilisation du menu virtuel est simple, une fois invoqué, nous devrons appuyer sur la touche correspondante à l'action que nous voulons exécuter.

Une fois appuyé, il sera exécuté et nous serons toujours informés de ce qui a été fait. Si nous appuyons sur une touche qui n'est pas attribuée, le menu virtuel se fermera et nous pourrons également le fermer avec Échap.

##### Raccourcis clavier du menu virtuel

Le menu virtuel de Traducteur Avancé vous permet d'accéder rapidement aux fonctions les plus utiles de l'extension. Vous trouverez ci-dessous les raccourcis que vous pouvez utiliser pour effectuer diverses actions :

- **`P`**: **Ouvrir la configuration de l'extension**  
  Ouvre la configuration de Traducteur Avancé où vous pouvez ajuster les langues et les services de traduction.

- **`U`**: **Vérifier les mises à jour linguistiques de l'extension**  
  Recherche et télécharge les mises à jour disponibles pour les langues de l'extension.

- **`O`**: **Changer la langue source du traducteur**  
  Change la langue du texte que vous souhaitez traduire (langue source).

- **`D`**: **Changer la langue cible du traducteur**  
  Change la langue dans laquelle vous souhaitez traduire le texte (langue cible).

- **`C`**: **Changer le module de traduction**  
  Vous permet de basculer entre les services de traduction disponibles, tels que Google, DeepL, Microsoft, entre autres.

- **`A`**: **Supprimer toutes les traductions en cache pour toutes les applications*  
  Efface toutes les traductions stockées en cache.

- **`X`**: **Supprimer le cache de traduction pour l'application actuellement focalisée**  
  Efface les traductions en cache uniquement pour l'application que vous avez ouverte.

- **`G`**: **Activer ou désactiver le cache de traduction selon l'état actuel**  
  Active ou désactive la fonction de cache qui enregistre temporairement les traductions.

- **`L`**: **Copier le dernier texte traduit dans le Presse-papiers s'il n'y a pas de traduction en cours**  
  Copie la dernière traduction réalisée dans le presse-papiers pour pouvoir la coller là où vous en avez besoin.

- **`B`**: **Traduire le contenu du presse-papiers**  
  Traduit le contenu actuel du presse-papiers.

- **`V`**: **Traduire le dernier texte verbalisé**  
  Traduit le dernier texte lu par NVDA à haute voix.

- **`T`**: **Activer ou désactiver la traduction simultanée en ligne**  
  Active ou désactive la traduction automatique lors de la navigation dans les textes.

- **`S`**: **Traduire le texte sélectionné**  
  Traduit le texte que vous avez sélectionné dans l'application.

- **`Z`**: **Traduire le texte de l'objet navigateur**  
  Traduit le texte d'un objet spécifique dans le navigateur, tel qu'un bouton ou une zone de texte.

- **`W`**: **Interface de traduction**  
  Ouvre la fenêtre graphique où vous pouvez introduire manuellement le texte que vous souhaitez traduire.

- **`I`**: **Détecter la langue sélectionnée**  
  Détecte automatiquement la langue du texte sélectionné.

- **`J`**: **Activer ou désactiver l'alternance automatique si la source détectée correspond à la sible**  
  Active ou désactive l'alternance automatique si la langue source détectée correspond à la langue cible.

- **`K`**: **Intervertir la langue principale avec la langue alternative**  
  Échange la langue principale avec la langue alternative dans la configuration du traducteur.

- **`H`**: **Afficher l'historique des traductions**  
  Affiche un historique des traductions récentes effectuées.

- **`F1`**: **Afficher un dialogue avec la liste des commandes d'une seule touche**  
  Affiche un dialogue avec la liste des commandes d'une seule touche pour le Traducteur Avancé.

#### Détecter la langue sélectionnée

Cette option vous permet de détecter automatiquement la langue du texte que vous avez sélectionné dans n'importe quelle application :
1. Sélectionnez le texte dont vous souhaitez connaître la langue.
2. Utiliser le raccourci clavier configuré dans le dialogue "Gestes de commandes" (ou le menu virtuel) pour activer l'option "Détecter la langue sélectionnée".
3. Le système détectera et vous informera de la langue dans laquelle le texte sélectionné est rédigé.
Cette fonctionnalité est utile lorsque vous n'êtes pas sûr de la langue d'un texte et que vous devez la connaître avant de le traduire ou d'effectuer toute autre action.

#### Alternance automatique des langues dans le Traducteur Avancé pour NVDA

  1. Activez l'alternance automatique en appuyant sur le raccourci clavier correspondant ou en accédant à partir du menu virtuel.
  2. Si le texte que vous sélectionnez est dans la même langue que la langue cible, le système changera automatiquement la langue cible en langue alternative pour éviter des traductions inutiles.
  3. Vous pouvez désactiver cette option à tout moment en utilisant le même raccourci.

##### Configuration des langues dans l'extension

- Vous pouvez configurer les **langues cible** et les **langues alternatives** en accédant à la **Configuration de l'extension** dans la section **Général**. De là, vous pourrez sélectionner les langues qui seront utilisées pour l'alternance  automatique.

Cette fonctionnalité est utile pour éviter toute confusion lors de la traduction de textes dont la langue source est la même que la langue cible, en passant automatiquement à une langue alternative configurée.

#### Aide dans les Dialogues de l'extension

Ajout d'une fonctionnalité pour afficher une aide contextuelle dans les dialogues de l'extension. Appuyer sur la combinaison de touches `Ctrl+H`, une petite description de la fonction du widget actuellement focalisé sera affichée.

N'importe où dans les dialogues de l'extension, si vous avez besoin d'informations sur la fonction d'un bouton, d'une zone de texte, d'un curseur ou d'un autre contrôle, vous pouvez simplement appuyer sur `Ctrl+H`. Cela affichera une brève description du widget focalisé, fournissant un guide rapide sur son utilisation.

#### Traduire le texte de l'objet navigateur

Cette fonctionnalité vous permet de traduire le texte d'un objet spécifique dans le navigateur ou dans toute autre application utilisée par NVDA. Il peut être activé via le menu virtuel ou via une combinaison de touches attribuée dans  le dialogue "Gestes de commandes" de l'extension.

1. Placez le curseur sur l'objet que vous souhaitez traduire (cela peut être un bouton, une zone de texte, etc.
2. Activez la fonctionnalité en appuyant sur la combinaison de touches attribuée ou via le menu virtuel.
3. L'extension traduira le texte contenu dans cet objet et l'affichera ou le verbalisera, selon la configuration.

- Traduit tout texte contenu dans l'objet sélectionné dans une page Web, une application ou toute autre interface avec laquelle NVDA interagit.
- Utile pour traduire de petits morceaux de texte qui ne font pas partie du corps principal d'une page ou d'une application, tels que des menus, des boutons ou des étiquettes.
- Si l'objet ne contient pas de texte ou est inaccessible, l'extension affichera un message informant qu'il n'y a pas de texte à traduire.

- Vous pouvez accéder à cette fonctionnalité à la fois depuis le menu virtuel de l'extension et en configurant un raccourci clavier dans le dialogue "Gestes de commandes" de NVDA.

#### Module d'OpenAI

Un nouveau module a été ajouté pour traduire avec OpenAI avec le modèle chatGPT-4º-mini, qui est le moins cher et le plus rapide.

Ce module est en test, connaissant parfois un peu de décalage (lag), mais il s'améliorera dans les prochaines versions.

Ce module nécessite qu'une clé API soit attribuée dans le dialogue "Configuration de l'extension" dans l'onglet "Modules de traduction".

OpenAI est payant, c'est donc à l'utilisateur de vérifier ses frais.

Dans le lien suivant, vous pouvez voir les frais que nous avons :

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Amélioration du module Microsoft

Le module de traduction Microsoft a été écrit à partir de zéro et a amélioré la vitesse, la stabilité et la possibilité d'avoir plus de temps de traduction jusqu'à ce qu'il se bloque en raison de son utilisation et que nous devions attendre quelques minutes pour traduire à nouveau.

Maintenant, dans les tests effectués et en traduisant simultanément beaucoup de texte plus que l'utilisation normale, je n'ai subi aucune restriction.

Donc pour le moment il fonctionne et a été amélioré par rapport au module précédent.

#### Autres

* Correction d'un problème avec la verbalisation de certains messages.
* Modification de la façon de vérifier s'il y a Internet.
* Corrections d'erreurs.
* Langue française officiellement ajoutée.

[Retour au sommaire](#sommaire)

<h3 id="version-2024-09-19">Version 2024.09.19</h3>

* Correction du retour de langues en configuration.

Maintenant toujours retournera les langues de code ISO 639-1 dans la fonction obtenerLenguaje du manager de configuration.

* Résolu [Issue #13](https://github.com/hxebolax/TranslateAdvanced/issues/13)

Importation de module html : Ajout d'importation html pour utiliser la fonction html.unescape(), qui supprime toutes les entités HTML, y compris les entités numériques comme (').

Suppression de code inutile : Les méthodes _load_html_entities et unescape ont été supprimées, car html.unescape() est désormais utilisé dans les modules Google web.

[Retour au sommaire](#sommaire)

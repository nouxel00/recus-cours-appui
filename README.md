# Reçus – Cours d'appui 1re année

Logiciel pour générer les reçus de paiement des étudiants inscrits aux cours d'appui
(Électricité générale, Mathématiques, Électronique numérique, Thermodynamique).

**Il fonctionne sans connexion internet.** Toutes les données restent sur l'appareil.

## Ce que fait le logiciel

- Saisie du **nom**, du ou des **prénoms** et de la **classe** (1ATC/A, 1ATC/B, 1ATC/C)
- Reçu numéroté automatiquement (N° 0001, 0002…), avec la date, le montant payé
  (10 000 FCFA, en chiffres et en lettres), le paiement Orange Money,
  les matières et le **lien du groupe WhatsApp avec son code QR**
- **Total d'argent encaissé**, total du jour et répartition par classe
- Reçu à télécharger en image (à envoyer sur WhatsApp), à imprimer ou à enregistrer en PDF
- Liste des inscrits avec recherche, filtre par classe et export Excel
- Alerte si un étudiant a déjà un reçu (pour éviter les doublons)
- Sauvegarde et restauration des données

## Installation

### Sur ordinateur (le plus simple)

1. Cliquez sur le bouton vert **Code** en haut de cette page, puis **Download ZIP**.
2. Décompressez le fichier ZIP.
3. Ouvrez **`index.html`** avec **Google Chrome** (double-clic ou clic droit → Ouvrir avec → Chrome).
4. Ajoutez la page à vos favoris pour la retrouver facilement.

Utilisez toujours le **même fichier**, dans le **même navigateur**, pour retrouver vos reçus.

### Sur téléphone

1. Avec une connexion internet, ouvrez dans Chrome :
   **https://nouxel00.github.io/recus-cours-appui/**
2. Menu ⋮ → **Ajouter à l'écran d'accueil** (ou **Installer l'application**).
3. L'application s'ouvre ensuite depuis l'écran d'accueil, **même sans internet**.

## Première utilisation

Ouvrez l'onglet **Paramètres** et collez le **lien du groupe WhatsApp**
(dans WhatsApp : ouvrez le groupe → nom du groupe → *Inviter via un lien* → *Copier le lien*).
Le montant, le numéro Orange Money et le nom du responsable peuvent aussi être modifiés à cet endroit.

## Sauvegardez régulièrement

Les reçus sont enregistrés dans le navigateur. Si l'historique du navigateur est effacé, ils sont perdus.
Dans **Paramètres → Télécharger une sauvegarde**, enregistrez le fichier obtenu sur une clé USB ou sur Google Drive.
**Restaurer une sauvegarde** permet de tout récupérer, y compris sur un autre appareil.

---

Le dossier `src/` contient le code source (`python3 src/build.py` reconstruit `index.html`).
Code QR : bibliothèque *qrcode-generator* © Kazuhiko Arase, licence MIT.

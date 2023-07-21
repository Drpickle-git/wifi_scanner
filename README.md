
# Wifi_Scanner

Wifi_Scanner est un outil simple de balayage du réseau local pour trouver les adresses IP des appareils connectés.

## Fonctionnalités

- Scan du sous-réseau 192.168.1.x pour trouver les appareils connectés.
- Affiche les adresses IP des appareils trouvés ainsi que leurs noms d'hôte (lorsque disponibles).

## Comment utiliser

1. Assurez-vous d'avoir Python installé sur votre système.
2. Téléchargez le code source de Wifi_Scanner depuis ce dépôt GitHub.

   ```
   git clone <lien-du-dépôt>
   ```

3. Ouvrez un terminal ou une invite de commandes et accédez au répertoire du projet.

   ```
   cd Wifi_Scanner
   ```

4. Exécutez le script en tapant la commande suivante :

   ```
   python wifi_scanner.py
   ```

5. Le script commencera à scanner les adresses IP du sous-réseau et affichera les résultats.

## Exigences

- Python 3.x

## Remarques

- Si certains appareils n'ont pas de nom d'hôte configuré ou ne répondent pas aux requêtes, leur nom ne sera pas affiché dans les résultats du scan.
- Assurez-vous d'être connecté au réseau local que vous souhaitez scanner.

## Avertissement

Ce script est fourni tel quel, sans garantie d'aucune sorte. L'auteur n'est pas responsable de tout dommage potentiel causé par l'utilisation de ce script. Utilisez-le à vos propres risques.

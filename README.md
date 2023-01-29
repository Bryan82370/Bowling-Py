# Projet_bowling
## Etatpe à suivre
- Installer Ubuntu sur une VM

- Installer java :
    - sudo apt install default-jre

- Installer Bambo et suivre guide https://confluence.atlassian.com/bamboo/installing-bamboo-on-linux-289276792.html

- Lancer bamboo avec la commande ./bin/start-bamboo.sh

- Lancer le site: http://localhost:8085 et suivre les indications

- S'incrire sur Atlassian
- Générer une licence: https://my.atlassian.com/products
    - Sélectionner new licence + bamboo
    - Orga: Bamboo
    - Server ID: celui de http://localhost:8085
    
- Ajouter le lien github dans Parametre -> Linked Repository
- Activer bambbo specs
   
 - Créer un nouveau projet
    - Sélectionner le projet git
    - Generer un access token https://github.com/settings/tokens?type=beta
    - Sauvegarder
    
  - Aller dans l'onglet Spec 
    - Générer la spécification trouvé sur github
    
  - Aller voir le build

- Configurer git:
    - git config user.email "MY_NAME@example.com"
    - git config user.name "FIRST_NAME LAST_NAME"

- Cloner le projet: https://github.com/sabrinacathalo/Projet_bowling

# TCbot

## Présentation
Bot qui check l'etat du ssh et du rdp des pc du depart TC a l'INSA de Lyon.
Utilisation du script de WGW101 [disponible ici](https://github.com/WGW101/tc_pc_scan) pour le scan des pcs

## Lancement du projet

Le projet est fourni avec un Dockfile. Il faut donc build l'image puis la run. POur ce faire :

 - Clone du projet :  
  `git clone --recursive https://github.com/titouan-joseph/TCbot`
 
 - Racine du projet :  
 `cd TCbot`

 - Build :  
 `docker build --tag tcbot .`
 
 - Lancer le container :  
 `docker run -itd --env BOT_TOKEN={TOKEN_FROM_DISCORD} --name container_tcbot tcbot`

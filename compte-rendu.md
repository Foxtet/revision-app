# Compte Rendu

## Partie 0 —  Mise en place du projet fil rouge

### Question 1

#### Pourquoi utilise-t-on gunicorn en production plutôt que le serveur intégré de Flask (app.run()) ? <!-- rumdl-disable-line MD013 -->

Le serveur intégré flask ne sert que de développement.
En production il faut utiliser un serveur comme gunicorn.

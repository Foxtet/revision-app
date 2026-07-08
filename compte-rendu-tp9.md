# Compte Rendu

## Partie 0 — Reprise du TP 8 & accès au projet GCP

### Question 1

#### Pourquoi choisit-on une région comme europe-west1 plutôt qu'une région américaine pour un service destiné à des utilisateurs européens ? <!-- rumdl-disable-line MD013 -->

La zone permet de se conformer aux normes du pays (RGPD).

## Partie 1 - Construire et publier l'image sur Artifact Registry <!-- rumdl-disable-line MD013 -->

### Question 2

#### À quoi sert Artifact Registry dans le cycle de déploiement, et pourquoi ne déploie-t-on pas le code source « tel quel » sur Cloud Run ? <!-- rumdl-disable-line MD013 -->

Un Artifact Registry au niveau de GCP permet de stocker un son image Docker.

De cette manière, l'image est enregistrée sous un tag prédictible, et on peut
toujours servir le même conteneur sans avoir de modifications dessus.

## Partie 2 — Premier déploiement sur Cloud Run (déployer l'image)

### Question 3

#### Quelle différence entre déployer avec --image (une image déjà construite) et avec --source . (Cloud Build reconstruit) ? Lequel respecte la chaîne d'usine logicielle et pourquoi ? <!-- rumdl-disable-line MD013 -->

Selon [Medium](https://medium.com/google-developer-experts/this-is-cloud-run-nine-ways-to-deploy-and-when-to-use-each-72661f7bb6db),
l'argument `--source` permet de pousser un répertoire zippé ou non, et Google
Cloud Run s'occupe de build l'image, ce qui peut être utile pour du test, mais
ce n'est pas pertinent pour la prod car pas immuable.

## Partie 3 — Nouvelle version : la CI publie l'image, on redéploie

### Question 4

#### Chaque déploiement crée une nouvelle révision Cloud Run. Qu'est-ce qu'une révision, et qu'advient-il de l'ancienne après un déploiement réussi ? <!-- rumdl-disable-line MD013 -->

L'ancienne reste dans la liste des révisions mais n'est plus active, cela
permet de faire un rollback.

## Partie 4 — Révisions, répartition du trafic & rollback

### Question 5

#### Votre v1.1.0 est en production et un bug critique apparaît. Décrivez comment revenir à la v1.0.0 en quelques secondes, et pourquoi c'est possible sans reconstruire d'image. <!-- rumdl-disable-line MD013 -->

La commande `gcloud deploy targets rollback` permet d'effectuer un rollback
sans avoir à reconstruire l'image.

## Partie 5 — Configuration : variables d'environnement & secrets

### Question 6

#### Pourquoi injecter une clé d'API via Secret Manager (--set-secrets) plutôt que de l'écrire dans le Dockerfile ou dans le code ? <!-- rumdl-disable-line MD013 -->

Injecter la clé via le param `--set-secret` permet de passer la clé en variable
d'environnement de manière sécurisé, en passant par le Secret Store de GCP.

L'écrire dans le code serait une faille de sécurité.

## Partie 6 — Déploiement continu : sur main, CI verte (WIF)

### Question 7

#### Quel est l'avantage de la Workload Identity Federation par rapport à une clé JSON de service account stockée dans un GitHub Secret ? <!-- rumdl-disable-line MD013 -->

Selon l'article de [Dev.to](https://dev.to/mukesh1811/stop-using-json-keys-secure-your-github-actions-with-workload-identity-federation-49h6),
Les JSON Keys sont de nature statique, elles ne sont pas automatiquement
révoquées, sont physiquement copiables et n'ont pas de rotaiton automatique
du secret, ce qui crée un risque de compromission et d'oubli.

Avec le protocole OIDC, GitHub et GCP peuvent communiquer facilement
via des Tokens OIDC contenant un JWT qui vit sur une courte période.

Cela permet d'avoir un accès sur le moment et pas réutilisable.

### Question 8

#### Dans un pipeline CD, on utilise souvent needs: quality et if: github.ref == 'refs/heads/main' sur le job de déploiement. Que garantit chacune de ces deux conditions, et pourquoi les combiner ? <!-- rumdl-disable-line MD013 -->

`needs: quality` permet d'assurer la qualité du code via un job défini qui
s'assure de ces paramètres.
Le `github.ref = refs/heads/main` permet de cibler la branche principale à son
dernier commit, afin de déclencher un job sur la production.

Cela permet de s'assurer de la qualité du code lors d'un merge sur la branche
principale.

## Partie 7 — Observabilité, IaC (rappel TP 8) & recherche autonome

### Question 9

#### Le « démarrage à froid » (cold start) désigne la latence quand Cloud Run doit démarrer une instance après un passage à zéro. Quel réglage permet de l'atténuer, et quel est son compromis ? Citez votre source. <!-- rumdl-disable-line MD013 -->

Selon l'article de [Medium](https://medium.com/google-cloud/3-solutions-to-mitigate-the-cold-starts-on-cloud-run-8c60f0ae7894),
il est possible de paramétrer l'instance pour avoir un nombre de containers
scalé à 1 minimum via le paramètre `--min-instances`.
Le souci est qu'on a toujours une instance qui tourne, même si non-utilisée.

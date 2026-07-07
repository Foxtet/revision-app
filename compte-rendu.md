# Compte Rendu

## Partie 0 —  Mise en place du projet fil rouge

### Question 1

#### Pourquoi utilise-t-on gunicorn en production plutôt que le serveur intégré de Flask (app.run()) ? <!-- rumdl-disable-line MD013 -->

Le serveur intégré flask ne sert que de développement.
En production il faut utiliser un serveur comme gunicorn.

## Partie 1 — Révision Git & collaboration

### Question 2

#### Quelle est la différence entre un merge --no-ff et un merge fast-forward ? Pourquoi préfère-t-on --no-ff pour intégrer une branche de fonctionnalité ? <!-- rumdl-disable-line MD013 -->

Le mode fast-foward permet d'effectuer un PR/MR sans créer un commit de merge.

C'est utile lorsque la branche n'a pas divergé de la branche sur laquelle elle
se base.

Une branche de feature peut prendre du temps et la branche main peut en attendant
recevoir d'autres branches de features, il faut alors gérer le merge
correctement.

### Question 3

#### Selon le Semantic Versioning (MAJOR.MINOR.PATCH), quel numéro incrémenter dans chacun de ces cas : (a) correction d'un bug, (b) ajout d'une route sans casser l'existant, (c) changement du format de réponse JSON ? <!-- rumdl-disable-line MD013 -->

A: PATCH (0.0.1)
Un fix est de nature un patch du code existant.

B: MINOR (0.1.0)
Si une route est ajoutée, elle ne modifie pas le code existant.

C: MAJOR (1.0.0)
Si la réponse passe au JSON, alors les utilisatueurs de l'application seront
impactés, ce qui est un Breaking Change.

## Partie 2 — Révision Intégration Continue (CI)

### Question 4

#### Pourquoi place-t-on les étapes de formatage et de lint avant les tests dans le pipeline ? Comment appelle-t-on ce principe ? <!-- rumdl-disable-line MD013 -->

Le formattage et le lint permettent de corriger un code qui aurait été rejetté
par les tests, c'est ce qu'on appelle une approche Shift-Left ou la correction
arrive le plus tôt possible.

### Question 5

#### Que fait l'option --cov-fail-under=80 de pytest, et quel est l'intérêt d'un tel seuil dans la CI ? <!-- rumdl-disable-line MD013 -->

Pytest effectue des tests sur toutes les fonctions python.
Le paramètre impose la règle que si l'ensemble des test
combinés donnent un résultat de moins de 80% de réussite, alors le test est
échoué.

## Partie 3 — Révision Qualité & Sécurité

### Question 6

#### Distinguez en une phrase chacun de ces 4 outils : un formatter (black), un linter (ruff), un outil de SAST (bandit) et un outil de SCA (pip-audit). <!-- rumdl-disable-line MD013 -->

**formatter**:

Un Formatter va détecter les erreurs via un mécanisme de Lint, et les corriger
selon des règles définies.

**Lint**:

Un Linter remonte les erreurs sans les corriger.

**SAST**:

Un SAST permet d'analyser le code source qu'on lui fournit afin d'y détecter
des vulnérabilités de sécurité.

**SCA**:

Le SCA vient scanner les librairies associées aux dépendances utilisées par le
code et essaie de trouver des vulnérabilités associées.

### Question 7

#### Un secret (clé API) a été commité par erreur puis poussé. Quelles sont les étapes correctes pour réagir ? <!-- rumdl-disable-line MD013 -->

Quand un secret est poussé sur un dépôt distant, un moyen de résoudre le
problème est d'effectuer un `git reset` sur le commit d'avant.

Un `git revert` serait plus pratique pour conserver l'historique, mais sur ce
genre de failles c'est le seul moyen de nettoyer l'historique des traces.

## Partie 4 — Révision Livraison Continue & artefacts

### Question 8

#### On dit qu'un artefact doit être « construit une seule fois, déployé partout » (build once, deploy everywhere). Pourquoi ne faut-il pas reconstruire l'image entre staging et production ? <!-- rumdl-disable-line MD013 -->

Le staging doit représenter l'environnement de production, et donc l'image doit
être identique. Il est possible de surcharger les environnements via d'autres
métodes comme les variables d'environnements.

### Question 9

#### Pourquoi ne faut-il jamais déployer le tag :latest en production ? <!-- rumdl-disable-line MD013 -->

Le tag `:latest` est comme `HEAD`, il représente l'état le plus actuel de
l'image docker, se baser sur un tag latest c'est prendre le risque de casser la
production à cause d'un changement non prévu.

## Partie 5 — Révision Documentation

### Question 10

#### Citez 3 avantages concrets de la « Documentation as Code » (documentation versionnée avec le code). <!-- rumdl-disable-line MD013 -->

La documentation as code apporte les avantages suivants:

1. Proche du code, la documentation peut parser le code source et le documenter
  automatiquement, ce qui permet d'avoir une documentation qui ne périme pas ou
  peu
2. Si elle est versionnée, alors il est possible de consulter la documentation
  de l'ancienne documentation pour tracer les changements effectuées
3. La documentation automatique n'a pas à être faite manuellement, cela permet
  d'avoir tous les avantages de la documentation
  sans avoir à l'écrire.

## Partie 6 — Ouverture au cloud : Infrastructure as Code

### Question 11

#### Qu'apporte l'Infrastructure as Code (Terraform) par rapport à la création manuelle des ressources dans la console web du fournisseur cloud ? <!-- rumdl-disable-line MD013 -->

L'IaC permet de décrire une infrastructure reproductible, elle décrit les
ressources que l'on souhaite créer et en conserve un état. De cette manière, si
la ressource est détruite, elle est décrite dans le code, ce qui permet de la
recréer à l'identique.

C'est la philosophie du Pet et Cattle, l'IaC favorise le Cattle.

## Partie 7 — Ouverture au cloud : Kubernetes & GitOps

### Question 12

#### Cloud Run et Kubernetes déploient tous deux des conteneurs. Dans quels cas choisir l'un plutôt que l'autre ? <!-- rumdl-disable-line MD013 -->

Cloud Run est plus adapté si on a besoin d'instancier une quantité petite à
moyenne de conteneurs qui n'ont besoin que d'être servi.

Kubernetes devient intéressant (managé ou selfhosté) à partir du moment ou on
on a besoin de beaucoup plus de possibilités, que ça soit de la gestion réseau, RBAC ou autres.

### Question 13

#### Qu'est-ce que le GitOps et quel est son principal intérêt <!-- rumdl-disable-line MD013 -->

Le GitOps est une philosophie où on part du principe que les dépôts Git sont la
source de vérité absolue.

Un outil comme ArgoCD s'occupera alors de faire de la sync et de l'auto-heal en
comparant les objets Kubernetes actuels avec ce que dit le dépôt Git, et
fera de son mieux pour raccorder l'état avec Git.

## Partie 8 — Quiz de synthèse & recherche autonome

### Question 14

#### Présentez le service de conteneurs managés du fournisseur choisi : nom, principe, 2 points communs et 2 différences avec Cloud Run. Indiquez la source (lien de la doc consultée). <!-- rumdl-disable-line MD013 -->

Le service de conteneurs managés de Google Cloud est Google Kubernetes Engine
(GKE).

Il s'agit d'un service managé mettant a disposition un cluster Kubernetes sans
avoir à gérer entièrement l'infrastructure de ce dernier.

**Points communs avec Cloud Run :**

Les deux services permettent de déployer et d'exécuter des applications
conteneurisées.

Les deux prennent en charge la montée en charge automatique afin d'adapter les
ressources aux besoins de l'application.

Différences avec Cloud Run :

GKE offre un contrôle complet sur l'orchestration des conteneurs, tandis que
Cloud Run masque cette complexité et ne nécessite pas de gérer un cluster
Kubernetes.

Cloud Run peut réduire automatiquement le nombre d'instances jusqu'à zéro
lorsqu'il n'y a plus de trafic, alors que GKE repose sur un cluster Kubernetes
dont les nœuds restent généralement actifs, même si les applications ne
reçoivent pas de requêtes.

Sources:

[GKE et Cloud Run | Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run?hl=fr)
[Choosing Between GKE and Cloud Run | by Paul Durivage](https://medium.com/google-cloud/choosing-between-gke-and-cloud-run-46f57b87035c)

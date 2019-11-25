# CS Emmental

## Prérequis (sur Linux)

*  Vérifier l'installation de docker-compose, sinon installer: `docker-compose --version`
*  Vérifier l'installation de make, sinon installer: `make --version`

## Lancer la plateforme en local

*  [Télécharger](https://drive.google.com/open?id=1rX1tePughA2alUDQ74jRkjONKfvRIqv4) et copier à la racine les volumes locaux de mongodb
*  Lancer l'application: `make run`
*  Aller sur la [page d'accueil](http://localhost:8080/) de l'application

NB: Lors de la première installation, il est prudent de lancer `pipenv install` dans le dossier back et `npm install && npm run serve` dans le dossier front

## Développement

*  Le hot reload est activé sur les docker back et front
*  Pour voir les logs, utiliser la commande: `docker logs <docker_name> -f`
*  Pour insérer des données dans mongodb: 
    `docker exec -it <mongo_docker_name> mongo`
    `use cs-emmental`
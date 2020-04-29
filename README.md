# cours-python

## Commande Docker

```docker run -ti container```  --> pour créer et lancer le conteneur Docker (-ti = lancer le terminal et le laisser ouvert)

Dans mon cas, je prends l'image ubuntu donc ```docker run -ti ubuntu```. Docker va télécharger image ubuntu. On remarque aussi lorsqu'on lance deux fois la commande, ca va créer un nouveau conteneur

```docker ps -a```  --> voir les différents conteneurs

```docker pull container```  --> récupérer une image dans le docker

```docker rm id_container```  --> supprimer le conteneur

```docker start -a -i id_conteneur```  --> pour démarrer le conteneur

Pour savoir si le docker est bien up, lancer votre conteneur avec start. Ouvrez un autre terminal et lancer la commande
```docker ps```.  Vous allez voir la liste des conteneurs qui sont start

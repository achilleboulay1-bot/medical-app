# Application de Gestion Médicale

Application Flask pour la gestion de cabinet médical/kinésithérapie.

## Installation

1. **Installer les dépendances Python** :
```bash
pip install -r requirements.txt
```

2. **Créer un fichier `.env`** (optionnel, pour la production) :
```env
SECRET_KEY=votre-cle-secrete-ici
DATABASE_URL=sqlite:///medical_practice.db
ENCRYPTION_KEY=votre-cle-encryption-ici
```

## Lancement de l'application

### Option 1 : Exécuter directement le fichier Python
```bash
python "app.py1/App.py 1"
```

### Option 2 : Utiliser Flask (recommandé)
```bash
export FLASK_APP="app.py1/App.py 1"
flask run
```

Ou en mode debug :
```bash
export FLASK_APP="app.py1/App.py 1"
export FLASK_DEBUG=1
flask run
```

## Accès à l'application

Une fois lancée, l'application sera accessible à l'adresse :
- **http://127.0.0.1:5000** ou **http://localhost:5000**

## Première utilisation

1. Créez un compte utilisateur via la page d'inscription
2. Connectez-vous avec vos identifiants
3. La base de données sera créée automatiquement au premier lancement

## Note

Le fichier source se trouve dans `app.py1/App.py 1`. Pour faciliter l'utilisation, vous pouvez le renommer en `app.py` à la racine du projet.



# Guide de déploiement - Mettre le site en ligne

## Option 1 : Render (Recommandé - Gratuit pour commencer)

### Étapes :

1. **Créer un compte sur Render**
   - Allez sur https://render.com
   - Créez un compte gratuit (avec GitHub, Google, ou email)

2. **Préparer votre code sur GitHub**
   - Créez un compte GitHub si vous n'en avez pas : https://github.com
   - Installez Git sur votre Mac si ce n'est pas fait :
     ```bash
     # Vérifier si Git est installé
     git --version
     ```
   - Dans le terminal, allez dans votre dossier :
     ```bash
     cd "/Users/achille/Medecin:kiné..."
     ```
   - Initialisez Git et créez un dépôt :
     ```bash
     git init
     git add .
     git commit -m "Premier commit"
     ```
   - Créez un nouveau dépôt sur GitHub (sur github.com, cliquez sur "New repository")
   - Connectez votre code local à GitHub :
     ```bash
     git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git
     git branch -M main
     git push -u origin main
     ```
     (Remplacez VOTRE_USERNAME et VOTRE_REPO par vos valeurs)

3. **Déployer sur Render**
   - Sur Render, cliquez sur "New +" → "Web Service"
   - Connectez votre dépôt GitHub
   - Sélectionnez votre dépôt
   - Configurez :
     - **Name** : medical-app (ou le nom que vous voulez)
     - **Environment** : Python 3
     - **Build Command** : `pip install -r requirements.txt`
     - **Start Command** : `gunicorn app:app`
   - Cliquez sur "Create Web Service"
   - Render va construire et déployer votre site (5-10 minutes)

4. **Configurer les variables d'environnement**
   - Dans Render, allez dans "Environment"
   - Ajoutez ces variables :
     - `SECRET_KEY` : Générez une clé secrète (vous pouvez utiliser : `python3 -c "import secrets; print(secrets.token_hex(32))"`)
     - `ENCRYPTION_KEY` : Générez une autre clé (même commande)
     - `DATABASE_URL` : Render créera automatiquement une base de données PostgreSQL, utilisez cette URL

5. **Votre site est en ligne !**
   - Render vous donnera une URL comme : `https://votre-app.onrender.com`
   - Partagez cette URL avec qui vous voulez !

---

## Option 2 : Railway (Alternative gratuite)

1. Allez sur https://railway.app
2. Créez un compte avec GitHub
3. Cliquez sur "New Project" → "Deploy from GitHub repo"
4. Sélectionnez votre dépôt
5. Railway détectera automatiquement Python et déploiera
6. Ajoutez les variables d'environnement dans "Variables"
7. Votre site sera disponible sur une URL Railway

---

## Option 3 : Fly.io (Gratuit avec limites)

1. Installez Fly CLI : https://fly.io/docs/getting-started/installing-flyctl/
2. Créez un compte : `fly auth signup`
3. Dans votre dossier : `fly launch`
4. Suivez les instructions
5. Déployez : `fly deploy`

---

## Variables d'environnement importantes

Pour la production, vous devez définir :
- `SECRET_KEY` : Clé secrète pour les sessions (générez-en une unique)
- `ENCRYPTION_KEY` : Clé pour chiffrer les données sensibles
- `DATABASE_URL` : URL de la base de données (fournie par l'hébergeur)

---

## Notes importantes

⚠️ **Sécurité** :
- Ne partagez JAMAIS vos clés secrètes
- Utilisez HTTPS (généralement fourni automatiquement)
- Changez les mots de passe par défaut

💡 **Conseil** : Commencez par Render, c'est le plus simple et gratuit pour tester.

---

## Besoin d'aide ?

Si vous rencontrez des problèmes :
1. Vérifiez les logs dans votre dashboard Render/Railway
2. Assurez-vous que toutes les dépendances sont dans `requirements.txt`
3. Vérifiez que les variables d'environnement sont bien configurées


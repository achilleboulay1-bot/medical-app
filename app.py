# Point d'entrée pour le déploiement
# Ce fichier importe l'application depuis le fichier source
import sys
import os

# Ajouter le dossier app.py1 au chemin Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app.py1'))

# Importer l'application Flask
# Note: Le nom du fichier contient un espace, donc on doit l'importer différemment
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("app_module", os.path.join(os.path.dirname(__file__), "app.py1", "App.py 1"))
    app_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app_module)
    
    # Exporter l'application Flask
    app = app_module.app
    
    # Initialiser la base de données au démarrage
    def init_db():
        with app.app_context():
            try:
                app_module.db.create_all()
                
                # Créer les templates email par défaut si nécessaire
                if not app_module.EmailTemplate.query.first():
                    import json
                    templates = [
                        app_module.EmailTemplate(
                            name='Confirmation de rendez-vous',
                            template_type='email',
                            subject='Confirmation de votre rendez-vous',
                            body='Bonjour {{patient_name}},\n\nVotre rendez-vous est confirmé pour le {{appointment_date}} à {{appointment_time}}.\n\nCordialement,\n{{practitioner_name}}',
                            variables=json.dumps(['patient_name', 'appointment_date', 'appointment_time', 'practitioner_name'])
                        ),
                        app_module.EmailTemplate(
                            name='Rappel de rendez-vous',
                            template_type='email',
                            subject='Rappel: Votre rendez-vous demain',
                            body='Bonjour {{patient_name}},\n\nCeci est un rappel pour votre rendez-vous demain à {{appointment_time}}.\n\nCordialement,\n{{practitioner_name}}',
                            variables=json.dumps(['patient_name', 'appointment_time', 'practitioner_name'])
                        ),
                        app_module.EmailTemplate(
                            name='Annulation de rendez-vous',
                            template_type='email',
                            subject='Annulation de votre rendez-vous',
                            body='Bonjour {{patient_name}},\n\nVotre rendez-vous du {{appointment_date}} a été annulé.\n\nCordialement,\n{{practitioner_name}}',
                            variables=json.dumps(['patient_name', 'appointment_date', 'practitioner_name'])
                        )
                    ]
                    for template in templates:
                        app_module.db.session.add(template)
                    app_module.db.session.commit()
            except Exception as e:
                print(f"Erreur lors de l'initialisation de la base de données: {e}")
    
    # Initialiser la base de données
    init_db()
    
except Exception as e:
    print(f"Erreur lors du chargement de l'application: {e}")
    raise

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


#!/bin/bash

REPO="Serenity-System/serenaia-beaute-backend"

# BACK-7.1
gh issue create --repo $REPO --title "[BACK-7.1] Créer environnement virtuel Python 3.11" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer l'environnement virtuel Python pour le projet.

## 📋 Tâche
\`\`\`bash
python3.11 -m venv venv
source venv/bin/activate
python --version  # Vérifier 3.11+
\`\`\`

## ✅ Critère
- [x] venv créé
- [x] Python 3.11+ vérifié

## ⏱️ 15 min"

# BACK-7.2
gh issue create --repo $REPO --title "[BACK-7.2] Créer requirements.txt avec dépendances" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer le fichier requirements.txt avec toutes les dépendances.

## 📋 Tâche
- [ ] Créer requirements.txt
- [ ] Ajouter FastAPI, uvicorn, SQLAlchemy, etc.
- [ ] \`pip install -r requirements.txt\`
- [ ] Vérifier installations

## ✅ Critère
- [x] requirements.txt créé
- [x] Toutes dépendances installées

## 🔗 Dépend: BACK-7.1

## ⏱️ 30 min"

# BACK-7.3
gh issue create --repo $REPO --title "[BACK-7.3] Créer structure dossiers app/" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer l'arborescence complète du projet backend.

## 📋 Tâche
\`\`\`bash
mkdir -p app/{api/v1,models,schemas,services,tasks,utils}
touch app/{__init__,main,config,database,deps}.py
touch app/api/{__init__}.py
touch app/api/v1/{__init__,router}.py
\`\`\`

## ✅ Critère
- [x] Structure complète créée
- [x] Tous __init__.py présents

## ⏱️ 20 min"

# BACK-7.4
gh issue create --repo $REPO --title "[BACK-7.4] Créer app/main.py (FastAPI init)" \
  --label "atomic,medium-task,phase-1-backend" \
  --body "## 🎯 Objectif
Créer le point d'entrée FastAPI de l'application.

## 📋 Tâche
- [ ] Créer app = FastAPI()
- [ ] Configurer metadata (title, version)
- [ ] Ajouter CORS middleware
- [ ] Inclure api/v1/router
- [ ] Test: \`uvicorn app.main:app --reload\`

## ✅ Critère
- [x] main.py créé
- [x] Serveur démarre sans erreur
- [x] Swagger accessible sur /docs

## 🔗 Dépend: BACK-7.3

## ⏱️ 1h"

# BACK-7.5
gh issue create --repo $REPO --title "[BACK-7.5] Créer app/config.py (Settings)" \
  --label "atomic,medium-task,phase-1-backend" \
  --body "## 🎯 Objectif
Créer la configuration centralisée avec Pydantic Settings.

## 📋 Tâche
- [ ] Importer BaseSettings de pydantic-settings
- [ ] Créer classe Settings
- [ ] Champs: DATABASE_URL, SECRET_KEY, etc.
- [ ] Charger depuis .env

## ✅ Critère
- [x] config.py créé
- [x] Settings testées avec .env.example

## 🔗 Dépend: BACK-7.3

## ⏱️ 1h"

# BACK-7.6
gh issue create --repo $REPO --title "[BACK-7.6] Créer app/database.py (SQLAlchemy)" \
  --label "atomic,medium-task,phase-1-backend" \
  --body "## 🎯 Objectif
Configurer la connexion PostgreSQL avec SQLAlchemy.

## 📋 Tâche
- [ ] Créer engine SQLAlchemy
- [ ] Créer SessionLocal
- [ ] Créer Base (declarative_base)
- [ ] Function get_db() generator

## ✅ Critère
- [x] database.py créé
- [x] Connexion testée

## 🔗 Dépend: BACK-7.5

## ⏱️ 1h"

# BACK-7.7
gh issue create --repo $REPO --title "[BACK-7.7] Créer app/deps.py (dependencies)" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer les dépendances FastAPI réutilisables.

## 📋 Tâche
- [ ] Import get_db from database
- [ ] Créer get_current_user dependency (placeholder)
- [ ] Documenter usage

## ✅ Critère
- [x] deps.py créé
- [x] get_db fonctionnel

## 🔗 Dépend: BACK-7.6

## ⏱️ 30 min"

# BACK-7.8
gh issue create --repo $REPO --title "[BACK-7.8] Créer api/v1/router.py" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer le router principal v1 de l'API.

## 📋 Tâche
- [ ] Créer APIRouter avec prefix=\"/api/v1\"
- [ ] Créer endpoint GET / (hello world)
- [ ] Inclure dans main.py

## ✅ Critère
- [x] router.py créé
- [x] GET /api/v1/ répond 200

## 🔗 Dépend: BACK-7.4

## ⏱️ 20 min"

# BACK-7.9
gh issue create --repo $REPO --title "[BACK-7.9] Créer .env.example" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer le fichier .env.example avec toutes les variables.

## 📋 Tâche
\`\`\`bash
DATABASE_URL=postgresql://...
SECRET_KEY=changeme
STRIPE_SECRET_KEY=sk_test_...
etc.
\`\`\`

## ✅ Critère
- [x] .env.example créé
- [x] Toutes variables documentées

## ⏱️ 20 min"

# BACK-7.10
gh issue create --repo $REPO --title "[BACK-7.10] Créer .gitignore" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer .gitignore pour Python/FastAPI.

## 📋 Tâche
- [ ] Ignorer venv/, __pycache__/, .env
- [ ] Ignorer .pytest_cache/, .coverage
- [ ] Ignorer *.pyc, *.pyo

## ✅ Critère
- [x] .gitignore créé
- [x] Patterns corrects

## ⏱️ 10 min"

# BACK-7.11
gh issue create --repo $REPO --title "[BACK-7.11] Créer endpoint /health" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Créer endpoint health check.

## 📋 Tâche
- [ ] GET /health
- [ ] Retourne {\"status\": \"ok\", \"timestamp\": \"...\"}
- [ ] Test avec curl

## ✅ Critère
- [x] /health répond 200
- [x] JSON valide

## 🔗 Dépend: BACK-7.8

## ⏱️ 15 min"

# BACK-7.12
gh issue create --repo $REPO --title "[BACK-7.12] Test démarrage serveur uvicorn" \
  --label "atomic,quick-win,phase-1-backend" \
  --body "## 🎯 Objectif
Valider que le serveur démarre correctement.

## 📋 Tâche
- [ ] \`uvicorn app.main:app --reload\`
- [ ] Tester /health
- [ ] Tester /docs (Swagger)
- [ ] Tester /redoc
- [ ] Vérifier logs

## ✅ Critère
- [x] Serveur démarre sans erreur
- [x] Tous endpoints accessibles

## 🔗 Dépend: BACK-7.11

## ⏱️ 20 min"

echo "✅ BACK-7: 12 micro-issues créées (Setup FastAPI) !"

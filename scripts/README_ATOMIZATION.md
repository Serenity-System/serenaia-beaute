# 🔬 Système d'Atomisation - Sérénaia Beauté

## 🎯 Objectif

Transformer les issues macro (40-60h) en micro-issues atomiques (30min-2h max) parfaitement adaptées à Claude Code.

## ✅ Avantages Micro-Issues

### Pour Claude Code
- ✅ **Pas de perte de contexte** : Tâches 1-2h max
- ✅ **Objectif unique et clair** : Un seul fichier/fonction
- ✅ **Testable immédiatement** : Feedback rapide
- ✅ **Dépendances minimales** : 2-3 max

### Pour le Suivi
- ✅ **Progression granulaire** : Visibilité précise
- ✅ **Estimation fiable** : Tâches courtes = moins d'incertitude
- ✅ **Parallélisation** : Plusieurs développeurs simultanément
- ✅ **Blocages identifiés rapidement** : Issues courtes = feedback rapide

## 📊 État Actuel

| Phase | Issues Macro | Micro-Issues | Statut |
|-------|--------------|--------------|--------|
| Phase 0 | 6 | 25 | ✅ Créées (#59-#83) |
| Backend Phase 1 | 26 | 145 | ✅ Créées (#84-#203) |
| Frontend Public | 15 | ~90 | ⏳ À créer |
| Frontend CRM | 20 | ~120 | ⏳ À créer |
| Déploiement | 12 | ~70 | ⏳ À créer |
| Lancement | 5 | ~25 | ⏳ À créer |
| Phase 2 | 15 | ~80 | ⏳ À créer |
| **TOTAL** | **93** | **~555** | **31% complété** |

## 🚀 Scripts Disponibles

### 1. Backend (✅ Complété)

```bash
# Déjà créées : 170 micro-issues Backend
# Issues #59-#203 dans serenaia-beaute-backend
```

**Groupes créés** :
- Phase 0 : BACK-1 à BACK-6 (25 issues)
- BACK-7 : Setup FastAPI (12 issues)
- BACK-8 : Modèles SQLAlchemy (18 issues)
- BACK-9 : Alembic (6 issues)
- BACK-10 : Stripe (10 issues)
- BACK-11 : Auth JWT (8 issues)
- BACK-12 : API Booking (10 issues)
- BACK-13 : OVH SMS (8 issues)
- BACK-14 : Docker (7 issues)
- BACK-15 : Redis (6 issues)
- BACK-16 : PayPal (8 issues)
- BACK-17 : Sumup (6 issues)
- BACK-18 : Tests (10 issues)
- BACK-19 : Sécurité (8 issues)
- BACK-20 : Logging (7 issues)
- BACK-21 : CI/CD (9 issues)
- BACK-22 : Documentation (6 issues)
- BACK-23 : Emails (8 issues)
- BACK-24 : API Disponibilités (8 issues)
- BACK-25 : API Bons Cadeaux (8 issues)
- BACK-26 : API Clients (10 issues)

### 2. Frontend Public (⏳ À créer)

```bash
# Script: create_frontend_public_atomic.sh
# ~90 micro-issues à créer
```

**Groupes prévus** :
- FP-1 : Setup Next.js (10 issues)
- FP-2 : Page Accueil (8 issues)
- FP-3 : Page Réservation (10 issues)
- FP-4 : Page Bons Cadeaux (6 issues)
- FP-5 : Déploiement Vercel (6 issues)
- FP-6 à FP-15 : Pages et composants restants (~50 issues)

### 3. Frontend CRM (⏳ À créer)

```bash
# Script: create_frontend_crm_atomic.sh
# ~120 micro-issues à créer
```

**Groupes prévus** :
- FC-1 : Setup CRM (10 issues)
- FC-2 : Login (5 issues)
- FC-3 : Dashboard (8 issues)
- FC-4 à FC-20 : Modules CRM (~97 issues)

### 4. Déploiement (⏳ À créer)

```bash
# Script: create_deploy_atomic.sh
# ~70 micro-issues à créer
```

### 5. Lancement (⏳ À créer)

```bash
# Script: create_launch_atomic.sh
# ~25 micro-issues à créer
```

### 6. Phase 2 (⏳ À créer)

```bash
# Script: create_phase2_atomic.sh
# ~80 micro-issues à créer
```

## 📝 Format Standard Micro-Issue

```markdown
## 🎯 Objectif
[Description claire et concise]

**Groupe parent**: [ex: Setup FastAPI]

## 📋 Tâche
- [ ] Étape 1
- [ ] Étape 2
- [ ] Étape 3

## ✅ Critères d'Acceptance
- [x] Fonctionnalité implémentée
- [x] Tests passent (si applicable)
- [x] Code committé

## 🔗 Dépendances
[issues prérequis si applicable]

## ⏱️ Estimation: [30min-2h]

## 📝 Notes
Tâche atomique conçue pour Claude Code (1-2h max, sans perte de contexte)
```

## 🏷️ Labels Utilisés

- `atomic` : Tâche atomique (toutes les micro-issues)
- `quick-win` : < 1h (tâches rapides)
- `medium-task` : 1-2h (tâches moyennes)
- `phase-0` : Phase 0 - Préparation
- `phase-1-backend` : Backend Phase 1
- `phase-1-frontend-public` : Frontend Public
- `phase-1-frontend-crm` : Frontend CRM
- `deployment` : Déploiement
- `launch` : Lancement
- `phase-2` : Phase 2 Extensions

## 🔢 Nomenclature

Format : `[GROUP-X.Y]` où :
- **GROUP** : BACK, FP, FC, DEPLOY, LAUNCH, P2
- **X** : Numéro issue parent (ex: 7, 8, 9...)
- **Y** : Numéro sous-issue (ex: 1, 2, 3...)

**Exemples** :
- `[BACK-7.1]` : Backend issue #7, sous-issue 1
- `[FP-3.5]` : Frontend Public issue #3, sous-issue 5
- `[FC-10.12]` : Frontend CRM issue #10, sous-issue 12

## 🛠️ Comment Utiliser

### Option 1 : Créer toutes les micro-issues d'une phase

```bash
# Frontend Public
bash scripts/create_frontend_public_atomic.sh

# Frontend CRM
bash scripts/create_frontend_crm_atomic.sh

# Déploiement
bash scripts/create_deploy_atomic.sh
```

### Option 2 : Script Python pour plus de contrôle

```bash
# Groupe spécifique
python scripts/atomize_issues_complete.py --group FP-1

# Phase complète
python scripts/atomize_issues_complete.py --phase frontend-public

# Tout d'un coup (⚠️ long)
python scripts/atomize_issues_complete.py --all
```

### Option 3 : Atomisation progressive

Créer les micro-issues au fur et à mesure des besoins :
1. Commencer par Backend (✅ déjà fait)
2. Passer à Frontend Public quand prêt
3. Puis Frontend CRM
4. Déploiement vers la fin
5. Phase 2 après MVP

## 📈 Workflow Recommandé avec Claude Code

### 1. Filtrer par label
```bash
gh issue list --repo Serenity-System/serenaia-beaute-backend \
  --label atomic,phase-1-backend
```

### 2. Trier par dépendances
- Commencer par issues sans dépendances
- Suivre l'ordre numérique (BACK-7.1 → BACK-7.2 → ...)

### 3. Workflow Claude Code
```
1. Choisir une micro-issue (30min-2h)
2. Demander à Claude Code de la réaliser
3. Claude termine sans perte de contexte
4. Fermer l'issue
5. Passer à la suivante
```

### 4. Parallélisation
Plusieurs développeurs/Claude instances peuvent travailler simultanément sur des micro-issues indépendantes.

## 🎯 Exemple Concret

**Avant atomisation** :
```
Issue #7: Setup FastAPI - Structure complète
Estimation: 40-60h
Scope: Trop large, perte de contexte probable
```

**Après atomisation** :
```
BACK-7.1: Créer venv Python 3.11 (15min) ✅
BACK-7.2: Créer requirements.txt (30min) ✅
BACK-7.3: Créer structure dossiers (20min) ✅
BACK-7.4: Créer main.py (1h) ✅
... (8 autres micro-issues)
```

**Résultat** :
- ✅ Chaque tâche < 2h
- ✅ Progression visible
- ✅ Pas de perte de contexte
- ✅ Parallelisable

## 🚦 Ordre d'Exécution Recommandé

### MVP (Phase 1)
1. ✅ **Backend** (#59-#203) - COMPLÉTÉ
2. ⏳ **Frontend Public** - À atomiser
3. ⏳ **Frontend CRM** - À atomiser
4. ⏳ **Déploiement** - À atomiser
5. ⏳ **Lancement** - À atomiser

### Extensions (Phase 2)
6. ⏳ **Phase 2** - À atomiser plus tard

## 📚 Ressources

- **Plan d'atomisation complet** : `/tmp/atomization_plan.md`
- **Scripts** :
  - `create_phase0_atomic.sh` (✅ exécuté)
  - `create_back7_atomic.sh` (✅ exécuté)
  - `create_backend_remaining.sh` (✅ exécuté)
  - `atomize_all_issues.py` (template Python)
  - `atomize_issues_complete.py` (script complet)
- **Issues GitHub** :
  - Backend : https://github.com/Serenity-System/serenaia-beaute-backend/issues
  - Frontend Public : https://github.com/Serenity-System/serenaia-beaute-frontend-public/issues
  - Frontend CRM : https://github.com/Serenity-System/serenaia-beaute-frontend-crm/issues

## 🤖 Optimisé pour Claude Code

Ce système d'atomisation a été spécifiquement conçu pour maximiser l'efficacité de Claude Code :

- **Contexte minimal** : Chaque issue tient dans la fenêtre de contexte
- **Objectif clair** : Un seul fichier/fonction par issue
- **Tests rapides** : Validation immédiate
- **Commits atomiques** : Une micro-issue = un commit propre

## 📞 Support

Pour toute question sur le système d'atomisation :
- Consulter ce README
- Vérifier `/tmp/atomization_plan.md` pour le détail complet
- Issues GitHub pour suivi

---

**Version** : 1.0
**Dernière mise à jour** : 2026-01-12
**Statut** : Backend atomisé (170 issues), restant à faire (385 issues)

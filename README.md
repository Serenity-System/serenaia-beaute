# 🌸 Sérénaia Beauté - Plateforme de Gestion Institut

[![Backend Issues](https://img.shields.io/github/issues/Serenity-System/serenaia-beaute-backend?label=Backend)](https://github.com/Serenity-System/serenaia-beaute-backend/issues)
[![Frontend Public Issues](https://img.shields.io/github/issues/Serenity-System/serenaia-beaute-frontend-public?label=Frontend%20Public)](https://github.com/Serenity-System/serenaia-beaute-frontend-public/issues)
[![Frontend CRM Issues](https://img.shields.io/github/issues/Serenity-System/serenaia-beaute-frontend-crm?label=Frontend%20CRM)](https://github.com/Serenity-System/serenaia-beaute-frontend-crm/issues)

> **Plateforme complète de gestion pour institut de beauté** : Site vitrine + CRM + Paiements + Notifications

---

## 🚀 Quick Start pour Claude Code

### 📋 Consulter le Guide Complet

**→ [Issue #1 : Guide Complet du Projet](https://github.com/Serenity-System/serenaia-beaute/issues/1)** ⭐

Cette issue contient **TOUT** :
- Vue d'ensemble du projet
- Architecture technique complète
- **555 micro-issues atomiques** (30min-2h chacune)
- Ordre d'exécution recommandé
- Quick start et ressources

### 🎯 Commencer Immédiatement

```bash
# 1. Consulter la référence
gh issue view 1 --repo Serenity-System/serenaia-beaute

# 2. Voir les tâches Backend (170 créées)
gh issue list --repo Serenity-System/serenaia-beaute-backend --label atomic

# 3. Commencer par la première tâche
gh issue view 59 --repo Serenity-System/serenaia-beaute-backend
```

---

## 📊 Progression Actuelle : 31% (170/555 tâches)

```
Phase 0:      ████████████████████████████████████████ 100% ✅ (25 issues)
Backend:      ████████████████████████████████████████ 100% ✅ (145 issues)
Frontend Pub: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% ⏳ (90 issues)
Frontend CRM: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% ⏳ (120 issues)
Deploy:       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% ⏳ (70 issues)
Launch:       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% ⏳ (25 issues)
Phase 2:      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0% ⏳ (80 issues)
```

**✅ Backend atomisé** : 170 micro-issues créées (#59-#203)
**⏳ Frontend & Deploy** : 385 micro-issues à créer

---

## 🏗️ Architecture

### Backend API (FastAPI)
- **Repo** : [serenaia-beaute-backend](https://github.com/Serenity-System/serenaia-beaute-backend)
- **Tech** : FastAPI, PostgreSQL, Redis, SQLAlchemy, Alembic
- **Issues** : 170 micro-issues atomiques créées ✅

### Frontend Public (Next.js)
- **Repo** : [serenaia-beaute-frontend-public](https://github.com/Serenity-System/serenaia-beaute-frontend-public)
- **Tech** : Next.js 14, Tailwind, shadcn/ui, Stripe
- **Issues** : ~90 micro-issues à créer

### Frontend CRM (Next.js)
- **Repo** : [serenaia-beaute-frontend-crm](https://github.com/Serenity-System/serenaia-beaute-frontend-crm)
- **Tech** : Next.js 14, shadcn/ui, FullCalendar, NextAuth
- **Issues** : ~120 micro-issues à créer

### Infrastructure
- **Backend** : Google Cloud Run
- **Database** : Cloud SQL PostgreSQL
- **Cache** : Memorystore Redis
- **Frontend** : Vercel
- **CI/CD** : GitHub Actions

---

## 📦 Repositories

| Repo | Description | Issues |
|------|-------------|--------|
| **[serenaia-beaute-backend](https://github.com/Serenity-System/serenaia-beaute-backend)** | API REST FastAPI | 170 ✅ |
| **[serenaia-beaute-frontend-public](https://github.com/Serenity-System/serenaia-beaute-frontend-public)** | Site vitrine | ~90 ⏳ |
| **[serenaia-beaute-frontend-crm](https://github.com/Serenity-System/serenaia-beaute-frontend-crm)** | Backoffice CRM | ~120 ⏳ |
| **[serenaia-beaute](https://github.com/Serenity-System/serenaia-beaute)** | Documentation | Ce repo |

---

## 🎯 Fonctionnalités Principales

### MVP (Phase 1)
- ✅ **Réservation en ligne 24/7** - Clients réservent sans intervention
- ✅ **Paiements sécurisés** - Stripe, PayPal, Sumup Air
- ✅ **Notifications automatiques** - SMS (OVH) + Email confirmation
- ✅ **CRM complet** - Gestion clients, historique, statistiques
- ✅ **Calendrier temps réel** - Disponibilités, créneaux, drag&drop
- ✅ **Point de vente** - Caisse tactile, produits + services
- ✅ **Gestion stocks** - Suivi inventaire, alertes
- ✅ **Bons cadeaux** - Achat en ligne, PDF, validation

### Extensions (Phase 2)
- ⏳ Module fidélité (points, récompenses)
- ⏳ Galerie photos (avant/après, consentement RGPD)
- ⏳ Automatisations marketing (anniversaire, réactivation)
- ⏳ Multi-praticiens (plusieurs esthéticiennes)
- ⏳ Application mobile (PWA ou native)
- ⏳ Analytics avancés (BI, prédictions CA)

---

## 📚 Documentation

### Documents Essentiels (dans ce repo)

| Document | Description |
|----------|-------------|
| **[Issue #1](https://github.com/Serenity-System/serenaia-beaute/issues/1)** | 📋 Guide complet (TOUT est dedans !) |
| `ISSUES_MASTER_LIST.md` | Vue d'ensemble 93 issues macro |
| `scripts/README_ATOMIZATION.md` | Système d'atomisation |
| `scripts/atomization_plan.md` | Détail 555 micro-issues |

### Documents Techniques (dans `/docs`)

| Document | Description |
|----------|-------------|
| `ARCHITECTURE_BDD.md` | Schéma BDD complet (16 tables) |
| `CONTRACTS_API_SPEC.md` | Spécifications API REST |
| `USER_FLOWS_V2.md` | Parcours utilisateurs |
| `TECHNICAL_ARCHITECTURE.md` | Architecture globale |

---

## 🤖 Système d'Atomisation

**Concept** : Transformer les issues macro (40-60h) en **micro-issues atomiques (30min-2h)**

### Avantages
✅ **Zéro perte de contexte** pour Claude Code
✅ **Progression granulaire** visible
✅ **Parallélisation** facile
✅ **Estimation fiable**

### Format Micro-Issue
```
[BACK-7.1] Créer environnement virtuel Python 3.11
🎯 Objectif clair
📋 3-5 étapes max
✅ Critères d'acceptance
🔗 Dépendances (si nécessaire)
⏱️ Estimation: 15min-2h
```

### Labels
- `atomic` : Tâche atomique
- `quick-win` : < 1h
- `medium-task` : 1-2h
- `phase-0`, `phase-1-backend`, etc.

---

## 🚦 Workflow Recommandé

### Pour Claude Code

1. **Consulter** [Issue #1](https://github.com/Serenity-System/serenaia-beaute/issues/1) - Guide complet
2. **Lister** les issues atomiques disponibles
   ```bash
   gh issue list --repo Serenity-System/serenaia-beaute-backend --label atomic
   ```
3. **Choisir** une tâche (30min-2h)
4. **Exécuter** sans perte de contexte
5. **Commit** + fermer issue
6. **Répéter** 🔄

### Ordre d'Exécution

1. ✅ **Phase 0** (#59-#83) - Config initiale - CRÉÉE
2. ✅ **Backend** (#84-#203) - API complète - CRÉÉE
3. ⏳ **Frontend Public** - Site vitrine - À CRÉER
4. ⏳ **Frontend CRM** - Backoffice - À CRÉER
5. ⏳ **Déploiement** - Production GCP - À CRÉER
6. ⏳ **Lancement** - Go-live - À CRÉER
7. ⏳ **Phase 2** - Extensions - Post-MVP

---

## 📈 Estimations

| Phase | Issues | Estimation | Semaines |
|-------|--------|------------|----------|
| Phase 0 | 25 | 30-40h | 1 |
| Backend | 145 | 300-400h | 8 |
| Frontend Public | 90 | 120-160h | 4 |
| Frontend CRM | 120 | 200-280h | 6 |
| Déploiement | 70 | 80-100h | 3 |
| Lancement | 25 | 30-40h | 1 |
| **MVP Total** | **475** | **760-1020h** | **23** |
| Phase 2 | 80 | 400-600h | 15 |
| **TOTAL** | **555** | **1160-1620h** | **38** |

_Basé sur 40h/semaine, 1 développeur_

---

## 🔗 Liens Rapides

- **📋 [Issue #1 - Guide Complet](https://github.com/Serenity-System/serenaia-beaute/issues/1)** ← COMMENCER ICI
- **[Backend Issues](https://github.com/Serenity-System/serenaia-beaute-backend/issues)** - 170 créées
- **[Frontend Public Issues](https://github.com/Serenity-System/serenaia-beaute-frontend-public/issues)**
- **[Frontend CRM Issues](https://github.com/Serenity-System/serenaia-beaute-frontend-crm/issues)**
- **[GitHub Project](https://github.com/orgs/Serenity-System/projects/4)**

---

## 🎓 Pour les Nouveaux Développeurs

Si tu arrives sur le projet :

1. **Lis [Issue #1](https://github.com/Serenity-System/serenaia-beaute/issues/1)** - Tout est là !
2. **Clone** les 3 repos (backend, frontend-public, frontend-crm)
3. **Commence** par Phase 0 (#59-#83) - Configuration rapide
4. **Puis** Backend (#84-#203) - Fondation API
5. **Follow** l'ordre recommandé dans Issue #1

---

## 📞 Support

- **Issues** : Créer une issue dans le repo concerné
- **Documentation** : Consulter `/docs` et `scripts/`
- **Référence** : [Issue #1](https://github.com/Serenity-System/serenaia-beaute/issues/1)

---

**Version** : 1.0
**Dernière mise à jour** : 2026-01-12
**Maintenu par** : @tincenv
**Organisation** : [Serenity-System](https://github.com/Serenity-System)

**🚀 Prêt pour développement atomique avec Claude Code !**

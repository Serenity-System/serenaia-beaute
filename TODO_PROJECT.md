# 📋 TODO List Complète - Projet Sérénaïa Beauté

**Date de création:** 2026-01-11
**Version:** 1.0
**Durée estimée totale:** 3-4 mois (Phase 1) + 2 mois (Phase 2)

---

## 🎯 Légende

- 🔴 **Critique** : Bloquant, priorité absolue
- 🟠 **Important** : Nécessaire pour le MVP
- 🟡 **Moyen** : Amélioration, peut attendre
- ✅ **Fait**
- ⏸️ **En attente** de décision/validation
- 🚧 **En cours**

---

# PHASE 0 : Préparation & Validation (Semaine 1-2)

## 📝 Documentation & Décisions

### Décisions Critiques
- [ ] 🔴 **Valider terminal de paiement** : Acheter Sumup Air (59€) + Créer comptes Stripe/Sumup
- [ ] 🔴 **Décider virement bons cadeaux** : Option A (exclu), B (délai 48h), ou C (code non activé)
- [ ] 🔴 **Définir zone géographique** : Ville, adresse (pour SEO + page Contact)
- [ ] 🟠 **Définir catalogue produits minimum** : 5-10 produits (nom, prix, fournisseur)

### Documents à Créer/Compléter
- [x] ✅ `PROJECT_BRIEF.md` - Brief complet
- [x] ✅ `TECHNICAL_ARCHITECTURE.md` - Architecture technique
- [x] ✅ `CRM_SPECIFICATIONS.md` - Specs CRM
- [x] ✅ `MVP_VALIDATED.md` - Scope MVP validé
- [x] ✅ `ANALYSE_CRITIQUE.md` - Analyse des problèmes
- [x] ✅ `COMPARAISON_PAIEMENTS.md` - Sumup vs Stripe
- [x] ✅ `DECISIONS_FINALES.md` - Décisions validées
- [ ] 🔴 `STRATEGIE_TESTS.md` - Stratégie de tests complète
- [ ] 🔴 `CGV_TEMPLATE.md` - Conditions Générales de Vente
- [ ] 🔴 `CONTENUS_TEMPORAIRES.md` - Textes temporaires du site
- [ ] 🟠 `CATALOGUE_PRODUITS.md` - Liste produits à vendre
- [ ] 🟠 `CHARTE_GRAPHIQUE.md` - Couleurs, typo, logo
- [ ] 🟠 `POLITIQUE_CONFIDENTIALITE.md` - RGPD
- [ ] 🟠 `MENTIONS_LEGALES.md` - Mentions légales

### Contenu & Assets
- [ ] 🔴 **Logo Sérénaïa Beauté** (vectoriel SVG + PNG)
- [ ] 🔴 **Photos professionnelles** :
  - [ ] Portrait de la praticienne (page À propos)
  - [ ] Photos des prestations (5 catégories)
  - [ ] Photos d'ambiance (cabine, produits)
  - [ ] 5-10 photos avant/après (avec consentements signés)
- [ ] 🟠 **Rédaction des textes** (ou validation des textes générés) :
  - [ ] Page Accueil (hero, sections)
  - [ ] Page À propos (présentation complète)
  - [ ] Descriptions prestations (toutes catégories)
  - [ ] Page Contact (texte d'introduction)
- [ ] 🟠 **Créer structure répertoires images** :
  ```
  /public/images/
    /prestations/
    /galerie/
    /apropos/
    /logo/
  ```

---

# PHASE 1 : MVP - Backend API (Semaine 3-6)

## 🏗️ Setup & Infrastructure

### Environnement de Développement
- [ ] 🔴 **Initialiser repo Git**
  - [ ] Créer organisation GitHub (Serenity-System ou autre)
  - [ ] Créer repo `serenaia-beaute-backend`
  - [ ] Initialiser `.gitignore` (Python, .env)
  - [ ] Créer `README.md`
- [ ] 🔴 **Setup environnement local**
  - [ ] Python 3.11+ (venv)
  - [ ] PostgreSQL local (Docker ou installation)
  - [ ] Redis local (Docker ou installation)
  - [ ] Variables d'environnement (`.env.example`)

### Structure Projet Backend
- [ ] 🔴 **Créer structure FastAPI** (selon TECHNICAL_ARCHITECTURE.md)
  ```
  backend/
  ├── app/
  │   ├── main.py
  │   ├── config.py
  │   ├── database.py
  │   ├── deps.py
  │   ├── api/v1/
  │   ├── models/
  │   ├── schemas/
  │   ├── services/
  │   ├── tasks/
  │   └── utils/
  ├── alembic/
  ├── tests/
  ├── Dockerfile
  ├── requirements.txt
  └── .env.example
  ```

## 🗄️ Base de Données

### Schéma & Migrations
- [ ] 🔴 **Initialiser Alembic** (migrations)
- [ ] 🔴 **Créer modèles SQLAlchemy** (16 tables) :
  - [ ] `users` - Administrateurs
  - [ ] `services` - Prestations
  - [ ] `bookings` - Réservations
  - [ ] `clients` - Base CRM
  - [ ] `payments` - Transactions (avec gestion acomptes)
  - [ ] `gift_cards` - Bons cadeaux
  - [ ] `products` - Catalogue produits
  - [ ] `stock_movements` - Mouvements stocks
  - [ ] `service_history` - Historique soins
  - [ ] `availabilities` - Horaires disponibles
  - [ ] `blocked_dates` - Jours congés
  - [ ] `notifications` - Log SMS/Emails
  - [ ] `loyalty_points` - Points fidélité (Phase 2)
  - [ ] `consents` - Consentements RGPD
  - [ ] `invoices` - Factures
  - [ ] `photos` - Galerie avant/après (Phase 2)
- [ ] 🔴 **Créer index optimisés** (voir TECHNICAL_ARCHITECTURE.md)
- [ ] 🔴 **Migrer le schéma** (`alembic upgrade head`)
- [ ] 🟠 **Créer jeu de données de test** (100 clients fictifs, 200 RDV)

### Correction Architecture
- [ ] 🔴 **Corriger modèle `payments`** pour gérer acomptes + solde :
  - Ajouter `total_amount`, `paid_amount`, `remaining_amount`
  - Support de plusieurs paiements pour 1 réservation

## ⚙️ API Backend

### Configuration & Core
- [ ] 🔴 **Configuration** (`config.py`)
  - [ ] Variables d'environnement (DATABASE_URL, SECRET_KEY, etc.)
  - [ ] Validation Pydantic Settings
- [ ] 🔴 **Connexion base de données** (`database.py`)
  - [ ] AsyncEngine SQLAlchemy
  - [ ] SessionLocal
- [ ] 🔴 **Dependencies** (`deps.py`)
  - [ ] `get_db()` - Session DB
  - [ ] `get_current_user()` - JWT auth
- [ ] 🔴 **Main app** (`main.py`)
  - [ ] Initialisation FastAPI
  - [ ] CORS middleware
  - [ ] Security headers
  - [ ] Router principal
  - [ ] Documentation OpenAPI

### Schémas Pydantic
- [ ] 🔴 **Créer schémas Pydantic** (validation) :
  - [ ] `booking.py` (BookingCreate, BookingUpdate, BookingResponse)
  - [ ] `service.py`
  - [ ] `gift_card.py`
  - [ ] `payment.py`
  - [ ] `client.py`
  - [ ] `product.py`
  - [ ] etc.

### Services Métier
- [ ] 🔴 **Services métier** (`services/`) :
  - [ ] `booking_service.py` - Logique réservations
  - [ ] `payment_service.py` - Intégration paiements
  - [ ] `sms_service.py` - OVH SMS API
  - [ ] `email_service.py` - Resend/SendGrid
  - [ ] `pdf_service.py` - Génération PDFs (bons cadeaux, factures)
  - [ ] `calendar_service.py` - Gestion disponibilités
  - [ ] `stock_service.py` - Mouvements stocks
  - [ ] `client_service.py` - CRM

### Endpoints API Publics
- [ ] 🔴 **Services / Prestations**
  - [ ] `GET /api/v1/services` - Liste prestations
  - [ ] `GET /api/v1/services/{id}` - Détail prestation
- [ ] 🔴 **Disponibilités**
  - [ ] `GET /api/v1/availabilities?date=YYYY-MM-DD` - Créneaux disponibles
- [ ] 🔴 **Réservations**
  - [ ] `POST /api/v1/bookings` - Créer réservation
  - [ ] `GET /api/v1/bookings/{id}` - Détail (avec token)
  - [ ] `DELETE /api/v1/bookings/{id}/cancel` - Annuler
- [ ] 🔴 **Bons Cadeaux**
  - [ ] `POST /api/v1/gift-cards` - Acheter bon cadeau
  - [ ] `GET /api/v1/gift-cards/{code}` - Vérifier validité
- [ ] 🔴 **Paiements**
  - [ ] `POST /api/v1/payments/stripe` - Créer paiement Stripe
  - [ ] `POST /api/v1/payments/stripe/webhook` - Webhook Stripe
  - [ ] `POST /api/v1/payments/paypal` - Créer paiement PayPal
  - [ ] `POST /api/v1/payments/paypal/webhook` - Webhook PayPal
- [ ] 🔴 **Avis Google**
  - [ ] `GET /api/v1/reviews` - Récupérer avis Google

### Endpoints API Admin (Authentifiés)
- [ ] 🔴 **Authentification**
  - [ ] `POST /api/v1/auth/login` - Login admin (JWT)
  - [ ] `POST /api/v1/auth/refresh` - Refresh token
  - [ ] `POST /api/v1/auth/logout` - Logout (blacklist token)
- [ ] 🔴 **Dashboard**
  - [ ] `GET /api/v1/admin/dashboard/stats` - Stats globales
  - [ ] `GET /api/v1/admin/dashboard/today` - Stats du jour
  - [ ] `GET /api/v1/admin/dashboard/upcoming` - Prochains RDV
- [ ] 🔴 **Clients (CRM)**
  - [ ] `GET /api/v1/admin/clients` - Liste paginée + filtres
  - [ ] `GET /api/v1/admin/clients/{id}` - Fiche client
  - [ ] `POST /api/v1/admin/clients` - Créer client
  - [ ] `PUT /api/v1/admin/clients/{id}` - Modifier
  - [ ] `DELETE /api/v1/admin/clients/{id}` - Anonymiser (RGPD)
  - [ ] `GET /api/v1/admin/clients/{id}/bookings` - Historique RDV
  - [ ] `GET /api/v1/admin/clients/segments` - Segments
- [ ] 🔴 **Réservations Admin**
  - [ ] `GET /api/v1/admin/bookings` - Liste + filtres
  - [ ] `GET /api/v1/admin/bookings/{id}` - Détails
  - [ ] `POST /api/v1/admin/bookings` - Créer manuellement
  - [ ] `PUT /api/v1/admin/bookings/{id}` - Modifier
  - [ ] `DELETE /api/v1/admin/bookings/{id}` - Annuler
  - [ ] `POST /api/v1/admin/bookings/{id}/complete` - Marquer complété
- [ ] 🔴 **Prestations Admin**
  - [ ] CRUD complet (`GET`, `POST`, `PUT`, `DELETE`)
- [ ] 🔴 **Bons Cadeaux Admin**
  - [ ] `GET /api/v1/admin/gift-cards` - Liste
  - [ ] `PUT /api/v1/admin/gift-cards/{id}/extend` - Prolonger
  - [ ] `DELETE /api/v1/admin/gift-cards/{id}` - Désactiver
- [ ] 🔴 **Paiements Admin**
  - [ ] `GET /api/v1/admin/payments` - Transactions
  - [ ] `POST /api/v1/admin/payments/{id}/refund` - Rembourser
  - [ ] `PUT /api/v1/admin/payments/{id}/confirm` - Confirmer virement
- [ ] 🔴 **Produits / Stocks**
  - [ ] `GET /api/v1/admin/products` - Catalogue
  - [ ] CRUD produits
  - [ ] `POST /api/v1/admin/stock-movements` - Mouvement stock
  - [ ] `GET /api/v1/admin/stock-movements` - Historique
- [ ] 🔴 **Disponibilités**
  - [ ] `GET /api/v1/admin/availabilities` - Config horaires
  - [ ] CRUD availabilities
  - [ ] `POST /api/v1/admin/blocked-dates` - Bloquer date
  - [ ] `DELETE /api/v1/admin/blocked-dates/{id}` - Débloquer
- [ ] 🔴 **Statistiques**
  - [ ] `GET /api/v1/admin/stats/monthly` - Rapport mensuel
  - [ ] `GET /api/v1/admin/stats/yearly` - Rapport annuel
  - [ ] `GET /api/v1/admin/stats/export` - Export CSV
- [ ] 🔴 **Paramètres**
  - [ ] `GET /api/v1/admin/settings` - Config globale
  - [ ] `PUT /api/v1/admin/settings` - Modifier config

### Intégrations Externes
- [ ] 🔴 **Stripe**
  - [ ] Checkout Session (acomptes)
  - [ ] Payment Intents (gestion capture partielle)
  - [ ] Webhooks (payment_intent.succeeded, etc.)
  - [ ] Remboursements
- [ ] 🔴 **PayPal**
  - [ ] Orders API
  - [ ] Webhooks
  - [ ] Refunds
- [ ] 🔴 **OVH SMS API**
  - [ ] Envoi SMS (confirmation, rappel)
  - [ ] Templating
  - [ ] Gestion erreurs
- [ ] 🔴 **Resend / SendGrid (Emails)**
  - [ ] Envoi emails transactionnels
  - [ ] Templates HTML
  - [ ] Pièces jointes (PDFs)
- [ ] 🔴 **Google Business Profile API**
  - [ ] Récupération avis
  - [ ] Mise à jour automatique
- [ ] 🟠 **Google Cloud Storage**
  - [ ] Upload PDFs (bons cadeaux)
  - [ ] Upload photos (galerie)

### Automatisations
- [ ] 🔴 **Background Tasks** (FastAPI BackgroundTasks)
  - [ ] Envoi SMS confirmation réservation
  - [ ] Envoi email confirmation
  - [ ] Génération PDF bon cadeau
- [ ] 🟠 **Tâches Planifiées** (optionnel: Celery ou APScheduler)
  - [ ] Rappel 24h avant RDV (daily cron)
  - [ ] Demande d'avis 48h après (daily cron)
  - [ ] Clôture caisse automatique (21h)
  - [ ] Backup quotidien (3h du matin)

### Sécurité
- [ ] 🔴 **JWT Authentication**
  - [ ] Génération tokens (access + refresh)
  - [ ] Validation tokens
  - [ ] Blacklist tokens (logout)
- [ ] 🔴 **Password Hashing** (bcrypt)
- [ ] 🔴 **Rate Limiting** (slowapi ou middleware custom)
- [ ] 🔴 **Input Validation** (Pydantic)
- [ ] 🔴 **CORS** configuré strictement
- [ ] 🔴 **Security Headers**
  - X-Content-Type-Options
  - X-Frame-Options
  - X-XSS-Protection
  - Strict-Transport-Security

### Tests Backend
- [ ] 🔴 **Tests Unitaires** (pytest)
  - [ ] Services métier (coverage 80%+)
  - [ ] Utils et helpers
  - [ ] Validation Pydantic
- [ ] 🔴 **Tests d'Intégration**
  - [ ] Endpoints API (status codes, réponses)
  - [ ] Base de données (transactions, rollbacks)
- [ ] 🟠 **Tests Mocks** (intégrations externes)
  - [ ] Stripe (mode test)
  - [ ] PayPal (sandbox)
  - [ ] OVH SMS (mock)
  - [ ] Emails (mock)

### Documentation
- [ ] 🔴 **OpenAPI / Swagger** (auto-généré FastAPI)
- [ ] 🟠 **README.md** backend
  - Installation
  - Configuration
  - Lancement dev
  - Tests
- [ ] 🟠 **Postman Collection** (ou Insomnia)

---

# PHASE 1 : MVP - Frontend Public (Semaine 7-9)

## 🏗️ Setup Frontend Public

### Environnement
- [ ] 🔴 **Créer repo Git** `serenaia-beaute-frontend-public`
- [ ] 🔴 **Initialiser Next.js 14+**
  ```bash
  npx create-next-app@latest frontend-public --typescript --tailwind --app
  ```
- [ ] 🔴 **Installer dépendances** :
  - [ ] Tailwind CSS (déjà installé)
  - [ ] shadcn/ui (composants)
  - [ ] React Hook Form + Zod (formulaires)
  - [ ] Framer Motion (animations)
  - [ ] @tanstack/react-query (cache API)
  - [ ] date-fns (dates)
  - [ ] @stripe/stripe-js (Stripe)

### Structure Projet
- [ ] 🔴 **Créer structure Next.js** :
  ```
  app/
  ├── (public)/
  │   ├── page.tsx           # Accueil
  │   ├── a-propos/
  │   ├── prestations/
  │   ├── reservation/
  │   ├── bon-cadeau/
  │   ├── avis/
  │   └── contact/
  ├── layout.tsx
  ├── globals.css
  components/
  ├── ui/                    # shadcn/ui
  ├── forms/
  ├── calendar/
  └── shared/
  lib/
  ├── api-client.ts          # Client API
  ├── utils.ts
  └── validators.ts          # Zod schemas
  public/
  └── images/
  ```

## 🎨 Design System

### Configuration Tailwind
- [ ] 🔴 **Personnaliser `tailwind.config.ts`** :
  - [ ] Couleurs (rose poudré, beige, doré)
  - [ ] Typographies (serif titres, sans-serif texte)
  - [ ] Breakpoints responsive
- [ ] 🔴 **Installer shadcn/ui** :
  ```bash
  npx shadcn-ui@latest init
  ```
- [ ] 🔴 **Ajouter composants shadcn** :
  - [ ] Button
  - [ ] Input
  - [ ] Select
  - [ ] Calendar
  - [ ] Dialog
  - [ ] Card
  - [ ] Badge
  - [ ] etc.

### Composants UI Réutilisables
- [ ] 🔴 **Layout**
  - [ ] Header (navigation)
  - [ ] Footer
  - [ ] Navigation mobile (burger menu)
- [ ] 🔴 **Shared**
  - [ ] ServiceCard (carte prestation)
  - [ ] ReviewCard (carte avis)
  - [ ] Button (CTA primaire/secondaire)
  - [ ] Section (conteneur sections)
- [ ] 🔴 **Forms**
  - [ ] FormField (wrapper React Hook Form)
  - [ ] DatePicker (calendrier)
  - [ ] TimePicker (sélection heure)
  - [ ] PhoneInput (champ téléphone formaté)

## 📄 Pages Frontend Public

### Page Accueil
- [ ] 🔴 **Hero Section**
  - [ ] Titre principal + baseline
  - [ ] Image d'ambiance
  - [ ] CTA "Prendre rendez-vous"
- [ ] 🔴 **Section Prestations Populaires**
  - [ ] 3-4 prestations mises en avant
  - [ ] Cards cliquables → Page prestations
- [ ] 🔴 **Section Avis Clients**
  - [ ] Carrousel de 5 meilleurs avis
  - [ ] Note moyenne + nombre d'avis
  - [ ] Lien "Voir tous les avis"
- [ ] 🔴 **Section CTA Finale**
  - [ ] "Offrir un bon cadeau"
  - [ ] "Prendre rendez-vous"

### Page À propos
- [ ] 🔴 **Contenu**
  - [ ] Photo portrait
  - [ ] Présentation personnelle
  - [ ] Parcours et certifications
  - [ ] Philosophie et valeurs
  - [ ] Zone d'intervention
  - [ ] Marques de produits utilisés
- [ ] 🔴 **Design**
  - [ ] Mise en page élégante
  - [ ] Sections structurées
  - [ ] Animations douces (scroll reveal)

### Page Prestations
- [ ] 🔴 **Liste des prestations par catégorie** :
  - [ ] Beauté des ongles
  - [ ] Beauté du regard
  - [ ] Soins du visage
  - [ ] Modelages bien-être
  - [ ] Épilations
  - [ ] Forfaits et offres
- [ ] 🔴 **Fonctionnalités**
  - [ ] Filtres par catégorie
  - [ ] Recherche
  - [ ] Affichage : Nom, Durée, Prix, Description
  - [ ] Bouton "Réserver" direct
- [ ] 🔴 **Design**
  - [ ] Cards prestations élégantes
  - [ ] Grid responsive (mobile, tablet, desktop)

### Page Réservation
- [ ] 🔴 **Étape 1 : Sélection Prestation**
  - [ ] Liste déroulante prestations
  - [ ] Affichage : Durée + Prix
- [ ] 🔴 **Étape 2 : Choix Date & Heure**
  - [ ] Calendrier interactif (date-fns ou react-day-picker)
  - [ ] Créneaux horaires disponibles (fetch API)
  - [ ] Pas de créneaux passés
  - [ ] Bloquer dates indisponibles
- [ ] 🔴 **Étape 3 : Informations Client**
  - [ ] Formulaire : Nom, Prénom, Email, Téléphone
  - [ ] Validation Zod
  - [ ] Notes optionnelles
- [ ] 🔴 **Étape 4 : Récapitulatif**
  - [ ] Résumé réservation
  - [ ] Total + Acompte 30%
  - [ ] Conditions annulation
  - [ ] Acceptation CGV (checkbox obligatoire)
- [ ] 🔴 **Étape 5 : Paiement**
  - [ ] Intégration Stripe Checkout
  - [ ] Redirection → Page confirmation
- [ ] 🔴 **Page Confirmation**
  - [ ] Message succès
  - [ ] Récapitulatif RDV
  - [ ] Email + SMS envoyés automatiquement
  - [ ] Lien "Ajouter au calendrier" (iCal)
  - [ ] Lien annulation (avec token)

### Page Bon Cadeau
- [ ] 🔴 **Choix Type**
  - [ ] Radio button : "Montant libre" ou "Prestation spécifique"
  - [ ] Si montant libre : Input montant (min 20€ ?)
  - [ ] Si prestation : Sélection liste prestations
- [ ] 🔴 **Personnalisation**
  - [ ] Nom bénéficiaire
  - [ ] Message personnalisé (max 200 caractères)
  - [ ] Nom expéditeur
  - [ ] Email bénéficiaire (optionnel)
- [ ] 🔴 **Paiement**
  - [ ] Stripe Checkout (totalité)
  - [ ] Confirmation
- [ ] 🔴 **Page Confirmation**
  - [ ] PDF téléchargeable
  - [ ] Envoi email automatique
  - [ ] Code unique affiché (SERA-XXXX-XXXX)

### Page Avis
- [ ] 🔴 **Widget Google Reviews**
  - [ ] Note moyenne
  - [ ] Nombre d'avis
- [ ] 🔴 **Liste Avis**
  - [ ] Pagination
  - [ ] Filtres (note, date)
  - [ ] Affichage : Prénom, Date, Note, Commentaire
- [ ] 🔴 **CTA "Laisser un avis"**
  - [ ] Lien vers Google Business Profile

### Page Contact
- [ ] 🔴 **Formulaire de Contact**
  - [ ] Nom, Email, Téléphone, Message
  - [ ] Objet de la demande (select)
  - [ ] Validation + Envoi API
  - [ ] Message confirmation
- [ ] 🔴 **Informations**
  - [ ] Téléphone (cliquable mobile)
  - [ ] Email (cliquable)
  - [ ] Adresse (si publique)
  - [ ] Horaires d'ouverture
  - [ ] Réseaux sociaux (Instagram, Facebook)
- [ ] 🟠 **Carte Google Maps** (optionnel)

### Layout & Navigation
- [ ] 🔴 **Header**
  - [ ] Logo
  - [ ] Menu navigation (7 liens)
  - [ ] Bouton CTA "Réserver"
  - [ ] Menu burger (mobile)
- [ ] 🔴 **Footer**
  - [ ] Liens navigation
  - [ ] Réseaux sociaux
  - [ ] CGV, Mentions légales, Politique confidentialité
  - [ ] Copyright

## ⚙️ Fonctionnalités Frontend

### Client API
- [ ] 🔴 **Créer `lib/api-client.ts`**
  - [ ] Axios ou Fetch wrapper
  - [ ] Base URL depuis env var
  - [ ] Gestion erreurs
  - [ ] Types TypeScript
- [ ] 🔴 **Endpoints publics** :
  - [ ] `getServices()` - Liste prestations
  - [ ] `getAvailabilities(date)` - Créneaux dispo
  - [ ] `createBooking(data)` - Créer réservation
  - [ ] `createGiftCard(data)` - Acheter bon cadeau
  - [ ] `getReviews()` - Récupérer avis Google
  - [ ] `sendContactForm(data)` - Formulaire contact

### React Query
- [ ] 🔴 **Setup React Query**
  - [ ] Provider dans `layout.tsx`
  - [ ] Queries pour prestations, disponibilités, avis
  - [ ] Cache automatique (staleTime, cacheTime)

### Stripe Checkout
- [ ] 🔴 **Intégrer Stripe.js**
  - [ ] `@stripe/stripe-js`
  - [ ] Checkout Session (redirection)
  - [ ] Page retour (success / cancel)
  - [ ] Gestion webhooks (backend valide paiement)

### Optimisations
- [ ] 🔴 **Performance**
  - [ ] Images optimisées (Next.js Image)
  - [ ] Lazy loading composants
  - [ ] Code splitting automatique
  - [ ] Lighthouse score > 90
- [ ] 🔴 **SEO**
  - [ ] Metadata (title, description) par page
  - [ ] Open Graph (réseaux sociaux)
  - [ ] Sitemap.xml
  - [ ] robots.txt
- [ ] 🔴 **Accessibilité**
  - [ ] Contraste WCAG AA minimum
  - [ ] Navigation clavier
  - [ ] Labels ARIA

### Tests Frontend
- [ ] 🟠 **Tests Unitaires** (Jest + React Testing Library)
  - [ ] Composants UI
  - [ ] Formulaires (validation)
- [ ] 🟠 **Tests E2E** (Playwright)
  - [ ] Parcours réservation complet
  - [ ] Achat bon cadeau
  - [ ] Formulaire contact

---

# PHASE 1 : MVP - Frontend CRM (Semaine 10-12)

## 🏗️ Setup Frontend CRM

### Environnement
- [ ] 🔴 **Créer repo Git** `serenaia-beaute-frontend-crm`
- [ ] 🔴 **Initialiser Next.js 14+** (identique frontend public)
- [ ] 🔴 **Installer dépendances** :
  - [ ] Mêmes que frontend public
  - [ ] + recharts ou chart.js (graphiques)
  - [ ] + @tanstack/react-table (tables de données)
  - [ ] + date-fns (manipulation dates)

### Structure Projet CRM
- [ ] 🔴 **Créer structure** :
  ```
  app/
  ├── (auth)/
  │   └── login/page.tsx
  ├── (dashboard)/
  │   ├── layout.tsx         # Sidebar + Header
  │   ├── page.tsx           # Dashboard
  │   ├── clients/
  │   ├── reservations/
  │   ├── prestations/
  │   ├── bons-cadeaux/
  │   ├── paiements/
  │   ├── disponibilites/
  │   ├── avis/
  │   ├── statistiques/
  │   └── parametres/
  components/
  ├── layout/
  │   ├── Sidebar.tsx
  │   ├── Header.tsx
  ├── dashboard/
  ├── tables/
  └── forms/
  lib/
  ├── api-client.ts          # Client API avec JWT
  └── auth.ts                # Gestion auth
  ```

## 🔐 Authentification CRM

### Page Login
- [ ] 🔴 **Formulaire Login**
  - [ ] Email + Password
  - [ ] Validation
  - [ ] Erreurs gérées (mauvais identifiants)
- [ ] 🔴 **JWT Storage**
  - [ ] LocalStorage ou HttpOnly Cookie
  - [ ] Refresh token logic
  - [ ] Auto-refresh avant expiration
- [ ] 🔴 **Protected Routes**
  - [ ] Middleware Next.js (vérifier token)
  - [ ] Redirection → /login si non authentifié

## 📊 Module 1 : Dashboard

### Vue d'Ensemble
- [ ] 🔴 **Stats du Jour** (4 cards)
  - [ ] Nombre RDV aujourd'hui
  - [ ] CA du jour
  - [ ] Prochains RDV (timeline)
  - [ ] Alertes (RDV en attente, paiements)
- [ ] 🔴 **Stats du Mois** (4 cards)
  - [ ] Nombre total RDV
  - [ ] CA total
  - [ ] Taux d'annulation
  - [ ] Bons cadeaux vendus
- [ ] 🔴 **Graphiques** (recharts)
  - [ ] Évolution réservations (ligne)
  - [ ] Répartition par prestation (camembert)
  - [ ] Revenus par mois (barres)
- [ ] 🔴 **Widgets**
  - [ ] Prochains RDV aujourd'hui (liste cliquable)
  - [ ] Alertes (stocks bas, virements en attente)

## 👥 Module 2 : Gestion Clients (CRM)

### Liste Clients
- [ ] 🔴 **Table de données** (@tanstack/react-table)
  - [ ] Colonnes : Nom, Email, Téléphone, Nb RDV, CA, Dernière visite, Segment
  - [ ] Tri par colonne
  - [ ] Filtres (segment, date)
  - [ ] Recherche (nom, email, téléphone)
  - [ ] Pagination
  - [ ] Actions : Voir détails, Modifier, Anonymiser
- [ ] 🔴 **Boutons Actions**
  - [ ] Créer nouveau client
  - [ ] Export CSV

### Fiche Client Détaillée
- [ ] 🔴 **Onglet Informations**
  - [ ] Formulaire édition (nom, email, téléphone, adresse)
  - [ ] Date de naissance
  - [ ] Segment (badge coloré)
  - [ ] Notes privées (textarea)
- [ ] 🔴 **Onglet Questionnaire Santé**
  - [ ] Allergies (liste tags)
  - [ ] Problèmes de peau
  - [ ] Traitements en cours
  - [ ] Contre-indications
  - [ ] Date de mise à jour (badge alerte si > 1 an)
- [ ] 🔴 **Onglet Historique RDV**
  - [ ] Liste chronologique réservations
  - [ ] Détails : Date, Prestation, Durée, Prix, Statut
  - [ ] Notes de soin par prestation
  - [ ] Photos avant/après (si dispo)
- [ ] 🔴 **Onglet Achats Produits**
  - [ ] Liste produits achetés
  - [ ] Date, Quantité, Prix
- [ ] 🔴 **Onglet Statistiques**
  - [ ] Prestation favorite (graphique)
  - [ ] Fréquence de visite (jours entre visites)
  - [ ] CA total généré
  - [ ] Panier moyen
- [ ] 🔴 **Actions Rapides**
  - [ ] Créer RDV pour ce client
  - [ ] Envoyer email/SMS
  - [ ] Anonymiser (RGPD)

## 📅 Module 3 : Gestion Réservations

### Vue Calendrier
- [ ] 🔴 **Calendrier** (react-big-calendar ou FullCalendar)
  - [ ] Vues : Jour, Semaine, Mois
  - [ ] Codes couleur par statut
  - [ ] Drag & drop pour déplacer RDV
  - [ ] Double-clic → Détails
  - [ ] Temps de préparation visible (10-15 min)
- [ ] 🔴 **Ajout Manuel RDV**
  - [ ] Formulaire : Client (select), Prestation, Date, Heure
  - [ ] Validation disponibilité
  - [ ] Notes

### Liste Réservations
- [ ] 🔴 **Table de données**
  - [ ] Colonnes : Date, Heure, Client, Prestation, Statut, Paiement
  - [ ] Filtres : Date (plage), Statut, Prestation
  - [ ] Recherche client
  - [ ] Actions : Voir, Modifier, Annuler, Marquer complété
- [ ] 🔴 **Actions en Masse**
  - [ ] Confirmer plusieurs RDV
  - [ ] Envoyer rappel SMS
  - [ ] Export sélection

### Fiche Réservation
- [ ] 🔴 **Détails**
  - [ ] Client (lien fiche)
  - [ ] Prestation, Date, Heure, Durée
  - [ ] Prix total
  - [ ] Statut paiement (badge)
  - [ ] Mode de paiement
  - [ ] Notes client
  - [ ] Notes privées
- [ ] 🔴 **Actions**
  - [ ] Modifier date/heure (calendrier)
  - [ ] Annuler (avec raison)
  - [ ] Marquer complété
  - [ ] Envoyer rappel manuel
  - [ ] Rembourser (si annulation délai)
  - [ ] Imprimer récapitulatif

## 💳 Module 4 : Point de Vente (POS)

### Interface Caisse
- [ ] 🔴 **Vue Panier** (style caisse enregistreuse)
  - [ ] Liste articles (prestations + produits)
  - [ ] Total TTC + détail TVA
  - [ ] Bouton "Ajouter prestation"
  - [ ] Bouton "Ajouter produit"
  - [ ] Bouton "Appliquer code promo" (bon cadeau)
  - [ ] Remise manuelle (admin)
- [ ] 🔴 **Sélection Client**
  - [ ] Recherche rapide (nom, téléphone)
  - [ ] Ou "Client anonyme" (passage unique)
- [ ] 🔴 **Encaissement**
  - [ ] Choix mode paiement : Espèces, CB (Sumup), Lydia, Bon cadeau, Mixte
  - [ ] Si espèces : Input montant reçu → Calcul rendu monnaie
  - [ ] Si CB : Intégration Sumup API ou saisie manuelle
  - [ ] Si bon cadeau : Vérification code
- [ ] 🔴 **Ticket de Caisse**
  - [ ] Génération automatique (PDF)
  - [ ] Impression ou envoi email/SMS
  - [ ] QR code pour récupération

### Gestion de Caisse
- [ ] 🔴 **Ouverture Caisse**
  - [ ] Saisie fond de caisse initial
  - [ ] Date/heure ouverture
- [ ] 🔴 **Suivi Journée**
  - [ ] Total espèces, CB, autres
  - [ ] Nombre de transactions
  - [ ] Mouvements (entrées/sorties)
- [ ] 🔴 **Clôture Caisse**
  - [ ] Comptage espèces
  - [ ] Calcul écart (attendu vs réel)
  - [ ] Génération rapport de caisse (PDF)
  - [ ] Export comptable

## 📦 Module 5 : Gestion Stocks

### Catalogue Produits
- [ ] 🔴 **Liste Produits** (table)
  - [ ] Colonnes : Nom, Catégorie, Prix achat, Prix vente, Stock, Seuil alerte
  - [ ] Filtres : Catégorie, Statut (en vente, rupture)
  - [ ] Recherche
  - [ ] Actions : Voir, Modifier, Supprimer
- [ ] 🔴 **Fiche Produit**
  - [ ] Formulaire CRUD complet
  - [ ] Photo (upload)
  - [ ] Description
  - [ ] Fournisseur (nom, contact)
  - [ ] Prix achat (HT) / Prix vente (TTC)
  - [ ] Stock actuel / Seuil d'alerte
  - [ ] Statut (en vente, rupture, bientôt disponible)

### Mouvements de Stock
- [ ] 🔴 **Historique Mouvements** (table)
  - [ ] Colonnes : Date, Produit, Type (entrée/sortie), Quantité, Raison
  - [ ] Filtres : Date, Type, Produit
- [ ] 🔴 **Ajouter Mouvement**
  - [ ] Type : Entrée (réception fournisseur) ou Sortie (vente, utilisation)
  - [ ] Produit (select)
  - [ ] Quantité
  - [ ] Raison (texte libre)

### Alertes & Commandes
- [ ] 🔴 **Alertes Stock Bas**
  - [ ] Badge notification dans sidebar
  - [ ] Liste produits < seuil
  - [ ] Bouton "Commander"
- [ ] 🟠 **Commandes Fournisseurs** (Phase 2)
  - [ ] Liste produits à commander (suggestions)
  - [ ] Génération bon de commande (PDF)
  - [ ] Suivi livraison

### Statistiques Stocks
- [ ] 🟠 **Dashboard Stocks**
  - [ ] Valeur totale du stock
  - [ ] Top 10 produits vendus
  - [ ] Rotation des stocks
  - [ ] Produits périmés (alerte date)

## 💅 Module 6 : Gestion Prestations

### Liste Prestations
- [ ] 🔴 **Table CRUD** (Create, Read, Update, Delete)
  - [ ] Colonnes : Nom, Catégorie, Durée, Prix, Actif
  - [ ] Filtres : Catégorie, Statut
  - [ ] Actions : Modifier, Supprimer, Activer/Désactiver
  - [ ] Drag & drop pour ordre d'affichage
- [ ] 🔴 **Formulaire Prestation**
  - [ ] Nom
  - [ ] Catégorie (select)
  - [ ] Description courte et longue (textarea)
  - [ ] Durée (minutes)
  - [ ] Prix (€)
  - [ ] Image (upload)
  - [ ] Ordre d'affichage
  - [ ] Actif/Inactif (switch)

### Catégories
- [ ] 🔴 **Gestion Catégories**
  - [ ] CRUD catégories
  - [ ] Nom, Icône, Ordre

## 🎁 Module 7 : Gestion Bons Cadeaux

### Liste Bons Cadeaux
- [ ] 🔴 **Table de données**
  - [ ] Colonnes : Code, Type, Valeur, Acheteur, Bénéficiaire, Date achat, Expiration, Statut
  - [ ] Filtres : Statut, Type, Date
  - [ ] Recherche : Code, Email
  - [ ] Actions : Voir, Prolonger, Désactiver, Renvoyer PDF
- [ ] 🔴 **Fiche Bon Cadeau**
  - [ ] Détails complets
  - [ ] Historique d'utilisation (si utilisé → lien vers RDV)
  - [ ] Actions : Prolonger validité, Désactiver, Renvoyer PDF

### Statistiques Bons Cadeaux
- [ ] 🟠 **Dashboard**
  - [ ] CA généré
  - [ ] Taux d'utilisation (%)
  - [ ] Bons expirés non utilisés
  - [ ] Période favorite (graphique)

## 💰 Module 8 : Gestion Paiements

### Transactions
- [ ] 🔴 **Liste Transactions** (table)
  - [ ] Colonnes : Date, Montant, Mode, Statut, Lié à (RDV ou bon cadeau)
  - [ ] Filtres : Date, Mode, Statut
  - [ ] Recherche : Montant, ID transaction
  - [ ] Actions : Voir détails, Rembourser
- [ ] 🔴 **Virements en Attente**
  - [ ] Liste dédiée (badge notification)
  - [ ] Montant attendu, Date demande
  - [ ] Actions : Confirmer réception, Relancer client

### Statistiques Paiements
- [ ] 🟠 **Dashboard**
  - [ ] Revenus par mode de paiement (graphique)
  - [ ] Taux de succès paiements
  - [ ] Acomptes vs paiements complets
  - [ ] Revenus par prestation

### Remboursements
- [ ] 🔴 **Interface Remboursement**
  - [ ] Sélection transaction
  - [ ] Montant à rembourser (partiel ou total)
  - [ ] Raison (textarea)
  - [ ] Confirmation avec Stripe/PayPal API

## ⏰ Module 9 : Disponibilités

### Configuration Horaires
- [ ] 🔴 **Horaires Hebdomadaires**
  - [ ] Lundi à Dimanche
  - [ ] Heure début / Heure fin
  - [ ] Pause déjeuner (optionnel)
  - [ ] Actif / Inactif par jour (switch)
  - [ ] Durée créneaux (15, 30, 60 min)
- [ ] 🔴 **Sauvegarde**
  - [ ] Validation (heure fin > heure début)
  - [ ] API PUT /admin/availabilities

### Jours Bloqués
- [ ] 🔴 **Liste Dates Bloquées** (table)
  - [ ] Colonnes : Date, Raison
  - [ ] Actions : Modifier, Supprimer
- [ ] 🔴 **Ajouter Jour Bloqué**
  - [ ] Date picker
  - [ ] Raison (congés, férié, formation)
  - [ ] Possibilité de bloquer plage de dates (ex: vacances 15-30 août)

### Vue Temps Réel
- [ ] 🟠 **Calendrier Disponibilités**
  - [ ] Vue mensuelle
  - [ ] Créneaux libres vs réservés
  - [ ] Synchronisation Redis (temps réel)

## ⭐ Module 10 : Avis Google

### Synchronisation Avis
- [ ] 🔴 **Widget Google Reviews**
  - [ ] Note moyenne (étoiles)
  - [ ] Nombre total d'avis
  - [ ] Bouton "Synchroniser" (fetch API)
- [ ] 🔴 **Liste Avis** (table)
  - [ ] Colonnes : Nom, Note, Commentaire, Date
  - [ ] Filtres : Note (1-5 étoiles)
  - [ ] Recherche : Nom, Commentaire
- [ ] 🟠 **Répondre aux Avis** (Phase 2)
  - [ ] Interface réponse (textarea)
  - [ ] Publication via Google API

### Demande d'Avis Automatique
- [ ] 🟠 **Configuration** (Phase 2)
  - [ ] Activer/désactiver envoi auto (48h après RDV)
  - [ ] Template SMS/Email personnalisable
  - [ ] Historique des demandes envoyées

## 📊 Module 11 : Statistiques & Reporting

### Rapports Prédéfinis
- [ ] 🔴 **Rapport Mensuel**
  - [ ] Sélection mois
  - [ ] Affichage : Nb RDV, CA, Prestations populaires, Taux annulation
  - [ ] Export PDF
- [ ] 🟠 **Rapport Annuel**
  - [ ] Évolution mois par mois (tableau)
  - [ ] Comparaison année N vs N-1
  - [ ] Graphiques (revenus, croissance)

### Graphiques Interactifs
- [ ] 🔴 **Réservations** (ligne temporelle)
- [ ] 🔴 **Revenus** (barres mensuelles)
- [ ] 🔴 **Prestations** (camembert répartition)
- [ ] 🟠 **Horaires** (heatmap créneaux demandés)
- [ ] 🟠 **Avis** (évolution note moyenne)

### Export Données
- [ ] 🔴 **Export CSV**
  - [ ] Clients, Réservations, Paiements
  - [ ] Filtres : Plage de dates
  - [ ] Utilisation : Comptabilité

## ⚙️ Module 12 : Paramètres

### Compte Administrateur
- [ ] 🔴 **Profil Admin**
  - [ ] Email, Mot de passe (changement)
  - [ ] Photo de profil (upload)
  - [ ] Préférences (notifications, langue)
- [ ] 🟠 **Gestion Utilisateurs** (si multi-admin)
  - [ ] Liste admins
  - [ ] CRUD (créer, modifier, supprimer)
  - [ ] Rôles : Admin, Super Admin

### Paramètres du Site
- [ ] 🔴 **Informations Générales**
  - [ ] Nom entreprise
  - [ ] Logo (upload)
  - [ ] Couleurs charte (color picker)
  - [ ] Adresse, Téléphone, Email
  - [ ] Réseaux sociaux (Instagram, Facebook)
- [ ] 🟠 **Mentions Légales** (WYSIWYG editor)
  - [ ] CGV
  - [ ] Politique confidentialité
  - [ ] Mentions légales

### Paramètres Réservation
- [ ] 🔴 **Acompte**
  - [ ] Pourcentage (30% par défaut)
  - [ ] Obligatoire ou optionnel (switch)
- [ ] 🔴 **Annulation**
  - [ ] Délai minimum (24h par défaut)
  - [ ] Politique remboursement (texte)
- [ ] 🔴 **Créneaux**
  - [ ] Durée créneaux (15, 30, 60 min)
  - [ ] Délai minimum réservation (2h par défaut)
  - [ ] Nombre max RDV/jour

### Intégrations
- [ ] 🔴 **Clés API** (inputs sécurisés)
  - [ ] Stripe (Public Key, Secret Key)
  - [ ] PayPal (Client ID, Secret)
  - [ ] OVH SMS (Application Key, Secret, Consumer Key)
  - [ ] Resend/SendGrid (API Key)
  - [ ] Google Business (Location ID)
- [ ] 🔴 **Templates SMS/Email** (éditeur)
  - [ ] Confirmation RDV
  - [ ] Rappel 24h
  - [ ] Annulation
  - [ ] Demande d'avis
  - [ ] Variables dynamiques : `{nom}`, `{date}`, `{heure}`, `{prestation}`

---

# PHASE 1 : Déploiement & Infrastructure (Semaine 13)

## 🚀 Déploiement Production

### Configuration Domaines
- [ ] 🔴 **Acheter nom de domaine** (ex: serenaia-beaute.fr)
- [ ] 🔴 **Configuration DNS** :
  - [ ] `serenaia-beaute.fr` → Frontend Public (Vercel)
  - [ ] `www.serenaia-beaute.fr` → Redirection
  - [ ] `admin.serenaia-beaute.fr` → Frontend CRM (Vercel)
  - [ ] `api.serenaia-beaute.fr` → Backend API (Cloud Run ou Railway)

### Backend API
- [ ] 🔴 **Déploiement Cloud Run** (ou Railway/Render)
  - [ ] Créer projet GCP (ou compte Railway)
  - [ ] Créer service Cloud Run
  - [ ] Configurer secrets (Secret Manager)
  - [ ] Déployer image Docker
  - [ ] Configurer domaine custom
  - [ ] SSL automatique (Let's Encrypt)
- [ ] 🔴 **Base de Données**
  - [ ] Cloud SQL PostgreSQL (ou Supabase)
  - [ ] Configurer connexion sécurisée
  - [ ] Appliquer migrations (`alembic upgrade head`)
  - [ ] Créer admin initial (script)
- [ ] 🔴 **Redis**
  - [ ] Memorystore Redis (ou Upstash)
  - [ ] Configurer connexion
- [ ] 🔴 **Cloud Storage**
  - [ ] Créer bucket GCS (ou Cloudflare R2)
  - [ ] Permissions IAM
  - [ ] Upload test

### Frontend Public
- [ ] 🔴 **Déploiement Vercel**
  - [ ] Connecter repo GitHub
  - [ ] Configurer variables d'env (NEXT_PUBLIC_API_URL, etc.)
  - [ ] Déploiement automatique (git push → deploy)
  - [ ] Configurer domaine custom (serenaia-beaute.fr)
  - [ ] SSL automatique

### Frontend CRM
- [ ] 🔴 **Déploiement Vercel**
  - [ ] Connecter repo GitHub
  - [ ] Configurer variables d'env
  - [ ] Déploiement automatique
  - [ ] Configurer domaine custom (admin.serenaia-beaute.fr)

## 🔐 Configuration Sécurité

### SSL/TLS
- [ ] 🔴 **Certificats SSL** (Let's Encrypt via Vercel/Cloud Run)
- [ ] 🔴 **HTTPS obligatoire** (redirections HTTP → HTTPS)
- [ ] 🔴 **HSTS headers** (Strict-Transport-Security)

### Secrets Management
- [ ] 🔴 **Stocker secrets** (GCP Secret Manager ou variables Vercel)
  - [ ] DATABASE_URL
  - [ ] SECRET_KEY (JWT)
  - [ ] Clés API (Stripe, PayPal, OVH, etc.)
- [ ] 🔴 **Rotation secrets** (planifier changements réguliers)

### Monitoring
- [ ] 🔴 **Cloud Monitoring** (GCP) ou Sentry
  - [ ] Logs centralisés (backend)
  - [ ] Monitoring erreurs (frontend + backend)
  - [ ] Alertes (email si erreurs critiques)
- [ ] 🔴 **Uptime Monitoring** (UptimeRobot ou Cloud Monitoring)
  - [ ] Check toutes les 5 min
  - [ ] Alerte si down > 2 min

### Backups
- [ ] 🔴 **Configurer backups automatiques**
  - [ ] PostgreSQL : Snapshot quotidien (3h du matin)
  - [ ] Rétention : 7 jours + 1 mensuel (12 mois)
  - [ ] Cloud Storage : Versioning activé
- [ ] 🔴 **Tester restauration** (procédure documentée)

## 🧪 Tests Production

### Tests de Non-Régression
- [ ] 🔴 **Tests E2E sur Production**
  - [ ] Réservation complète
  - [ ] Achat bon cadeau
  - [ ] Login admin → CRUD
- [ ] 🔴 **Tests Paiements** (mode test Stripe)
  - [ ] Paiement CB réussi
  - [ ] Paiement échoué
  - [ ] Webhook reçu et traité

### Performance
- [ ] 🔴 **Load Testing** (Locust ou k6)
  - [ ] 100 utilisateurs simultanés
  - [ ] Vérifier P95 < 200ms
- [ ] 🔴 **Lighthouse Audit**
  - [ ] Score > 90 (Performance, SEO, Accessibilité)

## 📊 Analytics

### Google Analytics 4
- [ ] 🔴 **Setup GA4**
  - [ ] Créer propriété GA4
  - [ ] Installer tag sur frontend public
  - [ ] Événements personnalisés (réservation, bon cadeau)
- [ ] 🔴 **Google Search Console**
  - [ ] Ajouter propriété
  - [ ] Soumettre sitemap.xml
  - [ ] Vérifier indexation

### Google Business Profile
- [ ] 🔴 **Créer/Optimiser Profil**
  - [ ] Adresse, Horaires, Téléphone
  - [ ] Photos professionnelles
  - [ ] Description optimisée SEO
  - [ ] Catégorie : Institut de beauté
- [ ] 🔴 **Configurer API** (récupération avis)

---

# PHASE 1 : Lancement & Go-Live (Semaine 14)

## 🎉 Pré-Lancement

### Tests Finaux
- [ ] 🔴 **Checklist complète**
  - [ ] Tous les endpoints API fonctionnent
  - [ ] Tous les paiements fonctionnent (CB, PayPal, virement)
  - [ ] SMS envoyés automatiquement (test OVH)
  - [ ] Emails envoyés (test Resend/SendGrid)
  - [ ] PDFs générés (bons cadeaux, factures)
  - [ ] Webhooks Stripe/PayPal testés
  - [ ] Login admin fonctionne
  - [ ] Tous les modules CRM accessibles
- [ ] 🔴 **Tests Utilisateurs** (bêta testeurs)
  - [ ] 3-5 personnes testent réservation
  - [ ] Feedback recueilli
  - [ ] Bugs critiques corrigés

### Contenu Final
- [ ] 🔴 **Vérifier contenu**
  - [ ] Textes finaux validés (ou textes générés OK pour MVP)
  - [ ] Photos ajoutées (répertoire `/public/images/`)
  - [ ] Logo présent
  - [ ] CGV validées par avocat (ou template OK pour MVP)
  - [ ] Politique confidentialité
  - [ ] Mentions légales

### Formation Admin
- [ ] 🔴 **Former l'utilisateur final** (vous)
  - [ ] Vidéo démo du CRM (ou session live)
  - [ ] Documentation utilisateur (`GUIDE_CRM.md`)
  - [ ] FAQ technique

## 🚀 Lancement

### Communication
- [ ] 🔴 **Annonce Lancement**
  - [ ] Post Instagram/Facebook
  - [ ] Email aux contacts existants
  - [ ] Story : "Nouveau site en ligne !"
- [ ] 🔴 **Offre de Lancement** (optionnel)
  - [ ] -10% première réservation
  - [ ] Bon cadeau offert si parrainage

### Monitoring Jour J
- [ ] 🔴 **Surveillance Active** (24-48h)
  - [ ] Vérifier logs (erreurs ?)
  - [ ] Vérifier paiements (reçus ?)
  - [ ] Vérifier SMS/emails (envoyés ?)
  - [ ] Répondre rapidement aux problèmes

## 📈 Post-Lancement

### Collecte Feedback
- [ ] 🟠 **Semaine 1-2**
  - [ ] Interroger premières clientes (expérience site)
  - [ ] Identifier bugs/améliorations
  - [ ] Prioriser corrections

### Optimisations
- [ ] 🟠 **Corrections Mineures**
  - [ ] Typos, textes à améliorer
  - [ ] Ajustements UI/UX
  - [ ] Optimisations performance

---

# PHASE 2 : Extensions & Améliorations (Mois 5-6)

## 🎯 Module 13 : Programme de Fidélité

### Système de Points
- [ ] 🟠 **Modèle BDD** (table `loyalty_points`)
- [ ] 🟠 **Logique Accumulation**
  - [ ] 1€ = 1 point automatique
  - [ ] Double points événements spéciaux
- [ ] 🟠 **Utilisation Points**
  - [ ] 100 points = 5€ de réduction
  - [ ] Déduction au paiement (POS + en ligne)
- [ ] 🟠 **Niveaux Fidélité**
  - [ ] Bronze, Argent, Or, Platine
  - [ ] Calcul automatique selon CA généré
  - [ ] Avantages par niveau

### Interface CRM
- [ ] 🟠 **Dashboard Fidélité**
  - [ ] Stats : Nb clients par niveau
  - [ ] Points distribués / Points utilisés
- [ ] 🟠 **Fiche Client**
  - [ ] Affichage solde points
  - [ ] Niveau actuel (badge)
  - [ ] Historique gains/utilisations

### Interface Publique
- [ ] 🟠 **Espace Client** (optionnel)
  - [ ] Login client (email + password)
  - [ ] Carte virtuelle (QR code)
  - [ ] Solde points
  - [ ] Historique RDV

## 📸 Module 14 : Galerie Avant/Après

### Gestion Photos CRM
- [ ] 🟠 **Upload Photos**
  - [ ] Interface upload dans CRM
  - [ ] Association client + prestation
  - [ ] Tags (type prestation, difficulté)
- [ ] 🟠 **Consentement RGPD**
  - [ ] Formulaire signé électroniquement
  - [ ] Choix : Site web (oui/non), Réseaux sociaux (oui/non)
  - [ ] Floutage visage (option)
  - [ ] Stockage consentements (table `consents`)
- [ ] 🟠 **Galerie Admin**
  - [ ] Liste toutes les photos
  - [ ] Filtres : Client, Prestation, Consentement
  - [ ] Sélection pour galerie publique (switch)

### Galerie Publique
- [ ] 🟠 **Page Galerie** (frontend public)
  - [ ] Affichage meilleures photos (sélection admin)
  - [ ] Filtres par prestation
  - [ ] Lightbox (zoom)
  - [ ] Respect consentements

## 🤖 Module 15 : Automatisations Marketing

### Campagnes Automatiques
- [ ] 🟠 **Anniversaire Client**
  - [ ] Cron job quotidien (vérifier anniversaires)
  - [ ] Envoi SMS/Email automatique (-20% offert)
  - [ ] Template personnalisé
- [ ] 🟠 **Réactivation Inactifs**
  - [ ] Cron job hebdomadaire (clients > 3 mois sans visite)
  - [ ] Envoi offre spéciale
- [ ] 🟠 **Recommandation Réachat Produit**
  - [ ] 2 mois après achat produit
  - [ ] SMS : "Votre [produit] arrive bientôt à sa fin !"
- [ ] 🟠 **Saisonnalité**
  - [ ] Promo épilation avant été
  - [ ] Promo soins hydratants hiver

### Automatisations Opérationnelles
- [ ] 🟠 **Rappel Mise à Jour Questionnaire Santé**
  - [ ] Cron annuel (vérifier dates > 1 an)
  - [ ] Email/SMS rappel
- [ ] 🟠 **Demande Parrainage**
  - [ ] Après 3 prestations
  - [ ] Offre : 10€ parrain + 10€ filleul

## 💬 Module 16 : Messagerie Intégrée

### SMS depuis CRM
- [ ] 🟠 **Interface Envoi SMS**
  - [ ] Depuis fiche client (bouton "Envoyer SMS")
  - [ ] Textarea message
  - [ ] Templates pré-enregistrés (select)
  - [ ] Envoi via OVH API
- [ ] 🟠 **Historique Conversations**
  - [ ] Table `notifications` affichée dans fiche client
  - [ ] Filtre : SMS uniquement
- [ ] 🟠 **Campagnes SMS Groupées**
  - [ ] Sélection segment (VIP, inactifs, etc.)
  - [ ] Message personnalisé (variables dynamiques)
  - [ ] Envoi en masse (async avec Celery ou BackgroundTasks)

### Email depuis CRM
- [ ] 🟠 **Interface Envoi Email**
  - [ ] Depuis fiche client
  - [ ] Éditeur WYSIWYG (ex: TinyMCE)
  - [ ] Templates pré-enregistrés
  - [ ] Pièces jointes (factures, bons cadeaux)
- [ ] 🟠 **Tracking**
  - [ ] Ouverture (pixel tracking)
  - [ ] Clics (liens trackés)
  - [ ] Affichage dans fiche client

---

# PHASE 3 : Évolutions Futures (Mois 7+)

## 🔮 Fonctionnalités Avancées (À Planifier)

### Intégrations Comptables
- [ ] 🟡 **Pennylane, Quickbooks, Sage**
  - [ ] Export automatique factures
  - [ ] Synchronisation paiements

### Marketplace Produits
- [ ] 🟡 **Boutique E-Commerce Intégrée**
  - [ ] Vente produits en ligne
  - [ ] Commande + livraison
  - [ ] Recommandations après prestation

### Multi-Utilisateurs CRM
- [ ] 🟡 **Si embauche d'une collaboratrice**
  - [ ] Gestion de plusieurs techniciennes
  - [ ] Attribution RDV par technicienne
  - [ ] Statistiques individuelles

### Rendez-Vous Récurrents
- [ ] 🟡 **Abonnements**
  - [ ] Forfait : 4 soins/mois (ex: manucure)
  - [ ] Paiement récurrent Stripe Subscriptions
  - [ ] Réservation automatique créneaux

---

# MAINTENANCE & SUIVI

## 📊 Hebdomadaire
- [ ] 🔵 **Vérifier monitoring** (erreurs Sentry, logs)
- [ ] 🔵 **Vérifier backups** (dernier backup OK ?)
- [ ] 🔵 **Répondre aux feedbacks clients**

## 📅 Mensuel
- [ ] 🔵 **Analyser statistiques** (GA4, CRM)
- [ ] 🔵 **Optimisations** (corrections bugs mineurs)
- [ ] 🔵 **Mises à jour dépendances** (npm, pip)

## 📆 Trimestriel
- [ ] 🔵 **Tester restauration backup**
- [ ] 🔵 **Audit sécurité** (scan vulnérabilités)
- [ ] 🔵 **Roadmap** (planifier prochaines features)

## 📅 Annuel
- [ ] 🔵 **Renouveler nom de domaine**
- [ ] 🔵 **Mettre à jour CGV** (si changements légaux)
- [ ] 🔵 **Audit comptable** (expert-comptable)

---

## 📈 Estimation Durée Totale

| Phase | Durée Estimée | Charge Travail |
|-------|---------------|----------------|
| **Phase 0 : Préparation** | 1-2 semaines | 20-40h |
| **Phase 1 : Backend API (MVP)** | 3-4 semaines | 120-160h |
| **Phase 1 : Frontend Public (MVP)** | 2-3 semaines | 80-120h |
| **Phase 1 : Frontend CRM (MVP)** | 2-3 semaines | 80-120h |
| **Phase 1 : Déploiement** | 1 semaine | 20-40h |
| **Phase 1 : Lancement** | 1 semaine | 10-20h |
| **Total Phase 1 (MVP)** | **10-16 semaines** | **330-500h** |
| **Phase 2 : Extensions** | 6-8 semaines | 200-300h |
| **Total Projet Complet** | **16-24 semaines** | **530-800h** |

**Équivalent :** 3-6 mois selon disponibilité (full-time vs part-time)

---

## ✅ Critères de Succès

### MVP Réussi Si :
- [ ] Site public en ligne et fonctionnel
- [ ] Réservations en ligne possibles (paiement OK)
- [ ] Bons cadeaux achetables (PDF généré)
- [ ] CRM accessible et utilisable (12 modules)
- [ ] SMS/Emails automatiques envoyés
- [ ] Aucun bug critique
- [ ] Performance > 90 (Lighthouse)
- [ ] Sécurité OK (pas de vulnérabilités critiques)

### Projet Complet Réussi Si :
- [ ] Tout le MVP +
- [ ] Programme fidélité actif
- [ ] Galerie photos alimentée
- [ ] Automatisations marketing en place
- [ ] Messagerie intégrée utilisée
- [ ] Adoption par les clientes (> 50 RDV en ligne/mois)
- [ ] Satisfaction utilisateur (> 4,5/5 avis Google)

---

**Date de création:** 2026-01-11
**Version:** 1.0
**Total items:** ~500 tâches

# Plan d'Atomisation - Sérénaia Beauté

**Objectif**: Transformer les 93 issues en ~500-600 micro-issues de 1-2h max chacune

## Principes d'Atomisation

### Taille Cible
- **Durée**: 30min - 2h max par micro-issue
- **Scope**: 1 seul fichier ou 1 seule fonctionnalité
- **Dépendances**: Maximum 2-3 autres micro-issues
- **Validation**: Testable immédiatement

### Nomenclature
- **Backend**: `BACK-X.Y` (issue parent X, sous-issue Y)
- **Frontend Public**: `FP-X.Y`
- **Frontend CRM**: `FC-X.Y`

### Labels
- `atomic` : Tâche atomique
- `quick-win` : < 1h
- `medium-task` : 1-2h
- Conserver labels existants (priority, phase)

---

## PHASE 0 - Préparation (6 issues → ~25 micro-issues)

### #1 Terminal Sumup → 4 micro-issues
- BACK-1.1: Créer compte Sumup professionnel
- BACK-1.2: Commander terminal Sumup Air
- BACK-1.3: Configurer compte Stripe production
- BACK-1.4: Configurer compte PayPal Business

### #2 Décision Virements → 3 micro-issues
- BACK-2.1: Analyser options virements bons cadeaux (A/B/C)
- BACK-2.2: Documenter décision dans DECISIONS.md
- BACK-2.3: Créer workflow virement choisi

### #3 CGV → 5 micro-issues
- BACK-3.1: Générer CGV avec générateur en ligne
- BACK-3.2: Adapter CGV secteur esthétique
- BACK-3.3: Valider mentions légales RGPD
- BACK-3.4: Créer fichier docs/CGV.md
- BACK-3.5: Créer fichier docs/MENTIONS_LEGALES.md

### #4 Zone géographique → 3 micro-issues
- BACK-4.1: Définir adresse institut (Google Maps)
- BACK-4.2: Définir rayon déplacement à domicile
- BACK-4.3: Documenter dans config.py

### #5 Catalogue produits → 5 micro-issues
- BACK-5.1: Lister 5-10 produits vendus
- BACK-5.2: Définir prix et descriptions
- BACK-5.3: Créer fichier seed_data/products.json
- BACK-5.4: Trouver/créer images produits
- BACK-5.5: Documenter fournisseurs

### #6 Architecture BDD → 5 micro-issues
- BACK-6.1: Analyser gestion acomptes partiels
- BACK-6.2: Modifier table payments (champ amount_type)
- BACK-6.3: Ajouter relations Payment-Booking
- BACK-6.4: Mettre à jour ARCHITECTURE_BDD.md
- BACK-6.5: Créer migration Alembic

---

## PHASE 1 BACKEND (26 issues → ~180 micro-issues)

### #7 Setup FastAPI → 12 micro-issues
- BACK-7.1: Créer venv Python 3.11
- BACK-7.2: Créer requirements.txt
- BACK-7.3: Créer structure dossiers app/
- BACK-7.4: Créer app/main.py (FastAPI init)
- BACK-7.5: Créer app/config.py (Settings)
- BACK-7.6: Créer app/database.py (SQLAlchemy)
- BACK-7.7: Créer app/deps.py (dependencies)
- BACK-7.8: Créer api/v1/router.py
- BACK-7.9: Créer .env.example
- BACK-7.10: Créer .gitignore
- BACK-7.11: Health check endpoint /health
- BACK-7.12: Test démarrage serveur uvicorn

### #8 Modèles SQLAlchemy → 18 micro-issues (1 par table + base)
- BACK-8.1: Créer models/base.py (Base SQLAlchemy)
- BACK-8.2: Créer models/user.py
- BACK-8.3: Créer models/client.py
- BACK-8.4: Créer models/service.py
- BACK-8.5: Créer models/booking.py
- BACK-8.6: Créer models/payment.py
- BACK-8.7: Créer models/gift_card.py
- BACK-8.8: Créer models/product.py
- BACK-8.9: Créer models/stock_movement.py
- BACK-8.10: Créer models/loyalty_point.py
- BACK-8.11: Créer models/notification.py
- BACK-8.12: Créer models/availability.py
- BACK-8.13: Créer models/blocked_slot.py
- BACK-8.14: Créer models/review.py
- BACK-8.15: Créer models/photo.py
- BACK-8.16: Créer models/automation.py
- BACK-8.17: Créer models/__init__.py (imports)
- BACK-8.18: Valider relations entre tables

### #9 Alembic → 6 micro-issues
- BACK-9.1: Installer alembic
- BACK-9.2: Init alembic: `alembic init alembic`
- BACK-9.3: Configurer alembic.ini (DATABASE_URL)
- BACK-9.4: Configurer env.py (import models)
- BACK-9.5: Générer migration initiale
- BACK-9.6: Test migration up/down

### #10 Stripe → 10 micro-issues
- BACK-10.1: Créer compte Stripe test
- BACK-10.2: Installer stripe SDK
- BACK-10.3: Créer services/stripe_service.py
- BACK-10.4: Implémenter create_payment_intent()
- BACK-10.5: Implémenter confirm_payment()
- BACK-10.6: Implémenter refund_payment()
- BACK-10.7: Créer webhook endpoint /webhooks/stripe
- BACK-10.8: Gérer événement payment_intent.succeeded
- BACK-10.9: Gérer événement payment_intent.failed
- BACK-10.10: Tests unitaires stripe_service

### #11 Auth JWT → 8 micro-issues
- BACK-11.1: Créer utils/security.py (hash password)
- BACK-11.2: Créer utils/jwt.py (create_access_token)
- BACK-11.3: Créer schemas/auth.py (Token, Login)
- BACK-11.4: Créer api/v1/auth.py router
- BACK-11.5: Endpoint POST /auth/login
- BACK-11.6: Dependency get_current_user
- BACK-11.7: Créer premier user admin (seed)
- BACK-11.8: Tests auth flow complet

### #12 API Booking → 10 micro-issues
- BACK-12.1: Créer schemas/booking.py (BookingCreate)
- BACK-12.2: Créer services/booking_service.py
- BACK-12.3: Implémenter check_availability()
- BACK-12.4: Implémenter create_booking()
- BACK-12.5: Créer api/v1/bookings.py router
- BACK-12.6: Endpoint POST /bookings
- BACK-12.7: Endpoint GET /bookings/{id}
- BACK-12.8: Endpoint PATCH /bookings/{id}/status
- BACK-12.9: Trigger notification après création
- BACK-12.10: Tests CRUD bookings

### #13 OVH SMS → 8 micro-issues
- BACK-13.1: Créer compte OVH API
- BACK-13.2: Générer credentials OVH
- BACK-13.3: Installer ovh SDK
- BACK-13.4: Créer services/sms_service.py
- BACK-13.5: Implémenter send_sms()
- BACK-13.6: Template SMS confirmation booking
- BACK-13.7: Template SMS rappel 24h
- BACK-13.8: Tests envoi SMS (mode test)

### #14 Docker → 7 micro-issues
- BACK-14.1: Créer Dockerfile backend
- BACK-14.2: Créer docker-compose.yml (postgres)
- BACK-14.3: Ajouter service redis dans docker-compose
- BACK-14.4: Ajouter service backend dans docker-compose
- BACK-14.5: Script init-db.sh pour migrations
- BACK-14.6: Test build image Docker
- BACK-14.7: Test docker-compose up complet

### #15 Redis → 6 micro-issues
- BACK-15.1: Installer redis SDK
- BACK-15.2: Créer utils/redis.py (connexion)
- BACK-15.3: Implémenter cache_set()
- BACK-15.4: Implémenter cache_get()
- BACK-15.5: Implémenter cache_delete()
- BACK-15.6: Tests cache avec Redis

### #16 PayPal → 8 micro-issues
- BACK-16.1: Créer compte PayPal Business sandbox
- BACK-16.2: Installer paypalrestsdk
- BACK-16.3: Créer services/paypal_service.py
- BACK-16.4: Implémenter create_payment()
- BACK-16.5: Implémenter execute_payment()
- BACK-16.6: Webhook endpoint /webhooks/paypal
- BACK-16.7: Gérer événement PAYMENT.SALE.COMPLETED
- BACK-16.8: Tests PayPal service

### #17 Sumup → 6 micro-issues
- BACK-17.1: Créer compte Sumup développeur
- BACK-17.2: Obtenir API credentials Sumup
- BACK-17.3: Créer services/sumup_service.py
- BACK-17.4: Implémenter create_checkout()
- BACK-17.5: Implémenter check_payment_status()
- BACK-17.6: Tests Sumup service (sandbox)

### #18 Tests → 10 micro-issues
- BACK-18.1: Setup pytest.ini configuration
- BACK-18.2: Créer tests/conftest.py (fixtures)
- BACK-18.3: Créer fixture test_db
- BACK-18.4: Créer fixture test_client
- BACK-18.5: Tests models (test_models.py)
- BACK-18.6: Tests auth (test_auth.py)
- BACK-18.7: Tests bookings (test_bookings.py)
- BACK-18.8: Tests payments (test_payments.py)
- BACK-18.9: Configurer coverage (pytest-cov)
- BACK-18.10: Atteindre 80%+ coverage

### #19 Sécurité → 8 micro-issues
- BACK-19.1: Installer slowapi (rate limiting)
- BACK-19.2: Configurer rate limiter global
- BACK-19.3: Configurer CORS middleware
- BACK-19.4: Ajouter security headers middleware
- BACK-19.5: Configurer TrustedHostMiddleware
- BACK-19.6: Ajouter GZipMiddleware
- BACK-19.7: Créer endpoint /security-check
- BACK-19.8: Tests sécurité (rate limit)

### #20 Logging → 7 micro-issues
- BACK-20.1: Installer google-cloud-logging
- BACK-20.2: Installer sentry-sdk
- BACK-20.3: Créer utils/logging.py
- BACK-20.4: Configurer Google Cloud Logging
- BACK-20.5: Configurer Sentry (erreurs)
- BACK-20.6: Logging middleware (requêtes)
- BACK-20.7: Tests logging et erreurs

### #21 CI/CD → 9 micro-issues
- BACK-21.1: Créer .github/workflows/test.yml
- BACK-21.2: Workflow test (pytest sur PR)
- BACK-21.3: Workflow lint (ruff/black)
- BACK-21.4: Créer .github/workflows/deploy.yml
- BACK-21.5: Build image Docker dans CI
- BACK-21.6: Push vers Google Artifact Registry
- BACK-21.7: Deploy vers Cloud Run
- BACK-21.8: Health check post-deploy
- BACK-21.9: Rollback automatique si échec

### #22 Documentation → 6 micro-issues
- BACK-22.1: Configurer OpenAPI metadata
- BACK-22.2: Ajouter docstrings tous endpoints
- BACK-22.3: Créer examples Pydantic schemas
- BACK-22.4: Configurer Swagger UI (/docs)
- BACK-22.5: Configurer ReDoc (/redoc)
- BACK-22.6: Créer README.md API complet

### #23 Emails → 8 micro-issues
- BACK-23.1: Créer compte Resend/SendGrid
- BACK-23.2: Installer resend SDK
- BACK-23.3: Créer services/email_service.py
- BACK-23.4: Créer templates/email/booking_confirmation.html
- BACK-23.5: Créer templates/email/gift_card.html
- BACK-23.6: Implémenter send_email()
- BACK-23.7: Implémenter send_template_email()
- BACK-23.8: Tests envoi emails

### #24 API Disponibilités → 8 micro-issues
- BACK-24.1: Créer schemas/availability.py
- BACK-24.2: Créer services/availability_service.py
- BACK-24.3: Implémenter get_available_slots()
- BACK-24.4: Implémenter block_slot()
- BACK-24.5: Créer api/v1/availabilities.py
- BACK-24.6: Endpoint GET /availabilities
- BACK-24.7: Endpoint POST /availabilities/block
- BACK-24.8: Tests disponibilités

### #25 API Bons Cadeaux → 8 micro-issues
- BACK-25.1: Créer schemas/gift_card.py
- BACK-25.2: Créer services/gift_card_service.py
- BACK-25.3: Implémenter create_gift_card()
- BACK-25.4: Implémenter validate_gift_card()
- BACK-25.5: Créer api/v1/gift_cards.py
- BACK-25.6: Endpoint POST /gift-cards/purchase
- BACK-25.7: Endpoint POST /gift-cards/validate
- BACK-25.8: Tests gift cards

### #26 API Clients → 10 micro-issues
- BACK-26.1: Créer schemas/client.py
- BACK-26.2: Créer services/client_service.py
- BACK-26.3: Créer api/v1/clients.py
- BACK-26.4: Endpoint POST /clients
- BACK-26.5: Endpoint GET /clients
- BACK-26.6: Endpoint GET /clients/{id}
- BACK-26.7: Endpoint PATCH /clients/{id}
- BACK-26.8: Endpoint GET /clients/{id}/history
- BACK-26.9: Endpoint GET /clients/search
- BACK-26.10: Tests CRUD clients

---

## FRONTEND PUBLIC (15 issues → ~90 micro-issues)

### #1 Setup Next.js → 10 micro-issues
- FP-1.1: Créer projet Next.js 14 App Router
- FP-1.2: Installer Tailwind CSS
- FP-1.3: Installer shadcn/ui
- FP-1.4: Configurer tailwind.config.ts
- FP-1.5: Créer app/layout.tsx
- FP-1.6: Créer app/page.tsx
- FP-1.7: Configurer fonts (Google Fonts)
- FP-1.8: Créer lib/utils.ts (cn helper)
- FP-1.9: Créer .env.local.example
- FP-1.10: Test build production

### #2 Page Accueil → 8 micro-issues
- FP-2.1: Créer components/Hero.tsx
- FP-2.2: Créer components/ServicesSection.tsx
- FP-2.3: Créer components/TestimonialsSection.tsx
- FP-2.4: Créer components/CTASection.tsx
- FP-2.5: Assembler app/page.tsx
- FP-2.6: Ajouter animations (framer-motion)
- FP-2.7: Optimiser images (next/image)
- FP-2.8: Tests Lighthouse (>90 score)

### #3 Page Réservation → 10 micro-issues
- FP-3.1: Créer app/booking/page.tsx
- FP-3.2: Créer components/ServiceSelector.tsx
- FP-3.3: Créer components/DateTimePicker.tsx
- FP-3.4: Créer components/ClientForm.tsx
- FP-3.5: Créer components/PaymentForm.tsx
- FP-3.6: Créer lib/api/bookings.ts (API calls)
- FP-3.7: Gérer state formulaire (Zustand)
- FP-3.8: Intégrer Stripe Elements
- FP-3.9: Confirmation après paiement
- FP-3.10: Tests formulaire complet

### #4 Page Bons Cadeaux → 6 micro-issues
- FP-4.1: Créer app/gift-cards/page.tsx
- FP-4.2: Créer components/GiftCardSelector.tsx
- FP-4.3: Créer components/GiftCardForm.tsx
- FP-4.4: Intégrer paiement Stripe
- FP-4.5: Génération PDF bon cadeau
- FP-4.6: Email confirmation avec PDF

### #5 Déploiement Vercel → 6 micro-issues
- FP-5.1: Créer compte Vercel
- FP-5.2: Connecter repository GitHub
- FP-5.3: Configurer variables environnement
- FP-5.4: Setup domaine custom
- FP-5.5: Configurer SEO (metadata)
- FP-5.6: Test déploiement production

### #6 Page Services → 5 micro-issues
- FP-6.1: Créer app/services/page.tsx
- FP-6.2: Créer components/ServiceCard.tsx
- FP-6.3: Créer components/ServiceFilters.tsx
- FP-6.4: Fetch services depuis API
- FP-6.5: Animations et transitions

### #7 Page À Propos → 4 micro-issues
- FP-7.1: Créer app/about/page.tsx
- FP-7.2: Section histoire/valeurs
- FP-7.3: Section équipe (si multi-praticiens)
- FP-7.4: Images et galerie photos

### #8 Page Contact → 5 micro-issues
- FP-8.1: Créer app/contact/page.tsx
- FP-8.2: Créer components/ContactForm.tsx
- FP-8.3: Intégrer Google Maps
- FP-8.4: Afficher horaires
- FP-8.5: API route /api/contact

### #9 Widget Avis Google → 4 micro-issues
- FP-9.1: Créer composant GoogleReviews.tsx
- FP-9.2: Intégrer Google Places API
- FP-9.3: Afficher moyenne + étoiles
- FP-9.4: Carrousel derniers avis

### #10 Layout Composants → 6 micro-issues
- FP-10.1: Créer components/Header.tsx
- FP-10.2: Créer components/Footer.tsx
- FP-10.3: Créer components/Navigation.tsx
- FP-10.4: Menu mobile responsive
- FP-10.5: Sticky header au scroll
- FP-10.6: Dark mode toggle (optionnel)

### #11 Mentions Légales → 4 micro-issues
- FP-11.1: Créer app/legal/page.tsx
- FP-11.2: Créer app/terms/page.tsx (CGV)
- FP-11.3: Créer app/privacy/page.tsx
- FP-11.4: Banner cookies (RGPD)

### #12 Composant Calendrier → 5 micro-issues
- FP-12.1: Installer react-day-picker
- FP-12.2: Créer components/Calendar.tsx
- FP-12.3: Fetch disponibilités API
- FP-12.4: Désactiver dates indisponibles
- FP-12.5: Sélection heure (slots)

### #13 Composant Paiement → 5 micro-issues
- FP-13.1: Installer @stripe/stripe-js
- FP-13.2: Créer components/StripeCheckout.tsx
- FP-13.3: Setup Stripe Elements
- FP-13.4: Gérer erreurs paiement
- FP-13.5: Success/cancel callbacks

### #14 Tests E2E → 6 micro-issues
- FP-14.1: Installer Playwright
- FP-14.2: Configurer playwright.config.ts
- FP-14.3: Test booking flow complet
- FP-14.4: Test gift card purchase
- FP-14.5: Test formulaire contact
- FP-14.6: CI integration (GitHub Actions)

### #15 Optimisations → 6 micro-issues
- FP-15.1: Optimiser images (webp, responsive)
- FP-15.2: Lazy loading composants
- FP-15.3: Code splitting routes
- FP-15.4: Compression gzip/brotli
- FP-15.5: Cache stratégies (ISR)
- FP-15.6: Lighthouse audit >95

---

## FRONTEND CRM (20 issues → ~120 micro-issues)

### #1 Setup Next.js CRM → 10 micro-issues
- FC-1.1: Créer projet Next.js 14
- FC-1.2: Installer shadcn/ui composants
- FC-1.3: Créer layout CRM (sidebar)
- FC-1.4: Configurer next-auth
- FC-1.5: Créer middleware.ts (protection)
- FC-1.6: Setup Zustand stores
- FC-1.7: Créer lib/api/client.ts
- FC-1.8: Configurer .env.local
- FC-1.9: Theme provider (dark mode)
- FC-1.10: Test build

### #2 Page Login → 5 micro-issues
- FC-2.1: Créer app/login/page.tsx
- FC-2.2: Créer components/LoginForm.tsx
- FC-2.3: Intégrer next-auth credentials
- FC-2.4: Redirect après login
- FC-2.5: Tests auth flow

### #3 Dashboard → 8 micro-issues
- FC-3.1: Créer app/dashboard/page.tsx
- FC-3.2: Créer components/StatCard.tsx
- FC-3.3: Widget CA du jour
- FC-3.4: Widget RDV aujourd'hui
- FC-3.5: Widget Nouveaux clients
- FC-3.6: Graphique CA 30 jours (recharts)
- FC-3.7: Liste dernières réservations
- FC-3.8: Fetch data depuis API

### #4 Module Réservations → 8 micro-issues
- FC-4.1: Créer app/bookings/page.tsx
- FC-4.2: Créer components/BookingsTable.tsx
- FC-4.3: Filtres (date, status, client)
- FC-4.4: Créer app/bookings/[id]/page.tsx
- FC-4.5: Actions (confirmer, annuler)
- FC-4.6: Modal modification booking
- FC-4.7: Export CSV réservations
- FC-4.8: Tests CRUD bookings

### #5 Module Clients Liste → 6 micro-issues
- FC-5.1: Créer app/clients/page.tsx
- FC-5.2: Créer components/ClientsTable.tsx
- FC-5.3: Pagination clients
- FC-5.4: Filtres simples
- FC-5.5: Bouton créer client
- FC-5.6: Modal rapide client

### #6 Déploiement Vercel → 5 micro-issues
- FC-6.1: Setup Vercel project
- FC-6.2: Variables environnement
- FC-6.3: Configurer auth secret
- FC-6.4: Protection IP/password
- FC-6.5: Test déploiement

### #7 Clients Fiche Détaillée → 8 micro-issues
- FC-7.1: Créer app/clients/[id]/page.tsx
- FC-7.2: Onglet Informations
- FC-7.3: Onglet Historique RDV
- FC-7.4: Onglet Paiements
- FC-7.5: Onglet Fidélité
- FC-7.6: Onglet Notes
- FC-7.7: Édition informations
- FC-7.8: Calcul statistiques client

### #8 Clients Recherche → 6 micro-issues
- FC-8.1: Créer components/ClientSearch.tsx
- FC-8.2: Search par nom/email/téléphone
- FC-8.3: Filtres avancés (tags, fidélité)
- FC-8.4: Tri colonnes tableau
- FC-8.5: Sauvegarde filtres
- FC-8.6: Export résultats

### #9 Vue Calendrier → 10 micro-issues
- FC-9.1: Installer @fullcalendar/react
- FC-9.2: Créer app/calendar/page.tsx
- FC-9.3: Configurer FullCalendar
- FC-9.4: Fetch événements (bookings)
- FC-9.5: Vue jour/semaine/mois
- FC-9.6: Drag & drop RDV
- FC-9.7: Modal création RDV rapide
- FC-9.8: Color coding par service
- FC-9.9: Bloquer créneaux
- FC-9.10: Sync modifications API

### #10 Point de Vente → 10 micro-issues
- FC-10.1: Créer app/pos/page.tsx
- FC-10.2: Interface caisse tactile
- FC-10.3: Sélection produits
- FC-10.4: Sélection services
- FC-10.5: Panier temps réel
- FC-10.6: Sélection client existant
- FC-10.7: Paiement (Stripe/Sumup)
- FC-10.8: Ticket de caisse (print)
- FC-10.9: Historique ventes
- FC-10.10: Tests POS flow

### #11 Gestion Stocks → 8 micro-issues
- FC-11.1: Créer app/inventory/page.tsx
- FC-11.2: Liste produits avec stock
- FC-11.3: Alertes stock bas
- FC-11.4: Modal ajout produit
- FC-11.5: Modal mouvement stock
- FC-11.6: Historique mouvements
- FC-11.7: Export inventaire
- FC-11.8: Tests CRUD stocks

### #12 Gestion Prestations → 6 micro-issues
- FC-12.1: Créer app/services/page.tsx
- FC-12.2: Liste services/tarifs
- FC-12.3: Modal créer service
- FC-12.4: Modal éditer service
- FC-12.5: Activer/désactiver service
- FC-12.6: Catégories services

### #13 Bons Cadeaux Admin → 6 micro-issues
- FC-13.1: Créer app/gift-cards/page.tsx
- FC-13.2: Liste bons cadeaux
- FC-13.3: Filtres (utilisé/expiré)
- FC-13.4: Validation bon cadeau
- FC-13.5: Détails transactions
- FC-13.6: Régénérer PDF

### #14 Paiements → 8 micro-issues
- FC-14.1: Créer app/payments/page.tsx
- FC-14.2: Liste toutes transactions
- FC-14.3: Filtres (méthode, status, date)
- FC-14.4: Détails transaction
- FC-14.5: Initier remboursement
- FC-14.6: Export comptable
- FC-14.7: Réconciliation bancaire
- FC-14.8: Tests remboursements

### #15 Disponibilités Config → 6 micro-issues
- FC-15.1: Créer app/settings/availability/page.tsx
- FC-15.2: Horaires ouverture hebdomadaire
- FC-15.3: Exceptions/jours fériés
- FC-15.4: Durée par service
- FC-15.5: Buffers entre RDV
- FC-15.6: Sauvegarder config

### #16 Statistiques → 8 micro-issues
- FC-16.1: Créer app/reports/page.tsx
- FC-16.2: CA par période (jour/mois/an)
- FC-16.3: Top services vendus
- FC-16.4: Top clients
- FC-16.5: Taux de remplissage
- FC-16.6: Nouveaux clients
- FC-16.7: Graphiques (recharts)
- FC-16.8: Export PDF rapport

### #17 Paramètres → 6 micro-issues
- FC-17.1: Créer app/settings/page.tsx
- FC-17.2: Infos institut (nom, adresse)
- FC-17.3: Config notifications
- FC-17.4: Config emails/SMS
- FC-17.5: Config paiements (clés API)
- FC-17.6: Sauvegarder settings

### #18 Tests E2E CRM → 6 micro-issues
- FC-18.1: Setup Playwright CRM
- FC-18.2: Test login flow
- FC-18.3: Test création booking
- FC-18.4: Test POS vente
- FC-18.5: Test gestion client
- FC-18.6: CI integration

### #19 Notifications Toast → 4 micro-issues
- FC-19.1: Installer sonner (toast)
- FC-19.2: Setup ToastProvider
- FC-19.3: Success/error toasts
- FC-19.4: Standards notifications

### #20 Permissions RBAC → 6 micro-issues
- FC-20.1: Créer lib/permissions.ts
- FC-20.2: Définir rôles (admin, staff)
- FC-20.3: Middleware vérification rôles
- FC-20.4: UI conditionnelle par rôle
- FC-20.5: Tests permissions
- FC-20.6: Documentation RBAC

---

## DÉPLOIEMENT (12 issues → ~70 micro-issues)

### #27 Cloud SQL → 6 micro-issues
- DEPLOY-27.1: Créer instance Cloud SQL PostgreSQL
- DEPLOY-27.2: Configurer réplicas haute dispo
- DEPLOY-27.3: Setup connexions privées (VPC)
- DEPLOY-27.4: Migrer données depuis dev
- DEPLOY-27.5: Configurer backups automatiques
- DEPLOY-27.6: Tests connexion production

### #28 Memorystore Redis → 5 micro-issues
- DEPLOY-28.1: Créer instance Memorystore Redis
- DEPLOY-28.2: Configurer taille/tier
- DEPLOY-28.3: Setup connexion privée
- DEPLOY-28.4: Tester cache production
- DEPLOY-28.5: Monitoring Redis

### #29 Secret Manager → 6 micro-issues
- DEPLOY-29.1: Setup Secret Manager GCP
- DEPLOY-29.2: Migrer DATABASE_URL
- DEPLOY-29.3: Migrer clés API (Stripe, PayPal)
- DEPLOY-29.4: Migrer JWT_SECRET
- DEPLOY-29.5: Configurer accès Cloud Run
- DEPLOY-29.6: Rotation secrets automatique

### #30 Cloud Storage → 5 micro-issues
- DEPLOY-30.1: Créer bucket PDFs (bons cadeaux)
- DEPLOY-30.2: Créer bucket images (photos)
- DEPLOY-30.3: Configurer CORS
- DEPLOY-30.4: Setup CDN Cloud CDN
- DEPLOY-30.5: Tests upload/download

### #31 Monitoring → 7 micro-issues
- DEPLOY-31.1: Setup Cloud Monitoring
- DEPLOY-31.2: Dashboards métriques
- DEPLOY-31.3: Alertes uptime
- DEPLOY-31.4: Alertes erreurs (Sentry)
- DEPLOY-31.5: Alertes performances
- DEPLOY-31.6: Budget alerts (coûts)
- DEPLOY-31.7: Slack notifications

### #32 DNS Configuration → 5 micro-issues
- DEPLOY-32.1: Acheter domaine (ex: serenaia-beaute.fr)
- DEPLOY-32.2: Configurer DNS pour frontend public
- DEPLOY-32.3: Configurer DNS pour CRM
- DEPLOY-32.4: Configurer DNS pour API
- DEPLOY-32.5: Setup SSL/TLS automatique

### #33 Backups → 6 micro-issues
- DEPLOY-33.1: Configurer backups PostgreSQL quotidiens
- DEPLOY-33.2: Setup rétention 30 jours
- DEPLOY-33.3: Tests restauration backup
- DEPLOY-33.4: Documentation procédure restore
- DEPLOY-33.5: Backups fichiers (Cloud Storage)
- DEPLOY-33.6: Monitoring backups

### #34 Performance → 6 micro-issues
- DEPLOY-34.1: Setup Cloud CDN
- DEPLOY-34.2: Compression gzip/brotli
- DEPLOY-34.3: Cache headers optimaux
- DEPLOY-34.4: Database query optimization
- DEPLOY-34.5: Load balancing
- DEPLOY-34.6: Tests performances Lighthouse

### #35 Tests Load → 6 micro-issues
- DEPLOY-35.1: Installer k6 (load testing)
- DEPLOY-35.2: Script test booking flow
- DEPLOY-35.3: Script test API read
- DEPLOY-35.4: Run tests 100 users concurrents
- DEPLOY-35.5: Analyser résultats
- DEPLOY-35.6: Optimisations si nécessaire

### #36 CI/CD Production → 6 micro-issues
- DEPLOY-36.1: Workflow deploy production
- DEPLOY-36.2: Tests pré-deploy
- DEPLOY-36.3: Blue-green deployment
- DEPLOY-36.4: Smoke tests post-deploy
- DEPLOY-36.5: Rollback automatique
- DEPLOY-36.6: Notifications déploiement

### #37 Documentation → 6 micro-issues
- DEPLOY-37.1: Runbook déploiement
- DEPLOY-37.2: Runbook incidents
- DEPLOY-37.3: Procédures rollback
- DEPLOY-37.4: Architecture diagram
- DEPLOY-37.5: Contacts/escalation
- DEPLOY-37.6: Playbooks monitoring

### #38 RGPD Conformité → 6 micro-issues
- DEPLOY-38.1: Audit données personnelles
- DEPLOY-38.2: Politique confidentialité
- DEPLOY-38.3: Droit à l'oubli (endpoint)
- DEPLOY-38.4: Export données client
- DEPLOY-38.5: Consentements tracking
- DEPLOY-38.6: DPO contact

---

## LANCEMENT (5 issues → ~25 micro-issues)

### #39 Tests Finaux → 6 micro-issues
- LAUNCH-39.1: Checklist fonctionnalités MVP
- LAUNCH-39.2: Tests booking end-to-end
- LAUNCH-39.3: Tests paiements réels (faible montant)
- LAUNCH-39.4: Tests notifications SMS/Email
- LAUNCH-39.5: Tests mobile responsive
- LAUNCH-39.6: UAT utilisateur final

### #40 Contenu Final → 5 micro-issues
- LAUNCH-40.1: Vérifier tous textes
- LAUNCH-40.2: Vérifier images qualité
- LAUNCH-40.3: Vérifier liens/navigation
- LAUNCH-40.4: Vérifier SEO metadata
- LAUNCH-40.5: Vérifier CGV/mentions légales

### #41 Formation Admin → 5 micro-issues
- LAUNCH-41.1: Créer guide utilisateur CRM
- LAUNCH-41.2: Vidéos tutoriels (Loom)
- LAUNCH-41.3: Session formation live
- LAUNCH-41.4: Q&A support
- LAUNCH-41.5: Documentation FAQ

### #42 Communication → 5 micro-issues
- LAUNCH-42.1: Post Instagram lancement
- LAUNCH-42.2: Post Facebook lancement
- LAUNCH-42.3: Email clients existants
- LAUNCH-42.4: Communiqué presse local
- LAUNCH-42.5: Google My Business update

### #43 Go-Live → 4 micro-issues
- LAUNCH-43.1: Basculer DNS production
- LAUNCH-43.2: Monitoring 24h continu
- LAUNCH-43.3: Support réactif 48h
- LAUNCH-43.4: Collect feedback utilisateurs

---

## PHASE 2 (15 issues → ~80 micro-issues)

### #44 Module Fidélité → 8 micro-issues
- P2-44.1: BDD tables loyalty (points, tiers)
- P2-44.2: Service calcul points
- P2-44.3: API endpoints fidélité
- P2-44.4: CRM widget points client
- P2-44.5: Règles accumulation points
- P2-44.6: Récompenses/remises
- P2-44.7: Notifications seuils
- P2-44.8: Tests fidélité

### #45 Galerie Photos → 6 micro-issues
- P2-45.1: Upload photos backend
- P2-45.2: Consentements RGPD
- P2-45.3: Modération photos
- P2-45.4: Galerie publique frontend
- P2-45.5: Watermark automatique
- P2-45.6: Tests upload

### #46 Automatisations → 6 micro-issues
- P2-46.1: Campagne anniversaire client
- P2-46.2: Réactivation inactifs 3 mois
- P2-46.3: Recommandations produits
- P2-46.4: Promotions saisonnières
- P2-46.5: Scheduler Celery
- P2-46.6: Tests automatisations

### #47 Recommandations IA → 6 micro-issues
- P2-47.1: Analyser historique achats
- P2-47.2: Modèle ML recommandations
- P2-47.3: API endpoint /recommendations
- P2-47.4: Widget CRM suggestions
- P2-47.5: A/B testing
- P2-47.6: Métriques conversion

### #48 Messagerie CRM → 6 micro-issues
- P2-48.1: Interface envoi SMS CRM
- P2-48.2: Interface envoi Email CRM
- P2-48.3: Templates messages
- P2-48.4: Historique conversations
- P2-48.5: Réponses clients
- P2-48.6: Tests messagerie

### #49 Parrainage → 5 micro-issues
- P2-49.1: BDD table referrals
- P2-49.2: Codes parrainage uniques
- P2-49.3: Tracking conversions
- P2-49.4: Récompenses parrain/filleul
- P2-49.5: Dashboard parrainage

### #50 Abonnements → 6 micro-issues
- P2-50.1: Modèles abonnements BDD
- P2-50.2: Stripe Subscriptions intégration
- P2-50.3: Webhook renouvellements
- P2-50.4: Gestion annulations
- P2-50.5: CRM suivi abonnements
- P2-50.6: Tests subscriptions

### #51 Multi-praticiens → 7 micro-issues
- P2-51.1: Table practitioners BDD
- P2-51.2: Assignment RDV praticien
- P2-51.3: Calendriers séparés
- P2-51.4: Disponibilités par praticien
- P2-51.5: Stats par praticien
- P2-51.6: Permissions praticiens
- P2-51.7: Tests multi-users

### #52 Marketplace → 8 micro-issues
- P2-52.1: BDD partenaires/produits
- P2-52.2: API partenaires
- P2-52.3: Commission tracking
- P2-52.4: Frontend marketplace
- P2-52.5: Panier mixte (propre+partenaire)
- P2-52.6: Paiements split
- P2-52.7: Reporting partenaires
- P2-52.8: Tests marketplace

### #53 Avis Notations → 5 micro-issues
- P2-53.1: Table reviews BDD
- P2-53.2: API post/get reviews
- P2-53.3: Modération avis
- P2-53.4: Widget avis frontend
- P2-53.5: Sync Google Reviews

### #54 Analytics BI → 6 micro-issues
- P2-54.1: Setup Metabase/Superset
- P2-54.2: Dashboards avancés
- P2-54.3: Prédictions CA (ML)
- P2-54.4: Cohort analysis
- P2-54.5: Funnel conversions
- P2-54.6: Exports rapports

### #55 App Mobile → 8 micro-issues
- P2-55.1: Décision PWA vs Native
- P2-55.2: Setup projet mobile
- P2-55.3: Authentification mobile
- P2-55.4: Booking mobile
- P2-55.5: Paiements mobile
- P2-55.6: Notifications push
- P2-55.7: Tests mobile
- P2-55.8: Déploiement stores

### #56 Comptabilité → 5 micro-issues
- P2-56.1: Export FEC (Fichier Échanges Informatisé)
- P2-56.2: Intégration Sage/Ciel
- P2-56.3: Mapping comptes comptables
- P2-56.4: Rapports TVA
- P2-56.5: Tests export

### #57 Carte NFC → 6 micro-issues
- P2-57.1: Intégration Apple Wallet API
- P2-57.2: Intégration Google Wallet API
- P2-57.3: Génération passes
- P2-57.4: QR codes fidélité
- P2-57.5: Scan cartes CRM
- P2-57.6: Tests wallets

### #58 Chatbot IA → 8 micro-issues
- P2-58.1: Setup OpenAI API
- P2-58.2: Base connaissances (FAQs)
- P2-58.3: Widget chat frontend
- P2-58.4: Intent recognition
- P2-58.5: Escalade vers humain
- P2-58.6: Historique conversations
- P2-58.7: Training data
- P2-58.8: Tests chatbot

---

## RÉSUMÉ ATOMISATION

| Phase | Issues Actuelles | Micro-Issues | Ratio |
|-------|------------------|--------------|-------|
| Phase 0 | 6 | 25 | 4.2x |
| Backend Phase 1 | 26 | 180 | 6.9x |
| Frontend Public | 15 | 90 | 6.0x |
| Frontend CRM | 20 | 120 | 6.0x |
| Déploiement | 12 | 70 | 5.8x |
| Lancement | 5 | 25 | 5.0x |
| Phase 2 | 15 | 80 | 5.3x |
| **TOTAL** | **93** | **~590** | **6.3x** |

## Bénéfices Atomisation

### Pour Claude Code
- ✅ Tâches 1-2h max (pas de perte contexte)
- ✅ Objectif unique et clair
- ✅ Testable immédiatement
- ✅ Moins de dépendances complexes

### Pour le Suivi
- ✅ Progression granulaire visible
- ✅ Meilleure estimation temps
- ✅ Identification rapide blocages
- ✅ Parallélisation facile

### Exemple Atomisation

**Avant** (Issue #7):
- Titre: Setup FastAPI - Structure complète
- Durée: 40-60h
- Scope: Tout le setup backend

**Après** (12 micro-issues):
- BACK-7.1: Créer venv (30min)
- BACK-7.2: requirements.txt (30min)
- BACK-7.3: Structure dossiers (1h)
- BACK-7.4: main.py (1h)
- etc.

Chaque micro-issue = 1 commit Git + 1 test + 1 validation

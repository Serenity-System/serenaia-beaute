# ✅ MVP Validé - Sérénaïa Beauté

**Date:** 2026-01-11
**Version:** 1.0 - Scope Final

---

## 🎯 Périmètre Fonctionnel Validé

### Architecture Globale

```
📱 FRONTEND PUBLIC (Site Vitrine)
    ↓
🔌 API BACKEND UNIQUE (FastAPI)
    ↓
💻 FRONTEND CRM/ADMIN (Gestion Institut)
```

**Hébergement:**
- Frontend Public: Vercel → `https://serenaia-beaute.fr`
- Frontend CRM: Vercel → `https://admin.serenaia-beaute.fr`
- Backend API: Google Cloud Run → `https://api.serenaia-beaute.fr`
- Base de données: Cloud SQL PostgreSQL
- Cache: Memorystore Redis
- Storage: Google Cloud Storage

---

## 📋 Modules CRM Validés (12 modules)

### 🔴 Phase 1 - MVP (8 modules critiques)

| # | Module | Description | Priorité |
|---|--------|-------------|----------|
| 1 | **Point de Vente (POS)** | Caisse tactile, encaissement direct, ticket | 🔴 Critique |
| 2 | **Gestion des Stocks** | Produits de vente + fournitures, alertes stock | 🔴 Critique |
| 3 | **Fiche Client Détaillée** | Infos complètes, allergies, préférences | 🔴 Critique |
| 4 | **Historique des Soins** | Notes par prestation, photos avant/après | 🔴 Critique |
| 5 | **Planning Optimisé** | Calendrier avec temps préparation, drag & drop | 🔴 Critique |
| 6 | **Statistiques Avancées** | KPIs, graphiques, rapports automatiques | 🔴 Critique |
| 7 | **Facturation & Comptabilité** | Génération factures, export comptable | 🔴 Critique |
| 8 | **Conformité RGPD** | Consentements, droits clients, audit log | 🔴 Critique |

### 🟠 Phase 2 - Post-MVP (4 modules importants)

| # | Module | Description | Priorité |
|---|--------|-------------|----------|
| 9 | **Programme de Fidélité** | Points, niveaux (Bronze, Argent, Or), récompenses | 🟠 Important |
| 10 | **Galerie Avant/Après** | Photos avec consentement, portfolio public | 🟠 Important |
| 11 | **Automatisations Marketing** | Anniversaire, réactivation, upselling | 🟠 Important |
| 12 | **Messagerie Intégrée** | SMS/Email depuis le CRM, templates | 🟠 Important |

---

## ❌ Modules Exclus du Scope

- ❌ **App Mobile Technicienne** (PWA) - Pas nécessaire
- ❌ **Objectifs & Gamification** - Pas prioritaire
- ❌ **IA & Recommandations** - Trop complexe pour MVP
- ❌ **Réalité Augmentée** - Hors scope

---

## 🌐 Frontend Public - Pages & Fonctionnalités

### Pages du Site Vitrine

1. **Accueil**
   - Hero avec baseline "La douceur et l'élégance au service de votre beauté"
   - Prestations populaires (3-4)
   - Avis clients (carrousel)
   - Appel à l'action "Prendre rendez-vous"

2. **À propos**
   - Présentation personnelle
   - Parcours et certifications
   - Philosophie et valeurs
   - Zone d'intervention
   - Photos professionnelles

3. **Prestations**
   - Liste par catégorie :
     - 💅 Beauté des ongles
     - 👁️ Beauté du regard
     - 🌸 Soins du visage
     - 🙌 Modelages bien-être
     - ✨ Épilations
     - 🎯 Forfaits et offres
   - Chaque prestation : nom, durée, prix, description
   - Filtres par catégorie
   - Bouton "Réserver" direct

4. **Prendre rendez-vous**
   - Sélection de la prestation
   - Calendrier interactif avec disponibilités
   - Formulaire client (nom, prénom, email, téléphone)
   - Récapitulatif
   - Paiement sécurisé (30% acompte ou totalité)
   - Confirmation automatique (email + SMS)

5. **Offrir un bon cadeau**
   - Choix : montant libre OU prestation spécifique
   - Personnalisation (nom, message)
   - Paiement immédiat
   - PDF téléchargeable + envoi email
   - Code unique (format: SERA-XXXX-XXXX)

6. **Avis**
   - Widget Google Reviews
   - Note moyenne et nombre d'avis
   - Liste des avis avec filtres
   - Appel à l'action "Laisser un avis"

7. **Contact**
   - Formulaire de contact
   - Coordonnées (téléphone, email)
   - Réseaux sociaux
   - Zone d'intervention
   - Horaires

### Fonctionnalités Techniques Frontend Public

- ✅ Réservation en ligne avec calendrier temps réel
- ✅ Paiement multi-méthodes (Stripe, PayPal, Lydia, Wero, Virement)
- ✅ Bons cadeaux avec PDF personnalisé
- ✅ Intégration Google Reviews
- ✅ Responsive 100% mobile-first
- ✅ SEO optimisé (Next.js SSR/SSG)
- ✅ Animations douces (Framer Motion)
- ✅ Performance (Lighthouse score > 90)

---

## 💻 Frontend CRM - Modules Détaillés

### Module 1️⃣ : Point de Vente (POS)

#### Interface Caisse
- Sélection rapide prestations réalisées
- Ajout produits vendus (recherche ou scan)
- Calcul automatique du total
- Application remises (fidélité, promo)
- **Moyens de paiement** :
  - 💳 Carte bancaire (terminal physique + API)
  - 💵 Espèces
  - 📱 Lydia / Wero
  - 🎁 Bon cadeau (validation code)
  - 🔄 Paiement mixte

#### Gestion de Caisse
- Ouverture de caisse (fond initial)
- Suivi des ventes (espèces, CB, autres)
- Clôture de caisse (comptage, écarts)
- Mouvements (entrées/sorties)
- Historique complet

#### Ticket de Caisse
- Génération automatique
- Impression ou envoi email/SMS
- QR code pour récupération PDF
- Mentions légales + TVA

---

### Module 2️⃣ : Gestion des Stocks

#### Catalogue Produits

**Types de produits** :
- **Produits de vente** : Sérums, crèmes, vernis (vendus aux clientes)
- **Fournitures** : Cotons, cire, gel UV (utilisés pour prestations)
- **Équipement** : Matériel professionnel (inventaire)

**Fiche Produit** :
- Nom, Marque, Référence, Catégorie
- Prix d'achat (HT) / Prix de vente (TTC)
- Stock actuel / Seuil d'alerte
- Photo, Description
- Fournisseur

#### Mouvements de Stock
- ➕ Entrée (réception fournisseur)
- ➖ Sortie (vente ou utilisation prestation)
- 📊 Historique complet
- 🔔 Alertes automatiques (stock < seuil)

#### Commandes Fournisseurs
- Liste des produits à commander
- Génération bon de commande (PDF)
- Suivi livraison

#### Statistiques Stocks
- Valeur totale du stock
- Rotation des produits (meilleurs/pires ventes)
- Produits périmés (alerte date péremption)

---

### Module 3️⃣ : Fiche Client Détaillée

#### Informations Personnelles
- Identité : Nom, Prénom, Date de naissance
- Contact : Email, Téléphone, Adresse
- Préférences de contact (email, SMS, tel)

#### Profil Client
- Date première visite
- Fréquence de visite (1x/mois, 2x/mois, etc.)
- Panier moyen / CA total généré
- **Segment** : VIP, Fidèle, Nouveau, Inactif, À risque
- Source d'acquisition (réseaux sociaux, bouche-à-oreille, Google)

#### Informations Médicales & Allergies
- Allergies connues (produits, latex)
- Problèmes de peau (eczéma, acné, sensibilité)
- Traitements médicaux en cours
- Grossesse / Allaitement
- Contre-indications
- Date de mise à jour (annuelle)

#### Historique des Achats
- Prestations réalisées (liste chronologique)
- Produits achetés
- Factures (téléchargement PDF)

#### Préférences
- Prestations favorites
- Horaires préférés (matin, après-midi, soir)
- Jours préférés
- Notes privées (admin uniquement)

---

### Module 4️⃣ : Historique des Soins

#### Liste Chronologique
Pour chaque prestation réalisée :
- Date, Heure, Durée réelle
- Prestation(s) réalisée(s)
- Produits utilisés pendant le soin
- Prix payé
- **Notes de soin** :
  - État initial (peau, ongles, etc.)
  - Réaction aux produits
  - Résultat obtenu
  - Recommandations données
- **Photos avant/après** (avec consentement)

#### Suivi Évolution
- Timeline visuelle d'un même client
- Comparaison avant/après
- Protocoles suivis

---

### Module 5️⃣ : Planning Optimisé

#### Vue Calendrier
- Vues : Jour, Semaine, Mois
- **Codes couleur** par statut :
  - 🟢 Confirmé + payé
  - 🟡 Confirmé mais paiement en attente
  - 🔵 Complété
  - 🟠 En cours
  - 🔴 Annulé
  - ⚪ Libre

#### Fonctionnalités
- **Drag & drop** pour déplacer un RDV
- **Temps de préparation** : 10-15 min entre clients
- **Temps de trajet** : Calcul automatique (Google Maps API) pour déplacements à domicile
- **Prestations combinées** : Calcul durée totale automatique
- **Ajout manuel** de RDV (réservations téléphoniques)

#### Gestion des Disponibilités
- Configuration horaires hebdomadaires (Lun-Dim)
- Pause déjeuner
- Durée des créneaux (15, 30, 60 min)
- Jours fériés / Congés
- Blocage de créneaux spécifiques

#### Notifications Automatiques
**Client** :
- Confirmation RDV (immédiate)
- Rappel 24h avant
- Demande d'avis 48h après

**Admin** :
- Nouveau RDV (notification)
- Annulation client
- Récap RDV du lendemain (chaque soir)

---

### Module 6️⃣ : Statistiques Avancées

#### Dashboard Principal
**Stats du jour** :
- Nombre de RDV
- CA du jour (prestations + produits)
- Prochains RDV (liste)

**Stats du mois** :
- Nombre total de RDV
- CA total
- Taux d'annulation
- Bons cadeaux vendus

**Graphiques** :
- Évolution des réservations (ligne)
- Répartition par prestation (camembert)
- Revenus par mois (barres)
- Horaires les plus demandés (heatmap)

#### KPIs Essentiels
**Activité** :
- Taux de remplissage (% créneaux occupés)
- Taux d'annulation
- Taux de no-show
- Durée moyenne réelle vs théorique

**Financier** :
- CA quotidien/hebdomadaire/mensuel/annuel
- Répartition CA : Prestations vs Produits
- Panier moyen par client
- Marge brute (CA - coût produits)
- CA par prestation
- CA par canal (en ligne vs direct)

**Clients** :
- Nombre nouveaux clients
- Taux de rétention
- Fréquence moyenne de visite
- Lifetime Value (LTV)
- Taux de transformation (site → réservation)

**Produits** :
- Produits les plus vendus
- Rotation stocks
- Marge par produit
- Cross-selling

#### Rapports Automatiques
- **Quotidien** : Email chaque soir (RDV du jour, CA, alertes)
- **Hebdomadaire** : Résumé semaine, comparaison vs précédente
- **Mensuel** : Bilan complet, objectifs vs réalisé, recommandations

#### Export de Données
- Format : CSV, Excel, PDF
- Filtres : Plage dates, Type données
- Utilisation : Comptabilité, analyse

---

### Module 7️⃣ : Facturation & Comptabilité

#### Génération Factures
- Facture automatique après chaque vente
- Numérotation chronologique
- Mentions légales (TVA, SIRET, CGV)
- Envoi automatique par email
- Téléchargement PDF depuis CRM

#### Gestion TVA
- Calcul automatique (20%)
- Déclaration simplifiée
- Export pour déclaration

#### Export Comptable
- CSV / Excel pour expert-comptable
- Intégration possible : Pennylane, Quickbooks, Sage
- Réconciliation bancaire

#### Analyse Rentabilité
- Coût de revient par prestation (produits + temps)
- Marge par prestation
- Seuil de rentabilité

---

### Module 8️⃣ : Conformité RGPD

#### Gestion des Consentements
- Formulaire consentement à la 1ère visite :
  - Collecte données personnelles
  - Photos avant/après
  - Communication marketing (email, SMS)
  - Partage réseaux sociaux
- Historique des consentements
- Révocation possible à tout moment

#### Droits des Clients
- **Droit d'accès** : Téléchargement toutes données (PDF)
- **Droit de rectification** : Modification données
- **Droit à l'oubli** : Suppression/anonymisation
- **Portabilité** : Export JSON

#### Sécurité
- Chiffrement données sensibles
- Authentification 2FA (admin)
- Audit log de tous les accès
- Sauvegarde quotidienne chiffrée

---

### Module 9️⃣ : Programme de Fidélité (Phase 2)

#### Système de Points
- **1€ dépensé = 1 point**
- Points valables 1 an
- Cumul prestations + produits
- Double points événements spéciaux

#### Utilisation
- **100 points = 5€ de réduction**
- Utilisation partielle ou totale
- Historique gains/utilisations

#### Niveaux de Fidélité
- 🥉 **Bronze** : 0-500€ → 5% remise
- 🥈 **Argent** : 500-1000€ → 7% remise + 1 soin offert/an
- 🥇 **Or** : 1000-2000€ → 10% remise + 2 soins offerts/an
- 💎 **Platine** : >2000€ → 15% remise + 3 soins + cadeaux VIP

#### Carte Virtuelle
- QR code unique
- Solde points en temps réel
- Niveau actuel et avantages

#### Offres Spéciales
- Anniversaire : Soin offert ou -20%
- Parrainage : 10€ parrain + 10€ filleul
- Réactivation : Offre si pas de visite depuis 6 mois
- Saisonnières : Épilation été, soins hydratants hiver

---

### Module 🔟 : Galerie Avant/Après (Phase 2)

#### Gestion des Photos
- Upload depuis CRM
- Association prestation + client
- **Consentement RGPD** :
  - Formulaire signé électroniquement
  - Utilisation site web (oui/non)
  - Utilisation réseaux sociaux (oui/non)
  - Floutage visage (option)
- Tags : Type prestation, difficulté, résultat
- Galerie publique : Sélection meilleures photos

#### Suivi Visuel Client
- Timeline photos chronologique
- Comparaison avant/après
- Notes : Produits utilisés, protocole

---

### Module 1️⃣1️⃣ : Automatisations Marketing (Phase 2)

#### Campagnes Automatiques
- **Anniversaire client** : SMS/Email avec offre (-20%)
- **Réactivation inactifs** : Après 3/6 mois sans visite
- **Recommandation réachat produit** : 2 mois après achat
- **Saisonnalité** : Promo épilation avant été, soins hiver
- **Upselling** : Suggestion soin complémentaire après réservation

#### Automatisations Opérationnelles
- Rappel mise à jour questionnaire santé (annuel)
- Demande d'avis (48h après prestation)
- Demande parrainage (après 3 prestations)
- Alerte stock bas (email auto)
- Clôture caisse auto (récap à 21h)

---

### Module 1️⃣2️⃣ : Messagerie Intégrée (Phase 2)

#### SMS depuis CRM
- Envoi SMS groupés (campagnes)
- Envoi individuel (fiche client)
- Templates pré-enregistrés
- Historique conversations
- SMS bidirectionnel (réponses clients)

#### Email depuis CRM
- Emails personnalisés
- Templates WYSIWYG
- Pièces jointes (factures, bons cadeaux)
- Tracking ouverture et clics

#### WhatsApp Business (Optionnel)
- Intégration WhatsApp Business API
- Confirmation RDV
- Rappels et notifications
- Support client

---

## 🗄️ Base de Données - Modèle Complet

### Tables Principales

1. **users** - Administrateurs CRM
2. **services** - Prestations proposées
3. **bookings** - Réservations clients
4. **clients** - Base CRM complète
5. **payments** - Transactions
6. **gift_cards** - Bons cadeaux
7. **products** - Catalogue produits
8. **stock_movements** - Mouvements stocks
9. **service_history** - Historique soins par client
10. **availabilities** - Horaires disponibles
11. **blocked_dates** - Jours congés/fériés
12. **notifications** - Log SMS/Emails
13. **loyalty_points** - Points fidélité
14. **consents** - Consentements RGPD
15. **invoices** - Factures générées
16. **photos** - Galerie avant/après

---

## 🚀 Phasage du Projet

### Phase 1 : MVP Core (3-4 mois)

**Frontend Public** :
- ✅ Toutes les pages (7 pages)
- ✅ Réservation en ligne complète
- ✅ Paiement multi-méthodes
- ✅ Bons cadeaux
- ✅ Avis Google

**Backend API** :
- ✅ Endpoints publics
- ✅ Endpoints admin (authentification)
- ✅ Intégrations paiements
- ✅ SMS OVH API
- ✅ Emails automatiques
- ✅ Génération PDF

**Frontend CRM** (8 modules critiques) :
- ✅ Module 1 : POS
- ✅ Module 2 : Stocks
- ✅ Module 3 : Fiche Client
- ✅ Module 4 : Historique Soins
- ✅ Module 5 : Planning
- ✅ Module 6 : Statistiques
- ✅ Module 7 : Facturation
- ✅ Module 8 : RGPD

**Infrastructure** :
- ✅ Déploiement Cloud Run (Backend)
- ✅ Déploiement Vercel (2 frontends)
- ✅ Cloud SQL PostgreSQL
- ✅ Memorystore Redis
- ✅ Cloud Storage
- ✅ CI/CD Pipeline

---

### Phase 2 : Extensions (2 mois)

**Frontend CRM** (4 modules supplémentaires) :
- ✅ Module 9 : Programme Fidélité
- ✅ Module 10 : Galerie Photos
- ✅ Module 11 : Automatisations Marketing
- ✅ Module 12 : Messagerie Intégrée

**Optimisations** :
- Performance (caching avancé)
- SEO (référencement avancé)
- Analytics approfondies

---

### Phase 3 : Évolutions Futures (à définir)

- Intégration comptable avancée (Pennylane, etc.)
- Marketplace produits (vente en ligne)
- Système de rendez-vous récurrents
- Multi-utilisateurs CRM (plusieurs techniciennes)

---

## 💰 Technologies Finales Validées

### Frontend
- **Framework** : Next.js 14+ (App Router)
- **Styling** : Tailwind CSS
- **UI** : shadcn/ui
- **Forms** : React Hook Form + Zod
- **Animations** : Framer Motion

### Backend
- **Framework** : Python 3.11+ + FastAPI
- **ORM** : SQLAlchemy 2.0
- **Migrations** : Alembic
- **Task Queue** : Celery + Redis

### Infrastructure
- **Frontend** : Vercel
- **Backend** : Google Cloud Run (Docker)
- **Database** : Cloud SQL PostgreSQL
- **Cache** : Memorystore Redis
- **Storage** : Google Cloud Storage
- **CDN** : Cloud CDN ou Cloudflare

### APIs & Intégrations
- **Paiement** : Stripe, PayPal, Lydia, Wero
- **SMS** : OVH SMS API
- **Email** : Resend ou SendGrid
- **Avis** : Google Business Profile API
- **PDF** : WeasyPrint ou ReportLab

---

## 📊 Métriques de Succès

### KPIs de Lancement (3 mois après MVP)

**Trafic & Conversion** :
- Visiteurs uniques/mois : > 1000
- Taux de conversion (visite → réservation) : > 5%
- Taux de complétion formulaire réservation : > 80%

**Réservations** :
- Nombre de RDV en ligne : > 50/mois
- Taux de remplissage : > 70%
- Taux d'annulation : < 10%

**Ventes** :
- CA mensuel : Objectif à définir
- Panier moyen : Objectif à définir
- Bons cadeaux vendus : > 10/mois

**Satisfaction** :
- Note Google moyenne : > 4,5/5
- Taux de clients fidèles (>2 visites) : > 30%

---

## ✅ Prochaines Étapes Immédiates

1. **Validation finale du scope** avec le client
2. **Création de maquettes** (wireframes puis designs haute fidélité)
3. **Architecture détaillée de la base de données**
4. **Estimation budget et timeline précise**
5. **Setup de l'environnement de développement**
6. **Démarrage du développement** (Backend API en priorité)

---

**Date de création:** 2026-01-11
**Version:** 1.0 - Scope Final Validé
**Modules:** 12 modules CRM + Site vitrine complet

# 🎯 CRM - Spécifications - Sérénaïa Beauté

## 📋 Vue d'Ensemble

Le projet comportera **2 frontends distincts** utilisant **une seule API backend** :

1. **Frontend Public** : Site vitrine pour les clients
2. **Frontend CRM/Admin** : Interface de gestion complète (CRM)

**Date:** 2026-01-11
**Version:** 1.0

---

## 🏗️ Architecture à 2 Frontends

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND PUBLIC                           │
│                  (Site Vitrine Client)                       │
│                                                              │
│  Next.js + Tailwind CSS                                     │
│  URL: https://serenaia-beaute.fr                           │
│  Pages: Accueil, Prestations, Réservation, Contact, etc.   │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   │
                   │ API REST (JWT Auth pour admin)
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                    API BACKEND UNIQUE                        │
│                    (FastAPI + PostgreSQL)                    │
│                                                              │
│  Endpoints publics + Endpoints protégés (JWT)               │
│  Logique métier unique pour les 2 frontends                │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                    FRONTEND CRM/ADMIN                        │
│                  (Interface de Gestion)                      │
│                                                              │
│  Next.js + Tailwind CSS + shadcn/ui                         │
│  URL: https://admin.serenaia-beaute.fr                     │
│  Dashboard, Clients, Réservations, Stats, etc.             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🌐 Frontend 1 : Site Vitrine Public

### Objectif
Interface client pour présenter les services et permettre la réservation en ligne.

### URL
- Production : `https://serenaia-beaute.fr`
- Staging : `https://staging.serenaia-beaute.fr`

### Pages & Fonctionnalités

#### Pages Publiques
- **Accueil** : Hero, prestations populaires, avis clients, appel à l'action
- **À propos** : Présentation, valeurs, parcours, zone d'intervention
- **Prestations** : Liste catégorisée des services avec filtres
- **Prendre rendez-vous** : Calendrier interactif, sélection prestation, formulaire
- **Offrir un bon cadeau** : Achat de bons cadeaux (montant libre ou prestation)
- **Avis** : Affichage des avis Google Business, notation
- **Contact** : Formulaire de contact, coordonnées, carte

#### Fonctionnalités Clés
- 📅 **Réservation en ligne** avec calendrier en temps réel
- 💳 **Paiement sécurisé** (Stripe, PayPal, Lydia, Wero, virement)
- 🎁 **Achat de bons cadeaux** avec génération PDF
- ⭐ **Affichage des avis** Google synchronisés
- 📱 **100% responsive** (mobile-first)
- 🔔 **Confirmation par email/SMS** automatique

### Technologies
- **Framework** : Next.js 14+ (App Router)
- **Styling** : Tailwind CSS
- **UI** : shadcn/ui (composants réutilisables)
- **Forms** : React Hook Form + Zod
- **Animations** : Framer Motion
- **HTTP** : Axios / Fetch API

### Déploiement
- **Hébergement** : Vercel
- **CI/CD** : GitHub Actions → Vercel
- **SSL** : Let's Encrypt (auto via Vercel)

---

## 🖥️ Frontend 2 : CRM/Admin

### Objectif
Interface complète de gestion pour l'administrateur : clients, réservations, statistiques, configuration.

### URL
- Production : `https://admin.serenaia-beaute.fr`
- Staging : `https://admin-staging.serenaia-beaute.fr`

### Authentification
- **Login sécurisé** avec email + mot de passe
- **JWT Tokens** (access token + refresh token)
- **Rôles** : Admin, Super Admin (extensible)
- **2FA** (optionnel, phase 2)

---

## 🎯 Modules CRM

### 1. 📊 Dashboard

#### Vue d'Ensemble
- **Statistiques du jour** :
  - Nombre de réservations du jour
  - Revenus du jour
  - Prochains rendez-vous (liste)
- **Statistiques du mois** :
  - Nombre total de réservations
  - Revenus totaux
  - Taux d'annulation
  - Bons cadeaux vendus
- **Graphiques** :
  - Évolution des réservations (ligne)
  - Répartition par prestation (camembert)
  - Revenus par mois (barres)
  - Horaires les plus demandés (heatmap)

#### Widgets
- ⏰ **Prochains RDV aujourd'hui** (timeline)
- 📈 **KPIs** : Taux de remplissage, CA prévisionnel du mois
- ⚠️ **Alertes** : RDV en attente de confirmation, paiements en attente
- 📅 **Vue calendrier** : Vue mensuelle avec tous les RDV

---

### 2. 👥 Gestion des Clients (CRM)

#### Liste des Clients
- **Tableau** avec tri et filtres :
  - Nom, Prénom
  - Email, Téléphone
  - Nombre de réservations
  - CA généré
  - Date dernière visite
  - Statut (actif, inactif, VIP)
- **Recherche** : Par nom, email, téléphone
- **Export** : CSV, Excel

#### Fiche Client Détaillée
- **Informations personnelles** :
  - Nom, prénom, email, téléphone
  - Adresse complète
  - Date de naissance (optionnel)
  - Notes privées
- **Historique des réservations** :
  - Liste chronologique
  - Prestations réalisées
  - Montants payés
  - Statut (complété, annulé)
- **Statistiques client** :
  - Prestation favorite
  - Fréquence de visite (jours entre visites)
  - CA total généré
  - Nombre d'annulations
- **Actions** :
  - Créer une nouvelle réservation
  - Envoyer un email/SMS
  - Offrir une promotion
  - Bloquer le client (si nécessaire)

#### Segmentation
- **Clients VIP** : > X réservations ou > Y € dépensés
- **Clients inactifs** : Pas de visite depuis 3/6/12 mois
- **Nouveaux clients** : Première visite < 30 jours
- **Clients fidèles** : > 5 réservations

#### Campagnes Marketing
- **Envoi de SMS/Email groupés** :
  - Sélection par segment
  - Templates prédéfinis
  - Personnalisation (nom, prénom)
  - Historique des envois
- **Offres promotionnelles** :
  - Codes promo personnalisés
  - Offres ciblées (ex: réactivation clients inactifs)

---

### 3. 📅 Gestion des Réservations

#### Agenda / Calendrier
- **Vue calendrier** (jour, semaine, mois)
- **Créneaux colorés** par statut :
  - 🟢 Confirmé
  - 🟡 En attente de paiement
  - 🔵 Complété
  - 🔴 Annulé
- **Drag & drop** pour déplacer un RDV
- **Double-clic** pour voir les détails
- **Ajout manuel** de RDV (pour réservations téléphoniques)

#### Liste des Réservations
- **Tableau avec filtres** :
  - Date (aujourd'hui, cette semaine, ce mois, plage personnalisée)
  - Statut (tous, en attente, confirmé, complété, annulé)
  - Prestation
  - Mode de paiement
- **Actions en masse** :
  - Confirmer plusieurs RDV
  - Envoyer rappel SMS
  - Exporter la sélection

#### Fiche Réservation
- **Détails** :
  - Client (lien vers fiche client)
  - Date, heure, durée
  - Prestation
  - Prix
  - Statut paiement (en attente, acompte payé, payé intégralement)
  - Mode de paiement
  - Notes du client
  - Notes privées (admin)
- **Actions** :
  - Modifier la date/heure
  - Annuler le RDV (avec raison)
  - Marquer comme complété
  - Envoyer rappel manuel
  - Rembourser (si annulation dans les délais)
  - Imprimer récapitulatif

#### Notifications Automatiques
- **Configuration** :
  - Activer/désactiver rappels SMS 24h avant
  - Activer/désactiver emails de confirmation
  - Templates personnalisables
- **Historique** : Log de tous les SMS/emails envoyés

---

### 4. 💅 Gestion des Prestations

#### Liste des Prestations
- **CRUD complet** :
  - Créer, Modifier, Supprimer, Activer/Désactiver
- **Informations** :
  - Nom, Catégorie (ongles, regard, visage, massage, épilation)
  - Description courte et longue
  - Durée (en minutes)
  - Prix (€)
  - Image (upload)
  - Ordre d'affichage
  - Actif/Inactif (pour cacher temporairement)

#### Catégories
- **Gestion des catégories** :
  - Créer, Modifier, Supprimer
  - Ordre d'affichage
  - Icône

#### Forfaits & Packages
- **Création de forfaits** :
  - Nom du forfait
  - Combinaison de plusieurs prestations
  - Prix réduit
  - Validité (nombre de jours)
  - Conditions (ex: forfait étudiant)

---

### 5. 🎁 Gestion des Bons Cadeaux

#### Liste des Bons Cadeaux
- **Tableau** :
  - Code unique
  - Type (montant libre / prestation)
  - Valeur (€)
  - Acheteur (nom, email)
  - Bénéficiaire (nom, email)
  - Date d'achat
  - Date d'expiration
  - Statut (actif, utilisé, expiré)
  - Date d'utilisation (si utilisé)
- **Filtres** : Statut, Date d'achat, Type
- **Actions** :
  - Prolonger la validité
  - Désactiver (remboursement)
  - Renvoyer le PDF par email
  - Voir l'utilisation (lié à quelle réservation)

#### Statistiques
- **CA généré par les bons cadeaux**
- **Taux d'utilisation** (utilisés / vendus)
- **Bons expirés non utilisés**
- **Période favorite** pour les achats (ex: Noël, fête des mères)

---

### 6. 💰 Gestion des Paiements

#### Transactions
- **Liste de toutes les transactions** :
  - Date
  - Montant
  - Mode de paiement (Stripe, PayPal, Lydia, Wero, virement)
  - Statut (en attente, complété, échoué, remboursé)
  - Lié à (réservation ou bon cadeau)
  - ID transaction externe
- **Filtres** : Date, Mode de paiement, Statut
- **Recherche** : Par montant, ID transaction, client

#### Virements en Attente
- **Liste des virements à confirmer** :
  - Réservation associée
  - Montant attendu
  - Date de demande
  - Actions : Confirmer réception / Relancer client

#### Statistiques
- **Revenus par mode de paiement** (graphique)
- **Taux de succès des paiements**
- **Acomptes vs paiements complets**
- **Revenus par prestation**

#### Remboursements
- **Interface de remboursement** :
  - Sélection de la transaction
  - Montant à rembourser (partiel ou total)
  - Raison du remboursement
  - Confirmation avec Stripe/PayPal

---

### 7. ⏰ Gestion des Disponibilités

#### Configuration des Horaires
- **Horaires hebdomadaires** :
  - Lundi à Dimanche
  - Heures de début et de fin
  - Pause déjeuner (optionnel)
  - Actif / Inactif par jour
- **Durée des créneaux** : 15, 30, 60 minutes (configurable)

#### Jours Fériés & Congés
- **Liste des jours bloqués** :
  - Date
  - Raison (congés, férié, formation, etc.)
  - Actions : Ajouter, Modifier, Supprimer
- **Blocage de créneaux spécifiques** :
  - Date + heure spécifique
  - Raison

#### Gestion des Créneaux en Temps Réel
- **Vue calendrier** avec disponibilités
- **Créneaux déjà réservés** (non disponibles)
- **Créneaux libres** (affichés aux clients)
- **Synchronisation** : Mise à jour en temps réel via Redis

---

### 8. ⭐ Gestion des Avis

#### Avis Google
- **Synchronisation automatique** des avis Google Business Profile
- **Affichage** :
  - Note moyenne
  - Nombre total d'avis
  - Liste des derniers avis (nom, note, commentaire, date)
- **Actions** :
  - Répondre aux avis depuis le CRM (via API Google)
  - Signaler un avis inapproprié
  - Exporter les avis

#### Demande d'Avis Automatique
- **Configuration** :
  - Envoyer un email/SMS 48h après le RDV
  - Template personnalisable
  - Lien direct vers Google Reviews
  - Historique des demandes envoyées

---

### 9. 📊 Statistiques & Reporting

#### Rapports Prédéfinis
- **Rapport mensuel** :
  - Nombre de réservations
  - CA total
  - Prestations les plus demandées
  - Créneaux horaires favoris
  - Taux d'annulation
  - Nouveaux clients vs clients récurrents
- **Rapport annuel** :
  - Évolution mois par mois
  - Comparaison année N vs N-1
  - Croissance du CA
  - Top 10 des clients (CA)

#### Graphiques Interactifs
- **Réservations** : Ligne temporelle
- **Revenus** : Barres mensuelles
- **Prestations** : Camembert répartition
- **Horaires** : Heatmap des créneaux demandés
- **Avis** : Évolution de la note moyenne

#### Export de Données
- **Format** : CSV, Excel, PDF
- **Filtres** : Plage de dates, Type de données
- **Utilisation** : Comptabilité, analyse externe

---

### 10. ⚙️ Paramètres & Configuration

#### Compte Administrateur
- **Gestion des utilisateurs admin** :
  - Créer, Modifier, Supprimer
  - Rôles et permissions (Admin, Super Admin)
  - 2FA (authentification à 2 facteurs)
- **Profil** :
  - Email, Mot de passe
  - Photo de profil
  - Préférences (notifications, langue)

#### Paramètres du Site
- **Informations générales** :
  - Nom de l'entreprise
  - Logo (upload)
  - Couleurs de la charte (picker)
  - Adresse, Téléphone, Email
  - Zone géographique d'intervention
  - Réseaux sociaux (Instagram, Facebook)
- **Mentions légales** :
  - CGV (éditeur WYSIWYG)
  - Politique de confidentialité
  - Mentions légales

#### Paramètres de Réservation
- **Acompte** :
  - Pourcentage (30% par défaut, modifiable)
  - Obligatoire ou optionnel
- **Annulation** :
  - Délai minimum (24h par défaut)
  - Politique de remboursement
- **Créneaux** :
  - Durée des créneaux (15, 30, 60 min)
  - Délai minimum de réservation (ex: 2h à l'avance)
  - Nombre max de RDV par jour

#### Intégrations
- **Stripe** : Clés API (test / production)
- **PayPal** : Client ID / Secret
- **Lydia** : API Key
- **Wero** : API Key
- **OVH SMS** : Credentials
- **SendGrid / Resend** : API Key pour emails
- **Google Business** : Location ID pour avis

#### Templates Email/SMS
- **Éditeur de templates** :
  - Confirmation de réservation
  - Rappel 24h avant
  - Annulation
  - Demande d'avis
  - Variables dynamiques : `{nom}`, `{date}`, `{heure}`, `{prestation}`

---

## 🔐 Sécurité CRM

### Authentification
- **JWT Tokens** avec expiration courte (30 min)
- **Refresh Token** (7 jours)
- **Logout** avec blacklist du token
- **Tentatives de connexion limitées** (rate limiting)

### Permissions
- **Rôles** :
  - **Super Admin** : Accès total (config, stats, clients, réservations)
  - **Admin** : Gestion quotidienne (réservations, clients) mais pas config sensible
  - **Lecteur** : Consultation seulement (stats, rapports)

### Audit Log
- **Traçabilité de toutes les actions** :
  - Qui a fait quoi, quand
  - Modifications des réservations
  - Remboursements
  - Modification des prestations
  - Exports de données
- **Conservation** : 1 an minimum (RGPD)

---

## 📱 Fonctionnalités CRM Mobile

### Application CRM Mobile (Phase 2)
- **React Native** ou **PWA** (Progressive Web App)
- **Fonctionnalités** :
  - Voir l'agenda du jour
  - Détails des prochains RDV
  - Marquer un RDV comme complété
  - Appeler/envoyer SMS au client
  - Notifications push pour nouveaux RDV

---

## 🗂️ Structure du Frontend CRM

```
crm-frontend/
├── app/
│   ├── (auth)/
│   │   └── login/page.tsx
│   │
│   ├── (dashboard)/
│   │   ├── layout.tsx              # Layout avec sidebar
│   │   ├── page.tsx                # Dashboard principal
│   │   │
│   │   ├── clients/
│   │   │   ├── page.tsx            # Liste clients
│   │   │   └── [id]/page.tsx       # Fiche client
│   │   │
│   │   ├── reservations/
│   │   │   ├── page.tsx            # Calendrier + liste
│   │   │   └── [id]/page.tsx       # Détails réservation
│   │   │
│   │   ├── prestations/
│   │   │   ├── page.tsx            # CRUD prestations
│   │   │   └── [id]/edit/page.tsx
│   │   │
│   │   ├── bons-cadeaux/
│   │   │   ├── page.tsx            # Liste bons cadeaux
│   │   │   └── [id]/page.tsx       # Détails
│   │   │
│   │   ├── paiements/
│   │   │   └── page.tsx            # Transactions
│   │   │
│   │   ├── disponibilites/
│   │   │   └── page.tsx            # Config horaires
│   │   │
│   │   ├── avis/
│   │   │   └── page.tsx            # Gestion avis
│   │   │
│   │   ├── statistiques/
│   │   │   └── page.tsx            # Rapports
│   │   │
│   │   └── parametres/
│   │       ├── page.tsx            # Config générale
│   │       ├── compte/page.tsx     # Profil admin
│   │       └── integrations/page.tsx
│   │
│   └── api/
│       └── auth/[...nextauth]/route.ts
│
├── components/
│   ├── layout/
│   │   ├── Sidebar.tsx
│   │   ├── Header.tsx
│   │   └── Navbar.tsx
│   ├── dashboard/
│   │   ├── StatsCard.tsx
│   │   ├── RevenueChart.tsx
│   │   └── UpcomingAppointments.tsx
│   ├── calendar/
│   │   ├── Calendar.tsx
│   │   └── EventModal.tsx
│   ├── tables/
│   │   ├── ClientsTable.tsx
│   │   ├── BookingsTable.tsx
│   │   └── DataTable.tsx         # Table générique réutilisable
│   └── forms/
│       ├── ClientForm.tsx
│       └── BookingForm.tsx
│
├── lib/
│   ├── api-client.ts             # Client API avec JWT
│   ├── auth.ts                   # NextAuth config
│   └── utils.ts
│
└── types/
    ├── client.ts
    ├── booking.ts
    └── stats.ts
```

---

## 🔗 API Backend - Endpoints CRM

### Authentification
```
POST   /api/v1/auth/login          # Login admin
POST   /api/v1/auth/refresh        # Refresh token
POST   /api/v1/auth/logout         # Logout (blacklist token)
```

### Dashboard
```
GET    /api/v1/admin/dashboard/stats      # Stats globales
GET    /api/v1/admin/dashboard/today      # Stats du jour
GET    /api/v1/admin/dashboard/upcoming   # Prochains RDV
```

### Clients (CRM)
```
GET    /api/v1/admin/clients              # Liste paginée + filtres
GET    /api/v1/admin/clients/{id}         # Fiche client
POST   /api/v1/admin/clients              # Créer client
PUT    /api/v1/admin/clients/{id}         # Modifier client
DELETE /api/v1/admin/clients/{id}         # Supprimer client
GET    /api/v1/admin/clients/{id}/bookings # Historique RDV
GET    /api/v1/admin/clients/segments     # Segments (VIP, inactifs, etc.)
POST   /api/v1/admin/clients/campaign     # Envoyer campagne SMS/Email
```

### Réservations
```
GET    /api/v1/admin/bookings             # Liste + filtres
GET    /api/v1/admin/bookings/{id}        # Détails
POST   /api/v1/admin/bookings             # Créer manuellement
PUT    /api/v1/admin/bookings/{id}        # Modifier
DELETE /api/v1/admin/bookings/{id}        # Annuler
POST   /api/v1/admin/bookings/{id}/complete # Marquer complété
POST   /api/v1/admin/bookings/{id}/remind  # Envoyer rappel
```

### Prestations
```
GET    /api/v1/admin/services             # CRUD
POST   /api/v1/admin/services
PUT    /api/v1/admin/services/{id}
DELETE /api/v1/admin/services/{id}
```

### Bons Cadeaux
```
GET    /api/v1/admin/gift-cards           # Liste
GET    /api/v1/admin/gift-cards/{id}      # Détails
PUT    /api/v1/admin/gift-cards/{id}/extend # Prolonger validité
DELETE /api/v1/admin/gift-cards/{id}      # Désactiver
POST   /api/v1/admin/gift-cards/{id}/resend # Renvoyer PDF
```

### Paiements
```
GET    /api/v1/admin/payments             # Transactions
GET    /api/v1/admin/payments/pending     # Virements en attente
POST   /api/v1/admin/payments/{id}/refund # Rembourser
PUT    /api/v1/admin/payments/{id}/confirm # Confirmer virement
```

### Disponibilités
```
GET    /api/v1/admin/availabilities       # Config horaires
POST   /api/v1/admin/availabilities
PUT    /api/v1/admin/availabilities/{id}
DELETE /api/v1/admin/availabilities/{id}
POST   /api/v1/admin/blocked-dates        # Bloquer date
DELETE /api/v1/admin/blocked-dates/{id}   # Débloquer
```

### Avis
```
GET    /api/v1/admin/reviews              # Sync Google
POST   /api/v1/admin/reviews/{id}/reply   # Répondre
```

### Statistiques
```
GET    /api/v1/admin/stats/monthly        # Rapport mensuel
GET    /api/v1/admin/stats/yearly         # Rapport annuel
GET    /api/v1/admin/stats/export         # Export CSV
```

### Paramètres
```
GET    /api/v1/admin/settings             # Config globale
PUT    /api/v1/admin/settings             # Modifier config
GET    /api/v1/admin/templates            # Templates SMS/Email
PUT    /api/v1/admin/templates/{type}     # Modifier template
```

---

## 🚀 Déploiement des 2 Frontends

### Frontend Public
```yaml
# Vercel config
name: serenaia-beaute-public
domains:
  - serenaia-beaute.fr
  - www.serenaia-beaute.fr
env:
  NEXT_PUBLIC_API_URL: https://api.serenaia-beaute.fr
```

### Frontend CRM
```yaml
# Vercel config
name: serenaia-beaute-crm
domains:
  - admin.serenaia-beaute.fr
env:
  NEXT_PUBLIC_API_URL: https://api.serenaia-beaute.fr
  NEXT_PUBLIC_CRM_MODE: true
```

### Backend API
```yaml
# Cloud Run
service: serenaia-api
url: https://api.serenaia-beaute.fr
```

---

## 📈 Roadmap CRM

### Phase 1 (MVP)
- ✅ Authentification admin
- ✅ Dashboard de base
- ✅ Gestion des réservations
- ✅ Gestion des clients (CRUD)
- ✅ Gestion des prestations
- ✅ Bons cadeaux

### Phase 2
- 📧 Campagnes marketing
- 📊 Statistiques avancées
- 📱 Version mobile (PWA)
- 🤖 Automatisations avancées

### Phase 3
- 🧠 IA : suggestions de créneaux optimaux
- 🎯 Recommandations personnalisées
- 📈 Prédictions de revenus
- 🔗 Intégration comptabilité (Pennylane, Quickbooks)

---

**Date de création:** 2026-01-11
**Version:** 1.0

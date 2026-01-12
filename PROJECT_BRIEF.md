# 🌸 Sérénaïa Beauté - Brief Projet

## 📋 Informations Générales

**Nom du projet:** Sérénaïa Beauté
**Baseline:** "La douceur et l'élégance au service de votre beauté"
**Type de site:** Site vitrine élégant
**Activité:** Esthétique et bien-être à domicile

---

## 🎯 Objectif du Site

Créer un site vitrine simple et élégant permettant de :
- Présenter les services d'esthétique à domicile
- Permettre la prise de rendez-vous en ligne
- Proposer des bons cadeaux
- Afficher les avis clients
- Faciliter le contact

---

## 📑 Structure du Site

### Navigation Principale

1. **Accueil**
2. **À propos**
3. **Prestations**
4. **Prendre rendez-vous**
5. **Offrir un bon cadeau**
6. **Avis**
7. **Contact**

---

## 💅 Prestations

### Catégories de Services

#### 1. Beauté des ongles
- Manucure
- Pose de vernis semi-permanent
- Nail art (à définir)

#### 2. Beauté du regard
- Extensions de cils
- Rehaussement de cils
- Teinture cils/sourcils
- Restructuration sourcils

#### 3. Soins du visage
- Soin hydratant
- Soin anti-âge
- Soin purifiant
- Nettoyage de peau

#### 4. Modelages bien-être
*(Massages non thérapeutiques)*
- Massage californien
- Massage suédois
- Massage aux pierres chaudes
- Durées : 30min, 1h, 1h30

#### 5. Épilations
- Sourcils
- Lèvre supérieure
- Aisselles
- Jambes complètes/demi-jambes
- Maillot (classique, échancré, intégral)

#### 6. Forfaits et offres spéciales
- Forfaits étudiants
- Réductions spéciales
- Packages combinés

### Format des Prestations

Chaque prestation doit afficher :
- ✅ **Nom de la prestation**
- ⏱️ **Durée** (ex: 30 min, 1h, 1h30)
- 💰 **Prix** (en euros)

---

## 📅 Système de Prise de Rendez-vous

### ✅ Solution Retenue : Développement Sur-Mesure

#### Interface Utilisateur
- Agenda clair avec disponibilités en temps réel
- Sélection de la prestation dans une liste déroulante
- Choix de la date et de l'heure (créneaux définis)
- Formulaire de coordonnées client (nom, prénom, email, téléphone)
- Récapitulatif avant validation
- Interface responsive (mobile-first)

#### Automatisations

**📧 Emails automatiques :**
- Confirmation de réservation
- Récapitulatif avec détails (prestation, date, heure, lieu)
- Rappel 24h avant le RDV
- Confirmation d'annulation

**📱 SMS automatiques via OVH SMS API :**
- Confirmation de réservation avec détails
- Rappel 24h avant le RDV
- Lien de paiement si nécessaire
- Notification d'annulation

#### Conditions de Réservation

**Politique d'annulation:**
- Annulation possible jusqu'à 24h avant le rendez-vous
- Passé ce délai, l'acompte reste dû et non remboursable
- Annulation possible depuis un lien dans l'email/SMS de confirmation

**💳 Paiement Multi-Méthodes:**
- **30% d'acompte obligatoire** OU **Paiement de la totalité** à la réservation
- **Modes de paiement acceptés :**
  - 💳 **Stripe** (Carte bancaire)
  - 💙 **PayPal**
  - 🏦 **Virement bancaire** (avec confirmation manuelle)
  - 📱 **Lydia**
  - 🟣 **Wero**
- Paiement sécurisé avec redirection ou iframe
- Reçu/facture envoyé par email

#### Fonctionnalités Administrateur
- Gestion de l'agenda (disponibilités, jours de congés)
- Définition des créneaux horaires
- Validation manuelle des virements
- Gestion des annulations et remboursements
- Export des rendez-vous (CSV, iCal)
- Statistiques de réservation

---

## 👩‍⚕️ Page "À propos"

### Contenu à Définir

**Éléments à inclure:**
- [ ] Photo professionnelle souriante
- [ ] Présentation personnelle et parcours
- [ ] Formations et certifications
- [ ] Années d'expérience
- [ ] Philosophie et valeurs
  - Pourquoi le choix du domicile
  - Approche personnalisée
  - Douceur et écoute
  - Professionnalisme
  - Hygiène irréprochable
- [ ] Zone d'intervention géographique
- [ ] Marques de produits utilisés

**Ton:** Chaleureux, rassurant, professionnel

---

## 🎨 Identité Visuelle

### Palette de Couleurs Suggérée
- Rose poudré
- Beige/Nude
- Doré/Or rose
- Blanc cassé
- Touches de vert pastel (naturel/bien-être)

### Style Photographique
- Lumineuse et épurée
- Ambiance zen et apaisante
- Photos de qualité professionnelle
- Mise en valeur des mains, du visage, de l'atmosphère

### Typographie
- Police élégante mais lisible
- Serif pour les titres (élégance)
- Sans-serif pour le corps de texte (lisibilité)

### Ambiance Générale
- Douceur
- Féminité
- Élégance discrète
- Professionnalisme
- Bien-être et relaxation

---

## 🎁 Bons Cadeaux

### ✅ Fonctionnalités Complètes

#### Types de Bons Cadeaux
- **Montant libre** : L'acheteur choisit le montant (ex: 50€, 100€, etc.)
- **Prestation définie** : Sélection d'une prestation spécifique (ex: "Soin visage 1h")

#### Processus d'Achat
1. Choix du type (montant libre ou prestation)
2. Personnalisation :
   - Nom du bénéficiaire
   - Message personnalisé (max 200 caractères)
   - Nom de l'expéditeur
3. **Paiement immédiat en ligne** (tous les moyens : Stripe, PayPal, Lydia, Wero, virement)
4. Génération automatique du bon cadeau

#### Format de Livraison
- **📧 Envoi par email** : Email avec PDF en pièce jointe + code promo
- **📄 PDF téléchargeable** : Design élégant aux couleurs de la marque
- Option : envoi différé (pour offrir à une date précise)

#### Sécurité et Validation
- **Code promo unique** à usage unique (format : SERA-XXXX-XXXX)
- Vérification automatique lors de la réservation
- Impossible d'utiliser plusieurs fois le même code
- Traçabilité : qui a acheté, qui utilise, quand

#### Durée de Validité
- **Paramétrable par l'administrateur** dans l'interface d'admin
- **Valeur par défaut : 1 an** à partir de la date d'achat
- Date d'expiration affichée sur le bon cadeau
- Alerte email 1 mois avant expiration

#### Fonctionnalités Administrateur
- Liste de tous les bons cadeaux émis
- Statut : actif, utilisé, expiré
- Prolongation manuelle possible
- Export des données (comptabilité)
- Statistiques de ventes de bons cadeaux

#### Design du PDF
- Logo Sérénaïa Beauté
- Informations : code, montant/prestation, validité
- Message personnalisé
- Instructions d'utilisation
- Coordonnées de contact

---

## ⭐ Avis Clients

### ✅ Solution Retenue

#### Intégration Google Reviews
- Widget Google Business Profile intégré au site
- Affichage de la note moyenne et du nombre d'avis
- Lien direct "Laisser un avis sur Google"
- Mise à jour automatique des avis
- Crédibilité et référencement naturel

#### Widget d'Avis Intégré au Site
- Section dédiée "Témoignages clients" sur la page d'accueil
- Carrousel des meilleurs avis Google
- Notation par étoiles (1 à 5)
- Affichage : prénom, date, commentaire, note
- Design élégant et cohérent avec la charte graphique

#### Affichage sur les Pages
- **Page d'accueil** : 3-5 meilleurs avis en carrousel
- **Page Avis** : Liste complète paginée avec filtres
- **Page Prestations** : Avis liés à chaque type de prestation (optionnel)

#### Fonctionnalités
- ✅ Automatique via Google Business Profile
- ✅ Pas de modération manuelle nécessaire
- ✅ Authenticité garantie par Google
- ❌ Pas de système maison avec modération (choix délibéré)
- ❌ Pas de Trustpilot dans un premier temps

#### Incitation aux Avis
- Email automatique 48h après la prestation
- SMS avec lien court vers Google Reviews
- QR Code sur les cartes de visite / factures
- Message personnalisé remerciant et invitant à laisser un avis

---

## 📞 Page Contact

### Informations à Afficher
- Formulaire de contact
- Téléphone
- Email
- Réseaux sociaux (Instagram, Facebook)
- Zone d'intervention
- Horaires de disponibilité

### Formulaire de Contact
- Nom et prénom
- Email
- Téléphone
- Message
- Objet de la demande (renseignement, réclamation, autre)

---

## 🔧 Spécifications Techniques

### ✅ Stack Technique VALIDÉE

#### Frontend
- **Framework** : **Next.js** (React avec SSR/SSG pour SEO optimal)
- **Styling** : **Tailwind CSS** (utility-first, personnalisable)
- **Design** : Responsive mobile-first
- **Animations** : Framer Motion (animations douces et élégantes)
- **Forms** : React Hook Form + Yup/Zod (validation)
- **State Management** : Context API ou Zustand (léger)
- **UI Components** : shadcn/ui ou Headless UI

#### Backend
- **Framework** : **Python + FastAPI** ✅
- **API** : RESTful (documentation auto avec OpenAPI/Swagger)
- **Authentification** : JWT pour l'espace admin
- **Validation** : Pydantic (validation native FastAPI)
- **ORM** : SQLAlchemy 2.0 + Alembic (migrations)
- **Task Queue** : Celery + Redis (envoi SMS/emails asynchrones)
- **Background Tasks** : FastAPI BackgroundTasks pour tâches légères

#### Base de Données
- **Base principale** : **PostgreSQL** (rendez-vous, clients, prestations, bons cadeaux)
- **Cache & Queue** : **Redis** (sessions, disponibilités, task queue Celery)
- **Stockage fichiers** : **Google Cloud Storage** (PDFs bons cadeaux)

#### Hébergement & Infrastructure (Google Cloud Platform)
- **Frontend** : **Vercel** (déploiement auto depuis GitHub, edge functions)
- **Backend** : **Google Cloud Run** (conteneurisation Docker, auto-scaling)
- **Base de données** : **Cloud SQL PostgreSQL** (managé, backups auto)
- **Cache** : **Memorystore Redis** (Redis managé GCP)
- **Storage** : **Google Cloud Storage** (bucket pour PDFs)
- **CDN** : **Cloud CDN** ou Cloudflare (performance et sécurité)
- **Secrets** : **Secret Manager** (GCP)
- **CI/CD** : **Cloud Build** + GitHub Actions

#### APIs Tierces & Intégrations

**💳 Paiements :**
- **Stripe** : CB, Apple Pay, Google Pay
- **PayPal** : Checkout classique
- **Lydia** : API de paiement
- **Wero** : Intégration API
- **Virement** : IBAN + confirmation manuelle

**📱 SMS :**
- **OVH SMS API** : Envoi de SMS transactionnels
  - Confirmation de RDV
  - Rappels 24h avant
  - Liens de paiement
  - Annulations

**📧 Emails :**
- **Resend** ou **SendGrid** : Emails transactionnels
- Templates HTML élégants et responsive
- Pièces jointes (bons cadeaux PDF)

**📅 Calendrier :**
- Calendrier custom développé en React
- Synchronisation optionnelle avec Google Calendar

**⭐ Avis :**
- **Google Business Profile API** : Récupération automatique des avis
- Widget personnalisé d'affichage

**📄 Génération PDF :**
- **Puppeteer** ou **PDFKit** : Génération des bons cadeaux
- Templates personnalisés

#### Sécurité
- **HTTPS** : Obligatoire (Let's Encrypt)
- **RGPD** : Conformité totale
- **Rate Limiting** : Protection contre les abus
- **CSRF Protection** : Tokens anti-CSRF
- **Input Validation** : Toutes les entrées validées
- **Secrets** : Variables d'environnement sécurisées

#### Monitoring & Analytics
- **Cloud Logging** : Logs centralisés GCP
- **Cloud Monitoring** : Métriques d'infrastructure (CPU, mémoire, latence)
- **Sentry** : Monitoring des erreurs applicatives (frontend + backend)
- **Google Analytics 4** : Statistiques de visite et conversions
- **Uptime Checks** : Cloud Monitoring ou UptimeRobot
- **APM** : Cloud Trace (traçabilité des requêtes)

---

## ✅ Récapitulatif des Décisions Techniques Validées

| Fonctionnalité | Solution Retenue | Détails |
|---------------|------------------|---------|
| **Réservation** | Développement sur-mesure | Calendrier React custom, gestion complète des disponibilités |
| **Paiement** | Multi-méthodes | Stripe, PayPal, Lydia, Wero, Virement bancaire |
| **SMS** | OVH SMS API | Confirmations, rappels, annulations |
| **Emails** | Resend/SendGrid | Templates HTML personnalisés |
| **Bons cadeaux** | Montant libre + Prestation | PDF téléchargeable + envoi email, code unique |
| **Validité bons** | Admin configurable | Défaut : 1 an |
| **Avis** | Google Reviews + Widget | Intégration automatique, pas de modération manuelle |
| **Acompte** | 30% ou totalité | Configurable par l'admin |
| **Annulation** | 24h avant | Après délai : acompte dû |

---

## 📱 Responsive Design

### Priorités Mobile
- Navigation simplifiée
- Boutons d'appel direct (click to call)
- Formulaire de rendez-vous optimisé
- Chargement rapide des images
- Menu burger élégant

---

## 🔒 Aspects Légaux

### Mentions Obligatoires
- [ ] Mentions légales
- [ ] Politique de confidentialité (RGPD)
- [ ] Conditions générales de vente (CGV)
- [ ] Politique de cookies
- [ ] Informations sur le traitement des données personnelles

---

## 📊 SEO & Marketing

### Optimisations SEO
- Mots-clés : "esthéticienne à domicile", "soins beauté domicile", "manucure domicile", etc.
- Balises meta optimisées
- Contenu de qualité sur chaque page
- Optimisation des images (alt, compression)
- Vitesse de chargement
- Sitemap XML

### Réseaux Sociaux
- Intégration Instagram (galerie de réalisations)
- Page Facebook professionnelle
- Boutons de partage

---

## ✅ Checklist de Développement

### Phase 1 : Conception
- [ ] Finaliser le contenu de la page "À propos"
- [ ] Définir la liste complète des prestations avec durées et prix
- [ ] Choisir la palette de couleurs définitive
- [ ] Sélectionner les typographies
- [ ] Créer une maquette (wireframe)

### Phase 2 : Contenu
- [ ] Rédiger tous les textes
- [ ] Préparer les photos professionnelles
- [ ] Définir la zone géographique d'intervention
- [ ] Créer les CGV et mentions légales

### Phase 3 : Technique
- [ ] Choisir la stack technique
- [ ] Configurer le système de réservation
- [ ] Intégrer le paiement en ligne
- [ ] Configurer l'envoi de SMS
- [ ] Développer le site
- [ ] Tests sur tous les devices

### Phase 4 : Lancement
- [ ] Acheter le nom de domaine
- [ ] Configurer l'hébergement
- [ ] Mise en ligne
- [ ] Tests finaux
- [ ] Référencement Google
- [ ] Communication sur les réseaux sociaux

---

## 💡 Questions en Suspens

### À Clarifier
1. **Zone géographique** : Quelle ville/région couvrez-vous ?
2. **Horaires** : Quels jours et horaires de disponibilité ?
3. **Produits** : Quelles marques utilisez-vous ?
4. **Tarifs** : Grille tarifaire complète à définir
5. **Budget** : Quel budget pour le développement du site ?
6. **Délai** : Date de mise en ligne souhaitée ?
7. **Nom de domaine** : www.serenaia-beaute.fr disponible ?

---

## 📅 Prochaines Étapes

1. Finaliser le contenu de la page "À propos"
2. Établir la grille tarifaire complète
3. Choisir les photos et créer l'identité visuelle
4. Sélectionner les outils techniques (réservation, paiement, SMS)
5. Créer les maquettes du site
6. Démarrer le développement

---

**Date de création du brief:** 2026-01-11
**Dernière mise à jour:** 2026-01-11
**Version:** 2.0 - Spécifications techniques validées

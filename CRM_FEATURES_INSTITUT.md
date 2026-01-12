# 💅 Fonctionnalités CRM Spécifiques Institut de Beauté

**Date:** 2026-01-11
**Version:** 1.0

---

## 🎯 Vue d'Ensemble

CRM complet pour institut de beauté à domicile avec **double canal de vente** :
- 🌐 **Vente en ligne** : Réservations + Bons cadeaux sur le site
- 🏠 **Vente directe** : Encaissement sur place, vente de produits, upselling

---

## 💰 Module : Point de Vente (POS) - Vente Directe

### Interface Caisse Tactile

#### Vue Principale
```
┌─────────────────────────────────────────────────────────────┐
│  🛒 CAISSE - Client: Marie Dupont                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PANIER:                                         TOTAL: 85€ │
│  ✅ Soin visage hydratant (1h)          65€                 │
│  ✅ Sérum anti-âge (produit)            20€                 │
│                                                              │
│  [📦 Ajouter prestation] [🛍️ Ajouter produit]              │
│  [💳 ENCAISSER]  [🎁 Bon cadeau]  [❌ Annuler]              │
└─────────────────────────────────────────────────────────────┘
```

#### Fonctionnalités POS

**1. Encaissement Rapide**
- Sélection rapide des prestations réalisées
- Ajout de produits vendus (scan QR ou recherche)
- Application automatique des remises (fidélité, promo)
- **Moyens de paiement** :
  - 💳 Carte bancaire (terminal physique intégré)
  - 💵 Espèces (avec gestion de la caisse)
  - 📱 Lydia / Wero (scan QR)
  - 🎁 Bon cadeau (validation du code)
  - 🔄 Mixte (exemple: 50€ bon cadeau + 35€ CB)

**2. Ticket de Caisse**
- Génération automatique du ticket
- Impression ou envoi par email/SMS
- QR code pour récupérer le ticket en PDF
- Mentions légales + TVA

**3. Gestion de la Caisse**
- **Ouverture de caisse** : Fond de caisse initial
- **Ventes de la journée** : Total espèces, CB, autres
- **Clôture de caisse** : Comptage, écarts, dépôt banque
- **Historique** : Toutes les transactions de la journée
- **Mouvements** : Entrées/sorties (achat fournitures, remboursement)

---

## 📦 Module : Gestion des Stocks & Produits

### Catalogue Produits

**Types de produits** :
- **Produits de vente** : Sérums, crèmes, vernis, etc. (vendus aux clientes)
- **Fournitures consommables** : Cotons, cire, gel UV, etc. (utilisés pendant les soins)
- **Équipement** : Matériel professionnel (table de massage, lampe UV, etc.)

#### Fiche Produit
- Nom, Marque, Référence
- Catégorie (visage, ongles, épilation, etc.)
- **Prix d'achat** (HT)
- **Prix de vente** (TTC) avec marge automatique
- **Stock actuel** / Seuil d'alerte
- Photo du produit
- Description / Utilisation
- Fournisseur (coordonnées)
- **Statut** : En vente, Rupture, Bientôt disponible

#### Gestion des Stocks
- **Inventaire** : Comptage périodique avec ajustement
- **Mouvements de stock** :
  - ➕ Entrée (réception commande fournisseur)
  - ➖ Sortie (vente ou utilisation pour prestation)
  - 📊 Historique complet des mouvements
- **Alertes automatiques** : SMS/email quand stock < seuil
- **Commandes fournisseurs** :
  - Liste des produits à commander
  - Génération bon de commande (PDF)
  - Suivi de la livraison

#### Valorisation du Stock
- **Valeur totale du stock** (prix d'achat × quantité)
- **Rotation des stocks** : Produits qui se vendent le plus/le moins
- **Produits périmés** : Alerte pour les cosmétiques (date de péremption)

---

## 👤 Module : Fiche Client Détaillée (Spécial Institut)

### Informations Personnelles Complètes

**Identité & Contact** :
- Nom, Prénom, Date de naissance
- Email, Téléphone (mobile + fixe)
- Adresse complète (pour interventions à domicile)
- Préférences de contact (email, SMS, téléphone)

**Profil Client** :
- **Date de première visite**
- **Fréquence de visite** : 1x/mois, 2x/mois, occasionnel
- **Panier moyen** : CA moyen par visite
- **CA total généré**
- **Segment** : VIP, Fidèle, Nouveau, Inactif, À risque
- **Source d'acquisition** : Réseaux sociaux, bouche-à-oreille, Google, autre

### 💅 Historique des Soins

**Liste chronologique** de toutes les prestations réalisées :
- Date, Heure
- Prestation(s) réalisée(s)
- Durée réelle de la prestation
- Produits utilisés pendant le soin
- Technicienne (si plusieurs)
- **Notes de soin** :
  - État de la peau / ongles / cheveux
  - Réaction aux produits
  - Résultat obtenu
  - Recommandations données
- **Photos avant/après** (avec consentement RGPD)

### 🏥 Informations Médicales & Allergies

**Questionnaire santé** (rempli à la première visite) :
- Allergies connues (produits, latex, etc.)
- Problèmes de peau (eczéma, psoriasis, acné, sensibilité)
- Traitements médicaux en cours (Roaccutane, anticoagulants, etc.)
- Grossesse / Allaitement
- Contre-indications (épilation, soins spécifiques)
- **Date de mise à jour** : Mise à jour annuelle obligatoire

### 🛍️ Historique des Achats Produits

- Liste des produits achetés
- Date d'achat
- Quantité, Prix
- **Recommandations de réachat** : Alerte quand produit devrait être fini (ex: 2 mois après achat d'une crème)

### 💳 Historique des Paiements

- Toutes les transactions (prestations + produits)
- Moyens de paiement utilisés
- Factures générées (téléchargement PDF)

### ⭐ Préférences & Notes

- **Prestations favorites**
- **Préférences** :
  - Horaires préférés (matin, après-midi, soir)
  - Jour de la semaine préféré
  - Température de la pièce (massage)
  - Musique d'ambiance (oui/non)
- **Notes privées** (admin uniquement) :
  - Caractère du client (patient, pressé, bavard, discret)
  - Particularités à retenir
  - Anniversaire (pour offres spéciales)

---

## 🎁 Module : Programme de Fidélité

### Système de Points

**Accumulation de points** :
- **1€ dépensé = 1 point** (configurable)
- Points valables 1 an
- Cumul sur prestations + produits
- Double points lors d'événements spéciaux (anniversaire, Noël)

**Utilisation des points** :
- **100 points = 5€ de réduction** (configurable)
- Utilisation partielle ou totale lors du paiement
- Historique des points gagnés/utilisés

### Cartes de Fidélité Digitales

**Carte virtuelle** (dans l'espace client ou app) :
- QR code unique
- Solde de points en temps réel
- Niveau de fidélité (Bronze, Argent, Or, Platine)
- Avantages du niveau actuel

**Niveaux de Fidélité** :
- 🥉 **Bronze** : 0-500€ dépensés → 5% de remise
- 🥈 **Argent** : 500-1000€ → 7% de remise + 1 soin offert/an
- 🥇 **Or** : 1000-2000€ → 10% de remise + 2 soins offerts/an + priorité RDV
- 💎 **Platine** : >2000€ → 15% de remise + 3 soins offerts/an + cadeaux VIP

### Offres Spéciales Fidélité

- **Anniversaire** : Soin offert ou réduction 20%
- **Parrainage** : 10€ offerts pour le parrain + 10€ pour le filleul
- **Réactivation** : Offre spéciale si pas de visite depuis 6 mois
- **Offres saisonnières** : Réductions sur certaines prestations (été: épilation, hiver: soins hydratants)

---

## 📅 Module : Planning Optimisé Institut

### Vue Planning Avancée

**Calendrier intelligent** avec :
- **Temps de préparation** : 10-15 min entre chaque client (nettoyage, setup)
- **Durée réelle vs durée théorique** : Tracking automatique
- **Trajet** : Temps de déplacement entre 2 clients à domicile (Google Maps API)
- **Codes couleur** :
  - 🟢 Confirmé + payé
  - 🟡 Confirmé mais paiement en attente
  - 🔵 Complété
  - 🟠 En cours (client présent)
  - 🔴 Annulé
  - ⚪ Créneau libre

### Gestion des Prestations Combinées

- **Forfaits** : Plusieurs soins à la suite (ex: Manucure + Pédicure)
- **Calcul automatique de la durée totale** + temps de préparation
- **Optimisation** : Suggestion de créneaux pour optimiser le remplissage

### Rappels & Notifications

**Notifications automatiques** :
- **Client** :
  - Confirmation RDV (immédiate)
  - Rappel 24h avant
  - Rappel 2h avant (optionnel)
  - Demande d'avis (48h après)
- **Admin** :
  - Nouveau RDV (notification push)
  - Annulation client
  - RDV du lendemain (récap chaque soir)

---

## 🎨 Module : Galerie & Portfolio

### Photos Avant/Après

**Gestion des photos** :
- **Upload** depuis le CRM ou l'app mobile
- **Association** à une prestation et un client
- **Consentement RGPD** : Formulaire de consentement signé électroniquement
  - Utilisation sur le site web (oui/non)
  - Utilisation sur les réseaux sociaux (oui/non)
  - Floutage du visage (option)
- **Tags** : Type de prestation, difficulté, résultat
- **Galerie publique** : Sélection des meilleures photos pour le site vitrine

### Suivi Visuel Client

- **Timeline visuelle** : Photos chronologiques d'un même client
- **Comparaison** : Avant/après superposés
- **Notes** : Produits utilisés, protocole suivi

---

## 📊 Module : Statistiques Avancées Institut

### Indicateurs de Performance (KPI)

**Activité** :
- Nombre de RDV par jour/semaine/mois
- **Taux de remplissage** : % de créneaux occupés
- Taux d'annulation
- Taux de no-show (client absent sans prévenir)
- Durée moyenne réelle des prestations vs durée théorique

**Financier** :
- CA quotidien/hebdomadaire/mensuel/annuel
- **Répartition CA** : Prestations vs Vente de produits
- Panier moyen par client
- **Marge brute** : CA - Coût des produits utilisés
- CA par prestation
- CA par canal (en ligne vs direct)

**Clients** :
- Nombre de nouveaux clients
- Taux de rétention (clients revenus)
- Fréquence moyenne de visite
- **Lifetime Value (LTV)** : CA moyen par client sur sa durée de vie
- Taux de transformation (visiteurs site → réservation)

**Produits** :
- Produits les plus vendus
- Rotation des stocks
- Marge par produit
- **Cross-selling** : Produits vendus après une prestation

### Rapports Automatiques

**Rapport quotidien** (envoyé chaque soir par email) :
- Nombre de RDV du jour
- CA du jour (prestations + produits)
- Prochains RDV du lendemain
- Alertes (stock faible, RDV en attente de confirmation)

**Rapport hebdomadaire** :
- Résumé de la semaine
- Comparaison avec semaine précédente
- Top 3 des prestations
- Top 3 des clients (CA)

**Rapport mensuel** :
- Bilan complet du mois
- Objectifs vs réalisé
- Évolution mois par mois
- Recommandations automatiques (augmenter prix, promouvoir prestation peu demandée, etc.)

---

## 🤖 Module : Automatisations Institut

### Automatisations Marketing

**Campagnes automatiques** :
- **Anniversaire client** : SMS/Email avec offre spéciale (ex: -20%)
- **Réactivation inactifs** : Après 3/6 mois sans visite
- **Recommandation de réachat produit** : 2 mois après achat
- **Saisonnalité** : Promotion épilation avant l'été, soins hydratants en hiver
- **Upselling** : Suggestion de soin complémentaire après réservation

### Automatisations Opérationnelles

- **Rappel de mise à jour questionnaire santé** : Tous les ans
- **Demande d'avis** : 48h après prestation
- **Demande de parrainage** : Après 3 prestations
- **Alerte stock bas** : Email automatique quand stock < seuil
- **Clôture de caisse automatique** : Récapitulatif envoyé à 21h

---

## 📱 Module : Application Mobile Technicienne

### Version Mobile du CRM (PWA ou App Native)

**Fonctionnalités essentielles** :
- 📅 **Agenda du jour** : Vue simplifiée des RDV
- 👤 **Fiche client rapide** : Infos essentielles (allergies, préférences)
- ✅ **Marquer RDV comme terminé** (avec heure exacte de fin)
- 💳 **Encaisser** : Interface POS mobile simplifiée
- 📸 **Prendre photos avant/après** directement dans l'app
- 📝 **Notes de soin** : Dictée vocale pour gagner du temps
- 🔔 **Notifications push** : Nouveau RDV, annulation, rappels
- 📍 **Navigation GPS** : Itinéraire vers l'adresse client (prestations à domicile)
- 💬 **Messagerie** : Communication avec les clients (SMS intégré)

---

## 🎯 Module : Objectifs & Motivation

### Définition des Objectifs

**Objectifs mensuels** :
- CA cible du mois
- Nombre de prestations cibles
- Vente de produits cible
- Nouveaux clients cibles

**Suivi en temps réel** :
- Progression vers l'objectif (%)
- Projection fin de mois
- Écart vs objectif
- Suggestions pour rattraper le retard

### Gamification (Motivation)

- 🏆 **Badges** : Débloquer des badges (ex: "100 clientes satisfaites", "1000€ de CA en un jour")
- 📊 **Statistiques personnelles** : Meilleur jour, meilleur mois, record CA
- 🎉 **Célébrations** : Animation quand objectif atteint

---

## 💬 Module : Communication Client

### Messagerie Intégrée

**SMS depuis le CRM** :
- Envoi de SMS groupés (campagnes)
- Envoi individuel depuis la fiche client
- Templates pré-enregistrés
- Historique des conversations
- Réponses clients (SMS bidirectionnel)

**Email depuis le CRM** :
- Envoi d'emails personnalisés
- Templates WYSIWYG
- Pièces jointes (factures, bons cadeaux)
- Tracking d'ouverture et de clics

### WhatsApp Business (Optionnel)

- Intégration WhatsApp Business API
- Confirmation de RDV via WhatsApp
- Rappels et notifications
- Support client

---

## 🧾 Module : Facturation & Comptabilité

### Génération Automatique de Factures

- Facture générée après chaque vente (prestation + produits)
- Numérotation automatique et chronologique
- **Mentions légales** : TVA, SIRET, CGV
- **Export comptable** : CSV, Excel pour expert-comptable
- Intégration possible avec **Pennylane**, **Quickbooks**, **Sage**

### Gestion de la TVA

- Calcul automatique de la TVA (20% pour produits, 20% pour prestations)
- Déclaration simplifiée (report mensuel/trimestriel)
- Export des données pour déclaration

### Analyse de Rentabilité

- **Coût de revient** par prestation :
  - Produits consommés
  - Temps passé
  - Charges fixes réparties
- **Marge par prestation**
- **Seuil de rentabilité** : Combien de RDV pour couvrir les charges

---

## 🔐 Module : Conformité RGPD

### Gestion des Consentements

- **Formulaire de consentement** à la première visite :
  - Collecte et utilisation des données personnelles
  - Photos avant/après
  - Communication marketing (email, SMS)
  - Partage sur réseaux sociaux
- **Historique des consentements** : Date, type, statut
- **Révocation** : Client peut retirer son consentement à tout moment

### Droits des Clients

- **Droit d'accès** : Téléchargement de toutes les données du client (PDF)
- **Droit de rectification** : Modification des données
- **Droit à l'oubli** : Suppression complète du compte (anonymisation)
- **Portabilité** : Export des données en JSON

### Sécurité des Données

- Chiffrement des données sensibles (santé, paiement)
- Authentification forte (2FA pour admin)
- Audit log de tous les accès aux données clients
- Sauvegarde automatique quotidienne (backup chiffré)

---

## 🎁 Fonctionnalités Bonus

### Réalité Augmentée (Phase 3)

- **Essai virtuel** : Couleurs de vernis, maquillage (app mobile)
- **Simulation** : Résultat attendu d'une prestation (ex: forme d'ongles)

### Intelligence Artificielle

- **Recommandations personnalisées** :
  - Soin adapté au type de peau (questionnaire + IA)
  - Produits recommandés basés sur historique
- **Prédiction de la demande** :
  - Périodes de forte affluence
  - Prestations les plus demandées par saison
- **Optimisation des prix** :
  - Prix dynamiques selon la demande (yield management)

### Marketplace Interne

- **Vente de produits en ligne** (boutique e-commerce intégrée)
- Commande en ligne, retrait sur place ou livraison
- Recommandations de produits après une prestation

---

## 📋 Récapitulatif des Modules CRM Institut

| Module | Priorité | Phase |
|--------|----------|-------|
| Point de Vente (POS) | 🔴 Haute | 1 - MVP |
| Gestion des Stocks | 🔴 Haute | 1 - MVP |
| Fiche Client Détaillée | 🔴 Haute | 1 - MVP |
| Historique des Soins | 🔴 Haute | 1 - MVP |
| Planning Optimisé | 🔴 Haute | 1 - MVP |
| Programme de Fidélité | 🟠 Moyenne | 2 |
| Galerie Avant/Après | 🟠 Moyenne | 2 |
| Statistiques Avancées | 🟠 Moyenne | 1 - MVP |
| Automatisations Marketing | 🟠 Moyenne | 2 |
| App Mobile Technicienne | 🟠 Moyenne | 2 |
| Objectifs & Motivation | 🟡 Basse | 3 |
| Messagerie Intégrée | 🟠 Moyenne | 2 |
| Facturation & Compta | 🔴 Haute | 1 - MVP |
| Conformité RGPD | 🔴 Haute | 1 - MVP |
| IA & Recommandations | 🟡 Basse | 3 |
| Réalité Augmentée | 🟡 Basse | 3 |

---

**Votre avis ?** Quelles fonctionnalités vous semblent **indispensables** pour le MVP (Phase 1) et lesquelles peuvent attendre ? 🤔

---

**Date de création:** 2026-01-11
**Version:** 1.0

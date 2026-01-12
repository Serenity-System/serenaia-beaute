#!/bin/bash

REPO="Serenity-System/serenaia-beaute-backend"

# BACK-1.1: Créer compte Sumup professionnel
gh issue create --repo $REPO \
  --title "[BACK-1.1] Créer compte Sumup professionnel" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer un compte professionnel Sumup pour accepter les paiements par carte.

## 📋 Tâche
- [ ] Aller sur https://sumup.fr
- [ ] Créer compte professionnel
- [ ] Vérifier identité (KYC)
- [ ] Noter credentials dans 1Password/Bitwarden

## ✅ Critère d'Acceptance
- [x] Compte Sumup créé et vérifié
- [x] Credentials sauvegardés de manière sécurisée

## ⏱️ Estimation: 30 min"

# BACK-1.2: Commander terminal Sumup Air
gh issue create --repo $REPO \
  --title "[BACK-1.2] Commander terminal Sumup Air" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Commander le terminal Sumup Air pour les paiements en institut.

## 📋 Tâche
- [ ] Se connecter compte Sumup
- [ ] Commander terminal Sumup Air
- [ ] Configurer adresse livraison
- [ ] Suivre livraison

## ✅ Critère d'Acceptance
- [x] Terminal commandé
- [x] Numéro de suivi obtenu

## 🔗 Dépendance: BACK-1.1

## ⏱️ Estimation: 20 min"

# BACK-1.3: Configurer compte Stripe production
gh issue create --repo $REPO \
  --title "[BACK-1.3] Configurer compte Stripe production" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer et configurer le compte Stripe pour les paiements en ligne.

## 📋 Tâche
- [ ] Créer compte Stripe sur https://stripe.com
- [ ] Activer compte (KYC)
- [ ] Récupérer clés API (test + production)
- [ ] Configurer webhook endpoints
- [ ] Sauvegarder credentials

## ✅ Critère d'Acceptance
- [x] Compte Stripe activé
- [x] Clés API sauvegardées

## ⏱️ Estimation: 45 min"

# BACK-1.4: Configurer compte PayPal Business
gh issue create --repo $REPO \
  --title "[BACK-1.4] Configurer compte PayPal Business" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer compte PayPal Business pour paiements alternatifs.

## 📋 Tâche
- [ ] Créer compte PayPal Business
- [ ] Vérifier compte (KYC)
- [ ] Créer app développeur
- [ ] Récupérer credentials API
- [ ] Sauvegarder credentials

## ✅ Critère d'Acceptance
- [x] Compte PayPal Business vérifié
- [x] Credentials API sauvegardées

## ⏱️ Estimation: 45 min"

# BACK-2.1: Analyser options virements bons cadeaux
gh issue create --repo $REPO \
  --title "[BACK-2.1] Analyser options virements bons cadeaux" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Analyser les 3 options de virements pour les bons cadeaux et recommander une approche.

## 📋 Tâche
- [ ] Lire options A/B/C dans docs
- [ ] Évaluer complexité technique chaque option
- [ ] Évaluer délais chaque option
- [ ] Évaluer coûts chaque option
- [ ] Recommandation motivée

## ✅ Critère d'Acceptance
- [x] Document d'analyse créé
- [x] Recommandation claire avec justification

## ⏱️ Estimation: 1h30"

# BACK-2.2: Documenter décision virements
gh issue create --repo $REPO \
  --title "[BACK-2.2] Documenter décision virements dans DECISIONS.md" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Documenter la décision finale sur les virements bons cadeaux.

## 📋 Tâche
- [ ] Créer fichier docs/DECISIONS.md
- [ ] Documenter option choisie
- [ ] Expliquer rationale
- [ ] Lister impacts techniques

## ✅ Critère d'Acceptance
- [x] DECISIONS.md créé et commité
- [x] Décision claire et documentée

## 🔗 Dépendance: BACK-2.1

## ⏱️ Estimation: 30 min"

# BACK-2.3: Créer workflow virement choisi
gh issue create --repo $REPO \
  --title "[BACK-2.3] Créer workflow technique virement choisi" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Créer le workflow technique pour l'option de virement choisie.

## 📋 Tâche
- [ ] Créer diagramme workflow (Mermaid)
- [ ] Documenter étapes techniques
- [ ] Lister endpoints API nécessaires
- [ ] Identifier tables BDD nécessaires

## ✅ Critère d'Acceptance
- [x] Workflow documenté dans docs/
- [x] Diagramme créé

## 🔗 Dépendance: BACK-2.2

## ⏱️ Estimation: 1h"

# BACK-3.1: Générer CGV avec générateur en ligne
gh issue create --repo $REPO \
  --title "[BACK-3.1] Générer CGV avec générateur en ligne" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Générer les Conditions Générales de Vente de base.

## 📋 Tâche
- [ ] Utiliser générateur CGV en ligne
- [ ] Remplir infos institut
- [ ] Télécharger CGV générées
- [ ] Sauvegarder version brute

## ✅ Critère d'Acceptance
- [x] CGV de base générées

## ⏱️ Estimation: 30 min"

# BACK-3.2: Adapter CGV secteur esthétique
gh issue create --repo $REPO \
  --title "[BACK-3.2] Adapter CGV au secteur esthétique" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Adapter les CGV aux spécificités du secteur esthétique.

## 📋 Tâche
- [ ] Ajouter clauses spécifiques esthétique
- [ ] Conditions annulation/modification RDV
- [ ] Politique hygiène/contre-indications
- [ ] Clauses bons cadeaux

## ✅ Critère d'Acceptance
- [x] CGV adaptées au secteur
- [x] Clauses spécifiques ajoutées

## 🔗 Dépendance: BACK-3.1

## ⏱️ Estimation: 1h30"

# BACK-3.3: Valider mentions légales RGPD
gh issue create --repo $REPO \
  --title "[BACK-3.3] Valider mentions légales RGPD" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Valider conformité RGPD des CGV et mentions légales.

## 📋 Tâche
- [ ] Vérifier clauses RGPD
- [ ] Vérifier droit à l'oubli
- [ ] Vérifier consentements
- [ ] Vérifier DPO/contact

## ✅ Critère d'Acceptance
- [x] CGV conformes RGPD
- [x] Checklist conformité complétée

## 🔗 Dépendance: BACK-3.2

## ⏱️ Estimation: 1h"

# BACK-3.4: Créer fichier docs/CGV.md
gh issue create --repo $REPO \
  --title "[BACK-3.4] Créer fichier docs/CGV.md" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer le fichier markdown avec les CGV finales.

## 📋 Tâche
- [ ] Créer docs/CGV.md
- [ ] Formatter en Markdown
- [ ] Ajouter table des matières
- [ ] Commiter fichier

## ✅ Critère d'Acceptance
- [x] docs/CGV.md créé et commité
- [x] Bien formaté en Markdown

## 🔗 Dépendance: BACK-3.3

## ⏱️ Estimation: 20 min"

# BACK-3.5: Créer fichier docs/MENTIONS_LEGALES.md
gh issue create --repo $REPO \
  --title "[BACK-3.5] Créer fichier docs/MENTIONS_LEGALES.md" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer les mentions légales du site.

## 📋 Tâche
- [ ] Créer docs/MENTIONS_LEGALES.md
- [ ] Éditeur du site
- [ ] Hébergeur
- [ ] CNIL/DPO
- [ ] Cookies/tracking

## ✅ Critère d'Acceptance
- [x] MENTIONS_LEGALES.md créé et commité
- [x] Toutes sections présentes

## ⏱️ Estimation: 30 min"

# BACK-4.1: Définir adresse institut
gh issue create --repo $REPO \
  --title "[BACK-4.1] Définir adresse institut (Google Maps)" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Définir l'adresse exacte de l'institut.

## 📋 Tâche
- [ ] Obtenir adresse exacte
- [ ] Vérifier sur Google Maps
- [ ] Obtenir coordonnées GPS
- [ ] Documenter dans config

## ✅ Critère d'Acceptance
- [x] Adresse complète documentée
- [x] Coordonnées GPS notées

## ⏱️ Estimation: 15 min"

# BACK-4.2: Définir rayon déplacement à domicile
gh issue create --repo $REPO \
  --title "[BACK-4.2] Définir rayon déplacement à domicile" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Définir la zone de déplacement à domicile.

## 📋 Tâche
- [ ] Décider rayon max (ex: 15km)
- [ ] Lister communes couvertes
- [ ] Documenter dans config

## ✅ Critère d'Acceptance
- [x] Rayon défini
- [x] Communes listées

## ⏱️ Estimation: 15 min"

# BACK-4.3: Documenter config géographique
gh issue create --repo $REPO \
  --title "[BACK-4.3] Documenter config géographique dans config.py" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Documenter la configuration géographique dans le code.

## 📋 Tâche
- [ ] Créer GEOGRAPHIC_CONFIG dans app/config.py
- [ ] Ajouter adresse institut
- [ ] Ajouter coordonnées GPS
- [ ] Ajouter rayon déplacement
- [ ] Commiter

## ✅ Critère d'Acceptance
- [x] Config géo dans config.py
- [x] Commité

## 🔗 Dépendance: BACK-4.1, BACK-4.2

## ⏱️ Estimation: 20 min"

# BACK-5.1: Lister 5-10 produits vendus
gh issue create --repo $REPO \
  --title "[BACK-5.1] Lister 5-10 produits vendus" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Lister les produits qui seront vendus au lancement.

## 📋 Tâche
- [ ] Lister 5-10 produits
- [ ] Nom produit
- [ ] Marque
- [ ] Catégorie

## ✅ Critère d'Acceptance
- [x] Liste produits créée (CSV/Excel)

## ⏱️ Estimation: 30 min"

# BACK-5.2: Définir prix et descriptions
gh issue create --repo $REPO \
  --title "[BACK-5.2] Définir prix et descriptions produits" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Définir prix et descriptions pour chaque produit.

## 📋 Tâche
- [ ] Prix TTC pour chaque produit
- [ ] Description courte (50 char)
- [ ] Description longue (200 char)
- [ ] Bénéfices/ingrédients clés

## ✅ Critère d'Acceptance
- [x] Prix définis pour tous produits
- [x] Descriptions rédigées

## 🔗 Dépendance: BACK-5.1

## ⏱️ Estimation: 1h"

# BACK-5.3: Créer fichier seed_data/products.json
gh issue create --repo $REPO \
  --title "[BACK-5.3] Créer fichier seed_data/products.json" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer le fichier JSON avec les produits pour seeding BDD.

## 📋 Tâche
- [ ] Créer seed_data/products.json
- [ ] Format JSON valide
- [ ] Tous champs présents
- [ ] Commiter

## ✅ Critère d'Acceptance
- [x] products.json créé et commité
- [x] JSON valide

## 🔗 Dépendance: BACK-5.2

## ⏱️ Estimation: 30 min"

# BACK-5.4: Trouver/créer images produits
gh issue create --repo $REPO \
  --title "[BACK-5.4] Trouver/créer images produits" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Obtenir images pour chaque produit.

## 📋 Tâche
- [ ] Photographier produits OU
- [ ] Télécharger images officielles marques
- [ ] Optimiser images (format webp)
- [ ] Sauvegarder dans assets/

## ✅ Critère d'Acceptance
- [x] 1 image minimum par produit
- [x] Images optimisées

## ⏱️ Estimation: 1h"

# BACK-5.5: Documenter fournisseurs
gh issue create --repo $REPO \
  --title "[BACK-5.5] Documenter fournisseurs produits" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Documenter les fournisseurs pour chaque produit.

## 📋 Tâche
- [ ] Créer docs/SUPPLIERS.md
- [ ] Lister fournisseurs
- [ ] Contacts
- [ ] Conditions commande

## ✅ Critère d'Acceptance
- [x] SUPPLIERS.md créé
- [x] Fournisseurs documentés

## ⏱️ Estimation: 30 min"

# BACK-6.1: Analyser gestion acomptes partiels
gh issue create --repo $REPO \
  --title "[BACK-6.1] Analyser gestion acomptes partiels BDD" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Analyser comment gérer les acomptes partiels dans la BDD.

## 📋 Tâche
- [ ] Lire ARCHITECTURE_BDD.md actuelle
- [ ] Identifier problèmes acomptes
- [ ] Proposer solution (champs/tables)
- [ ] Documenter proposition

## ✅ Critère d'Acceptance
- [x] Problème identifié
- [x] Solution proposée documentée

## ⏱️ Estimation: 1h"

# BACK-6.2: Modifier table payments
gh issue create --repo $REPO \
  --title "[BACK-6.2] Modifier table payments (amount_type)" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Ajouter champ amount_type à la table payments.

## 📋 Tâche
- [ ] Ajouter champ amount_type (ENUM: full, deposit, remaining)
- [ ] Mettre à jour ARCHITECTURE_BDD.md
- [ ] Documenter changement

## ✅ Critère d'Acceptance
- [x] Champ ajouté dans schéma BDD
- [x] Documentation mise à jour

## 🔗 Dépendance: BACK-6.1

## ⏱️ Estimation: 30 min"

# BACK-6.3: Ajouter relations Payment-Booking
gh issue create --repo $REPO \
  --title "[BACK-6.3] Ajouter relations Payment-Booking multiples" \
  --label "atomic,medium-task,phase-0" \
  --body "## 🎯 Objectif
Permettre plusieurs paiements pour une même réservation.

## 📋 Tâche
- [ ] Relation booking_id dans payments
- [ ] Permettre multiple payments par booking
- [ ] Documenter dans ARCHITECTURE_BDD.md

## ✅ Critère d'Acceptance
- [x] Relation 1-N documentée
- [x] Schéma BDD mis à jour

## 🔗 Dépendance: BACK-6.2

## ⏱️ Estimation: 45 min"

# BACK-6.4: Mettre à jour ARCHITECTURE_BDD.md
gh issue create --repo $REPO \
  --title "[BACK-6.4] Mettre à jour ARCHITECTURE_BDD.md final" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Mettre à jour le document d'architecture BDD avec les corrections acomptes.

## 📋 Tâche
- [ ] Ouvrir docs/ARCHITECTURE_BDD.md
- [ ] Mettre à jour diagramme
- [ ] Mettre à jour descriptions tables
- [ ] Ajouter exemples acomptes
- [ ] Commiter

## ✅ Critère d'Acceptance
- [x] ARCHITECTURE_BDD.md à jour
- [x] Commité

## 🔗 Dépendance: BACK-6.3

## ⏱️ Estimation: 30 min"

# BACK-6.5: Créer migration Alembic acomptes
gh issue create --repo $REPO \
  --title "[BACK-6.5] Créer migration Alembic pour acomptes" \
  --label "atomic,quick-win,phase-0" \
  --body "## 🎯 Objectif
Créer la migration Alembic pour les modifications acomptes.

## 📋 Tâche
- [ ] Créer migration Alembic
- [ ] Ajouter champ amount_type
- [ ] Test migration up
- [ ] Test migration down
- [ ] Commiter

## ✅ Critère d'Acceptance
- [x] Migration créée
- [x] Testée (up/down)
- [x] Commitée

## 🔗 Dépendance: BACK-6.4

## ⏱️ Estimation: 45 min"

echo "✅ Phase 0: 25 micro-issues créées !"

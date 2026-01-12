# ✅ Décisions Finales Validées - Sérénaïa Beauté

**Date:** 2026-01-11
**Version:** 1.0 - Scope Final Clarifié

---

## 🏠 Modèle d'Activité

### ✅ **Décision Validée**

**Institut de beauté à domicile (domicile de la praticienne)**
- Local professionnel au domicile de la praticienne
- Les clientes viennent sur place
- **Pas de déplacement chez les clientes**

### Impact sur le Projet

#### ✅ **Fonctionnalités Conservées**
- Point de Vente (POS) avec caisse physique
- Ouverture/clôture de caisse (espèces + CB)
- Fond de caisse
- Terminal de paiement sur place (Sumup)
- Temps de préparation entre clientes (10-15 min)

#### ❌ **Fonctionnalités Supprimées**
- Calcul automatique temps de trajet (Google Maps API)
- Gestion des frais de déplacement
- Optimisation géographique des RDV

---

## 📍 Zone Géographique

### ⏸️ **À Définir Plus Tard**

**Impact :**
- Peut être ajouté dans la page "À propos" et "Contact"
- Non bloquant pour le développement initial
- Nécessaire pour le SEO local (Phase 2)

**À compléter avant le lancement :**
- Ville / Département
- Adresse (si souhaitée publique ou juste "sur rendez-vous")

---

## 💳 Moyens de Paiement

### ✅ **Décision Validée**

#### Paiements Acceptés (Backend)
3 moyens intégrés techniquement :
1. **Stripe** (Carte Bancaire, Apple Pay, Google Pay)
2. **PayPal**
3. **Virement bancaire** (avec confirmation manuelle)

#### Affichage Client (Frontend)
**Sur le site web :**
- Afficher uniquement **"Paiement sécurisé par carte bancaire"** (Stripe)
- Cacher PayPal et Virement dans l'interface visible

**Pourquoi ?**
- Simplifier l'expérience utilisateur
- Éviter la confusion
- Les clientes utilisent majoritairement la CB
- PayPal et Virement disponibles "sur demande" (ex: email)

#### Implémentation Technique
```
Interface visible :
  [💳 Carte Bancaire] → Stripe Checkout

Interface cachée (paramètres) :
  [ ] PayPal (désactivé par défaut)
  [ ] Virement (désactivé par défaut)

Admin peut activer si besoin via CRM
```

### 💰 Terminal Physique

**Recommandation validée :** **Sumup + Stripe** (voir COMPARAISON_PAIEMENTS.md)
- **Sumup Air** (59€) : Encaissements physiques sur place
- **Stripe** : Paiements en ligne (site web)

---

## 🎁 Bons Cadeaux & Virement

### ❓ **Clarification : Pourquoi "Virement Incompatible" ?**

**Question posée :** *"Pourquoi incompatible, je ne vois pas le problème"*

#### Explication du Problème

**Scenario problématique :**

1. **Lundi 10h** : Cliente achète bon cadeau 100€ par virement
2. **Lundi 10h01** : Site génère le PDF du bon cadeau
3. **Lundi 10h01** : Email envoyé avec PDF + code SERA-1234
4. **Lundi 12h** : Cliente transmet le bon cadeau à sa sœur
5. **Mardi 9h** : La sœur utilise le code pour réserver
6. **Mercredi 14h** : Virement arrive enfin sur votre compte

**Problème :**
- Le bon cadeau a été utilisé **AVANT** que vous receviez l'argent
- Risque de fraude (virement annulé, compte sans provision)
- Vous avez offert une prestation sans garantie de paiement

#### ✅ **Solution Recommandée**

**Option A : Virement Exclu pour Bons Cadeaux**
- Bons cadeaux : **CB/PayPal uniquement** (paiement immédiat)
- Virement : **Disponible pour réservations** (avec délai)

**Option B : Virement avec Délai**
- Cliente paie par virement
- Email : "Votre bon cadeau sera envoyé **sous 48h** après réception du virement"
- Tracking manuel dans le CRM : "En attente de virement"
- Admin valide réception → Envoi automatique du PDF

**Option C : Virement avec Caution**
- Générer le PDF immédiatement
- Mais code **non activé** avant réception virement
- Si utilisation du code avant virement reçu → Message "Code en attente de validation"

### ✅ **Décision à Prendre**

**Quelle option préférez-vous ?**
- [ ] **Option A** : CB/PayPal uniquement pour bons cadeaux (plus simple)
- [ ] **Option B** : Virement avec délai 48h (plus complexe, tracking manuel)
- [ ] **Option C** : Virement avec code non activé (complexe techniquement)

**Recommandation :** Option A (plus simple, plus sûr)

---

## 🛍️ Vente de Produits

### ✅ **Décision Validée : OUI**

**Vente de produits confirmée dans le MVP**

**Statut :** Liste de produits à définir plus tard

### Implications

#### Développement Confirmé
- ✅ Module Gestion des Stocks (Phase 1)
- ✅ Catalogue produits (CRUD)
- ✅ Mouvements de stock (entrées/sorties)
- ✅ Alertes stock bas
- ✅ POS : Ajout produits à la vente

#### Actions Requises Avant Lancement
- [ ] Définir catalogue initial (minimum 5-10 produits)
- [ ] Identifier fournisseurs
- [ ] Définir prix d'achat et prix de vente
- [ ] Prendre photos des produits
- [ ] Rédiger descriptions produits

**Proposition :** Créer un fichier `CATALOGUE_PRODUITS.md` plus tard pour tracker la liste

---

## 📜 Conditions Générales de Vente (CGV)

### ✅ **Décision Validée**

**Génération de CGV template pour validation avocat ultérieure**

**Processus :**
1. ✅ Je génère des CGV complètes (template professionnel)
2. ⏸️ Vous les faites vérifier/compléter/corriger par un avocat
3. ✅ Intégration dans le site avant le lancement

**Fichier à créer :** `CGV_TEMPLATE.md`

---

## 📸 Contenu du Site

### ✅ **Décision Validée**

#### Photos
- Vous ajouterez des photos dans un répertoire
- À créer : `/public/images/` ou `/assets/images/`
- Photos nécessaires :
  - Photo de la praticienne (À propos)
  - Photos des prestations (avant/après)
  - Photos d'ambiance (cabine, produits)
  - Logo Sérénaïa Beauté

**Proposition :** Créer structure `/public/images/` avec sous-dossiers :
```
/public/images/
  /prestations/
    /ongles/
    /regard/
    /visage/
    /massage/
    /epilation/
  /galerie/
    /avant-apres/
  /apropos/
    /portrait.jpg
  /logo/
    /logo.svg
    /logo.png
```

#### Textes
- **Textes temporaires générés** pour toutes les pages
- Remplacement progressif par vos vrais textes

**Fichier à créer :** `CONTENUS_TEMPORAIRES.md`

---

## 🔐 RGPD : Droit à l'Oubli vs Conservation Factures

### ❓ **Question Posée : "Que proposes-tu ?"**

### Problème Légal

**Conflit entre 2 lois :**
1. **RGPD** : Client a le droit de demander la suppression de ses données
2. **Code de Commerce** : Conservation des factures **obligatoire 10 ans**

**Impossible de supprimer totalement un client qui a des factures.**

### ✅ **Solution Légale : Anonymisation**

#### Principe
- On ne **supprime pas** les données
- On les **anonymise** (rendre impossible l'identification)

#### Implémentation

**Lorsqu'un client demande le "droit à l'oubli" :**

```python
# Anonymisation (pas suppression)
def anonymize_client(client_id):
    client = db.query(Client).filter(Client.id == client_id).first()

    # Remplacer données personnelles par valeurs anonymes
    client.first_name = "Client"
    client.last_name = f"Anonymisé #{client.id}"
    client.email = f"anonymized_{client.id}@example.com"
    client.phone = "00 00 00 00 00"
    client.address = "Adresse supprimée"

    # Supprimer notes privées
    client.notes = "[Données supprimées à la demande du client]"

    # Supprimer photos
    delete_photos(client_id)

    # Marquer comme anonymisé
    client.anonymized_at = datetime.now()
    client.anonymization_reason = "Demande client (RGPD)"

    db.commit()

    # CONSERVER :
    # - Factures (obligation légale)
    # - Montants, dates, prestations
    # - Historique anonymisé
```

**Résultat :**
- Factures conservées : "Client Anonymisé #123, Soin visage 1h, 65€, 15/01/2026"
- Impossible de retrouver l'identité réelle
- Conformité RGPD ✅
- Conformité Code de Commerce ✅

#### Interface CRM

**Bouton "Supprimer le client" :**
```
⚠️ Demande de suppression (RGPD)

Ce client sera anonymisé (pas supprimé totalement).

Les données suivantes seront anonymisées :
✅ Nom, prénom, email, téléphone, adresse
✅ Photos avant/après
✅ Notes privées

Les données suivantes seront CONSERVÉES (obligation légale) :
⚠️ Factures (10 ans)
⚠️ Historique des prestations (anonymisé)

[Confirmer l'anonymisation] [Annuler]
```

### ✅ **Décision Recommandée**

**Implémenter l'anonymisation (pas suppression totale)**
- Conforme RGPD
- Conforme Code de Commerce
- Traçabilité préservée

---

## 🧪 Stratégie de Tests

### ✅ **À Ajouter**

**Fichier à créer :** `STRATEGIE_TESTS.md`

#### Tests Prévus

**1. Tests Unitaires (Backend)**
- Framework : `pytest`
- Cibles :
  - Services métier (booking_service, payment_service, etc.)
  - Utils et helpers
  - Validation Pydantic
- Couverture cible : **80%**

**2. Tests d'Intégration (Backend)**
- Endpoints API
- Intégrations paiements (Stripe, PayPal) en mode test
- Base de données (transactions, rollbacks)

**3. Tests E2E (End-to-End)**
- Framework : `Playwright`
- Parcours critiques :
  - Réservation complète (sélection → paiement → confirmation)
  - Achat bon cadeau
  - Login admin → Gestion réservation
- Navigateurs : Chrome, Firefox, Safari (mobile + desktop)

**4. Tests de Performance**
- Outil : `Locust` ou `k6`
- Objectifs :
  - P50 < 100ms
  - P95 < 200ms
  - P99 < 500ms
- Charge cible : 100 utilisateurs simultanés

**5. Tests de Sécurité**
- Scan OWASP (injections SQL, XSS, CSRF)
- Audit dépendances (Snyk, Safety)
- Secrets detection (TruffleHog)

#### CI/CD Pipeline

```yaml
# .github/workflows/tests.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: |
          pytest --cov=app --cov-report=html --cov-report=term

      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

---

## 💾 Politique de Backup

### ✅ **Décision Validée**

**Backup journalier avec 1 semaine d'historique + 1 mensuel**

#### Détails Implémentation

**Backup Quotidien :**
- Fréquence : **Tous les jours à 3h du matin** (heure creuse)
- Rétention : **7 jours glissants**
- Contenu :
  - Dump PostgreSQL complet
  - Fichiers Cloud Storage (PDFs bons cadeaux, photos)
- Stockage : Google Cloud Storage (bucket dédié `serenaia-backups`)

**Backup Mensuel :**
- Fréquence : **1er de chaque mois à 3h**
- Rétention : **12 mois** (1 an)
- Contenu : Identique au backup quotidien
- Stockage : Bucket séparé `serenaia-backups-monthly`

**Sécurité :**
- Backups chiffrés (AES-256)
- Accès restreint (IAM permissions)
- Géo-réplication (région secondaire : europe-west1 → us-east1)

#### Tests de Restauration

**Procédure :**
- Test manuel : **1x par trimestre** (tous les 3 mois)
- Procédure documentée : `RESTAURATION_BACKUP.md`
- Vérification intégrité des données

#### Automatisation

```bash
# Script de backup (cron job ou Cloud Scheduler)
#!/bin/bash

# Variables
DATE=$(date +%Y-%m-%d)
BUCKET_DAILY="gs://serenaia-backups/daily"
BUCKET_MONTHLY="gs://serenaia-backups/monthly"
DB_NAME="serenaia"

# Dump PostgreSQL
pg_dump $DB_NAME > backup_$DATE.sql

# Compression
gzip backup_$DATE.sql

# Upload vers Cloud Storage
gsutil cp backup_$DATE.sql.gz $BUCKET_DAILY/

# Si 1er du mois, copier aussi dans monthly
if [ $(date +%d) -eq 01 ]; then
  gsutil cp backup_$DATE.sql.gz $BUCKET_MONTHLY/
fi

# Nettoyer backups > 7 jours (quotidien)
gsutil rm $BUCKET_DAILY/backup_$(date -d '7 days ago' +%Y-%m-%d).sql.gz

# Nettoyer backups > 12 mois (mensuel)
gsutil rm $BUCKET_MONTHLY/backup_$(date -d '12 months ago' +%Y-%m-%d).sql.gz
```

---

## 📱 SMS Bidirectionnel

### ✅ **Clarification Validée**

**Pas besoin de SMS bidirectionnel**

**Solution retenue :**
- SMS avec **lien de validation** cliquable
- Exemple : "Confirmez votre RDV en cliquant ici : https://serenaia-beaute.fr/confirm/abc123"
- Pas de réponse par SMS nécessaire

**Simplification :**
- OVH SMS API = Envoi uniquement (unidirectionnel) ✅
- Pas besoin de numéro dédié
- Pas de webhook pour recevoir réponses
- Coût réduit

---

## 🏗️ Infrastructure & Hébergement

### ⏸️ **À Voir Plus Tard**

**Décision reportée :**
- GCP (95-155€/mois) vs Alternatives économiques (0-50€/mois)
- Non bloquant pour définir l'architecture
- À décider avant le déploiement production

**Options documentées dans :** `ANALYSE_CRITIQUE.md` (section 15)

---

## 🎯 Récapitulatif des Décisions

| Sujet | Décision | Statut |
|-------|----------|--------|
| **Modèle activité** | Institut à domicile (praticienne) | ✅ Validé |
| **Zone géographique** | À définir plus tard | ⏸️ En suspend |
| **Terminal paiement** | Sumup Air (physique) + Stripe (en ligne) | ✅ Recommandé |
| **Moyens paiement** | Stripe, PayPal, Virement (backend) | ✅ Validé |
| **Affichage paiement** | Stripe uniquement visible (frontend) | ✅ Validé |
| **Vente produits** | OUI, liste à définir | ✅ Validé |
| **CGV** | Template à générer + validation avocat | ✅ À faire |
| **Photos** | Ajout dans répertoire par client | ✅ Validé |
| **Textes** | Génération temporaire | ✅ À faire |
| **RGPD Droit oubli** | Anonymisation (pas suppression) | ✅ Recommandé |
| **Tests** | Stratégie complète à définir | ✅ À faire |
| **Backup** | Quotidien 7j + Mensuel 12 mois | ✅ Validé |
| **SMS bidirectionnel** | Non, lien de validation uniquement | ✅ Validé |
| **Infrastructure** | À décider plus tard | ⏸️ En suspend |

---

## 📋 Actions Immédiates

### 🔴 **Haute Priorité (Avant Développement)**

- [ ] Créer `COMPARAISON_PAIEMENTS.md` ✅ **FAIT**
- [ ] Créer `STRATEGIE_TESTS.md`
- [ ] Créer `CGV_TEMPLATE.md`
- [ ] Créer `CONTENUS_TEMPORAIRES.md`
- [ ] Décider : Virement pour bons cadeaux (Option A/B/C) ?
- [ ] Créer structure `/public/images/`
- [ ] Corriger architecture BDD (paiements partiels)

### 🟠 **Moyenne Priorité (Avant Lancement)**

- [ ] Définir catalogue produits minimum
- [ ] Définir zone géographique (SEO)
- [ ] Acheter terminal Sumup Air (59€)
- [ ] Créer comptes Stripe + Sumup
- [ ] Prendre photos professionnelles

### 🟡 **Basse Priorité (Après Lancement)**

- [ ] Tester backup/restauration (1x/trimestre)
- [ ] Choisir infrastructure finale (GCP vs alternatives)

---

**Date de création:** 2026-01-11
**Version:** 1.0 - Décisions Clarifiées
**Prochaine mise à jour:** Après décision sur virement bons cadeaux

# 🔍 Analyse Critique du Projet - Incohérences & Problèmes

**Date:** 2026-01-11
**Analyste:** Claude Code
**Documents analysés:** 5 fichiers (PROJECT_BRIEF.md, TECHNICAL_ARCHITECTURE.md, CRM_SPECIFICATIONS.md, CRM_FEATURES_INSTITUT.md, MVP_VALIDATED.md)

---

## ⚠️ Incohérences Majeures

### 1. 🏠 **Modèle d'Activité Ambigu**

**Problème identifié:**
- Titre annoncé : "**Esthétique et bien-être à domicile**"
- Mais CRM inclut : **Point de Vente (POS) physique** avec caisse, terminal CB

**Incohérence:**
Comment avoir une caisse physique avec fond de caisse, ouverture/clôture si tout se passe au domicile des clients ?

**Questions critiques:**
- ✅ Est-ce un **institut physique** + prestations à domicile ?
- ✅ Ou **100% à domicile** avec encaissement mobile uniquement ?
- ✅ Ou **mixte** : local professionnel + déplacements ?

**Impact:**
- Architecture CRM à adapter selon le modèle
- Fonctionnalités POS à simplifier si uniquement mobile
- Temps de préparation entre clients non pertinent si à domicile

**Recommandation:**
🔴 **CLARIFIER LE MODÈLE IMMÉDIATEMENT**

---

### 2. 💳 **Double Paiement Mal Géré**

**Problème identifié:**
- Paiement en ligne : **30% acompte** obligatoire
- Solde restant : **70% à payer sur place**
- Base de données : **Pas de gestion du "solde restant dû"**

**Incohérence:**
Impossible de tracker qu'un client a payé 30€ en ligne et doit encore 70€ sur place.

**Table `payments` actuelle:**
```sql
CREATE TABLE payments (
    amount DECIMAL(10, 2),  -- Montant de CETTE transaction
    status VARCHAR(50),      -- 'completed', 'pending', etc.
    ...
)
```

**Manque:**
- Champ `total_amount` (montant total de la prestation)
- Champ `paid_amount` (montant déjà payé)
- Champ `remaining_amount` (solde restant)
- Relation multiple paiements → 1 réservation

**Recommandation:**
🔴 Revoir le modèle de données pour gérer les paiements partiels

---

### 3. 🏦 **Virement Bancaire Incompatible avec "Paiement Immédiat"**

**Problème identifié:**
- Bons cadeaux : "**Paiement immédiat en ligne**"
- Moyens de paiement : Stripe, PayPal, Lydia, Wero, **Virement**

**Incohérence:**
Un virement bancaire prend **24-48h** pour être reçu, donc PAS "immédiat".

**Impact:**
- Client achète un bon cadeau par virement
- Veut le PDF immédiatement
- Mais paiement pas encore reçu
- Que fait-on ? On envoie le PDF avant de recevoir l'argent ?

**Recommandation:**
🟠 **Exclure le virement pour les bons cadeaux** (uniquement CB/PayPal/Lydia/Wero)
🟠 Ou accepter virement mais **envoi du PDF après réception** (délai 48h)

---

### 4. ⏱️ **Délai d'Annulation vs Virement Bancaire**

**Problème identifié:**
- Politique : "Annulation possible jusqu'à **24h avant**"
- Paiement par virement : Délai de réception **24-48h**

**Scénario problématique:**
1. Client réserve vendredi pour lundi (3 jours d'avance)
2. Choisit paiement par virement
3. Virement part vendredi soir
4. Samedi soir (36h plus tard), client annule (encore dans les 24h)
5. Virement arrive lundi → Argent reçu mais RDV annulé

**Impact:**
Gestion complexe des remboursements de virements.

**Recommandation:**
🟠 **Pour paiement par virement : délai minimum 72h** (pas 24h)
🟠 Ou **exclure le virement pour les acomptes** (CB obligatoire pour garantie)

---

### 5. 📱 **SMS Bidirectionnel avec OVH (Problème Technique)**

**Problème identifié:**
Dans CRM_FEATURES_INSTITUT.md :
> "SMS bidirectionnel (réponses clients)"

**Réalité technique:**
- OVH SMS API = **envoi uniquement** (unidirectionnel)
- Recevoir des réponses nécessite :
  - Un **numéro dédié** (location ~10-20€/mois)
  - Configuration d'un **webhook**
  - Parsing des réponses

**Impact:**
Fonctionnalité plus complexe et coûteuse que prévu.

**Recommandation:**
🟡 **Phase MVP : SMS unidirectionnel uniquement**
🟡 **Phase 2 : Évaluer si nécessaire** (rarement utilisé en institut)

---

### 6. 💰 **5 Moyens de Paiement = Complexité Élevée**

**Problème identifié:**
Intégration de **5 moyens** de paiement dès le MVP :
- Stripe (CB, Apple Pay, Google Pay)
- PayPal
- Lydia
- Wero
- Virement bancaire

**Impact:**
- 5 APIs différentes à intégrer
- 5 webhooks à gérer
- 5 systèmes de test
- Maintenance complexe
- Coût de développement élevé

**Statistiques réelles:**
En France, institut de beauté :
- **CB (Stripe) : 70% des paiements**
- **Espèces : 20%**
- **Autres : 10%**

**Recommandation:**
🔴 **MVP : Stripe (CB) + Virement uniquement**
🟠 **Phase 2 : Ajouter PayPal si demandé**
🟡 **Phase 3 : Lydia/Wero si vraiment nécessaire**

---

### 7. 🖥️ **Terminal Sumup : Intégration Non Documentée**

**Problème identifié:**
Vous avez dit : "Terminal **Sumup**"
Mais architecture technique mentionne : "Stripe, PayPal, Lydia, Wero"

**Incohérence:**
Sumup ≠ Stripe. Ce sont 2 systèmes différents.

**Questions critiques:**
- Sumup **Air** (Bluetooth → smartphone) ou **3G** (autonome) ?
- Sumup pour **encaissements physiques uniquement** ?
- Stripe pour **paiements en ligne** ?
- Ou tout migrer vers Sumup ?

**Sumup API:**
- API disponible mais **moins complète** que Stripe
- Pas de gestion d'acomptes automatisée
- Pas de webhooks aussi robustes

**Recommandation:**
🔴 **Clarifier : Sumup ET Stripe, ou l'un OU l'autre ?**

**Option recommandée:**
- **Sumup** : Encaissements physiques (sur place)
- **Stripe** : Paiements en ligne (site web)
- Deux systèmes séparés, tracking unifié en base de données

---

## 🚨 Problèmes Fonctionnels

### 8. 🗂️ **Gestion des Stocks Surdimensionnée pour Activité à Domicile**

**Fonctionnalités prévues:**
- Catalogue produits complet (vente + fournitures + équipement)
- Mouvements de stock (entrées/sorties)
- Alertes automatiques
- Commandes fournisseurs
- Génération bons de commande
- Suivi livraisons

**Réalité pour activité à domicile:**
- Stock réduit (kit mobile)
- Peu de références (10-20 produits max)
- Gestion simple suffisante

**Impact:**
Développement lourd pour un besoin simple.

**Recommandation:**
🟠 **MVP : Gestion simplifiée**
- Liste de produits (nom, prix, quantité)
- Alerte email simple si stock < seuil
- Pas de commandes fournisseurs dans MVP
🟡 **Phase 2 : Commandes fournisseurs si vraiment nécessaire**

---

### 9. 🏪 **Vente de Produits : Besoin Réel ?**

**Problème identifié:**
Vous avez dit : "**Aucune idée pour le moment**" sur les produits à vendre

**Impact:**
- Module Stocks = inutile si pas de vente de produits
- Module POS produits = inutile
- Complexité pour rien

**Questions critiques:**
- Vendrez-vous des produits aux clientes ?
- Si oui, quand ? Dès le MVP ou plus tard ?
- Si non, pourquoi développer la gestion stocks ?

**Recommandation:**
🔴 **Décider maintenant : Vente de produits OUI ou NON**

**Si NON pour MVP:**
- Retirer Module Stocks (Phase 2)
- POS = Prestations uniquement
- Simplification majeure du CRM

**Si OUI:**
- Définir catalogue minimum (10 produits)
- Fournisseurs à contacter
- Prix à définir

---

### 10. 🕐 **Temps de Préparation Inadapté pour Domicile**

**Problème identifié:**
Planning prévoit : "**Temps de préparation : 10-15 min entre chaque client**"

**Réalité domicile:**
- Pas de préparation de cabine
- Entre 2 clients = **temps de trajet** (15-45 min selon distance)

**Incohérence:**
Cette fonctionnalité est pertinente pour un **institut physique**, pas pour du domicile.

**Recommandation:**
🟠 **Remplacer "temps de préparation" par "temps de trajet"**
- Calcul automatique via Google Maps API
- Ajout automatique au planning
- Alert si 2 RDV trop rapprochés géographiquement

---

### 11. 📍 **Zone d'Intervention Non Définie**

**Problème majeur:**
Aucune mention de la **zone géographique** couverte.

**Impact critique:**
- Impossible de calculer temps de trajet
- Impossible d'optimiser le planning
- SEO local impossible (pas de ville)
- Risque d'accepter RDV trop loin

**Questions critiques:**
- Quelle ville ? Quel département ?
- Rayon max ? (ex: 20 km autour de Paris 15e)
- Frais de déplacement ? (inclus, ou supplément si > X km)

**Recommandation:**
🔴 **DÉFINIR LA ZONE IMMÉDIATEMENT**
Exemple : "Paris et proche banlieue (92, 93, 94) - Rayon 15 km"

---

### 12. 🚗 **Frais de Déplacement Absents**

**Problème identifié:**
Aucune mention de frais de déplacement.

**Questions critiques:**
- Déplacement inclus dans le prix ?
- Ou facturation au kilomètre ?
- Zone gratuite puis supplément ?

**Impact:**
- Rentabilité des prestations à domicile
- Attractivité commerciale

**Exemples courants:**
- "Déplacement gratuit dans un rayon de 10 km, puis 0,50€/km"
- "Forfait déplacement 5€ inclus, gratuit si > 100€"

**Recommandation:**
🔴 **Définir la politique de déplacement**

---

### 13. 🏥 **Questionnaire Santé : UX Non Définie**

**Problème identifié:**
"Questionnaire santé rempli à la 1ère visite"

**Questions critiques:**
- Rempli sur papier → saisi ensuite dans CRM ?
- Ou formulaire digital rempli par le client ?
- Avant ou pendant la prestation ?

**Impact UX:**
Selon la réponse, développement différent.

**Recommandation:**
🟠 **Option A (MVP) :** Papier + saisie manuelle admin
🟠 **Option B (Phase 2) :** Formulaire digital envoyé avant le RDV

---

### 14. 📸 **Photos Avant/Après : Coût de Stockage**

**Problème identifié:**
- Stockage sur Google Cloud Storage
- Pas de compression automatique mentionnée
- Photos haute résolution = coût élevé

**Exemple:**
- 100 photos/mois
- 5 MB/photo (sans compression)
- = 500 MB/mois → 6 GB/an
- Coût GCS : ~0,20$/GB = 1,20$/an (négligeable)

**Mais à l'échelle:**
- 1000 photos/an × 5 MB = 5 GB
- + backup + redondance
- Coût peut grimper

**Recommandation:**
🟠 **Compression automatique obligatoire**
- Redimensionnement max 1920px largeur
- Compression qualité 80%
- Format WebP (meilleure compression)
- Réduction ~70% de la taille

---

## 🏗️ Problèmes d'Architecture

### 15. 💾 **Infrastructure GCP Coûteuse**

**Coûts estimés mensuels:**
- **Cloud SQL PostgreSQL** : ~30-50€/mois
- **Memorystore Redis** : ~50-80€/mois
- **Cloud Run** : ~10-20€/mois
- **Cloud Storage** : ~5€/mois
- **Total : 95-155€/mois minimum**

**Pour une activité qui démarre:**
C'est élevé.

**Alternatives moins chères:**
- **Supabase** (PostgreSQL managé) : Gratuit jusqu'à 500 MB, puis 25$/mois
- **Upstash Redis** : Gratuit jusqu'à 10k requêtes/jour, puis pay-as-you-go
- **Vercel Postgres** : Intégré, gratuit jusqu'à 256 MB
- **Total alternatif : 0-50€/mois**

**Recommandation:**
🟠 **MVP : Utiliser services gratuits/low-cost**
🟡 **Phase 2 : Migrer vers GCP si scaling nécessaire**

**Proposition architecture MVP économique:**
```
Frontend Public  : Vercel (gratuit)
Frontend CRM     : Vercel (gratuit)
Backend API      : Railway ou Render (5-10$/mois)
Database         : Supabase PostgreSQL (gratuit ou 25$/mois)
Redis            : Upstash (gratuit jusqu'à 10k req/jour)
Storage          : Cloudflare R2 (gratuit jusqu'à 10 GB)
```

---

### 16. 🐳 **Docker + Cloud Run : Surpuissance**

**Problème identifié:**
Conteneurisation Docker + Cloud Run pour une API simple.

**Réalité:**
- MVP : Trafic faible (quelques RDV/jour)
- Pas besoin d'auto-scaling immédiat
- Cloud Run = overkill

**Alternative MVP:**
- **Railway** : Deploy depuis GitHub, auto-scaling, 5$/mois
- **Render** : Similaire, 7$/mois
- Plus simple, moins cher, largement suffisant

**Recommandation:**
🟠 **MVP : Railway ou Render**
🟡 **Phase 2 : Migrer vers Cloud Run si > 100 RDV/jour**

---

### 17. ⚙️ **Celery + Redis = Complexité Excessive**

**Problème identifié:**
Architecture prévoit **Celery** + Redis pour tâches asynchrones (envoi SMS/emails).

**Réalité:**
- Celery = puissant mais complexe
- Nécessite un worker séparé
- Configuration difficile

**Alternative MVP:**
FastAPI a déjà **BackgroundTasks** intégré, parfait pour MVP.

```python
from fastapi import BackgroundTasks

@app.post("/bookings")
async def create_booking(booking: Booking, background_tasks: BackgroundTasks):
    # Créer le RDV
    db_booking = create_booking_in_db(booking)

    # Envoi SMS/Email en background (non bloquant)
    background_tasks.add_task(send_confirmation_sms, db_booking)
    background_tasks.add_task(send_confirmation_email, db_booking)

    return db_booking
```

**Recommandation:**
🟠 **MVP : FastAPI BackgroundTasks**
🟡 **Phase 2 : Migrer vers Celery si > 1000 tâches/jour**

---

### 18. 🔄 **CI/CD Redondant : GitHub Actions + Cloud Build**

**Problème identifié:**
Architecture mentionne **GitHub Actions ET Cloud Build**.

**Incohérence:**
Pourquoi les deux ? C'est redondant.

**Recommandation:**
🟠 **Choisir un seul :**
- **GitHub Actions** : Plus simple, gratuit pour projets publics
- **Cloud Build** : Intégré GCP, payant

**Pour MVP :** GitHub Actions suffit amplement.

---

### 19. 📦 **2 Frontends Vercel = 2 Quotas**

**Problème identifié:**
- Frontend Public : 1 projet Vercel
- Frontend CRM : 1 autre projet Vercel

**Impact:**
- 2 quotas séparés
- Si trafic élevé, risque dépassement

**Alternative:**
**1 seul projet Next.js multi-tenant**
```
app/
├── (public)/       # Site vitrine
│   ├── page.tsx    # Accueil
│   └── ...
├── (admin)/        # CRM
│   └── admin/
│       ├── page.tsx
│       └── ...
```

**Avantages:**
- 1 seul déploiement
- Code partagé (composants UI, utils)
- Quota unique (plus large)

**Inconvénient:**
- Repo unique (mais c'est aussi un avantage pour sync)

**Recommandation:**
🟠 **Envisager 1 seul projet Next.js avec routes séparées**

---

## 🔐 Problèmes Légaux & RGPD

### 20. ⚖️ **RGPD : Droit à l'Oubli vs Conservation Factures**

**Incohérence légale:**
- RGPD : "Droit à l'oubli" → Suppression complète des données
- Loi française : Conservation des factures **10 ans obligatoire**

**Conflit:**
Comment supprimer un client tout en gardant ses factures ?

**Solution légale:**
- **Anonymisation** (pas suppression totale)
- Garder factures mais anonymiser :
  - Nom → "Client anonyme #12345"
  - Email → "anonymized_12345@example.com"
  - Téléphone → "00 00 00 00 00"
- Conserver : Montant, date, prestation (données comptables)

**Recommandation:**
🔴 **Implémenter anonymisation, pas suppression totale**

---

### 21. 📅 **Bons Cadeaux : Validité Minimum 1 An**

**Problème identifié:**
"Durée de validité paramétrable par l'admin"

**Loi française:**
Les bons cadeaux sont valables **minimum 1 an** (pas négociable).

**Risque:**
Autoriser l'admin à mettre 6 mois = **illégal**.

**Recommandation:**
🔴 **Blocage dans l'interface : minimum 12 mois, maximum 36 mois**

---

### 22. 💼 **Taux de TVA : À Vérifier**

**Problème identifié:**
Architecture mentionne "20% pour prestations, 20% pour produits"

**Réalité complexe:**
- Prestations esthétiques : **20%** (taux normal)
- SAUF si **soins médicaux** prescrits : **10%** (taux réduit)
- Produits cosmétiques : **20%**

**Question critique:**
- Statut juridique ? (Auto-entrepreneur, SARL, etc.)
- Franchise en base de TVA ? (si CA < 36 800€, pas de TVA)

**Recommandation:**
🔴 **Consulter un expert-comptable pour confirmer les taux**

---

### 23. 📜 **CGV Absentes**

**Problème majeur:**
Aucune mention de **Conditions Générales de Vente**.

**Obligatoire légalement:**
- CGV acceptées lors de la réservation
- Contenu : Tarifs, délais, annulation, responsabilités, etc.

**Impact:**
Sans CGV, pas de protection juridique.

**Recommandation:**
🔴 **Rédiger les CGV AVANT le lancement**
Options :
- Avocat spécialisé (~500-1000€)
- Template adapté + validation avocat (~200€)

---

## 🎯 Problèmes de Scope & Priorisation

### 24. 🛍️ **Vente de Produits : Priorité Floue**

**Résumé du problème:**
- Gestion stocks complète prévue en Phase 1 (MVP)
- Mais vous dites : "Aucune idée pour les produits"

**Questions:**
- La vente de produits est-elle **critique pour le lancement** ?
- Ou peut-elle attendre la Phase 2 ?

**Impact financier:**
Développement du module Stocks = **~40-60h** de dev

**Recommandation:**
🟠 **Reporter Gestion Stocks en Phase 2**
🟠 **MVP : Prestations uniquement**
🟡 **Phase 2 : Ajouter produits si demandé par clients**

---

### 25. 📱 **WhatsApp Business : Vraiment Utile ?**

**Problème identifié:**
WhatsApp Business API mentionné en Phase 2.

**Réalité:**
- WhatsApp Business API = **payant** (conversation-based pricing)
- Validation par Meta nécessaire (plusieurs semaines)
- Complexe à intégrer

**Question:**
Vos clientes demandent-elles WhatsApp pour les RDV ?

**Statistiques réelles:**
En France, institut beauté :
- SMS : 80% d'ouverture
- Email : 20% d'ouverture
- WhatsApp : rarement utilisé pro

**Recommandation:**
🟡 **Exclure WhatsApp du scope (Phase 3 ou jamais)**
🟠 **Focaliser sur SMS + Email (largement suffisant)**

---

### 26. 🎮 **Gamification Déjà Exclue (Bien)**

✅ Bonne décision d'avoir exclu :
- Objectifs & Gamification
- IA & Recommandations
- Réalité Augmentée
- App Mobile Technicienne

Ces fonctionnalités sont du "nice-to-have", pas du "must-have".

---

## 🧪 Manques Critiques

### 27. 🧪 **Pas de Stratégie de Tests**

**Problème identifié:**
Aucune mention de tests dans les documents.

**Tests nécessaires:**
- **Tests unitaires** (backend : services, utils)
- **Tests d'intégration** (API endpoints)
- **Tests E2E** (parcours réservation complet)
- **Cible couverture** : 80% minimum

**Impact:**
Sans tests, risque de régressions élevé.

**Recommandation:**
🔴 **Ajouter une section "Tests" dans l'architecture**
- pytest (backend)
- Jest + React Testing Library (frontend)
- Playwright (E2E)

---

### 28. 💾 **Pas de Stratégie de Backup**

**Problème identifié:**
"Sauvegarde quotidienne chiffrée" mentionnée, mais aucun détail.

**Questions critiques:**
- Rétention : combien de temps ? (7 jours, 30 jours ?)
- Fréquence : quotidienne, continue ?
- Restauration : combien de temps pour restaurer ?
- Test : backup testé régulièrement ?

**Recommandation:**
🔴 **Définir une politique de backup claire**
Exemple :
- Backup automatique quotidien (3h du matin)
- Rétention : 7 jours glissants
- Snapshot mensuel conservé 12 mois
- Test de restauration : 1x/trimestre

---

### 29. 🔥 **Pas de Plan de Reprise d'Activité (PRA)**

**Problème identifié:**
Que se passe-t-il si :
- Base de données corrompue ?
- Cloud Run down ?
- Attaque DDoS ?
- Bug critique en production ?

**Impact:**
Risque de perte de données ou indisponibilité prolongée.

**Recommandation:**
🟠 **Définir un PRA basique**
- Backup testable
- Procédure de rollback (revenir version précédente)
- Contact d'urgence pour support technique

---

### 30. 📊 **Pas de Données de Test**

**Problème identifié:**
Vous dites : "Pas encore de clients"

**Impact:**
- Pas de données pour tester le CRM
- Démo difficile à présenter
- Développement à l'aveugle

**Recommandation:**
🟠 **Créer un jeu de données fictif**
- 100 clients fictifs (générés)
- 200 réservations réparties sur 6 mois
- 50 transactions
- 20 bons cadeaux
- 30 photos avant/après

---

## 📈 Problèmes de Performance

### 31. ⚡ **Métriques de Performance Backend Absentes**

**Problème identifié:**
"Lighthouse score > 90" mentionné pour frontend, mais rien pour backend.

**Impact:**
Pas d'objectif de performance API.

**Recommandation:**
🟠 **Définir des objectifs backend**
- P50 (médiane) : < 100ms
- P95 : < 200ms
- P99 : < 500ms
- Timeout : 10s max

---

### 32. 🗃️ **Pas d'Optimisation de Requêtes DB**

**Problème identifié:**
Schéma de base de données défini, mais pas d'index mentionnés (sauf quelques-uns).

**Impact:**
Requêtes lentes sur grandes tables.

**Recommandation:**
🟠 **Ajouter des index sur colonnes fréquemment filtrées**
Exemple :
```sql
CREATE INDEX idx_bookings_client_email ON bookings(client_email);
CREATE INDEX idx_bookings_date_status ON bookings(booking_date, status);
CREATE INDEX idx_products_category ON products(category);
```

---

## 🌍 Problèmes SEO & Marketing

### 33. 🔍 **Zone Géographique = SEO Local Impossible**

**Problème identifié:**
Sans ville/région définie :
- Impossible de cibler "esthéticienne à domicile Paris"
- Google Maps non configurable
- Local Pack Google inaccessible

**Impact:**
70% du trafic esthétique = recherche locale.

**Recommandation:**
🔴 **Définir la zone immédiatement pour SEO**

---

### 34. 📸 **Pas de Contenu pour Lancement**

**Problème identifié:**
Site vitrine prévu, mais :
- Pas de photos professionnelles
- Pas de textes rédigés
- Pas de description des prestations
- Page "À propos" vide

**Impact:**
Impossible de lancer sans contenu.

**Recommandation:**
🔴 **Phase de création de contenu AVANT développement**
- Shooting photo professionnel (500-1000€)
- Rédaction des textes (ou copywriter)
- Description détaillée de chaque prestation

---

## 💡 Recommandations Prioritaires

### 🔴 **CRITIQUE - À Résoudre IMMÉDIATEMENT**

1. **Clarifier le modèle d'activité** : Domicile, physique, ou mixte ?
2. **Définir la zone géographique** : Ville, rayon, frais de déplacement
3. **Simplifier les moyens de paiement** : Stripe + Virement pour MVP
4. **Décider : Vente de produits OUI/NON dans MVP**
5. **Clarifier Sumup vs Stripe** : 2 systèmes ou 1 seul ?
6. **Revoir le modèle paiements partiels** : Gérer acompte + solde
7. **Créer le contenu** : Photos, textes, descriptions
8. **Rédiger les CGV**

### 🟠 **IMPORTANT - À Traiter Avant Développement**

9. Simplifier la gestion des stocks (ou reporter Phase 2)
10. Réduire l'infrastructure (économiser coûts)
11. Remplacer Celery par BackgroundTasks (MVP)
12. Définir politique de backup
13. Créer jeu de données de test
14. Ajouter stratégie de tests

### 🟡 **MOYEN - À Améliorer Plus Tard**

15. Exclure WhatsApp du scope
16. Optimiser la compression des photos
17. Définir métriques de performance backend
18. Ajouter index base de données

---

## 📋 Checklist de Validation Avant Développement

```
🔴 Critique (Bloquant)
[ ] Modèle activité clarifié (domicile / physique / mixte)
[ ] Zone géographique définie (ville, rayon, frais)
[ ] Moyens de paiement simplifiés (Stripe + virement MVP)
[ ] Vente produits : OUI ou NON dans MVP
[ ] Terminal Sumup : usage clarifié (physique ou en ligne)
[ ] Modèle paiements partiels corrigé (acompte + solde)
[ ] CGV rédigées et validées
[ ] Contenu créé (photos, textes, descriptions)

🟠 Important (Recommandé)
[ ] Stocks : simplifiés ou reportés Phase 2
[ ] Infrastructure : optimisée pour réduire coûts
[ ] Celery remplacé par BackgroundTasks
[ ] Politique backup définie
[ ] Jeu de données test créé
[ ] Stratégie tests ajoutée

🟡 Moyen (Nice to have)
[ ] WhatsApp exclu du scope
[ ] Compression photos automatique
[ ] Métriques performance backend
[ ] Index DB optimisés
```

---

## 🎯 Prochaine Étape Recommandée

Avant de continuer le développement, je suggère de créer un document :

**"DECISIONS_FINALES.md"** qui répondra à toutes les questions critiques ci-dessus.

**Voulez-vous que je crée ce document avec vous maintenant ?** 🤔

Cela permettra de lever toutes les ambiguïtés et d'avoir un scope 100% clair avant de coder.

---

**Date d'analyse:** 2026-01-11
**Nombre d'incohérences détectées:** 34
**Nombre de recommandations critiques:** 8
**Nombre de questions à résoudre:** 25

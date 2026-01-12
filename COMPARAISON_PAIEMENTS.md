# 💳 Comparaison Détaillée : Sumup vs Stripe

**Date:** 2026-01-11
**Contexte:** Institut de beauté à domicile (local physique) avec paiements physiques + en ligne

---

## 🎯 Cas d'Usage pour Sérénaïa Beauté

### Besoins Identifiés

**Paiements Physiques (sur place)** :
- Encaissement après prestation (solde ou totalité)
- Terminal de paiement CB
- Gestion de caisse (espèces + CB)

**Paiements En Ligne** :
- Acompte 30% lors de la réservation web
- Paiement total des bons cadeaux
- Sécurisé et conforme PCI-DSS

---

## 📊 Comparaison Globale

| Critère | **Sumup** | **Stripe** |
|---------|-----------|------------|
| **Focus principal** | Paiements physiques (TPE) | Paiements en ligne |
| **Terminal matériel** | ✅ Oui (Sumup Air, 3G, etc.) | ❌ Non (lecteurs tiers uniquement) |
| **API en ligne** | 🟠 Limitée | ✅ Très complète |
| **Tarifs CB physique** | 0,99% + 0,25€ | 1,5% + 0,25€ (via lecteur tiers) |
| **Tarifs paiement en ligne** | 1,99% + 0,25€ | 1,5% + 0,25€ |
| **Webhooks** | 🟠 Basiques | ✅ Avancés et fiables |
| **Acomptes/paiements partiels** | ❌ Non natif | ✅ Oui (Payment Intents) |
| **Récurrence/abonnements** | ❌ Non | ✅ Oui (Subscriptions) |
| **Intégration technique** | 🟠 Moyenne | ✅ Excellente |
| **Support développeur** | 🟠 Limité | ✅ Excellent (doc complète) |
| **Marché français** | ✅ Populaire TPE | ✅ Leader paiements en ligne |

---

## 🏪 Option 1 : Sumup Uniquement

### ✅ Avantages

1. **Terminal Sumup Air (59€ TTC)**
   - Bluetooth, se connecte au smartphone/tablette
   - Très portable, idéal pour institut à domicile
   - Batterie longue durée
   - Accepte CB, sans contact, Apple Pay, Google Pay

2. **Tarif Compétitif (Physique)**
   - **0,99% + 0,25€** par transaction CB physique
   - Exemple : 100€ → frais 1,24€ (vs 1,75€ avec Stripe)
   - Économie significative sur gros volume

3. **Simplicité**
   - 1 seul compte
   - 1 seul tableau de bord
   - Virements unifiés
   - Moins de complexité comptable

4. **App Mobile Sumup**
   - Interface de caisse très simple
   - Historique des transactions
   - Statistiques basiques

5. **API Sumup pour Paiements En Ligne**
   - Possible d'intégrer sur le site web
   - Checkout Sumup (iframe ou redirection)

### ❌ Inconvénients

1. **API Moins Mature**
   - Documentation moins complète que Stripe
   - Fonctionnalités limitées (pas d'acomptes automatiques)
   - Webhooks moins fiables

2. **Paiements En Ligne Plus Chers**
   - **1,99% + 0,25€** (vs 1,5% chez Stripe)
   - Exemple : 100€ → frais 2,24€

3. **Gestion Acomptes Complexe**
   - Pas de système natif d'acompte 30%
   - À développer manuellement :
     - Autorisation de 30€ en ligne
     - Capture manuelle sur place pour les 70€ restants
   - Risque d'erreurs

4. **Moins Adapté Paiements En Ligne**
   - Pas de Checkout optimisé (UX moyenne)
   - Pas d'intégration Apple Pay/Google Pay web
   - Support développeur limité

5. **Fonctionnalités Avancées Absentes**
   - Pas de gestion d'abonnements
   - Pas de paiements récurrents
   - Pas de liens de paiement personnalisables
   - Pas d'automatisation avancée

### 💰 Coût Total Estimé (Sumup Uniquement)

**Hypothèses:**
- 50 transactions physiques/mois × 80€ moyen = 4000€
- 20 réservations en ligne/mois × 30€ acompte = 600€
- 5 bons cadeaux/mois × 100€ = 500€

**Calcul:**
- Physique : 4000€ × 0,99% + 50 × 0,25€ = 39,60€ + 12,50€ = **52,10€**
- En ligne : 1100€ × 1,99% + 25 × 0,25€ = 21,89€ + 6,25€ = **28,14€**
- **Total/mois : 80,24€**

**+ Terminal Sumup Air : 59€ TTC (achat unique)**

---

## 💻 Option 2 : Stripe Uniquement

### ✅ Avantages

1. **API Puissante et Complète**
   - Documentation excellente (français + anglais)
   - Bibliothèques officielles (Python, JavaScript, etc.)
   - Webhooks ultra-fiables
   - Support développeur réactif

2. **Gestion Acomptes Native**
   - **Payment Intents** avec capture partielle
   - Autorisation de 100€, capture de 30€ immédiate
   - Capture des 70€ restants plus tard (jusqu'à 7 jours)
   - Automatique, sécurisé, pas de risque d'erreur

3. **Checkout Optimisé**
   - Interface de paiement moderne et responsive
   - Apple Pay / Google Pay intégrés
   - Sauvegarde des cartes (clients récurrents)
   - Taux de conversion élevé (~90%)

4. **Tarif Compétitif (En Ligne)**
   - **1,5% + 0,25€** par transaction en ligne
   - Moins cher que Sumup pour paiements web

5. **Fonctionnalités Avancées**
   - Liens de paiement personnalisés (bons cadeaux)
   - Gestion d'abonnements (si forfaits récurrents)
   - Facturation automatique
   - Remboursements automatiques
   - Dashboard analytics puissant

6. **Terminal Stripe (Option)**
   - Stripe Reader M2 (59€)
   - Ou intégration avec terminaux tiers (Verifone, Ingenico)
   - Même compte que paiements en ligne

### ❌ Inconvénients

1. **Tarif Physique Plus Élevé**
   - **1,5% + 0,25€** par transaction physique
   - vs 0,99% chez Sumup
   - Exemple : 100€ → frais 1,75€ (vs 1,24€ Sumup)

2. **Terminal à Acheter**
   - Stripe Reader M2 : ~59€
   - Ou Verifone/Ingenico : 100-300€
   - Coût initial plus élevé

3. **Complexité (Légère)**
   - Plus de fonctionnalités = courbe d'apprentissage
   - Mais documentation excellente

### 💰 Coût Total Estimé (Stripe Uniquement)

**Hypothèses identiques:**
- 50 transactions physiques/mois × 80€ = 4000€
- 25 paiements en ligne/mois × 44€ moyen = 1100€

**Calcul:**
- Physique : 4000€ × 1,5% + 50 × 0,25€ = 60€ + 12,50€ = **72,50€**
- En ligne : 1100€ × 1,5% + 25 × 0,25€ = 16,50€ + 6,25€ = **22,75€**
- **Total/mois : 95,25€**

**+ Stripe Reader M2 : 59€ (ou gratuit si promo)**

**Différence vs Sumup : +15€/mois**

---

## 🔀 Option 3 : Sumup (Physique) + Stripe (En Ligne) **[RECOMMANDÉ]**

### ✅ Avantages

1. **Meilleur des Deux Mondes**
   - **Sumup** : Tarif imbattable pour paiements physiques (0,99%)
   - **Stripe** : API puissante pour paiements en ligne (1,5%)

2. **Optimisation des Coûts**
   - Économie sur transactions physiques (Sumup < Stripe)
   - Meilleure UX en ligne (Stripe > Sumup)

3. **Gestion Acomptes Simplifiée**
   - Stripe gère les acomptes 30% automatiquement (en ligne)
   - Sumup encaisse les soldes sur place (70%)

4. **Flexibilité**
   - Chaque outil dans son domaine d'expertise
   - Évolutif (peut retirer Sumup plus tard si volume augmente)

### ❌ Inconvénients

1. **Double Comptabilité**
   - 2 comptes bancaires ou 2 virements distincts
   - Réconciliation plus complexe
   - Besoin de tracker dans le CRM (table `payments` avec `provider`)

2. **Double Intégration Technique**
   - 2 APIs à intégrer (mais c'est gérable)
   - 2 webhooks à gérer

3. **Coût de 2 Terminaux**
   - Sumup Air : 59€
   - (Stripe Reader optionnel si besoin de backup)

### 💰 Coût Total Estimé (Sumup + Stripe)

**Calcul optimisé:**
- Physique (Sumup) : 4000€ × 0,99% + 50 × 0,25€ = **52,10€**
- En ligne (Stripe) : 1100€ × 1,5% + 25 × 0,25€ = **22,75€**
- **Total/mois : 74,85€**

**Économie vs Stripe seul : -20,40€/mois = -244€/an**
**Économie vs Sumup seul : -5,39€/mois = -65€/an**

**+ Terminal Sumup Air : 59€ (achat unique)**

---

## 📋 Tableau Récapitulatif des Coûts

| Scenario | Coût Mensuel | Coût Terminal | Total 1ère année |
|----------|--------------|---------------|------------------|
| **Sumup uniquement** | 80,24€ | 59€ | 1 021€ |
| **Stripe uniquement** | 95,25€ | 59€ | 1 202€ |
| **Sumup + Stripe** ✅ | 74,85€ | 59€ | **957€** |

**Meilleure option financière : Sumup + Stripe = -244€/an vs Stripe seul**

---

## 🛠️ Intégration Technique

### Architecture avec Sumup + Stripe

```
┌─────────────────────────────────────────────────────────────┐
│                    PAIEMENTS SUR PLACE                       │
│                                                              │
│  Terminal Sumup Air (Bluetooth)                             │
│         ↓                                                    │
│  App Sumup Mobile (tablette/smartphone)                     │
│         ↓                                                    │
│  API Sumup → Webhook → Backend FastAPI                     │
│         ↓                                                    │
│  Mise à jour booking.payment_status = "fully_paid"          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   PAIEMENTS EN LIGNE                         │
│                                                              │
│  Site Web → Stripe Checkout (iframe/redirect)              │
│         ↓                                                    │
│  Paiement acompte 30€ (Payment Intent avec capture)        │
│         ↓                                                    │
│  Webhook Stripe → Backend FastAPI                          │
│         ↓                                                    │
│  Mise à jour booking.payment_status = "deposit_paid"        │
│                                                              │
│  [Plus tard, sur place]                                     │
│  Option 1 : Sumup pour les 70€ restants                    │
│  Option 2 : Capture des 70€ via Stripe API (si CB en ligne)│
└─────────────────────────────────────────────────────────────┘
```

### Code Exemple : Gestion Acompte avec Stripe

```python
# Création d'un Payment Intent pour acompte 30%
import stripe

stripe.api_key = "sk_live_..."

# Total prestation : 100€
# Acompte : 30€

payment_intent = stripe.PaymentIntent.create(
    amount=10000,  # 100€ en centimes
    currency="eur",
    capture_method="manual",  # Important : capture manuelle
    metadata={
        "booking_id": "booking_123",
        "total_amount": 10000,
        "deposit_amount": 3000,
    }
)

# Client paie en ligne
# Stripe autorise 100€ mais ne capture QUE 30€

# Après autorisation réussie, capturer l'acompte
stripe.PaymentIntent.capture(
    payment_intent.id,
    amount_to_capture=3000  # Capture 30€ seulement
)

# Statut : deposit_paid (30€ capturés, 70€ restants)

# Option A : Sur place, encaisser 70€ avec Sumup
# → Créer transaction Sumup manuelle
# → Marquer booking comme "fully_paid"

# Option B : Sur place, capturer les 70€ restants via Stripe
stripe.PaymentIntent.capture(
    payment_intent.id,
    amount_to_capture=7000  # Capture les 70€ restants
)
```

---

## 🎯 Recommandation Finale

### **Option Recommandée : Sumup (Physique) + Stripe (En Ligne)**

**Justification :**

1. **Optimisation financière** : -244€/an vs Stripe seul
2. **Simplicité technique** : Stripe API excellente pour acomptes
3. **Flexibilité** : Meilleur outil pour chaque usage
4. **Scalabilité** : Si l'activité explose, possibilité de tout migrer vers Stripe

**Architecture validée :**
- **Sumup** : Encaissements sur place (TPE Sumup Air)
- **Stripe** : Paiements en ligne (acomptes réservations + bons cadeaux)
- Tracking unifié dans la base de données (table `payments`)

---

## 🚀 Roadmap d'Implémentation

### Phase 1 : MVP
1. ✅ Intégrer **Stripe** pour paiements en ligne
   - Checkout Stripe (réservations + bons cadeaux)
   - Webhooks (confirmation paiement)
   - Gestion acomptes 30% (Payment Intent)

2. ✅ Acheter **Terminal Sumup Air** (59€)
   - Configurer compte Sumup
   - Tester encaissements physiques

3. ✅ Intégrer **API Sumup** (optionnel)
   - Webhook Sumup → Backend
   - Tracking automatique des encaissements physiques
   - (Ou saisie manuelle dans le CRM si API trop complexe)

### Phase 2 : Optimisations
4. 🟠 Ajouter **PayPal** (si vraiment demandé par les clientes)
5. 🟡 Automatiser réconciliation bancaire

---

## 📝 Checklist de Décision

**Pour valider Sumup + Stripe :**

- [ ] Acheter Terminal Sumup Air (59€) → [Commander ici](https://www.sumup.com/)
- [ ] Créer compte Sumup (gratuit)
- [ ] Créer compte Stripe (gratuit)
- [ ] Valider que les 2 comptes peuvent virer sur le même IBAN
- [ ] Confirmer que la gestion de 2 comptes est acceptable
- [ ] Décider : Intégration API Sumup (automatique) ou saisie manuelle (plus simple)

---

**Questions ?**
- Êtes-vous d'accord avec **Sumup + Stripe** ?
- Ou préférez-vous **Stripe uniquement** (plus simple, légèrement plus cher) ?

---

**Date de création:** 2026-01-11
**Version:** 1.0

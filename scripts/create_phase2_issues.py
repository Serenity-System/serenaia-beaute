#!/usr/bin/env python3
"""
Script de création des 80 issues atomiques Phase 2 - Sérénaia Beauté
Extensions post-MVP pour fonctionnalités avancées
"""

# Définition des 80 issues Phase 2
PHASE2_ISSUES = [
    # P2-44: Module Fidélité (8 issues)
    {
        "id": "P2-44.1",
        "title": "BDD tables loyalty (points, tiers)",
        "objective": "Créer la structure de base de données pour le système de fidélité avec gestion des points et des niveaux (tiers).",
        "tasks": [
            "Créer modèle LoyaltyTier (niveaux: bronze, argent, or)",
            "Créer modèle LoyaltyTransaction (historique points)",
            "Ajouter champs loyalty_points et loyalty_tier_id sur Client",
            "Créer migration Alembic"
        ],
        "acceptance": [
            "Tables créées avec relations correctes",
            "Migration testée up/down",
            "Models documentés avec docstrings"
        ],
        "dependencies": None,
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-44.2",
        "title": "Service calcul points automatique",
        "objective": "Implémenter la logique métier de calcul et attribution automatique des points de fidélité.",
        "tasks": [
            "Créer services/loyalty_service.py",
            "Implémenter calculate_points(booking_amount) : 1€ = 1 point",
            "Implémenter add_points(client_id, points, reason)",
            "Hook après paiement booking/produit",
            "Logging toutes transactions points"
        ],
        "acceptance": [
            "Points ajoutés automatiquement après achat",
            "Historique complet dans LoyaltyTransaction",
            "Tests unitaires service"
        ],
        "dependencies": "P2-44.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-44.3",
        "title": "API endpoints fidélité CRUD",
        "objective": "Exposer les endpoints API pour consulter et gérer les points de fidélité côté CRM et client.",
        "tasks": [
            "Créer api/v1/loyalty.py router",
            "GET /loyalty/{client_id}/balance",
            "GET /loyalty/{client_id}/history",
            "POST /loyalty/{client_id}/add (admin uniquement)",
            "POST /loyalty/{client_id}/redeem (utiliser points)",
            "Schémas Pydantic responses"
        ],
        "acceptance": [
            "Tous endpoints fonctionnels",
            "Permissions correctes (client vs admin)",
            "Documentation OpenAPI complète"
        ],
        "dependencies": "P2-44.2",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-44.4",
        "title": "CRM widget points client",
        "objective": "Afficher les informations de fidélité directement dans la fiche client du CRM.",
        "tasks": [
            "Créer components/LoyaltyWidget.tsx",
            "Afficher solde points + tier actuel",
            "Afficher progression vers tier suivant",
            "Bouton ajouter/retirer points manuellement (admin)",
            "Historique transactions récentes"
        ],
        "acceptance": [
            "Widget visible dans fiche client",
            "Données temps réel depuis API",
            "Design cohérent avec CRM"
        ],
        "dependencies": "P2-44.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-44.5",
        "title": "Règles accumulation points par tier",
        "objective": "Définir et implémenter les règles d'accumulation différenciées selon le niveau de fidélité.",
        "tasks": [
            "Bronze: 1€ = 1 point (défaut)",
            "Argent: 1€ = 1.5 points (après 500 pts)",
            "Or: 1€ = 2 points (après 2000 pts)",
            "Implémenter get_multiplier(tier)",
            "Promotion automatique de tier",
            "Tests règles"
        ],
        "acceptance": [
            "Multiplicateurs appliqués correctement",
            "Promotions automatiques fonctionnelles",
            "Documentation règles dans code"
        ],
        "dependencies": "P2-44.2",
        "estimation": "1h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-44.6",
        "title": "Catalogue récompenses et remises",
        "objective": "Créer un catalogue de récompenses échangeables contre des points.",
        "tasks": [
            "Table LoyaltyReward (nom, points_cost, type)",
            "Types: discount_percent, discount_amount, free_service",
            "API GET /loyalty/rewards (catalogue)",
            "API POST /loyalty/redeem (échanger points)",
            "Validation solde suffisant"
        ],
        "acceptance": [
            "Catalogue récompenses consultable",
            "Échange points fonctionnel",
            "Points déduits après validation"
        ],
        "dependencies": "P2-44.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-44.7",
        "title": "Notifications seuils fidélité",
        "objective": "Notifier automatiquement les clients lorsqu'ils atteignent des seuils importants.",
        "tasks": [
            "Notification promotion tier (Bronze→Argent→Or)",
            "Notification seuil points (ex: 100, 500, 1000)",
            "Template Email félicitations",
            "Template SMS rappel points disponibles",
            "Trigger automatique après transaction"
        ],
        "acceptance": [
            "Notifications envoyées aux bons moments",
            "Templates personnalisés professionnels",
            "Logs envois notifications"
        ],
        "dependencies": "P2-44.5",
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-44.8",
        "title": "Tests complets module fidélité",
        "objective": "Valider l'ensemble du module fidélité avec des tests automatisés.",
        "tasks": [
            "Tests unitaires loyalty_service.py",
            "Tests API endpoints",
            "Tests règles accumulation",
            "Tests promotions tier",
            "Tests notifications",
            "Tests intégration booking→points"
        ],
        "acceptance": [
            "Coverage >80% module loyalty",
            "Tous tests passent",
            "Scénarios edge cases couverts"
        ],
        "dependencies": "P2-44.7",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-45: Galerie Photos (6 issues)
    {
        "id": "P2-45.1",
        "title": "Upload photos backend + Cloud Storage",
        "objective": "Implémenter le système d'upload sécurisé de photos vers Google Cloud Storage.",
        "tasks": [
            "Créer table Photo (url, client_id, consent, status)",
            "API POST /photos/upload (multipart/form-data)",
            "Upload vers GCS bucket photos/",
            "Validation format (jpg, png), taille max 10MB",
            "Génération URL signée temporaire",
            "Stockage metadata en BDD"
        ],
        "acceptance": [
            "Upload photos fonctionnel",
            "Photos stockées dans GCS",
            "Metadata en base correcte"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-45.2",
        "title": "Gestion consentements RGPD photos",
        "objective": "Implémenter le système de consentement explicite pour publication des photos.",
        "tasks": [
            "Champ consent_signed (bool) sur Photo",
            "Formulaire consentement digital",
            "Stockage date + signature consentement",
            "API POST /photos/{id}/consent",
            "Email récapitulatif consentement",
            "Documentation RGPD conformité"
        ],
        "acceptance": [
            "Consentement obligatoire avant publication",
            "Traçabilité complète consentements",
            "Email confirmation envoyé"
        ],
        "dependencies": "P2-45.1",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-45.3",
        "title": "Modération photos admin CRM",
        "objective": "Créer l'interface CRM pour modérer et valider les photos avant publication.",
        "tasks": [
            "Page CRM /photos/moderate",
            "Liste photos pending approval",
            "Preview photo haute qualité",
            "Actions: Approuver, Rejeter, Demander modification",
            "Notifications client (approval/rejet)",
            "Filtres par status"
        ],
        "acceptance": [
            "Interface modération fonctionnelle",
            "Workflow validation clair",
            "Notifications automatiques"
        ],
        "dependencies": "P2-45.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-45.4",
        "title": "Galerie publique frontend responsive",
        "objective": "Afficher les photos approuvées dans une galerie publique esthétique sur le site.",
        "tasks": [
            "Page frontend /gallery",
            "Composant PhotoGallery.tsx (masonry layout)",
            "Lazy loading images",
            "Lightbox photo plein écran",
            "Filtres par catégorie/service",
            "Optimisation next/image"
        ],
        "acceptance": [
            "Galerie responsive mobile/desktop",
            "Performances optimales (Lighthouse >90)",
            "UX fluide et professionnelle"
        ],
        "dependencies": "P2-45.3",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-45.5",
        "title": "Watermark automatique photos",
        "objective": "Ajouter automatiquement un watermark discret sur les photos publiées.",
        "tasks": [
            "Installer Pillow (traitement images)",
            "Créer service watermark_service.py",
            "Appliquer logo + texte (ex: ©Sérénaia Beauté)",
            "Position configurable (coin bas droit)",
            "Process lors de l'approval photo",
            "Tests watermark quality"
        ],
        "acceptance": [
            "Watermark appliqué automatiquement",
            "Qualité image préservée",
            "Logo professionnel et discret"
        ],
        "dependencies": "P2-45.3",
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-45.6",
        "title": "Tests module galerie photos",
        "objective": "Valider le module galerie avec tests automatisés complets.",
        "tasks": [
            "Tests upload photos",
            "Tests consentement workflow",
            "Tests modération",
            "Tests watermark",
            "Tests RGPD (droit oubli)",
            "Tests E2E galerie publique"
        ],
        "acceptance": [
            "Coverage >80%",
            "Tous scénarios RGPD validés",
            "Performance galerie testée"
        ],
        "dependencies": "P2-45.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-46: Automatisations Marketing (6 issues)
    {
        "id": "P2-46.1",
        "title": "Campagne anniversaire client automatique",
        "objective": "Envoyer automatiquement un message personnalisé aux clients pour leur anniversaire.",
        "tasks": [
            "Créer table Automation (type, config, active)",
            "Job quotidien détection anniversaires",
            "Template email anniversaire + code promo 15%",
            "Template SMS anniversaire",
            "Génération code promo unique 30j validité",
            "Logging envois"
        ],
        "acceptance": [
            "Messages envoyés automatiquement J-jour",
            "Code promo fonctionnel",
            "Tracking utilisation codes"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-46.2",
        "title": "Réactivation clients inactifs 3 mois",
        "objective": "Relancer automatiquement les clients n'ayant pas réservé depuis 3+ mois.",
        "tasks": [
            "Job hebdomadaire détection inactifs",
            "Segmentation: 3 mois, 6 mois, 12 mois",
            "Templates emails réactivation (3 variantes)",
            "Offre spéciale inactifs (ex: -20%)",
            "Tracking taux retour",
            "Désabonnement possible"
        ],
        "acceptance": [
            "Campagnes envoyées automatiquement",
            "Segmentation correcte clients",
            "Métriques ROI campagne"
        ],
        "dependencies": "P2-46.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-46.3",
        "title": "Recommandations produits post-soin",
        "objective": "Envoyer automatiquement des recommandations de produits après une prestation.",
        "tasks": [
            "Hook après booking completed",
            "Mapping service → produits recommandés",
            "Template email avec 3 produits + photos",
            "Liens directs achat (tracking UTM)",
            "Délai envoi: 24h après soin",
            "Tests A/B timing envoi"
        ],
        "acceptance": [
            "Emails pertinents envoyés",
            "Tracking clics et conversions",
            "Mapping service-produits efficace"
        ],
        "dependencies": "P2-46.1",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-46.4",
        "title": "Promotions saisonnières automatiques",
        "objective": "Planifier et envoyer automatiquement des campagnes marketing saisonnières.",
        "tasks": [
            "Calendrier promotions (Noël, St-Valentin, Fête des mères, etc.)",
            "Templates emails saisonniers",
            "Scheduling envois J-15, J-7, J-1",
            "Segmentation cible par promo",
            "Dashboard planification CRM",
            "Stats performances campagnes"
        ],
        "acceptance": [
            "Campagnes schedulées correctement",
            "Templates professionnels",
            "Métriques détaillées disponibles"
        ],
        "dependencies": "P2-46.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-46.5",
        "title": "Scheduler Celery automatisations",
        "objective": "Mettre en place l'infrastructure Celery pour exécuter les automatisations.",
        "tasks": [
            "Installer Celery + Redis backend",
            "Configurer celery.py tasks",
            "Créer tasks périodiques (daily, weekly)",
            "Monitoring Flower dashboard",
            "Error handling + retry logic",
            "Logs détaillés exécutions"
        ],
        "acceptance": [
            "Celery opérationnel en prod",
            "Tasks exécutées aux bonnes fréquences",
            "Monitoring erreurs efficace"
        ],
        "dependencies": "P2-46.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-46.6",
        "title": "Tests automatisations marketing",
        "objective": "Valider toutes les automatisations avec tests complets.",
        "tasks": [
            "Tests unitaires chaque automation",
            "Tests intégration Celery",
            "Mock envois emails/SMS (test mode)",
            "Tests segmentation clients",
            "Tests génération codes promo",
            "Tests tracking métriques"
        ],
        "acceptance": [
            "Coverage >80%",
            "Pas de spam clients en test",
            "Métriques correctement trackées"
        ],
        "dependencies": "P2-46.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-47: Recommandations IA (6 issues)
    {
        "id": "P2-47.1",
        "title": "Analyser historique achats clients",
        "objective": "Extraire et structurer les données historiques pour alimenter le modèle de recommandation.",
        "tasks": [
            "Query historique bookings + produits par client",
            "Feature engineering: fréquence, montant moyen, services préférés",
            "Détection patterns (ex: soins visage → crème hydratante)",
            "Export dataset CSV pour training",
            "Nettoyage données (outliers)",
            "Documentation features"
        ],
        "acceptance": [
            "Dataset structuré et propre",
            "Features pertinentes identifiées",
            "Patterns visibles dans données"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-47.2",
        "title": "Modèle ML recommandations collaboratives",
        "objective": "Entraîner un modèle de recommandation basé sur le filtrage collaboratif.",
        "tasks": [
            "Choisir algo: Collaborative Filtering (user-based)",
            "Installer scikit-learn / Surprise library",
            "Training modèle sur historique",
            "Cross-validation performances",
            "Sauvegarder modèle (pickle/joblib)",
            "Métriques: Precision@K, Recall@K"
        ],
        "acceptance": [
            "Modèle entraîné avec bonnes métriques",
            "Recommandations pertinentes en test",
            "Modèle sauvegardé et versionné"
        ],
        "dependencies": "P2-47.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-47.3",
        "title": "API endpoint /recommendations",
        "objective": "Exposer les recommandations IA via un endpoint API performant.",
        "tasks": [
            "Créer api/v1/recommendations.py",
            "GET /recommendations/{client_id} (top 5 produits/services)",
            "Charger modèle ML au démarrage",
            "Cache Redis résultats (TTL 1h)",
            "Fallback si modèle indisponible (règles métier)",
            "Logging prédictions"
        ],
        "acceptance": [
            "API rapide (<500ms)",
            "Recommandations cohérentes",
            "Cache efficace"
        ],
        "dependencies": "P2-47.2",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-47.4",
        "title": "Widget CRM suggestions intelligentes",
        "objective": "Afficher les recommandations IA dans la fiche client CRM pour aider à la vente.",
        "tasks": [
            "Composant RecommendationsWidget.tsx",
            "Affichage top 3 suggestions + scores confiance",
            "Bouton 'Ajouter au panier' direct",
            "Explication recommandation (ex: 'Achète souvent ensemble')",
            "Feedback thumbs up/down (amélioration modèle)",
            "Design card attrayant"
        ],
        "acceptance": [
            "Widget intégré fiche client",
            "Suggestions pertinentes",
            "Feedback collecté"
        ],
        "dependencies": "P2-47.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-47.5",
        "title": "A/B testing recommandations",
        "objective": "Mesurer l'impact business des recommandations IA via A/B testing.",
        "tasks": [
            "Groupe A: Recommandations IA",
            "Groupe B: Recommandations aléatoires",
            "Tracking conversions (ajout panier, achat)",
            "Métriques: Taux clic, Taux conversion, Panier moyen",
            "Dashboard résultats A/B",
            "Durée test: 1 mois minimum"
        ],
        "acceptance": [
            "Test A/B opérationnel",
            "Métriques trackées correctement",
            "Résultats analysables"
        ],
        "dependencies": "P2-47.4",
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-47.6",
        "title": "Métriques conversion recommandations",
        "objective": "Créer un dashboard pour suivre les performances des recommandations IA.",
        "tasks": [
            "Tracking impressions recommandations",
            "Tracking clics sur recommandations",
            "Tracking conversions (achats)",
            "Calcul ROI recommandations IA",
            "Dashboard CRM métriques ML",
            "Export rapports mensuels"
        ],
        "acceptance": [
            "Métriques précises et temps réel",
            "Dashboard visualisations claires",
            "ROI calculé automatiquement"
        ],
        "dependencies": "P2-47.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-48: Messagerie CRM (6 issues)
    {
        "id": "P2-48.1",
        "title": "Interface envoi SMS depuis CRM",
        "objective": "Permettre l'envoi de SMS individuels ou groupés directement depuis l'interface CRM.",
        "tasks": [
            "Page CRM /messages/sms",
            "Formulaire envoi SMS (destinataire(s), message)",
            "Compteur caractères (160 max par SMS)",
            "Sélection clients multiple (checkboxes)",
            "Envoi immédiat ou programmé",
            "Confirmation avant envoi"
        ],
        "acceptance": [
            "Interface intuitive et rapide",
            "Envoi SMS fonctionnel",
            "Programmation envois possible"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-48.2",
        "title": "Interface envoi Email depuis CRM",
        "objective": "Créer un éditeur d'emails riche pour communiquer avec les clients.",
        "tasks": [
            "Page CRM /messages/email",
            "Éditeur WYSIWYG (TipTap ou similaire)",
            "Templates emails prédéfinis",
            "Variables personnalisation ({{prenom}}, etc.)",
            "Upload pièces jointes",
            "Preview avant envoi"
        ],
        "acceptance": [
            "Éditeur riche fonctionnel",
            "Templates professionnels",
            "Personnalisation automatique"
        ],
        "dependencies": "P2-48.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-48.3",
        "title": "Bibliothèque templates messages",
        "objective": "Créer et gérer une bibliothèque de templates réutilisables.",
        "tasks": [
            "Table MessageTemplate (name, type, subject, body)",
            "CRUD templates API",
            "CRM page /messages/templates",
            "Catégories: Marketing, Relance, Remerciement, etc.",
            "Variables dynamiques supportées",
            "Duplication templates"
        ],
        "acceptance": [
            "CRUD templates fonctionnel",
            "Catégorisation claire",
            "Réutilisation facile"
        ],
        "dependencies": "P2-48.2",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-48.4",
        "title": "Historique conversations client",
        "objective": "Centraliser tous les échanges avec chaque client pour un suivi optimal.",
        "tasks": [
            "Table Message (type, direction, content, timestamp)",
            "Association Message-Client",
            "Timeline chronologique fiche client",
            "Filtres par type (SMS, Email, Manual note)",
            "Statut message (envoyé, lu, erreur)",
            "Export historique"
        ],
        "acceptance": [
            "Historique complet visible",
            "Timeline claire et chronologique",
            "Statuts messages trackés"
        ],
        "dependencies": "P2-48.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-48.5",
        "title": "Réponses clients et inbox",
        "objective": "Gérer les réponses des clients aux messages envoyés (inbox CRM).",
        "tasks": [
            "Webhook réponses SMS (OVH)",
            "Webhook réponses Email (Resend)",
            "Inbox CRM /messages/inbox",
            "Notifications nouvelles réponses",
            "Marquer comme lu/non-lu",
            "Répondre directement depuis inbox"
        ],
        "acceptance": [
            "Réponses clients reçues",
            "Inbox centralisée fonctionnelle",
            "Notifications temps réel"
        ],
        "dependencies": "P2-48.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-48.6",
        "title": "Tests module messagerie CRM",
        "objective": "Valider le module messagerie avec tests automatisés.",
        "tasks": [
            "Tests envoi SMS/Email",
            "Tests templates",
            "Tests historique",
            "Tests inbox + webhooks",
            "Tests permissions",
            "Tests E2E conversation complète"
        ],
        "acceptance": [
            "Coverage >80%",
            "Webhooks mockés et testés",
            "Scénarios réels simulés"
        ],
        "dependencies": "P2-48.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-49: Programme Parrainage (5 issues)
    {
        "id": "P2-49.1",
        "title": "BDD table referrals et codes",
        "objective": "Créer la structure de données pour gérer les parrainages.",
        "tasks": [
            "Table Referral (referrer_id, referred_id, code, status)",
            "Code parrainage unique par client",
            "Statuts: pending, completed, rewarded",
            "Timestamps création, conversion",
            "Index sur code pour recherche rapide",
            "Migration Alembic"
        ],
        "acceptance": [
            "Table créée avec contraintes",
            "Codes uniques générés",
            "Relations Client correctes"
        ],
        "dependencies": None,
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-49.2",
        "title": "Génération codes parrainage uniques",
        "objective": "Générer automatiquement un code parrainage personnalisé pour chaque client.",
        "tasks": [
            "Format code: PRENOM-XXXXX (ex: MARIE-AB3F9)",
            "Fonction generate_referral_code(client)",
            "Validation unicité code",
            "API GET /referral/my-code (client)",
            "Auto-génération à création compte",
            "Affichage code dans espace client"
        ],
        "acceptance": [
            "Codes générés automatiquement",
            "Format lisible et mémorable",
            "Pas de doublons"
        ],
        "dependencies": "P2-49.1",
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-49.3",
        "title": "Tracking conversions parrainage",
        "objective": "Tracker automatiquement les conversions et valider les parrainages réussis.",
        "tasks": [
            "Input code parrainage au signup",
            "Validation code existant",
            "Création Referral record (pending)",
            "Hook après premier booking filleul",
            "Passage status pending→completed",
            "Notification parrain + filleul"
        ],
        "acceptance": [
            "Conversions trackées automatiquement",
            "Statuts mis à jour correctement",
            "Notifications envoyées"
        ],
        "dependencies": "P2-49.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-49.4",
        "title": "Récompenses parrain et filleul",
        "objective": "Attribuer automatiquement les récompenses aux deux parties.",
        "tasks": [
            "Parrain: +500 points fidélité OU 20€ bon d'achat",
            "Filleul: -15% première réservation",
            "Attribution automatique après conversion",
            "Génération bon d'achat si choix parrain",
            "Expiration bons (3 mois)",
            "Historique récompenses"
        ],
        "acceptance": [
            "Récompenses attribuées automatiquement",
            "Choix parrain respecté",
            "Traçabilité complète"
        ],
        "dependencies": "P2-49.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-49.5",
        "title": "Dashboard parrainage client + CRM",
        "objective": "Afficher les statistiques et l'historique des parrainages.",
        "tasks": [
            "Widget client: Mon code + filleuls invités + récompenses gagnées",
            "Page CRM /referrals avec stats globales",
            "Top parrains (leaderboard)",
            "Métriques: Taux conversion, CA généré",
            "Export liste parrainages",
            "Graphiques évolution"
        ],
        "acceptance": [
            "Dashboard client motivant",
            "Analytics CRM complets",
            "Métriques précises"
        ],
        "dependencies": "P2-49.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-50: Abonnements Récurrents (6 issues)
    {
        "id": "P2-50.1",
        "title": "Modèles abonnements BDD",
        "objective": "Créer la structure de données pour gérer les abonnements récurrents.",
        "tasks": [
            "Table SubscriptionPlan (name, price, duration, services_included)",
            "Table Subscription (client_id, plan_id, status, next_billing)",
            "Statuts: active, paused, canceled, expired",
            "Types plans: Mensuel Essentiel, Premium, VIP",
            "Relation Subscription-Bookings (consommation)",
            "Migration Alembic"
        ],
        "acceptance": [
            "Tables créées avec relations",
            "Plans abonnement définis",
            "Migration testée"
        ],
        "dependencies": None,
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-50.2",
        "title": "Intégration Stripe Subscriptions",
        "objective": "Intégrer l'API Stripe Subscriptions pour gérer les paiements récurrents.",
        "tasks": [
            "Créer Stripe Products + Prices (plans)",
            "Implémenter create_subscription(client, plan)",
            "Sauvegarder stripe_subscription_id",
            "Implémenter update_subscription()",
            "Implémenter cancel_subscription()",
            "Tests mode sandbox"
        ],
        "acceptance": [
            "Subscriptions Stripe fonctionnelles",
            "Sync BDD-Stripe correct",
            "Tests passants"
        ],
        "dependencies": "P2-50.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-50.3",
        "title": "Webhooks renouvellements automatiques",
        "objective": "Gérer les webhooks Stripe pour les renouvellements et incidents de paiement.",
        "tasks": [
            "Endpoint /webhooks/stripe/subscriptions",
            "Événement invoice.paid → renouvellement OK",
            "Événement invoice.payment_failed → alerte client",
            "Événement customer.subscription.deleted → annulation",
            "Mise à jour statuts automatique",
            "Notifications client"
        ],
        "acceptance": [
            "Webhooks traités correctement",
            "Statuts synchronisés",
            "Notifications pertinentes envoyées"
        ],
        "dependencies": "P2-50.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-50.4",
        "title": "Gestion annulations et pauses",
        "objective": "Permettre aux clients de gérer leur abonnement (pause, reprise, annulation).",
        "tasks": [
            "API POST /subscriptions/{id}/pause",
            "API POST /subscriptions/{id}/resume",
            "API POST /subscriptions/{id}/cancel",
            "Pause: Skip next billing cycle",
            "Annulation: Fin période en cours puis stop",
            "Confirmations et emails explicatifs"
        ],
        "acceptance": [
            "Actions abonnement fonctionnelles",
            "Stripe synchronisé",
            "UX claire pour client"
        ],
        "dependencies": "P2-50.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-50.5",
        "title": "CRM suivi abonnements clients",
        "objective": "Créer l'interface CRM pour suivre et gérer les abonnements.",
        "tasks": [
            "Page CRM /subscriptions",
            "Liste tous abonnements actifs/inactifs",
            "Filtres par plan, statut",
            "Fiche abonnement détaillée",
            "Actions admin: pause, cancel, upgrade/downgrade",
            "Métriques: MRR, Churn rate, LTV"
        ],
        "acceptance": [
            "CRM abonnements complet",
            "Actions admin fonctionnelles",
            "Métriques business calculées"
        ],
        "dependencies": "P2-50.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-50.6",
        "title": "Tests module abonnements",
        "objective": "Valider le module abonnements avec tests automatisés.",
        "tasks": [
            "Tests création subscription",
            "Tests webhooks Stripe (mocks)",
            "Tests renouvellements",
            "Tests annulations",
            "Tests calcul MRR",
            "Tests E2E workflow complet"
        ],
        "acceptance": [
            "Coverage >80%",
            "Webhooks mockés correctement",
            "Scénarios edge cases couverts"
        ],
        "dependencies": "P2-50.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-51: Multi-praticiens (7 issues)
    {
        "id": "P2-51.1",
        "title": "Table practitioners et profils",
        "objective": "Créer la structure BDD pour gérer plusieurs esthéticiennes.",
        "tasks": [
            "Table Practitioner (user_id, name, specialties, bio, photo)",
            "Relation One-to-One avec User",
            "Champs: phone, email, hire_date, is_active",
            "Table many-to-many Practitioner-Service (compétences)",
            "Migration Alembic",
            "Seed 2 praticiens exemple"
        ],
        "acceptance": [
            "Table créée avec relations",
            "Profils praticiens structurés",
            "Migration testée"
        ],
        "dependencies": None,
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-51.2",
        "title": "Assignment RDV à praticien spécifique",
        "objective": "Permettre l'attribution d'une réservation à un praticien spécifique.",
        "tasks": [
            "Ajouter champ practitioner_id sur Booking",
            "API modification: sélection praticien à booking",
            "Validation compétences praticien-service",
            "Auto-assignment si pas de préférence",
            "Frontend: dropdown choix praticien",
            "Affichage praticien dans confirmation"
        ],
        "acceptance": [
            "Attribution praticien fonctionnelle",
            "Validation compétences OK",
            "Affichage clair pour client"
        ],
        "dependencies": "P2-51.1",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-51.3",
        "title": "Calendriers séparés par praticien",
        "objective": "Afficher un calendrier distinct pour chaque praticien dans le CRM.",
        "tasks": [
            "CRM: Sélecteur praticien sur vue calendrier",
            "Filtrage bookings par practitioner_id",
            "Color-coding par praticien",
            "Vue 'Tous les praticiens' agrégée",
            "Affichage charge travail individuelle",
            "Export planning praticien"
        ],
        "acceptance": [
            "Calendriers individuels fonctionnels",
            "Filtres praticiens intuitifs",
            "Vue globale disponible"
        ],
        "dependencies": "P2-51.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-51.4",
        "title": "Disponibilités par praticien",
        "objective": "Gérer des horaires et disponibilités spécifiques pour chaque praticien.",
        "tasks": [
            "Table PractitionerAvailability (horaires hebdomadaires)",
            "CRUD disponibilités par praticien",
            "CRM page /practitioners/{id}/availability",
            "Gestion exceptions (congés, absences)",
            "Check_availability() prend en compte praticien",
            "Affichage front: Disponibilités réelles par praticien"
        ],
        "acceptance": [
            "Horaires individualisés gérés",
            "Disponibilités correctes en booking",
            "Gestion congés fonctionnelle"
        ],
        "dependencies": "P2-51.3",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-51.5",
        "title": "Statistiques par praticien",
        "objective": "Calculer et afficher les stats de performance individuelles.",
        "tasks": [
            "CA par praticien",
            "Nombre bookings par praticien",
            "Taux remplissage calendrier",
            "Services les plus vendus par praticien",
            "Note satisfaction moyenne (si avis)",
            "Dashboard CRM /reports/practitioners"
        ],
        "acceptance": [
            "Stats précises calculées",
            "Dashboard comparatif disponible",
            "Métriques motivantes"
        ],
        "dependencies": "P2-51.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-51.6",
        "title": "Permissions et accès praticiens",
        "objective": "Gérer les permissions d'accès CRM selon le rôle (admin vs praticien).",
        "tasks": [
            "Rôle 'practitioner' dans RBAC",
            "Praticien: Voir uniquement SES bookings",
            "Praticien: Modifier uniquement SES disponibilités",
            "Admin: Accès complet tous praticiens",
            "Middleware vérification permissions",
            "Tests permissions"
        ],
        "acceptance": [
            "Permissions correctes appliquées",
            "Isolation données praticiens",
            "Sécurité validée"
        ],
        "dependencies": "P2-51.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-51.7",
        "title": "Tests module multi-praticiens",
        "objective": "Valider le module multi-praticiens avec tests automatisés.",
        "tasks": [
            "Tests CRUD praticiens",
            "Tests assignment bookings",
            "Tests disponibilités",
            "Tests permissions RBAC",
            "Tests stats par praticien",
            "Tests E2E booking avec praticien"
        ],
        "acceptance": [
            "Coverage >80%",
            "Tests permissions solides",
            "Scénarios multi-users validés"
        ],
        "dependencies": "P2-51.6",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-52: Marketplace Partenaires (8 issues)
    {
        "id": "P2-52.1",
        "title": "BDD partenaires et produits externes",
        "objective": "Créer la structure pour gérer des partenaires et leurs produits.",
        "tasks": [
            "Table Partner (name, contact, commission_rate, status)",
            "Modifier Product: ajouter partner_id (nullable)",
            "Produits propres: partner_id = NULL",
            "Produits partenaires: partner_id renseigné",
            "Table PartnerOrder (suivi commandes partenaires)",
            "Migration Alembic"
        ],
        "acceptance": [
            "Tables créées avec relations",
            "Distinction produits propres/partenaires",
            "Migration testée"
        ],
        "dependencies": None,
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.2",
        "title": "API gestion partenaires CRUD",
        "objective": "Créer les endpoints pour gérer les partenaires.",
        "tasks": [
            "Créer api/v1/partners.py",
            "POST /partners (création)",
            "GET /partners (liste)",
            "PATCH /partners/{id} (modification)",
            "DELETE /partners/{id} (désactivation)",
            "Schemas Pydantic Partner",
            "Permissions admin uniquement"
        ],
        "acceptance": [
            "CRUD partenaires fonctionnel",
            "Permissions correctes",
            "Documentation API complète"
        ],
        "dependencies": "P2-52.1",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.3",
        "title": "Commission tracking automatique",
        "objective": "Calculer et tracker automatiquement les commissions partenaires.",
        "tasks": [
            "Hook après vente produit partenaire",
            "Calcul commission (ex: 15% du prix)",
            "Table Commission (partner_id, amount, order_id, status)",
            "Statuts: pending, paid, disputed",
            "Agrégation commissions mensuelles",
            "Notifications partenaire"
        ],
        "acceptance": [
            "Commissions calculées automatiquement",
            "Traçabilité complète",
            "Rapports mensuels générés"
        ],
        "dependencies": "P2-52.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.4",
        "title": "Frontend marketplace produits mixtes",
        "objective": "Afficher une marketplace mêlant produits propres et partenaires.",
        "tasks": [
            "Page /shop avec tous produits",
            "Badge 'Partenaire' sur produits externes",
            "Filtres: Propres / Partenaires",
            "Tri par popularité, prix",
            "Composant ProductCard uniformisé",
            "SEO optimisé marketplace"
        ],
        "acceptance": [
            "Marketplace attrayante et claire",
            "Distinction produits visible",
            "Performance optimale"
        ],
        "dependencies": "P2-52.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.5",
        "title": "Panier mixte produits propres + partenaires",
        "objective": "Gérer un panier contenant différents types de produits.",
        "tasks": [
            "Logique panier: regrouper par source (propre/partenaire)",
            "Calcul frais livraison par source",
            "Affichage récapitulatif détaillé",
            "Information délais livraison différents",
            "Validation stock multi-sources",
            "Tests edge cases panier"
        ],
        "acceptance": [
            "Panier mixte fonctionnel",
            "Calculs corrects",
            "UX claire pour client"
        ],
        "dependencies": "P2-52.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.6",
        "title": "Paiements split multi-bénéficiaires",
        "objective": "Implémenter le split de paiement entre institut et partenaires.",
        "tasks": [
            "Stripe Connect: Onboarding partenaires",
            "Créer Connected Accounts partenaires",
            "Payment Intent avec transfers automatiques",
            "Calcul split: Partenaire 85%, Institut 15%",
            "Gestion erreurs transfer",
            "Tests sandbox multi-beneficiaires"
        ],
        "acceptance": [
            "Paiements split fonctionnels",
            "Partenaires payés automatiquement",
            "Comptabilité correcte"
        ],
        "dependencies": "P2-52.5",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.7",
        "title": "Reporting partenaires dashboard",
        "objective": "Créer un dashboard pour les partenaires pour suivre leurs ventes.",
        "tasks": [
            "Page /partners/{id}/dashboard (accès partenaire)",
            "Ventes du mois (quantité, CA)",
            "Commissions dues/payées",
            "Top produits vendus",
            "Export factures mensuelles",
            "Graphiques évolution"
        ],
        "acceptance": [
            "Dashboard partenaire fonctionnel",
            "Métriques précises temps réel",
            "Exports comptables disponibles"
        ],
        "dependencies": "P2-52.6",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-52.8",
        "title": "Tests module marketplace",
        "objective": "Valider le module marketplace avec tests automatisés.",
        "tasks": [
            "Tests CRUD partenaires",
            "Tests calcul commissions",
            "Tests panier mixte",
            "Tests paiements split (mocks Stripe)",
            "Tests permissions partenaires",
            "Tests E2E achat produit partenaire"
        ],
        "acceptance": [
            "Coverage >80%",
            "Tests Stripe Connect mockés",
            "Scénarios complexes validés"
        ],
        "dependencies": "P2-52.7",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-53: Avis et Notations (5 issues)
    {
        "id": "P2-53.1",
        "title": "Table reviews et modèle BDD",
        "objective": "Créer la structure pour stocker les avis clients.",
        "tasks": [
            "Table Review (booking_id, client_id, rating, comment)",
            "Rating: 1-5 étoiles",
            "Champs: is_verified, is_public, created_at",
            "Relation One-to-One Review-Booking",
            "Index sur client_id et rating",
            "Migration Alembic"
        ],
        "acceptance": [
            "Table créée avec contraintes",
            "Relations correctes",
            "Migration testée"
        ],
        "dependencies": None,
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-53.2",
        "title": "API post et get reviews",
        "objective": "Créer les endpoints pour soumettre et récupérer les avis.",
        "tasks": [
            "POST /bookings/{id}/review (client uniquement)",
            "Validation: 1 review par booking",
            "GET /reviews (publics uniquement)",
            "GET /reviews/stats (moyenne, distribution)",
            "Filtres: service, rating, date",
            "Schemas Pydantic"
        ],
        "acceptance": [
            "API reviews fonctionnelle",
            "Validation doublons OK",
            "Stats calculées correctement"
        ],
        "dependencies": "P2-53.1",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-53.3",
        "title": "Modération avis CRM",
        "objective": "Permettre la modération des avis avant publication.",
        "tasks": [
            "Page CRM /reviews/moderate",
            "Liste avis pending approval",
            "Actions: Approuver, Rejeter, Demander modification",
            "Champ admin_note (raison rejet)",
            "Notification client (approval/rejet)",
            "Filtres par status, rating"
        ],
        "acceptance": [
            "Interface modération fonctionnelle",
            "Workflow validation clair",
            "Notifications automatiques"
        ],
        "dependencies": "P2-53.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-53.4",
        "title": "Widget avis frontend public",
        "objective": "Afficher les avis clients sur le site public.",
        "tasks": [
            "Composant ReviewsSection.tsx (homepage)",
            "Affichage moyenne + nb avis",
            "Carrousel 3-5 meilleurs avis",
            "Page /reviews avec tous avis",
            "Filtres par service, rating",
            "Schema markup Google (SEO)"
        ],
        "acceptance": [
            "Widget avis attractif",
            "Performance optimale",
            "SEO rich snippets fonctionnels"
        ],
        "dependencies": "P2-53.3",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-53.5",
        "title": "Sync Google Reviews bidirectionnelle",
        "objective": "Synchroniser automatiquement avec les avis Google My Business.",
        "tasks": [
            "Google My Business API setup",
            "Import avis Google → BDD (daily job)",
            "Marquage source: 'google' vs 'internal'",
            "Affichage mixte avis Google + internes",
            "Réponse aux avis Google depuis CRM",
            "Tests sync"
        ],
        "acceptance": [
            "Avis Google importés automatiquement",
            "Affichage unifié sources multiples",
            "Réponses synchronisées"
        ],
        "dependencies": "P2-53.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-54: Analytics Avancés et BI (6 issues)
    {
        "id": "P2-54.1",
        "title": "Setup Metabase ou Superset BI",
        "objective": "Installer et configurer une plateforme Business Intelligence.",
        "tasks": [
            "Choisir: Metabase (simple) vs Superset (avancé)",
            "Docker container BI tool",
            "Connexion read-only PostgreSQL",
            "Configuration utilisateurs admin",
            "Sécurisation accès (VPN ou IP whitelist)",
            "Documentation setup"
        ],
        "acceptance": [
            "BI tool opérationnel",
            "Connexion BDD fonctionnelle",
            "Accès sécurisé configuré"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-54.2",
        "title": "Dashboards avancés business",
        "objective": "Créer des dashboards analytiques pour le pilotage business.",
        "tasks": [
            "Dashboard CA détaillé (évolution, sources)",
            "Dashboard Clients (acquisition, rétention, segments)",
            "Dashboard Services (performances, popularité)",
            "Dashboard Marketing (ROI campagnes, conversions)",
            "Filtres temporels interactifs",
            "Export PDF dashboards"
        ],
        "acceptance": [
            "Dashboards complets et lisibles",
            "Données temps réel",
            "Exports fonctionnels"
        ],
        "dependencies": "P2-54.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-54.3",
        "title": "Prédictions CA avec Machine Learning",
        "objective": "Implémenter un modèle prédictif de chiffre d'affaires.",
        "tasks": [
            "Extraire historique CA quotidien",
            "Feature engineering: tendances, saisonnalité",
            "Modèle time series (Prophet ou ARIMA)",
            "Training et validation modèle",
            "Prédictions CA 30-90 jours",
            "Dashboard prédictions vs réel"
        ],
        "acceptance": [
            "Prédictions générées automatiquement",
            "Précision raisonnable (MAPE <20%)",
            "Visualisations claires"
        ],
        "dependencies": "P2-54.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-54.4",
        "title": "Cohort analysis clients",
        "objective": "Analyser la rétention clients par cohortes d'acquisition.",
        "tasks": [
            "Grouper clients par mois inscription",
            "Calculer taux rétention M1, M3, M6, M12",
            "Visualisation heatmap cohortes",
            "Identification cohortes high-value",
            "Comparaison sources acquisition",
            "Dashboard CRM cohort analysis"
        ],
        "acceptance": [
            "Analyse cohortes automatisée",
            "Visualisations claires",
            "Insights actionnables"
        ],
        "dependencies": "P2-54.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-54.5",
        "title": "Funnel conversions e-commerce",
        "objective": "Analyser le tunnel de conversion du site public.",
        "tasks": [
            "Tracking événements: Visite → Service → Date → Panier → Paiement",
            "Calcul taux conversion chaque étape",
            "Identification points friction (drop-off)",
            "Segmentation par source trafic",
            "Visualisation funnel interactif",
            "Alertes baisse conversion"
        ],
        "acceptance": [
            "Funnel complet tracké",
            "Taux conversion précis",
            "Alertes configurées"
        ],
        "dependencies": "P2-54.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-54.6",
        "title": "Exports rapports automatisés",
        "objective": "Automatiser la génération et envoi de rapports périodiques.",
        "tasks": [
            "Rapport hebdomadaire: CA, bookings, nouveaux clients",
            "Rapport mensuel: Synthèse complète + graphiques",
            "Génération PDF automatique",
            "Email automatique aux stakeholders",
            "Scheduling Celery tasks",
            "Personnalisation rapports par destinataire"
        ],
        "acceptance": [
            "Rapports générés automatiquement",
            "PDF professionnels",
            "Envois ponctuels confirmés"
        ],
        "dependencies": "P2-54.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-55: Application Mobile (8 issues)
    {
        "id": "P2-55.1",
        "title": "Décision PWA vs React Native",
        "objective": "Analyser et décider l'approche technique pour l'application mobile.",
        "tasks": [
            "Comparer PWA vs React Native (avantages/inconvénients)",
            "Critères: Budget, délai, features natives nécessaires",
            "Tester PWA capabilities (push notifs, offline, etc.)",
            "POC simple chaque approche",
            "Documenter décision dans DECISIONS.md",
            "Validation décision avec stakeholders"
        ],
        "acceptance": [
            "Analyse comparative complète",
            "Décision documentée et justifiée",
            "POCs fonctionnels testés"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.2",
        "title": "Setup projet mobile (PWA ou RN)",
        "objective": "Initialiser le projet mobile selon la décision technique.",
        "tasks": [
            "Si PWA: Next.js PWA plugin, manifest.json, service worker",
            "Si RN: React Native CLI setup, structure dossiers",
            "Configuration build iOS + Android",
            "Setup navigation (React Navigation)",
            "Thème et design system mobile",
            "Test build et déploiement local"
        ],
        "acceptance": [
            "Projet mobile initialisé",
            "Build fonctionnel iOS/Android",
            "Architecture claire"
        ],
        "dependencies": "P2-55.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.3",
        "title": "Authentification mobile",
        "objective": "Implémenter le login et gestion session mobile.",
        "tasks": [
            "Écrans Login + Signup mobile",
            "JWT token storage sécurisé (SecureStore/Keychain)",
            "Auto-login si token valide",
            "Logout et refresh token",
            "Biométrie optionnelle (Face ID, Touch ID)",
            "Tests auth flow"
        ],
        "acceptance": [
            "Auth mobile fonctionnelle",
            "Sécurité tokens respectée",
            "Biométrie opérationnelle"
        ],
        "dependencies": "P2-55.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.4",
        "title": "Module booking mobile",
        "objective": "Adapter le flow de réservation pour mobile.",
        "tasks": [
            "Écrans: Sélection service, Date/heure, Récapitulatif",
            "Navigation fluide entre étapes",
            "Affichage calendrier mobile optimisé",
            "Sélection praticien si multi-praticiens",
            "Validation formulaire",
            "Confirmation visuelle"
        ],
        "acceptance": [
            "Flow booking mobile complet",
            "UX optimisée tactile",
            "Performance fluide"
        ],
        "dependencies": "P2-55.3",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.5",
        "title": "Paiements mobile intégrés",
        "objective": "Intégrer les solutions de paiement mobile (Apple Pay, Google Pay).",
        "tasks": [
            "Stripe Apple Pay setup",
            "Stripe Google Pay setup",
            "Boutons paiement natifs",
            "Fallback: formulaire carte classique",
            "Gestion 3D Secure mobile",
            "Tests paiements sandbox"
        ],
        "acceptance": [
            "Apple Pay et Google Pay fonctionnels",
            "UX paiement optimale",
            "Sécurité respectée"
        ],
        "dependencies": "P2-55.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.6",
        "title": "Notifications push Firebase/APNS",
        "objective": "Implémenter les notifications push natives.",
        "tasks": [
            "Firebase Cloud Messaging setup (Android)",
            "Apple Push Notification Service setup (iOS)",
            "Backend: Send push notification service",
            "Gestion tokens devices",
            "Notifications: Confirmation booking, Rappel 24h",
            "Deep linking depuis notification"
        ],
        "acceptance": [
            "Push notifications fonctionnelles iOS/Android",
            "Taux livraison >90%",
            "Deep links opérationnels"
        ],
        "dependencies": "P2-55.5",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.7",
        "title": "Tests mobile (E2E et unit)",
        "objective": "Valider l'application mobile avec tests automatisés.",
        "tasks": [
            "Setup Detox (React Native) ou Playwright (PWA)",
            "Tests E2E: Login, Booking, Paiement",
            "Tests unitaires composants critiques",
            "Tests notifications push (mocks)",
            "Tests offline mode",
            "CI/CD integration tests"
        ],
        "acceptance": [
            "Coverage tests >70%",
            "Tests E2E stables",
            "CI/CD mobile opérationnel"
        ],
        "dependencies": "P2-55.6",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-55.8",
        "title": "Déploiement App Store et Play Store",
        "objective": "Publier l'application sur les stores officiels.",
        "tasks": [
            "Création comptes développeur Apple + Google",
            "Préparation assets (icônes, screenshots, descriptions)",
            "Build production signée (iOS + Android)",
            "Soumission App Store Connect",
            "Soumission Google Play Console",
            "Gestion review et publication"
        ],
        "acceptance": [
            "App publiée sur les deux stores",
            "Review approuvée",
            "Utilisateurs peuvent télécharger"
        ],
        "dependencies": "P2-55.7",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-56: Intégration Comptabilité (5 issues)
    {
        "id": "P2-56.1",
        "title": "Export FEC (Fichier Échanges Informatisé)",
        "objective": "Générer le fichier FEC réglementaire pour conformité fiscale française.",
        "tasks": [
            "Étudier format FEC (norme DGFiP)",
            "Mapping données: Transactions → Format FEC",
            "Génération fichier CSV FEC",
            "Validation format (outil DGFiP)",
            "API GET /accounting/fec?start_date&end_date",
            "Tests avec exemples officiels"
        ],
        "acceptance": [
            "FEC généré conforme norme",
            "Validation DGFiP OK",
            "Export disponible CRM"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-56.2",
        "title": "Intégration Sage ou Ciel comptabilité",
        "objective": "Connecter le système à un logiciel comptable professionnel.",
        "tasks": [
            "Choisir: Sage 100 vs Ciel Compta",
            "Étudier API ou import CSV",
            "Mapping comptes comptables (PCG)",
            "Export écritures comptables",
            "Tests import dans logiciel",
            "Documentation procédure"
        ],
        "acceptance": [
            "Export compatible Sage/Ciel",
            "Import testé et validé",
            "Procédure documentée"
        ],
        "dependencies": "P2-56.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-56.3",
        "title": "Mapping comptes comptables automatique",
        "objective": "Définir et automatiser l'affectation des comptes comptables.",
        "tasks": [
            "Compte 707: Ventes prestations services",
            "Compte 411: Clients",
            "Compte 512: Banque",
            "Compte 445: TVA collectée",
            "Table AccountMapping (transaction_type → compte)",
            "Service get_account_code(transaction)"
        ],
        "acceptance": [
            "Mapping comptes complet",
            "Affectation automatique correcte",
            "Conformité PCG français"
        ],
        "dependencies": "P2-56.2",
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-56.4",
        "title": "Rapports TVA automatisés",
        "objective": "Générer automatiquement les déclarations de TVA.",
        "tasks": [
            "Calcul TVA collectée (ventes)",
            "Calcul TVA déductible (achats)",
            "Rapport CA3 (déclaration TVA)",
            "Détail par taux TVA (20%, 10%, 5.5%)",
            "Export PDF rapport TVA",
            "Page CRM /accounting/vat"
        ],
        "acceptance": [
            "Rapports TVA exacts",
            "Conformité déclarations fiscales",
            "Export comptable disponible"
        ],
        "dependencies": "P2-56.3",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-56.5",
        "title": "Tests module comptabilité",
        "objective": "Valider le module comptabilité avec tests automatisés.",
        "tasks": [
            "Tests génération FEC",
            "Tests mapping comptes",
            "Tests calculs TVA",
            "Tests export Sage/Ciel",
            "Validation données réglementaires",
            "Tests edge cases fiscaux"
        ],
        "acceptance": [
            "Coverage >80%",
            "Conformité fiscale validée",
            "Scénarios réels testés"
        ],
        "dependencies": "P2-56.4",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-57: Carte Membre NFC/Wallet (6 issues)
    {
        "id": "P2-57.1",
        "title": "Intégration Apple Wallet API",
        "objective": "Permettre aux clients d'ajouter leur carte fidélité dans Apple Wallet.",
        "tasks": [
            "Setup Apple Developer compte + certificates",
            "Générer Pass Type ID",
            "Créer service generate_apple_pass(client)",
            "Design pass (logo, couleurs, layout)",
            "Endpoint API /wallet/apple/pass/{client_id}",
            "Tests ajout Wallet iOS"
        ],
        "acceptance": [
            "Pass Apple Wallet généré",
            "Ajout Wallet fonctionnel iOS",
            "Design professionnel"
        ],
        "dependencies": None,
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-57.2",
        "title": "Intégration Google Wallet API",
        "objective": "Permettre aux clients Android d'ajouter leur carte dans Google Wallet.",
        "tasks": [
            "Setup Google Pay & Wallet API",
            "Créer service generate_google_pass(client)",
            "Design pass Google (template)",
            "Endpoint API /wallet/google/pass/{client_id}",
            "JWT signing pour sécurité",
            "Tests ajout Wallet Android"
        ],
        "acceptance": [
            "Pass Google Wallet généré",
            "Ajout Wallet Android fonctionnel",
            "Sécurité JWT OK"
        ],
        "dependencies": "P2-57.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-57.3",
        "title": "Génération passes fidélité dynamiques",
        "objective": "Générer des passes avec données client dynamiques (points, tier).",
        "tasks": [
            "Affichage solde points sur pass",
            "Affichage tier fidélité (bronze/argent/or)",
            "QR code unique par client",
            "Barcode 128 (fallback)",
            "Update automatique pass (push notifications)",
            "Expiration optionnelle"
        ],
        "acceptance": [
            "Données dynamiques correctes",
            "Updates push fonctionnels",
            "QR/Barcode scannables"
        ],
        "dependencies": "P2-57.2",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-57.4",
        "title": "QR codes fidélité personnalisés",
        "objective": "Générer des QR codes uniques pour identifier rapidement les clients.",
        "tasks": [
            "Générer QR code par client (UUID)",
            "Stockage qr_code_data sur Client",
            "Library qrcode Python",
            "Format QR: JSON {client_id, loyalty_code}",
            "Affichage QR dans espace client web",
            "Affichage QR dans pass Wallet"
        ],
        "acceptance": [
            "QR codes générés automatiquement",
            "Format JSON standardisé",
            "Affichage multi-supports"
        ],
        "dependencies": "P2-57.3",
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-57.5",
        "title": "Scanner cartes/QR depuis CRM POS",
        "objective": "Permettre au CRM de scanner les cartes fidélité pour identification rapide.",
        "tasks": [
            "Module scan QR code CRM (webcam ou scanner)",
            "Décodage QR → récupération client_id",
            "Affichage immédiat fiche client",
            "Attribution points via scan",
            "Support barcode 128 également",
            "Tests scan multi-devices"
        ],
        "acceptance": [
            "Scan QR fonctionnel CRM",
            "Identification instantanée client",
            "Attribution points rapide"
        ],
        "dependencies": "P2-57.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-57.6",
        "title": "Tests module Wallet/NFC",
        "objective": "Valider le module carte membre avec tests automatisés.",
        "tasks": [
            "Tests génération passes Apple/Google",
            "Tests QR code génération/décodage",
            "Tests updates passes dynamiques",
            "Tests scan CRM",
            "Tests sécurité JWT",
            "Tests E2E ajout Wallet"
        ],
        "acceptance": [
            "Coverage >80%",
            "Tests multi-plateformes",
            "Sécurité validée"
        ],
        "dependencies": "P2-57.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },

    # P2-58: Chatbot IA (8 issues)
    {
        "id": "P2-58.1",
        "title": "Setup OpenAI API et configuration",
        "objective": "Configurer l'accès à l'API OpenAI pour le chatbot.",
        "tasks": [
            "Créer compte OpenAI + API key",
            "Installer openai SDK Python",
            "Créer service chatbot_service.py",
            "Configuration modèle (GPT-4 ou GPT-3.5-turbo)",
            "Gestion rate limiting",
            "Tests connexion API"
        ],
        "acceptance": [
            "API OpenAI opérationnelle",
            "Service chatbot fonctionnel",
            "Rate limiting configuré"
        ],
        "dependencies": None,
        "estimation": "1h",
        "labels": ["atomic", "quick-win", "phase-2"]
    },
    {
        "id": "P2-58.2",
        "title": "Base connaissances et FAQs",
        "objective": "Créer une base de connaissances pour entraîner le chatbot.",
        "tasks": [
            "Compiler FAQs institut (horaires, services, tarifs, etc.)",
            "Créer documents knowledge base (Markdown)",
            "Table KnowledgeArticle (question, answer, category)",
            "Embedding vectoriel articles (OpenAI embeddings)",
            "Recherche sémantique similarité",
            "CRUD knowledge base CRM"
        ],
        "acceptance": [
            "Base connaissances structurée",
            "Recherche sémantique fonctionnelle",
            "CRUD CRM opérationnel"
        ],
        "dependencies": "P2-58.1",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-58.3",
        "title": "Widget chat frontend public",
        "objective": "Intégrer un widget de chat sur le site public.",
        "tasks": [
            "Composant ChatWidget.tsx (bulle flottante)",
            "Interface conversation (messages user/bot)",
            "Envoi message API /chat/message",
            "Affichage réponse streaming (effet typing)",
            "Historique conversation session",
            "Design moderne et accessible"
        ],
        "acceptance": [
            "Widget chat intégré",
            "UX fluide et réactive",
            "Streaming responses fonctionnel"
        ],
        "dependencies": "P2-58.2",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-58.4",
        "title": "Intent recognition et actions",
        "objective": "Détecter les intentions utilisateur et déclencher actions appropriées.",
        "tasks": [
            "Intents: book_appointment, check_hours, get_pricing, contact",
            "Extraction entités (service, date, etc.)",
            "Actions: Redirection booking, affichage horaires, etc.",
            "Prompts système pour guider IA",
            "Fallback si intent inconnu",
            "Logs intents détectés"
        ],
        "acceptance": [
            "Intents détectés correctement",
            "Actions appropriées déclenchées",
            "Taux succès >80%"
        ],
        "dependencies": "P2-58.3",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-58.5",
        "title": "Escalade vers humain (handoff)",
        "objective": "Permettre le transfert vers un opérateur humain si nécessaire.",
        "tasks": [
            "Bouton 'Parler à un humain' dans chat",
            "Détection automatique si bot en difficulté",
            "Notification staff CRM (nouvelle demande)",
            "Interface CRM pour reprendre conversation",
            "Historique complet transféré",
            "Email de suivi si hors horaires"
        ],
        "acceptance": [
            "Escalade manuelle et auto fonctionnelles",
            "Notifications temps réel",
            "Reprise conversation fluide"
        ],
        "dependencies": "P2-58.4",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-58.6",
        "title": "Historique conversations persistant",
        "objective": "Sauvegarder et afficher l'historique des conversations chatbot.",
        "tasks": [
            "Table Conversation (session_id, messages, created_at)",
            "Sauvegarde messages user + bot",
            "Association conversation-client si authentifié",
            "Page CRM /chatbot/history",
            "Recherche conversations",
            "Export conversations CSV"
        ],
        "acceptance": [
            "Historique complet sauvegardé",
            "CRM accès conversations",
            "Recherche fonctionnelle"
        ],
        "dependencies": "P2-58.5",
        "estimation": "1-2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-58.7",
        "title": "Training data et amélioration continue",
        "objective": "Collecter les données pour améliorer le chatbot en continu.",
        "tasks": [
            "Feedback thumbs up/down après réponse",
            "Marquage conversations réussies/échecs",
            "Export training data pour fine-tuning",
            "Dashboard métriques chatbot (satisfaction, résolution)",
            "Identification questions fréquentes non couvertes",
            "Ajout auto suggestions FAQ"
        ],
        "acceptance": [
            "Feedback collecté systématiquement",
            "Métriques trackées",
            "Amélioration continue possible"
        ],
        "dependencies": "P2-58.6",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    },
    {
        "id": "P2-58.8",
        "title": "Tests module chatbot IA",
        "objective": "Valider le module chatbot avec tests automatisés.",
        "tasks": [
            "Tests unitaires chatbot_service",
            "Tests intent recognition (mocks OpenAI)",
            "Tests escalade humain",
            "Tests historique conversations",
            "Tests E2E conversation complète",
            "Tests performance (latence réponses)"
        ],
        "acceptance": [
            "Coverage >80%",
            "Tests OpenAI mockés",
            "Performance validée (<2s réponse)"
        ],
        "dependencies": "P2-58.7",
        "estimation": "2h",
        "labels": ["atomic", "medium-task", "phase-2"]
    }
]

def main():
    """Affiche le résumé des issues à créer"""
    print(f"📊 PHASE 2 - Extensions Post-MVP")
    print(f"=" * 80)
    print(f"Total issues à créer: {len(PHASE2_ISSUES)}")
    print()

    # Grouper par module
    modules = {}
    for issue in PHASE2_ISSUES:
        module = issue['id'].split('.')[0]
        if module not in modules:
            modules[module] = []
        modules[module].append(issue)

    print("📦 Modules:")
    for module, issues in modules.items():
        print(f"  {module}: {len(issues)} issues")

    print()
    print("✅ Script prêt pour création via GitHub API")

if __name__ == "__main__":
    main()

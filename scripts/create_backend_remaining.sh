#!/bin/bash
# Script pour créer les micro-issues Backend restantes (BACK-18 à BACK-26)

REPO="Serenity-System/serenaia-beaute-backend"

echo "🔧 Création BACK-18 à BACK-26 (restantes Backend Phase 1)..."

# BACK-18: Tests (10 micro-issues)
gh issue create --repo $REPO --title "[BACK-18.1] Setup pytest.ini configuration" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Configurer pytest\n- [ ] Créer pytest.ini\n- [ ] Config paths, markers\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-18.2] Créer tests/conftest.py (fixtures)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Fixtures pytest globales\n- [ ] Créer conftest.py\n- [ ] Fixtures réutilisables\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-18.3] Créer fixture test_db" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Fixture BDD test\n- [ ] test_db fixture\n- [ ] Setup/teardown\n\n## 🔗 Dép: BACK-18.2\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-18.4] Créer fixture test_client FastAPI" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 TestClient FastAPI\n- [ ] Fixture test_client\n\n## 🔗 Dép: BACK-18.2\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-18.5] Tests models (test_models.py)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests unitaires modèles\n- [ ] Tests tous modèles\n- [ ] Relations\n\n## 🔗 Dép: BACK-18.3, BACK-8.18\n\n## ⏱️ 2h"
gh issue create --repo $REPO --title "[BACK-18.6] Tests auth (test_auth.py)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests authentification\n- [ ] Test login\n- [ ] Test JWT\n\n## 🔗 Dép: BACK-18.4, BACK-11.8\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-18.7] Tests bookings (test_bookings.py)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests réservations\n- [ ] CRUD bookings\n\n## 🔗 Dép: BACK-18.4, BACK-12.10\n\n## ⏱️ 2h"
gh issue create --repo $REPO --title "[BACK-18.8] Tests payments (test_payments.py)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests paiements\n- [ ] Tests Stripe/PayPal\n\n## 🔗 Dép: BACK-18.4, BACK-10.10\n\n## ⏱️ 2h"
gh issue create --repo $REPO --title "[BACK-18.9] Configurer coverage pytest-cov" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Coverage code\n- [ ] Install pytest-cov\n- [ ] Config .coveragerc\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-18.10] Atteindre 80%+ coverage" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Target 80% coverage\n- [ ] Run coverage\n- [ ] Ajouter tests manquants\n\n## 🔗 Dép: BACK-18.9\n\n## ⏱️ 2h"

# BACK-19: Sécurité (8 micro-issues)
gh issue create --repo $REPO --title "[BACK-19.1] Installer slowapi (rate limiting)" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Rate limiting\n- [ ] pip install slowapi\n\n## ⏱️ 10min"
gh issue create --repo $REPO --title "[BACK-19.2] Configurer rate limiter global" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Rate limit config\n- [ ] Limiter global\n- [ ] Par endpoint\n\n## 🔗 Dép: BACK-19.1\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-19.3] Configurer CORS middleware" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 CORS\n- [ ] CORSMiddleware\n- [ ] Origins autorisées\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-19.4] Ajouter security headers middleware" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Security headers\n- [ ] X-Frame-Options\n- [ ] X-Content-Type-Options\n- [ ] CSP\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-19.5] Configurer TrustedHostMiddleware" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Trusted hosts\n- [ ] TrustedHostMiddleware\n\n## ⏱️ 20min"
gh issue create --repo $REPO --title "[BACK-19.6] Ajouter GZipMiddleware" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Compression\n- [ ] GZipMiddleware\n\n## ⏱️ 15min"
gh issue create --repo $REPO --title "[BACK-19.7] Créer endpoint /security-check" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Security check endpoint\n- [ ] GET /security-check\n- [ ] Vérif headers\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-19.8] Tests sécurité (rate limit)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests sécurité\n- [ ] Test rate limit\n- [ ] Test CORS\n\n## 🔗 Dép: BACK-19.2\n\n## ⏱️ 1h"

# BACK-20: Logging (7 micro-issues)
gh issue create --repo $REPO --title "[BACK-20.1] Installer google-cloud-logging" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 GCP Logging SDK\n- [ ] pip install google-cloud-logging\n\n## ⏱️ 10min"
gh issue create --repo $REPO --title "[BACK-20.2] Installer sentry-sdk" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Sentry error tracking\n- [ ] pip install sentry-sdk\n\n## ⏱️ 10min"
gh issue create --repo $REPO --title "[BACK-20.3] Créer utils/logging.py" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Setup logging\n- [ ] Créer logging.py\n- [ ] Config loggers\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-20.4] Configurer Google Cloud Logging" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 GCP Logging\n- [ ] Setup client GCP\n- [ ] Handler\n\n## 🔗 Dép: BACK-20.1, BACK-20.3\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-20.5] Configurer Sentry (erreurs)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Sentry init\n- [ ] sentry_sdk.init()\n- [ ] DSN\n\n## 🔗 Dép: BACK-20.2\n\n## ⏱️ 45min"
gh issue create --repo $REPO --title "[BACK-20.6] Logging middleware (requêtes)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Request logging\n- [ ] Middleware logs\n- [ ] Toutes requêtes\n\n## 🔗 Dép: BACK-20.4\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-20.7] Tests logging et erreurs" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests logging\n- [ ] Test logs\n- [ ] Test Sentry capture\n\n## 🔗 Dép: BACK-20.6\n\n## ⏱️ 1h"

# BACK-21: CI/CD (9 micro-issues)
gh issue create --repo $REPO --title "[BACK-21.1] Créer .github/workflows/test.yml" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 CI tests\n- [ ] Workflow test.yml\n- [ ] pytest sur PR\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-21.2] Workflow test (pytest sur PR)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Run pytest CI\n- [ ] matrix Python versions\n- [ ] Run tests\n\n## 🔗 Dép: BACK-21.1\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-21.3] Workflow lint (ruff/black)" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Linting CI\n- [ ] ruff check\n- [ ] black --check\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-21.4] Créer .github/workflows/deploy.yml" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Deploy workflow\n- [ ] deploy.yml\n- [ ] Trigger on main\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-21.5] Build image Docker dans CI" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Docker build CI\n- [ ] Build image\n- [ ] Tag version\n\n## 🔗 Dép: BACK-21.4, BACK-14.6\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-21.6] Push vers Google Artifact Registry" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Push image GCP\n- [ ] Auth GCP\n- [ ] Push registry\n\n## 🔗 Dép: BACK-21.5\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-21.7] Deploy vers Cloud Run" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Deploy Cloud Run\n- [ ] gcloud run deploy\n- [ ] Config service\n\n## 🔗 Dép: BACK-21.6\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-21.8] Health check post-deploy" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Verify deployment\n- [ ] curl /health\n- [ ] Fail si erreur\n\n## 🔗 Dép: BACK-21.7\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-21.9] Rollback automatique si échec" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Auto rollback\n- [ ] Detect failures\n- [ ] Rollback previous\n\n## 🔗 Dép: BACK-21.8\n\n## ⏱️ 1h30"

# BACK-22: Documentation (6 micro-issues)
gh issue create --repo $REPO --title "[BACK-22.1] Configurer OpenAPI metadata" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 OpenAPI config\n- [ ] title, version, description\n- [ ] contact, license\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-22.2] Ajouter docstrings tous endpoints" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Docstrings\n- [ ] Tous endpoints documentés\n- [ ] Examples\n\n## ⏱️ 2h"
gh issue create --repo $REPO --title "[BACK-22.3] Créer examples Pydantic schemas" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Schema examples\n- [ ] Config examples\n- [ ] Tous schemas\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-22.4] Configurer Swagger UI (/docs)" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Swagger UI\n- [ ] Config /docs\n- [ ] Logo, theme\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-22.5] Configurer ReDoc (/redoc)" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 ReDoc\n- [ ] Config /redoc\n\n## ⏱️ 20min"
gh issue create --repo $REPO --title "[BACK-22.6] Créer README.md API complet" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 README API\n- [ ] Setup instructions\n- [ ] Endpoints overview\n- [ ] Auth guide\n\n## ⏱️ 1h30"

# BACK-23: Emails (8 micro-issues)
gh issue create --repo $REPO --title "[BACK-23.1] Créer compte Resend/SendGrid" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Email service\n- [ ] Compte Resend ou SendGrid\n- [ ] API key\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-23.2] Installer resend SDK" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 SDK email\n- [ ] pip install resend\n\n## ⏱️ 10min"
gh issue create --repo $REPO --title "[BACK-23.3] Créer services/email_service.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Email service\n- [ ] Créer email_service.py\n\n## 🔗 Dép: BACK-23.2\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-23.4] Template email booking_confirmation.html" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Template confirmation\n- [ ] HTML template\n- [ ] Variables dynamiques\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-23.5] Template email gift_card.html" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Template bon cadeau\n- [ ] HTML template\n- [ ] Design\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-23.6] Implémenter send_email()" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Function send_email\n- [ ] send_email() generic\n\n## 🔗 Dép: BACK-23.3\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-23.7] Implémenter send_template_email()" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Templates emails\n- [ ] send_template_email()\n- [ ] Render templates\n\n## 🔗 Dép: BACK-23.6\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-23.8] Tests envoi emails" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests emails\n- [ ] Mock emails\n- [ ] Tests templates\n\n## 🔗 Dép: BACK-23.7\n\n## ⏱️ 1h"

# BACK-24: API Disponibilités (8 micro-issues)
gh issue create --repo $REPO --title "[BACK-24.1] Créer schemas/availability.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Schemas disponibilités\n- [ ] AvailabilityRequest\n- [ ] AvailabilityResponse\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-24.2] Créer services/availability_service.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Service disponibilités\n- [ ] Créer availability_service.py\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-24.3] Implémenter get_available_slots()" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Calcul slots dispo\n- [ ] get_available_slots()\n- [ ] Algo disponibilités\n\n## 🔗 Dép: BACK-24.2\n\n## ⏱️ 2h"
gh issue create --repo $REPO --title "[BACK-24.4] Implémenter block_slot()" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Bloquer créneau\n- [ ] block_slot()\n\n## 🔗 Dép: BACK-24.3\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-24.5] Créer api/v1/availabilities.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Router disponibilités\n- [ ] Créer availabilities.py\n\n## ⏱️ 20min"
gh issue create --repo $REPO --title "[BACK-24.6] Endpoint GET /availabilities" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 GET dispo\n- [ ] GET /availabilities\n- [ ] Query params\n\n## 🔗 Dép: BACK-24.5, BACK-24.3\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-24.7] Endpoint POST /availabilities/block" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Block slot\n- [ ] POST /availabilities/block\n\n## 🔗 Dép: BACK-24.6, BACK-24.4\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-24.8] Tests disponibilités" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests API dispo\n- [ ] Tests endpoints\n- [ ] Tests algo\n\n## 🔗 Dép: BACK-24.7\n\n## ⏱️ 1h30"

# BACK-25: API Bons Cadeaux (8 micro-issues)
gh issue create --repo $REPO --title "[BACK-25.1] Créer schemas/gift_card.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Schemas bons cadeaux\n- [ ] GiftCardPurchase\n- [ ] GiftCardValidate\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-25.2] Créer services/gift_card_service.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Service gift cards\n- [ ] Créer gift_card_service.py\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-25.3] Implémenter create_gift_card()" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Créer bon cadeau\n- [ ] create_gift_card()\n- [ ] Code unique\n\n## 🔗 Dép: BACK-25.2\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-25.4] Implémenter validate_gift_card()" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Valider bon cadeau\n- [ ] validate_gift_card()\n- [ ] Check code\n\n## 🔗 Dép: BACK-25.3\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-25.5] Créer api/v1/gift_cards.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Router gift cards\n- [ ] Créer gift_cards.py\n\n## ⏱️ 20min"
gh issue create --repo $REPO --title "[BACK-25.6] Endpoint POST /gift-cards/purchase" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Achat bon cadeau\n- [ ] POST /gift-cards/purchase\n- [ ] Paiement\n\n## 🔗 Dép: BACK-25.5, BACK-25.3\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-25.7] Endpoint POST /gift-cards/validate" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Validation code\n- [ ] POST /gift-cards/validate\n\n## 🔗 Dép: BACK-25.6, BACK-25.4\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-25.8] Tests gift cards" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests gift cards\n- [ ] Tests CRUD\n- [ ] Tests validation\n\n## 🔗 Dép: BACK-25.7\n\n## ⏱️ 1h30"

# BACK-26: API Clients (10 micro-issues)
gh issue create --repo $REPO --title "[BACK-26.1] Créer schemas/client.py" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Schemas clients\n- [ ] ClientCreate\n- [ ] ClientUpdate\n- [ ] ClientResponse\n\n## ⏱️ 45min"
gh issue create --repo $REPO --title "[BACK-26.2] Créer services/client_service.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Service clients\n- [ ] Créer client_service.py\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-26.3] Créer api/v1/clients.py" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Router clients\n- [ ] Créer clients.py\n\n## ⏱️ 20min"
gh issue create --repo $REPO --title "[BACK-26.4] Endpoint POST /clients" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Créer client\n- [ ] POST /clients\n\n## 🔗 Dép: BACK-26.3, BACK-26.2\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-26.5] Endpoint GET /clients" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Liste clients\n- [ ] GET /clients\n- [ ] Pagination\n\n## 🔗 Dép: BACK-26.4\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-26.6] Endpoint GET /clients/{id}" --label "atomic,quick-win,phase-1-backend" --body "## 🎯 Détails client\n- [ ] GET /clients/{id}\n\n## 🔗 Dép: BACK-26.5\n\n## ⏱️ 30min"
gh issue create --repo $REPO --title "[BACK-26.7] Endpoint PATCH /clients/{id}" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Modifier client\n- [ ] PATCH /clients/{id}\n\n## 🔗 Dép: BACK-26.6\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-26.8] Endpoint GET /clients/{id}/history" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Historique client\n- [ ] GET /clients/{id}/history\n- [ ] RDV passés\n\n## 🔗 Dép: BACK-26.7\n\n## ⏱️ 1h"
gh issue create --repo $REPO --title "[BACK-26.9] Endpoint GET /clients/search" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Recherche clients\n- [ ] GET /clients/search\n- [ ] Query params\n\n## 🔗 Dép: BACK-26.8\n\n## ⏱️ 1h30"
gh issue create --repo $REPO --title "[BACK-26.10] Tests CRUD clients" --label "atomic,medium-task,phase-1-backend" --body "## 🎯 Tests clients\n- [ ] Tests tous endpoints\n\n## 🔗 Dép: BACK-26.9\n\n## ⏱️ 2h"

echo "✅ Backend Phase 1 complètement atomisé : 180 micro-issues créées !"

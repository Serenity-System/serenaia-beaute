# 🏗️ Architecture Technique - Sérénaïa Beauté

## 📋 Vue d'Ensemble

**Date:** 2026-01-11
**Version:** 1.0

---

## 🎯 Stack Technique Validée

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND                              │
│                                                              │
│  Next.js 14+ (App Router) + React 18+                       │
│  Tailwind CSS + shadcn/ui                                   │
│  Déployé sur: Vercel                                        │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   │ HTTPS/REST API
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                        BACKEND                               │
│                                                              │
│  Python 3.11+ + FastAPI                                     │
│  Conteneurisé: Docker                                       │
│  Déployé sur: Google Cloud Run                             │
└──────────────────┬──────────────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
┌───────▼────────┐   ┌───────▼────────┐
│   PostgreSQL    │   │     Redis      │
│   Cloud SQL     │   │  Memorystore   │
│   (données)     │   │  (cache/queue) │
└─────────────────┘   └────────────────┘
```

---

## 🎨 Frontend - Next.js

### Technologies
- **Framework:** Next.js 14+ (App Router)
- **UI Library:** React 18+
- **Styling:** Tailwind CSS 3.4+
- **Components:** shadcn/ui (composants réutilisables)
- **Animations:** Framer Motion
- **Forms:** React Hook Form + Zod
- **HTTP Client:** Fetch API native / Axios
- **State:** Context API + React Query (cache serveur)

### Structure de Projet

```
frontend/
├── app/
│   ├── (public)/
│   │   ├── page.tsx                 # Accueil
│   │   ├── a-propos/page.tsx
│   │   ├── prestations/page.tsx
│   │   ├── reservation/page.tsx
│   │   ├── bon-cadeau/page.tsx
│   │   ├── avis/page.tsx
│   │   └── contact/page.tsx
│   ├── (admin)/
│   │   └── admin/
│   │       ├── dashboard/page.tsx
│   │       ├── reservations/page.tsx
│   │       ├── prestations/page.tsx
│   │       └── bons-cadeaux/page.tsx
│   ├── api/                         # Route handlers Next.js
│   ├── layout.tsx
│   └── globals.css
├── components/
│   ├── ui/                          # shadcn/ui components
│   ├── forms/
│   ├── calendar/
│   ├── payment/
│   └── shared/
├── lib/
│   ├── api-client.ts                # Client API
│   ├── utils.ts
│   └── validators.ts                # Zod schemas
├── hooks/
│   ├── useBooking.ts
│   ├── usePayment.ts
│   └── useGiftCard.ts
├── types/
│   └── index.ts                     # Types TypeScript
└── public/
    ├── images/
    └── fonts/
```

### Variables d'Environnement Frontend

```env
# API
NEXT_PUBLIC_API_URL=https://api.serenaia-beaute.fr

# Analytics
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX

# Stripe
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=pk_live_...

# PayPal
NEXT_PUBLIC_PAYPAL_CLIENT_ID=...
```

---

## ⚙️ Backend - FastAPI

### Technologies
- **Framework:** FastAPI 0.109+
- **Python:** 3.11+
- **ORM:** SQLAlchemy 2.0
- **Migrations:** Alembic
- **Validation:** Pydantic V2
- **Authentication:** python-jose (JWT)
- **Task Queue:** Celery + Redis
- **ASGI Server:** Uvicorn + Gunicorn

### Structure de Projet

```
backend/
├── app/
│   ├── main.py                      # Point d'entrée FastAPI
│   ├── config.py                    # Configuration (env vars)
│   ├── database.py                  # Connexion DB
│   ├── deps.py                      # Dependencies (auth, DB session)
│   │
│   ├── api/
│   │   ├── v1/
│   │   │   ├── router.py            # Router principal v1
│   │   │   ├── auth.py              # Login admin
│   │   │   ├── bookings.py          # Réservations
│   │   │   ├── services.py          # Prestations
│   │   │   ├── gift_cards.py        # Bons cadeaux
│   │   │   ├── payments.py          # Paiements
│   │   │   ├── reviews.py           # Avis Google
│   │   │   └── admin.py             # Routes admin
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                  # Admin users
│   │   ├── booking.py               # Réservations
│   │   ├── service.py               # Prestations
│   │   ├── gift_card.py             # Bons cadeaux
│   │   ├── payment.py               # Paiements
│   │   └── availability.py          # Disponibilités
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── booking.py               # Pydantic schemas
│   │   ├── service.py
│   │   ├── gift_card.py
│   │   └── payment.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── booking_service.py       # Logique métier réservations
│   │   ├── payment_service.py       # Intégration paiements
│   │   ├── sms_service.py           # OVH SMS
│   │   ├── email_service.py         # Emails
│   │   ├── pdf_service.py           # Génération PDF
│   │   └── calendar_service.py      # Gestion calendrier
│   │
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── celery_app.py            # Config Celery
│   │   ├── notifications.py         # Tâches SMS/Email
│   │   └── reminders.py             # Rappels 24h
│   │
│   └── utils/
│       ├── __init__.py
│       ├── security.py              # JWT, hashing
│       └── helpers.py
│
├── alembic/
│   ├── versions/                    # Migrations DB
│   └── env.py
│
├── tests/
│   ├── conftest.py
│   ├── test_bookings.py
│   ├── test_payments.py
│   └── test_gift_cards.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
└── .env.example
```

### Variables d'Environnement Backend

```env
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/serenaia
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key-256-bits
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# APIs Paiement
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
PAYPAL_CLIENT_ID=...
PAYPAL_CLIENT_SECRET=...
LYDIA_API_KEY=...
WERO_API_KEY=...

# SMS
OVH_APPLICATION_KEY=...
OVH_APPLICATION_SECRET=...
OVH_CONSUMER_KEY=...
OVH_SMS_ACCOUNT=...

# Email
SENDGRID_API_KEY=...
FROM_EMAIL=contact@serenaia-beaute.fr

# Google Cloud
GCP_PROJECT_ID=serenaia-beaute
GCS_BUCKET_NAME=serenaia-pdf-bucket
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

# Google Business
GOOGLE_BUSINESS_LOCATION_ID=...

# Environment
ENV=production
DEBUG=False
CORS_ORIGINS=https://serenaia-beaute.fr,https://www.serenaia-beaute.fr
```

---

## 🗄️ Base de Données - PostgreSQL

### Modèle de Données

#### Table: `users` (Administrateurs)
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `services` (Prestations)
```sql
CREATE TABLE services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,  -- 'ongles', 'regard', 'visage', 'massage', 'epilation'
    description TEXT,
    duration_minutes INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    image_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `bookings` (Réservations)
```sql
CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    service_id UUID REFERENCES services(id),
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255) NOT NULL,
    client_phone VARCHAR(20) NOT NULL,
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',  -- 'pending', 'confirmed', 'cancelled', 'completed'
    payment_status VARCHAR(50) DEFAULT 'pending',  -- 'pending', 'deposit_paid', 'fully_paid', 'refunded'
    payment_amount DECIMAL(10, 2),
    payment_method VARCHAR(50),  -- 'stripe', 'paypal', 'lydia', 'wero', 'transfer'
    notes TEXT,
    cancellation_reason TEXT,
    cancelled_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `payments`
```sql
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id),
    gift_card_id UUID REFERENCES gift_cards(id),
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_provider VARCHAR(50),  -- 'stripe', 'paypal', 'lydia', 'wero'
    provider_payment_id VARCHAR(255),  -- ID transaction externe
    status VARCHAR(50) DEFAULT 'pending',  -- 'pending', 'completed', 'failed', 'refunded'
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `gift_cards` (Bons Cadeaux)
```sql
CREATE TABLE gift_cards (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(50) UNIQUE NOT NULL,  -- SERA-XXXX-XXXX
    type VARCHAR(50) NOT NULL,  -- 'amount', 'service'
    amount DECIMAL(10, 2),  -- Montant libre
    service_id UUID REFERENCES services(id),  -- Ou prestation spécifique
    buyer_name VARCHAR(255) NOT NULL,
    buyer_email VARCHAR(255) NOT NULL,
    recipient_name VARCHAR(255) NOT NULL,
    recipient_email VARCHAR(255),
    custom_message TEXT,
    purchase_date DATE DEFAULT CURRENT_DATE,
    expiry_date DATE NOT NULL,
    is_used BOOLEAN DEFAULT FALSE,
    used_at TIMESTAMP,
    used_by_booking_id UUID REFERENCES bookings(id),
    status VARCHAR(50) DEFAULT 'active',  -- 'active', 'used', 'expired', 'refunded'
    pdf_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `availabilities` (Disponibilités)
```sql
CREATE TABLE availabilities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    day_of_week INTEGER NOT NULL,  -- 0=Lundi, 6=Dimanche
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `blocked_dates` (Jours de congés)
```sql
CREATE TABLE blocked_dates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    date DATE NOT NULL UNIQUE,
    reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Table: `notifications` (Log des notifications)
```sql
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id),
    type VARCHAR(50) NOT NULL,  -- 'sms', 'email'
    channel VARCHAR(50) NOT NULL,  -- 'confirmation', 'reminder', 'cancellation'
    recipient VARCHAR(255) NOT NULL,
    content TEXT,
    status VARCHAR(50) DEFAULT 'pending',  -- 'pending', 'sent', 'failed'
    sent_at TIMESTAMP,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Index Recommandés

```sql
CREATE INDEX idx_bookings_date ON bookings(booking_date, booking_time);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_gift_cards_code ON gift_cards(code);
CREATE INDEX idx_gift_cards_status ON gift_cards(status);
CREATE INDEX idx_payments_booking ON payments(booking_id);
CREATE INDEX idx_notifications_booking ON notifications(booking_id);
```

---

## 🔄 Redis - Cache & Task Queue

### Usage

1. **Session Management** (cache)
   - Tokens JWT blacklistés
   - Sessions utilisateur admin

2. **Disponibilités en Cache**
   - Cache des créneaux disponibles (TTL: 5 min)
   - Invalidation lors de nouvelle réservation

3. **Rate Limiting**
   - Limitation des appels API par IP
   - Protection contre les abus

4. **Celery Task Queue**
   - Envoi asynchrone des SMS
   - Envoi des emails
   - Génération des PDFs
   - Rappels automatiques

### Structure des Clés Redis

```
# Cache disponibilités
availability:2026-01-15  → JSON des créneaux disponibles

# Rate limiting
ratelimit:api:192.168.1.1  → Compteur

# Celery
celery-task-meta-{task_id}  → Résultats des tâches
```

---

## 🐳 Docker & Déploiement

### Dockerfile Backend

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY ./app ./app
COPY ./alembic ./alembic
COPY alembic.ini .

# Run migrations and start server
CMD alembic upgrade head && \
    uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Cloud Run Configuration

```yaml
# service.yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: serenaia-backend
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/minScale: '1'
        autoscaling.knative.dev/maxScale: '10'
    spec:
      containers:
      - image: gcr.io/serenaia-beaute/backend:latest
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: database-url
              key: url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: redis-url
              key: url
        resources:
          limits:
            memory: 512Mi
            cpu: '1'
```

---

## 🔐 Sécurité

### Mesures Implémentées

1. **HTTPS Obligatoire** (Let's Encrypt / GCP managed SSL)
2. **CORS** configuré strictement
3. **Rate Limiting** sur toutes les routes
4. **Input Validation** via Pydantic
5. **SQL Injection Prevention** via SQLAlchemy ORM
6. **XSS Protection** via headers HTTP
7. **CSRF Tokens** pour les formulaires
8. **Secrets Management** via GCP Secret Manager
9. **JWT avec expiration** courte (30 min)
10. **Password Hashing** avec bcrypt

### Headers de Sécurité

```python
# middleware.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    return response
```

---

## 📊 Monitoring & Observabilité

### Métriques Suivies

**Cloud Monitoring:**
- Latence des requêtes (P50, P95, P99)
- Taux d'erreur 5xx
- Utilisation CPU/Mémoire
- Nombre de requêtes/minute

**Application:**
- Nombre de réservations par jour
- Taux de conversion (visite → réservation)
- Revenus générés (prestations + bons cadeaux)
- Taux d'annulation

**Business:**
- Prestations les plus populaires
- Horaires les plus demandés
- Origine géographique des clients
- Moyens de paiement utilisés

### Alertes Configurées

- Latence > 500ms pendant 5 min
- Taux d'erreur > 5%
- Service down (uptime check failed)
- Base de données > 80% capacité
- Échec d'envoi SMS/Email > 10 en 1h

---

## 🚀 CI/CD Pipeline

### GitHub Actions Workflow

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          cd backend
          pip install -r requirements.txt
          pytest

  deploy-backend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Cloud SDK
        uses: google-github-actions/setup-gcloud@v1
      - name: Build and push Docker image
        run: |
          gcloud builds submit --tag gcr.io/${{ secrets.GCP_PROJECT_ID }}/backend
      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy serenaia-backend \
            --image gcr.io/${{ secrets.GCP_PROJECT_ID }}/backend \
            --region europe-west1 \
            --platform managed

  deploy-frontend:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
```

---

## 📝 API Documentation

### Endpoints Principaux

#### Publics

```
GET    /api/v1/services              # Liste des prestations
GET    /api/v1/services/{id}         # Détail prestation

GET    /api/v1/availabilities        # Créneaux disponibles (?date=2026-01-15)
POST   /api/v1/bookings              # Créer une réservation
GET    /api/v1/bookings/{id}         # Détail réservation (avec token)
DELETE /api/v1/bookings/{id}/cancel  # Annuler réservation

POST   /api/v1/gift-cards            # Acheter bon cadeau
GET    /api/v1/gift-cards/{code}     # Vérifier validité

POST   /api/v1/payments/stripe       # Créer paiement Stripe
POST   /api/v1/payments/webhook      # Webhook Stripe

GET    /api/v1/reviews               # Récupérer avis Google
```

#### Admin (Authentifié)

```
POST   /api/v1/auth/login            # Login admin
POST   /api/v1/auth/refresh          # Refresh token

GET    /api/v1/admin/bookings        # Liste réservations
PUT    /api/v1/admin/bookings/{id}   # Modifier réservation

GET    /api/v1/admin/gift-cards      # Liste bons cadeaux
PUT    /api/v1/admin/gift-cards/{id} # Prolonger bon cadeau

GET    /api/v1/admin/services        # CRUD prestations
POST   /api/v1/admin/services
PUT    /api/v1/admin/services/{id}
DELETE /api/v1/admin/services/{id}

GET    /api/v1/admin/availabilities  # CRUD disponibilités
POST   /api/v1/admin/availabilities
PUT    /api/v1/admin/availabilities/{id}
DELETE /api/v1/admin/availabilities/{id}

GET    /api/v1/admin/stats           # Statistiques
```

---

## 🧪 Tests

### Types de Tests

1. **Tests Unitaires** (pytest)
   - Services métier
   - Validation Pydantic
   - Helpers et utils

2. **Tests d'Intégration**
   - Routes API
   - Intégrations paiements (mocked)
   - Base de données

3. **Tests E2E** (Playwright)
   - Parcours de réservation complet
   - Achat de bon cadeau
   - Interface admin

### Commandes

```bash
# Backend
cd backend
pytest --cov=app --cov-report=html

# Frontend
cd frontend
npm test
npm run test:e2e
```

---

## 📦 Dépendances Principales

### Backend (requirements.txt)

```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
alembic==1.13.1
pydantic==2.5.3
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
asyncpg==0.29.0
redis==5.0.1
celery==5.3.6
stripe==8.0.0
python-dotenv==1.0.0
httpx==0.26.0
pytest==7.4.4
pytest-asyncio==0.23.3
```

### Frontend (package.json)

```json
{
  "dependencies": {
    "next": "^14.1.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "tailwindcss": "^3.4.0",
    "framer-motion": "^11.0.0",
    "react-hook-form": "^7.49.0",
    "zod": "^3.22.0",
    "@tanstack/react-query": "^5.17.0",
    "@stripe/stripe-js": "^2.4.0",
    "date-fns": "^3.0.0"
  }
}
```

---

**Date de dernière mise à jour:** 2026-01-11
**Version:** 1.0

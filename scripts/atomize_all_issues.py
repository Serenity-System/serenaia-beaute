#!/usr/bin/env python3
"""
Script pour créer automatiquement toutes les micro-issues atomiques.
Usage: python atomize_all_issues.py
"""

import subprocess
import json
from typing import List, Dict

# Configuration des micro-issues par groupe parent
ATOMIC_ISSUES = {
    "BACK-8": {
        "parent_title": "Modèles SQLAlchemy",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"id": "8.1", "title": "Créer models/base.py (Base SQLAlchemy)", "estimate": "30min", "deps": "BACK-7.6"},
            {"id": "8.2", "title": "Créer models/user.py", "estimate": "45min", "deps": "BACK-8.1"},
            {"id": "8.3", "title": "Créer models/client.py", "estimate": "1h", "deps": "BACK-8.1"},
            {"id": "8.4", "title": "Créer models/service.py", "estimate": "45min", "deps": "BACK-8.1"},
            {"id": "8.5", "title": "Créer models/booking.py", "estimate": "1h", "deps": "BACK-8.1"},
            {"id": "8.6", "title": "Créer models/payment.py", "estimate": "1h", "deps": "BACK-8.1"},
            {"id": "8.7", "title": "Créer models/gift_card.py", "estimate": "45min", "deps": "BACK-8.1"},
            {"id": "8.8", "title": "Créer models/product.py", "estimate": "45min", "deps": "BACK-8.1"},
            {"id": "8.9", "title": "Créer models/stock_movement.py", "estimate": "1h", "deps": "BACK-8.8"},
            {"id": "8.10", "title": "Créer models/loyalty_point.py", "estimate": "45min", "deps": "BACK-8.3"},
            {"id": "8.11", "title": "Créer models/notification.py", "estimate": "45min", "deps": "BACK-8.1"},
            {"id": "8.12", "title": "Créer models/availability.py", "estimate": "1h", "deps": "BACK-8.1"},
            {"id": "8.13", "title": "Créer models/blocked_slot.py", "estimate": "45min", "deps": "BACK-8.12"},
            {"id": "8.14", "title": "Créer models/review.py", "estimate": "45min", "deps": "BACK-8.3"},
            {"id": "8.15", "title": "Créer models/photo.py", "estimate": "45min", "deps": "BACK-8.3"},
            {"id": "8.16", "title": "Créer models/automation.py", "estimate": "1h", "deps": "BACK-8.1"},
            {"id": "8.17", "title": "Créer models/__init__.py (imports tous modèles)", "estimate": "20min", "deps": "BACK-8.16"},
            {"id": "8.18", "title": "Valider relations entre tous modèles", "estimate": "1h", "deps": "BACK-8.17"},
        ]
    },
    "BACK-9": {
        "parent_title": "Alembic Migrations",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,quick-win,phase-1-backend",
        "issues": [
            {"id": "9.1", "title": "Installer alembic package", "estimate": "10min", "deps": "BACK-7.2"},
            {"id": "9.2", "title": "Initialiser alembic: alembic init", "estimate": "15min", "deps": "BACK-9.1"},
            {"id": "9.3", "title": "Configurer alembic.ini (DATABASE_URL)", "estimate": "30min", "deps": "BACK-9.2"},
            {"id": "9.4", "title": "Configurer env.py (import models)", "estimate": "45min", "deps": "BACK-9.3, BACK-8.17"},
            {"id": "9.5", "title": "Générer migration initiale: alembic revision", "estimate": "1h", "deps": "BACK-9.4"},
            {"id": "9.6", "title": "Test migration up/down", "estimate": "30min", "deps": "BACK-9.5"},
        ]
    },
    "BACK-10": {
        "parent_title": "Intégration Stripe",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"id": "10.1", "title": "Créer compte Stripe test mode", "estimate": "30min", "deps": ""},
            {"id": "10.2", "title": "Installer stripe SDK Python", "estimate": "10min", "deps": "BACK-7.2"},
            {"id": "10.3", "title": "Créer services/stripe_service.py", "estimate": "30min", "deps": "BACK-10.2"},
            {"id": "10.4", "title": "Implémenter create_payment_intent()", "estimate": "1h30", "deps": "BACK-10.3"},
            {"id": "10.5", "title": "Implémenter confirm_payment()", "estimate": "1h", "deps": "BACK-10.4"},
            {"id": "10.6", "title": "Implémenter refund_payment()", "estimate": "1h", "deps": "BACK-10.5"},
            {"id": "10.7", "title": "Créer webhook endpoint /webhooks/stripe", "estimate": "1h", "deps": "BACK-10.3"},
            {"id": "10.8", "title": "Gérer événement payment_intent.succeeded", "estimate": "1h30", "deps": "BACK-10.7"},
            {"id": "10.9", "title": "Gérer événement payment_intent.failed", "estimate": "1h", "deps": "BACK-10.8"},
            {"id": "10.10", "title": "Tests unitaires stripe_service", "estimate": "2h", "deps": "BACK-10.9"},
        ]
    },
}

def create_issue_body(issue: Dict) -> str:
    """Génère le body de l'issue."""
    body = f"""## 🎯 Objectif
{issue['title']}

## 📋 Tâche
- [ ] TODO: Détailler les étapes

## ✅ Critère d'Acceptance
- [x] Tâche complétée
- [x] Tests passent (si applicable)
- [x] Commitée

"""
    if issue.get('deps'):
        body += f"## 🔗 Dépendance: {issue['deps']}\n\n"

    body += f"## ⏱️ Estimation: {issue['estimate']}"
    return body

def create_atomic_issue(repo: str, issue_id: str, title: str, labels: str, body: str) -> str:
    """Crée une issue via gh CLI."""
    full_title = f"[{issue_id}] {title}"
    cmd = [
        "gh", "issue", "create",
        "--repo", repo,
        "--title", full_title,
        "--label", labels,
        "--body", body
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise Exception(f"Failed to create issue {issue_id}: {result.stderr}")

def main():
    """Crée toutes les micro-issues atomiques."""
    total = 0

    for group_id, config in ATOMIC_ISSUES.items():
        print(f"\n🔧 Création groupe {group_id}: {config['parent_title']}")
        print(f"   {len(config['issues'])} micro-issues à créer...")

        for issue in config['issues']:
            try:
                body = create_issue_body(issue)
                url = create_atomic_issue(
                    repo=config['repo'],
                    issue_id=f"{group_id}.{issue['id'].split('.')[-1]}",
                    title=issue['title'],
                    labels=config['labels'],
                    body=body
                )
                print(f"   ✅ {issue['id']}: {url}")
                total += 1
            except Exception as e:
                print(f"   ❌ {issue['id']}: {e}")

        print(f"   ✅ Groupe {group_id} complété: {len(config['issues'])} issues")

    print(f"\n🎉 Total: {total} micro-issues atomiques créées !")

if __name__ == "__main__":
    main()

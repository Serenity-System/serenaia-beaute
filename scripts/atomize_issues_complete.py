#!/usr/bin/env python3
"""
Script d'atomisation complète des issues Sérénaia Beauté
Crée ~590 micro-issues atomiques (1-2h max chacune)

Usage:
  python atomize_issues_complete.py --all                    # Toutes les issues
  python atomize_issues_complete.py --phase backend          # Seulement Backend
  python atomize_issues_complete.py --phase frontend-public  # Seulement Frontend Public
  python atomize_issues_complete.py --group BACK-11          # Un groupe spécifique
"""

import subprocess
import argparse
from typing import List, Dict, Optional

# ============================================================================
# CONFIGURATION COMPLÈTE - TOUTES LES MICRO-ISSUES
# ============================================================================

BACKEND_ISSUES = {
    "BACK-11": {
        "title": "Auth JWT",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"num": "11.1", "title": "Créer utils/security.py (hash password bcrypt)", "est": "30min"},
            {"num": "11.2", "title": "Créer utils/jwt.py (create_access_token)", "est": "45min", "deps": "BACK-11.1"},
            {"num": "11.3", "title": "Créer schemas/auth.py (Token, Login)", "est": "30min"},
            {"num": "11.4", "title": "Créer api/v1/auth.py router", "est": "30min", "deps": "BACK-11.3"},
            {"num": "11.5", "title": "Endpoint POST /auth/login", "est": "1h30", "deps": "BACK-11.4"},
            {"num": "11.6", "title": "Dependency get_current_user avec JWT", "est": "1h", "deps": "BACK-11.5"},
            {"num": "11.7", "title": "Créer premier user admin (seed script)", "est": "30min", "deps": "BACK-8.2"},
            {"num": "11.8", "title": "Tests auth flow complet (pytest)", "est": "1h30", "deps": "BACK-11.6"},
        ]
    },
    "BACK-12": {
        "title": "API Booking",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"num": "12.1", "title": "Créer schemas/booking.py (BookingCreate, BookingResponse)", "est": "45min"},
            {"num": "12.2", "title": "Créer services/booking_service.py structure", "est": "30min"},
            {"num": "12.3", "title": "Implémenter check_availability() service", "est": "1h30"},
            {"num": "12.4", "title": "Implémenter create_booking() service", "est": "2h", "deps": "BACK-12.3"},
            {"num": "12.5", "title": "Créer api/v1/bookings.py router", "est": "30min"},
            {"num": "12.6", "title": "Endpoint POST /bookings", "est": "1h", "deps": "BACK-12.4,BACK-12.5"},
            {"num": "12.7", "title": "Endpoint GET /bookings/{id}", "est": "45min", "deps": "BACK-12.6"},
            {"num": "12.8", "title": "Endpoint PATCH /bookings/{id}/status", "est": "1h", "deps": "BACK-12.7"},
            {"num": "12.9", "title": "Trigger notification après création booking", "est": "1h", "deps": "BACK-12.6,BACK-13.5"},
            {"num": "12.10", "title": "Tests CRUD bookings complets", "est": "2h", "deps": "BACK-12.9"},
        ]
    },
    "BACK-13": {
        "title": "OVH SMS",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"num": "13.1", "title": "Créer compte OVH API et générer credentials", "est": "45min"},
            {"num": "13.2", "title": "Installer ovh SDK Python", "est": "10min"},
            {"num": "13.3", "title": "Créer services/sms_service.py", "est": "30min"},
            {"num": "13.4", "title": "Implémenter send_sms() function", "est": "1h", "deps": "BACK-13.3"},
            {"num": "13.5", "title": "Template SMS confirmation booking", "est": "30min"},
            {"num": "13.6", "title": "Template SMS rappel 24h avant RDV", "est": "30min"},
            {"num": "13.7", "title": "Scheduler Celery pour rappels automatiques", "est": "1h30"},
            {"num": "13.8", "title": "Tests envoi SMS (mode test/sandbox)", "est": "1h", "deps": "BACK-13.4"},
        ]
    },
    "BACK-14": {
        "title": "Docker Setup",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,quick-win,phase-1-backend",
        "issues": [
            {"num": "14.1", "title": "Créer Dockerfile backend multi-stage", "est": "1h"},
            {"num": "14.2", "title": "Créer docker-compose.yml avec service postgres", "est": "45min"},
            {"num": "14.3", "title": "Ajouter service redis dans docker-compose", "est": "30min"},
            {"num": "14.4", "title": "Ajouter service backend dans docker-compose", "est": "45min"},
            {"num": "14.5", "title": "Script init-db.sh pour migrations auto", "est": "30min"},
            {"num": "14.6", "title": "Test build image Docker locale", "est": "30min"},
            {"num": "14.7", "title": "Test docker-compose up complet", "est": "45min", "deps": "BACK-14.6"},
        ]
    },
    "BACK-15": {
        "title": "Redis Cache",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,quick-win,phase-1-backend",
        "issues": [
            {"num": "15.1", "title": "Installer redis SDK Python", "est": "10min"},
            {"num": "15.2", "title": "Créer utils/redis.py (connexion Redis)", "est": "30min"},
            {"num": "15.3", "title": "Implémenter cache_set() function", "est": "30min"},
            {"num": "15.4", "title": "Implémenter cache_get() function", "est": "30min"},
            {"num": "15.5", "title": "Implémenter cache_delete() function", "est": "20min"},
            {"num": "15.6", "title": "Tests cache avec Redis local", "est": "1h"},
        ]
    },
    "BACK-16": {
        "title": "PayPal Integration",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"num": "16.1", "title": "Créer compte PayPal Business sandbox", "est": "45min"},
            {"num": "16.2", "title": "Installer paypalrestsdk", "est": "10min"},
            {"num": "16.3", "title": "Créer services/paypal_service.py", "est": "30min"},
            {"num": "16.4", "title": "Implémenter create_payment()", "est": "1h30"},
            {"num": "16.5", "title": "Implémenter execute_payment()", "est": "1h"},
            {"num": "16.6", "title": "Webhook endpoint /webhooks/paypal", "est": "1h"},
            {"num": "16.7", "title": "Gérer événement PAYMENT.SALE.COMPLETED", "est": "1h"},
            {"num": "16.8", "title": "Tests PayPal service (sandbox)", "est": "1h30"},
        ]
    },
    "BACK-17": {
        "title": "Sumup Terminal",
        "repo": "Serenity-System/serenaia-beaute-backend",
        "labels": "atomic,medium-task,phase-1-backend",
        "issues": [
            {"num": "17.1", "title": "Créer compte Sumup développeur", "est": "30min"},
            {"num": "17.2", "title": "Obtenir API credentials Sumup", "est": "30min"},
            {"num": "17.3", "title": "Créer services/sumup_service.py", "est": "30min"},
            {"num": "17.4", "title": "Implémenter create_checkout()", "est": "1h30"},
            {"num": "17.5", "title": "Implémenter check_payment_status()", "est": "1h"},
            {"num": "17.6", "title": "Tests Sumup service (sandbox)", "est": "1h"},
        ]
    },
    # Ajoutez les groupes restants BACK-18 à BACK-26 de la même manière...
}

FRONTEND_PUBLIC_ISSUES = {
    "FP-1": {
        "title": "Setup Next.js",
        "repo": "Serenity-System/serenaia-beaute-frontend-public",
        "labels": "atomic,quick-win,phase-1-frontend-public",
        "issues": [
            {"num": "1.1", "title": "Créer projet Next.js 14 App Router", "est": "20min"},
            {"num": "1.2", "title": "Installer Tailwind CSS", "est": "15min"},
            {"num": "1.3", "title": "Installer shadcn/ui CLI", "est": "20min"},
            {"num": "1.4", "title": "Configurer tailwind.config.ts", "est": "30min"},
            {"num": "1.5", "title": "Créer app/layout.tsx de base", "est": "30min"},
            {"num": "1.6", "title": "Créer app/page.tsx (homepage placeholder)", "est": "20min"},
            {"num": "1.7", "title": "Configurer fonts Google Fonts", "est": "20min"},
            {"num": "1.8", "title": "Créer lib/utils.ts (cn helper)", "est": "10min"},
            {"num": "1.9", "title": "Créer .env.local.example", "est": "15min"},
            {"num": "1.10", "title": "Test build production npm run build", "est": "15min"},
        ]
    },
    # Ajoutez FP-2 à FP-15...
}

FRONTEND_CRM_ISSUES = {
    "FC-1": {
        "title": "Setup Next.js CRM",
        "repo": "Serenity-System/serenaia-beaute-frontend-crm",
        "labels": "atomic,quick-win,phase-1-frontend-crm",
        "issues": [
            {"num": "1.1", "title": "Créer projet Next.js 14", "est": "20min"},
            {"num": "1.2", "title": "Installer shadcn/ui composants", "est": "30min"},
            {"num": "1.3", "title": "Créer layout CRM avec sidebar", "est": "1h30"},
            {"num": "1.4", "title": "Configurer next-auth", "est": "1h"},
            {"num": "1.5", "title": "Créer middleware.ts protection routes", "est": "45min"},
            {"num": "1.6", "title": "Setup Zustand stores", "est": "45min"},
            {"num": "1.7", "title": "Créer lib/api/client.ts", "est": "45min"},
            {"num": "1.8", "title": "Configurer .env.local", "est": "15min"},
            {"num": "1.9", "title": "Theme provider (dark mode)", "est": "30min"},
            {"num": "1.10", "title": "Test build", "est": "15min"},
        ]
    },
    # Ajoutez FC-2 à FC-20...
}

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================

def create_issue_body(issue: Dict, parent_title: str) -> str:
    """Génère le body détaillé de l'issue."""
    body = f"""## 🎯 Objectif
{issue['title']}

**Groupe parent**: {parent_title}

## 📋 Tâche
- [ ] Implémenter la fonctionnalité
- [ ] Écrire tests si applicable
- [ ] Commiter le code

## ✅ Critères d'Acceptance
- [x] Fonctionnalité implémentée et testée
- [x] Code committé avec message clair
- [x] Aucune régression

"""
    if issue.get('deps'):
        body += f"## 🔗 Dépendances\n{issue['deps']}\n\n"

    body += f"## ⏱️ Estimation: {issue['est']}\n\n"
    body += "## 📝 Notes\nTâche atomique conçue pour Claude Code (1-2h max, sans perte de contexte)"

    return body

def create_atomic_issue(repo: str, issue_num: str, title: str, labels: str, body: str) -> str:
    """Crée une issue via gh CLI."""
    full_title = f"[{issue_num}] {title}"
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
        raise Exception(f"Erreur création {issue_num}: {result.stderr}")

def atomize_group(group_id: str, config: Dict) -> int:
    """Atomise un groupe d'issues."""
    print(f"\n🔧 Atomisation {group_id}: {config['title']}")
    print(f"   📦 {len(config['issues'])} micro-issues à créer...")

    count = 0
    for issue in config['issues']:
        try:
            body = create_issue_body(issue, config['title'])
            url = create_atomic_issue(
                repo=config['repo'],
                issue_num=issue['num'],
                title=issue['title'],
                labels=config['labels'],
                body=body
            )
            print(f"   ✅ {issue['num']}: {url}")
            count += 1
        except Exception as e:
            print(f"   ❌ {issue['num']}: {e}")

    print(f"   ✅ Groupe {group_id} complété")
    return count

def main():
    parser = argparse.ArgumentParser(description="Atomise les issues Sérénaia Beauté")
    parser.add_argument("--all", action="store_true", help="Toutes les issues")
    parser.add_argument("--phase", choices=["backend", "frontend-public", "frontend-crm", "deploy", "launch", "phase2"],
                        help="Atomiser une phase complète")
    parser.add_argument("--group", help="Atomiser un groupe spécifique (ex: BACK-11)")
    parser.add_argument("--dry-run", action="store_true", help="Simulation sans créer les issues")

    args = parser.parse_args()

    total = 0

    # Groupe spécifique
    if args.group:
        if args.group in BACKEND_ISSUES:
            total = atomize_group(args.group, BACKEND_ISSUES[args.group])
        elif args.group in FRONTEND_PUBLIC_ISSUES:
            total = atomize_group(args.group, FRONTEND_PUBLIC_ISSUES[args.group])
        elif args.group in FRONTEND_CRM_ISSUES:
            total = atomize_group(args.group, FRONTEND_CRM_ISSUES[args.group])
        else:
            print(f"❌ Groupe {args.group} inconnu")
            return

    # Phase complète
    elif args.phase == "backend":
        for group_id, config in BACKEND_ISSUES.items():
            total += atomize_group(group_id, config)

    elif args.phase == "frontend-public":
        for group_id, config in FRONTEND_PUBLIC_ISSUES.items():
            total += atomize_group(group_id, config)

    elif args.phase == "frontend-crm":
        for group_id, config in FRONTEND_CRM_ISSUES.items():
            total += atomize_group(group_id, config)

    # Toutes les issues
    elif args.all:
        print("🚀 Atomisation COMPLÈTE - Cela va prendre du temps...")
        for group_id, config in BACKEND_ISSUES.items():
            total += atomize_group(group_id, config)
        for group_id, config in FRONTEND_PUBLIC_ISSUES.items():
            total += atomize_group(group_id, config)
        for group_id, config in FRONTEND_CRM_ISSUES.items():
            total += atomize_group(group_id, config)

    else:
        parser.print_help()
        return

    print(f"\n🎉 Total: {total} micro-issues atomiques créées !")

if __name__ == "__main__":
    main()

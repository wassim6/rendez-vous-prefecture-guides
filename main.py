# main.py
"""
Script d'exemple pour le dépôt 'guide-rendez-vous-prefecture'.
Ce script ne fait rien de particulier : il sert uniquement d'illustration.
"""

import datetime
import random

def simulate_rdv_process():
    """
    Simule (de manière fictive) une recherche de rendez-vous en préfecture.
    """
    prefectures = ["Paris", "Lyon", "Marseille", "Bordeaux", "Lille"]
    rdv_status = random.choice(["Créneau trouvé ✅", "Aucun créneau disponible ❌"])
    prefecture = random.choice(prefectures)
    print(f"[{datetime.datetime.now()}] Préfecture : {prefecture} → {rdv_status}")

if __name__ == "__main__":
    print("Simulation de prise de rendez-vous en préfecture en cours...")
    for _ in range(3):
        simulate_rdv_process()
    print("Simulation terminée.")

import os
import subprocess


def run_flake8():
    # Chemin du répertoire à analyser
    project_dir = os.path.dirname(os.path.abspath(__file__))

    # Commande flake8
    command = [
        "flake8",
        project_dir,
        "--format=html",
        "--htmldir=flake8-report",
        "--exclude=.venv,.git,__pycache__,data",
    ]

    try:
        print("Exécution de flake8...")
        subprocess.run(command, check=True)
        print("Analyse terminée. Rapport généré 'flake8-report'.")
    except subprocess.CalledProcessError as e:
        print("flake8 a détecté des erreurs.")
        print(e)


if __name__ == "__main__":
    run_flake8()

import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

LIMIT_MB = 100
WARN_MB = 50

IGNORED_FOLDERS = ["data", "reports", "models", "__pycache__"]
IGNORED_EXTS = [".csv", ".pkl", ".pyc", ".log"]

def run(command, exit_on_error=False):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Comando fallido: {command}\n{e.stderr.strip()}")
        if exit_on_error:
            sys.exit(1)
        return None

def is_git_repo():
    return os.path.isdir(".git")

def create_gitignore():
    gitignore_path = Path(".gitignore")
    if not gitignore_path.exists():
        print("[INFO] Creando .gitignore...")
        with gitignore_path.open("w") as f:
            for folder in IGNORED_FOLDERS:
                f.write(f"{folder}/\n")
            for ext in IGNORED_EXTS:
                f.write(f"*{ext}\n")

def remove_large_files():
    print("[INFO] Buscando archivos grandes...")
    deleted = []
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = Path(root) / file
            if not file_path.is_file():
                continue
            size_mb = file_path.stat().st_size / (1024 * 1024)
            if size_mb > LIMIT_MB:
                print(f"[REMOVE] {file_path} - {size_mb:.2f} MB (excede {LIMIT_MB} MB)")
                run(f"git rm --cached \"{file_path}\"")
                deleted.append(str(file_path))
            elif size_mb > WARN_MB:
                print(f"[WARN] {file_path} - {size_mb:.2f} MB (supera {WARN_MB} MB pero aceptado)")
    return deleted

def clean_git_history_auto():
    print("[INFO] Limpiando historial Git por archivos grandes...")
    run('git filter-branch --force --index-filter "git rm --cached --ignore-unmatch -r data reports models" --prune-empty --tag-name-filter cat -- --all', exit_on_error=True)
    print("[INFO] Push forzado sin preguntar...")
    run("git push origin --force --all", exit_on_error=True)
    print("[OK] Push forzado completo. Historial limpio.")

def git_sync():
    if not is_git_repo():
        print("[ERROR] No es un repositorio Git.")
        sys.exit(1)

    print("[INFO] Sincronizando con GitHub...")

    create_gitignore()
    run("git add .gitignore")

    run("git pull origin main")

    removed = remove_large_files()

    run("git add .")
    run("git commit -m \"Sincronizacion automatica: limpieza y subida\"")

    print("[INFO] Haciendo push...")
    push_result = run("git push origin main")

    if push_result is None:
        print("[INFO] Push fallido. Se asume conflicto por archivos grandes. Ejecutando limpieza automatica...")
        clean_git_history_auto()

    print("[OK] Sincronizacion finalizada.")
    if removed:
        print("[INFO] Archivos grandes ignorados del push normal:")
        for f in removed:
            print(f"   - {f}")

if __name__ == "__main__":
    git_sync()

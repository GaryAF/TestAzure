import os
import subprocess

# Exécuter ls -l dans le dossier courant
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout) 
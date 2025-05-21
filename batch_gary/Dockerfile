FROM python:3.9-slim

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxss1 \
    libasound2 \
    libxtst6 \
    libxrandr2 \
    xvfb \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Configurer les variables d'environnement pour Chrome/Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMIUM_BIN=/usr/bin/chromium
ENV CHROME_PATH=/usr/lib/chromium/
ENV CHROMIUM_PATH=/usr/lib/chromium/

# Copier les fichiers du projet
WORKDIR /app
COPY . /app/

# Installation des dépendances Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Exécution du script
CMD ["python", "main.py"]
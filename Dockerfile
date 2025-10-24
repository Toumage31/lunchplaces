# Utilise une image Python officielle légère
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le code dans le conteneur
COPY choose_lunchplace.py .

# Installer FastAPI et Uvicorn
RUN pip install fastapi uvicorn

# Exposer le port 8000
EXPOSE 8000

# Démarrer l'application
CMD ["uvicorn", "choose_lunchplace:app", "--host", "0.0.0.0", "--port", "8000"]

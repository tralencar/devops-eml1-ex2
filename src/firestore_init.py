import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import os
from pathlib import Path

# Nome da coleção
collection_name = 'devops-eml1-ex2'

# Diretórios
ROOT_DIR = Path(__file__).resolve().parents[1]
CREDENTIAL_PATH = os.path.join(ROOT_DIR, '.env', 'serviceAccountKey.json')
CSV_PATH = os.path.join(ROOT_DIR, 'data', 'cloud_input', 'water_potability_without_target.csv')

# Inicializa o Firebase Admin com a chave da pasta .env
if not firebase_admin._apps:
    cred = credentials.Certificate(str(CREDENTIAL_PATH))
    firebase_admin.initialize_app(cred)

# Inicializa o Firestore
db = firestore.client()

# Leitura do csv
df = pd.read_csv(CSV_PATH)

# Upload database
for i, row in df.iterrows():
    doc_ref = db.collection(collection_name).document(str(i))  # ID opcional
    doc_ref.set(row.to_dict())

print("✅ Inicialização concluída com sucesso para a coleção:", collection_name)
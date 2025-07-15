import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import pickle
from pathlib import Path

# === Função para autenticação no Firebase ===
def iniciar_firebase(cred_path: Path):
    if not firebase_admin._apps:
        cred = credentials.Certificate(str(cred_path))
        firebase_admin.initialize_app(cred)
    return firestore.client()

# === Função para carregar os dados do Firestore ===
def carregar_dados_firestore(db, collection_name: str) -> pd.DataFrame:
    docs = db.collection(collection_name).stream()
    data = []
    for doc in docs:
        row = doc.to_dict()
        row['id'] = doc.id
        data.append(row)
    return pd.DataFrame(data)

# === Função para carregar o modelo .pkl completo ===
def carregar_modelo(model_path: Path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

# === Função para aplicar pré-processamento ===
def preprocessar_dados(df: pd.DataFrame, model_package: dict) -> pd.DataFrame:
    df_proc = df.copy()
    df_proc = df_proc.fillna(model_package['median'])
    return df_proc[model_package['columns']]

# === Função para salvar os resultados no Firestore ===
def salvar_predicoes_firestore(db, collection_name: str, df: pd.DataFrame):
    for _, row in df.iterrows():
        doc_id = row['id']
        update_data = {"Potability": int(row['Potability'])}
        db.collection(collection_name).document(doc_id).update(update_data)

# === Função principal ===
def main():
    # === Configurações ===
    ROOT_DIR = Path(__file__).resolve().parents[1]
    CREDENTIAL_PATH = ROOT_DIR / '.env' / 'serviceAccountKey.json'
    MODEL_PATH = ROOT_DIR / 'src' / 'best_rf_full.pkl'
    COLLECTION_NAME = 'devops-eml1-ex2'

    print("🚀 Iniciando pipeline de predição...")

    # === 1. Inicializar Firebase e carregar dados ===
    db = iniciar_firebase(CREDENTIAL_PATH)
    df_input = carregar_dados_firestore(db, COLLECTION_NAME)
    print(f"📥 {df_input.shape[0]} registros carregados do Firestore")

    # === 2. Carregar modelo treinado ===
    model_package = carregar_modelo(MODEL_PATH)

    # === 3. Pré-processar dados ===
    df_processed = preprocessar_dados(df_input, model_package)

    # === 4. Realizar predição ===
    model = model_package['model']
    df_input['Potability'] = model.predict(df_processed)
    print("✅ Predições realizadas com sucesso.")

    # === 5. Atualizar Firestore ===
    salvar_predicoes_firestore(db, COLLECTION_NAME, df_input)
    print("✅ Resultados atualizados no Firestore com sucesso.")

# === Executar script ===
if __name__ == "__main__":
    main()

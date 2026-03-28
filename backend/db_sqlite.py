import sqlite3
import pandas as pd

# Fichier SQLite dans l'environnement Colab
DB_PATH = "/content/market.db"


def get_connection():
    """
    Retourne une connexion SQLite vers le fichier DB_PATH.
    """
    return sqlite3.connect(DB_PATH)


def init_prices_table(df: pd.DataFrame):
    """
    Crée/remplace la table prices_minute avec les données fournies.
    """
    conn = get_connection()
    df.to_sql("prices_minute", conn, if_exists="replace", index=False)
    conn.close()

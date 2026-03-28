import pandas as pd
from .db_sqlite import get_connection


def get_prices(ticker: str = "TSLA", limit: int = 240) -> dict:
    """
    Retourne les derniers 'limit' points pour un ticker,
    sous forme de dict (prêt pour une future API).
    """
    conn = get_connection()
    query = """
    SELECT ts, close, volume
    FROM prices_minute
    WHERE ticker = ?
    ORDER BY ts DESC
    LIMIT ?
    """
    df = pd.read_sql(query, conn, params=(ticker, limit))
    conn.close()

    df = df.sort_values("ts")
    records = df.to_dict(orient="records")

    return {
        "ticker": ticker,
        "data": records,
    }

import yfinance as yf
import pandas as pd

TICKERS = ["TSLA", "MSFT"]


def download_intraday(
    ticker: str,
    interval: str = "1m",
    period: str = "1d",
) -> pd.DataFrame | None:
    """
    Télécharge les données intraday depuis Yahoo Finance pour un ticker donné.
    """
    df = yf.download(tickers=ticker, interval=interval, period=period)
    if df.empty:
        print(f"Aucune donnée pour {ticker}")
        return None

    df.reset_index(inplace=True)
    df["ticker"] = ticker
    df.rename(
        columns={
            "Datetime": "ts",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        },
        inplace=True,
    )
    df = df[["ticker", "ts", "open", "high", "low", "close", "volume"]]
    return df


def get_all_tickers_data(tickers: list[str] | None = None) -> pd.DataFrame:
    """
    Télécharge et concatène les données pour tous les tickers.
    """
    if tickers is None:
        tickers = TICKERS

    all_data: list[pd.DataFrame] = []
    for t in tickers:
        df_t = download_intraday(t)
        if df_t is not None:
            all_data.append(df_t)

    if not all_data:
        return pd.DataFrame()

    return pd.concat(all_data, ignore_index=True)

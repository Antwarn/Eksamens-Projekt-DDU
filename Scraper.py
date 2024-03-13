import yfinance as yf

def hent_aktiekurs(symbol):
    aktie = yf.Ticker(symbol)
    historik = aktie.history(period="1d", interval="1m")  # Hent data for den seneste dag med minutintervaller
    return historik

def main():
    aktie_symbol = input("Indtast aktiesymbol (f.eks. 'AAPL' for Apple): ")

    try:
        aktiekurs_data = hent_aktiekurs(aktie_symbol)
        print("Aktiekursdata for", aktie_symbol, ":\n", aktiekurs_data)
    except Exception as e:
        print("Fejl:", str(e))

if __name__ == "__main__":
    main()

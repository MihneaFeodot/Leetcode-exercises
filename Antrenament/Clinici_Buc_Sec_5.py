import pandas as pd

# 1. Numele fisierului tau (asigura-te ca scriptul e in acelasi folder cu fisierul)
nume_fisier_intrare = "Furnizori_CNAS.xlsx"
nume_fisier_iesire = "clinici_sector_5.xlsx"

try:
    # 2. Incarcam datele
    df = pd.read_excel(nume_fisier_intrare)

    # 3. Filtram randurile care contin "Sector 5" (fara sa conteze coloana)
    # Convertim totul la string si cautam "Sector 5" (case insensitive)
    masca = df.apply(lambda row: row.astype(str).str.contains('Sector 5', case=False).any(), axis=1)
    rezultate = df[masca]

    # 4. Afisam in consola si salvam in noul fisier
    if not rezultate.empty:
        print(f"Am gasit {len(rezultate)} clinici in Sectorul 5.")
        rezultate.to_excel(nume_fisier_iesire, index=False)
        print(f"Fisierul a fost salvat ca: {nume_fisier_iesire}")
    else:
        print("Nu am gasit nicio clinica care sa contina 'Sector 5'.")

except Exception as e:
    print(f"Eroare: {e}")


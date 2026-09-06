def main():
    print("--- Notenrechner ---")
    print("Gib deine Noten ein. Tippe 'fertig' ein, wenn du alle Noten eingegeben hast.")

    noten = []

    while True:
        eingabe = input("Eingabe: ").strip()
        
        if eingabe.lower() == 'fertig':
            break

        try:
            note = float(eingabe)

            if 1.0 <= note <= 6.0:
                noten.append(note)
            else:
                print("Bitte eine Note zwischen 1 und 6 eingeben")
        except ValueError:
            print("Ungültige Eingabe. Gebe bitte eine Zahl oder fertig ein.")

    if not noten:
        print("Es wurden keine Noten eingegeben.")
        return

    durchschnitt = sum(noten) / len(noten)
    beste_note = min(noten)
    schlechteste_note = max(noten)

    bestanden_status = "Bestanden!" if durchschnitt <= 4.0 else "Nicht bestanden!"

    print("\n" + "="*30)
    print("          AUSWERTUNG          ")
    print("="*30)
    print(f"Eingegebene Noten:  {noten}")
    print(f"Anzahl der Noten:  {len(noten)}")
    print(f"Beste Note:        {beste_note:.1f}")
    print(f"Schlechteste Note: {schlechteste_note:.1f}")
    print(f"Notendurchschnitt: {durchschnitt:.2f}")
    print("-"*30)
    print(f"Status:            {bestanden_status}")
    print("="*30)

if __name__ == "__main__":
    main()

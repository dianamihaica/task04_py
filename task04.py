while True:
    # Solicită introducerea numărului de produse
    try:
        numar_produse = int(input("Introduceți numărul total de produse din comandă: "))
        if numar_produse < 1 or numar_produse > 50:
            print("Eroare: Număr de produse invalid.")
            continue
    except ValueError:
        print("Eroare: Introduceți un număr întreg valid pentru produsele comenzii.")
        continue

    # Solicită introducerea prețului comenzii
    try:
        pret_comanda = float(input("Introduceți prețul comenzii: "))
        if pret_comanda <= 0:
            print("Eroare: Prețul trebuie să fie mai mare decât 0.")
            continue
    except ValueError:
        print("Eroare: Introduceți un număr valid pentru prețul comenzii.")
        continue

    # Solicită introducerea statusului plății
    status_plata = input("Introduceți statusul plății (plătit/neplătit/în așteptare): ").strip().lower()
    if status_plata == "plătit":
        # Comanda este validă și poate fi procesată
        print(f"Comandă validă:\nNumăr de produse: {numar_produse}, Preț: {pret_comanda:.2f}, Status plată: {status_plata}")
        break
    elif status_plata in ["neplătit", "în așteptare"]:
        print("Comanda nu este plătită, nu poate fi procesată.")
    else:
        print("Eroare: Status de plată necunoscut.")

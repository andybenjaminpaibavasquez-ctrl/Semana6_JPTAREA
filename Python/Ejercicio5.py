tasa = 0.015  # 1.5% mensual
meses = 0

saldo = float(input("Depósito inicial: S/"))
meta = float(input("Meta a alcanzar: S/"))

print(f"Mes 0: S/{saldo:.2f}")

while saldo < meta:
    saldo = saldo * (1 + tasa)
    meses = meses + 1
    print(f"Mes {meses}: S/{saldo:.2f}")

print(f"Alcanzará la meta en {meses} meses.")

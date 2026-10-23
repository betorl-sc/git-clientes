def registrar_cliente(codigo, nombre, saldo=0.0):
	"""Registra un nuevo cliente con su saldo inicial."""
	return {
		"codigo": codigo,
		"nombre": nombre,
		"saldo": saldo,
		"activo": True
	}

def calcular_interes(saldo, tasa_porcentaje):
	"""Calcula el interés sobre el saldo pendiente."""
	return round(saldo * (tasa_porcentaje / 100), 2)

if __name__ == "__main__":
	cliente1 = registrar_cliente("CLI-001", "Distribuidora Los Andes", 2500.50)
	interes = calcular_interes(cliente1["saldo"], 5.0)
	print(f"Cliente registrado: {cliente1}")
	print(f"Interés por mora (5%): S/ {interes}")

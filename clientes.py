def registrar_cliente(codigo, nombre, saldo=0.0):
	"""Registra un nuevo cliente con su saldo inicial."""
	return {
		"codigo": codigo,
		"nombre": nombre,
		"saldo": saldo,
		"activo": True
	}

if __name__ == "__main__":
	cliente1 = registrar_cliente("CLI-001", "Distribuidora Los Andes", 2500.50)
	print(f"Cliente registrado con éxito: {cliente1}")

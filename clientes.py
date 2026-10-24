def registrar_cliente(codigo, nombre, saldo=0.0):
	"""Registra un nuevo cliente con su saldo inicial."""
	return {
		"codigo": codigo,
		"nombre": nombre,
		"saldo": saldo,
		"activo": True
	}

def calcular_interes(saldo, tasa_porcentaje):
	"""Calcula el interés sobre el saldo pendiente (solo si hay deuda)."""
	if saldo <= 0:
		return 0.0
	return round(saldo * (tasa_porcentaje / 100), 2)

def calcular_descuento(saldo, tasa_porcentaje):
	"""Calcula el monto final con descuento por pronto pago."""
	if saldo <= 0:
		return 0.0
	descuento = saldo * (tasa_porcentaje / 100)
	return round(saldo - descuento, 2)

def formatear_moneda(monto):
	"""Devuelve el monto formateado en moneda local."""
	return f"S/ {monto:,.2f}"

if __name__ == "__main__":
	cliente_deudor = registrar_cliente("CLI-001", "Distribuidora Los Andes", 2500.50)

	saldo_original = cliente_deudor["saldo"]
	saldo_con_descuento = calcular_descuento(saldo_original, 5.0)

	print(f"Cliente: {cliente_deudor['nombre']}")
	print(f"Saldo original: {formatear_moneda(saldo_original)}")
	print(f"Saldo con pronto pago (5% desc): {formatear_moneda(saldo_con_descuento)}")

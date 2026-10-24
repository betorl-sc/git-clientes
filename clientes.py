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

def formatear_moneda(monto):
	"""Devuelve el monto formateado en moneda local."""
	return f"S/ {monto:,.2f}"

if __name__ == "__main__":
	cliente_deudor = registrar_cliente("CLI-001", "Distribuidora Los Andes", 2500.50)
	cliente_al_dia = registrar_cliente("CLI-002", "Comercial El Sol", 0.0)

	print(f"Cliente 1: {cliente_deudor['nombre']} | Mora: {formatear_moneda(calcular_interes(cliente_deudor['saldo'], 12.0))}")
	print(f"Cliente 2: {cliente_al_dia['nombre']} | Mora: {formatear_moneda(calcular_interes(cliente_al_dia['saldo'], 12.0))}")

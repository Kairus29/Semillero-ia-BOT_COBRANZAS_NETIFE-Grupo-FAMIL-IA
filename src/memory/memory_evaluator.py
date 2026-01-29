LEGAL_KEYWORDS = [
    "deuda", "cobranza", "interés", "mora", "pago", "crédito",
    "obligación", "contrato", "saldo", "cuota", "plazo",
    "acreedor", "deudor", "refinanciar", "diferido"
]

FORBIDDEN_TOPICS = [
    "recomendación personal",
    "opinión médica",
    "consejo ilegal",
    "evasión",
    "fraude"
]


def should_learn(query: str, response: str):
    q = query.lower()
    r = response.lower()

    # 1. Tema legal / cobranzas
    if not any(word in q for word in LEGAL_KEYWORDS):
        return False, "Tema fuera del dominio de cobranzas"

    # 2. Evitar temas peligrosos
    if any(word in r for word in FORBIDDEN_TOPICS):
        return False, "Respuesta potencialmente riesgosa"

    # 3. Evitar preguntas muy cortas o vacías
    if len(q) < 15:
        return False, "Consulta demasiado vaga"

    return True, "Conocimiento legal válido"

import hashlib
from datetime import datetime


def generate_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def save_memory(vectorstore, query: str, response: str, reason: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    raw_entry = f"""
[{timestamp}]
Pregunta: {query}
Respuesta: {response}
Motivo: {reason}
"""

    entry_hash = generate_hash(raw_entry)

    with open("memory_log.txt", "a", encoding="utf-8") as f:
        f.write(raw_entry)
        f.write(f"HASH: {entry_hash}\n")
        f.write("-" * 60 + "\n")

from langchain_community.vectorstores import Chroma

def retrieve_context(vectorstore: Chroma, query: str, k: int = 3) -> str:
    total_docs = vectorstore._collection.count()
    k = min(k, total_docs)
    results = vectorstore.similarity_search(query, k=k)
    return "\n".join(doc.page_content for doc in results)



def build_prompt(context: str, query: str) -> str:
    return f"""
Eres un asistente experto en cobranzas en Ecuador.
Responde de forma profesional, objetiva y basada en normativa vigente.
Evita la primera persona.
Si no existe respaldo legal suficiente, indícalo claramente.

Base normativa disponible:

Contexto disponible:
{context}

Consulta del usuario:
{query}

Respuesta:
"""


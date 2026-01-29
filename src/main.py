import os

# ==============================
# DESACTIVAR TELEMETRÍA
# ==============================
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = ""
os.environ["CHROMA_TELEMETRY"] = "false"

from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from config.settings import (
    GROQ_API_KEY,
    CHROMA_PERSIST_DIR,
    EMBEDDING_MODEL_NAME
)

from rag.rag_retriever import retrieve_context, build_prompt
from rag.pdf_loader import load_pdfs_from_folder, split_documents
from memory.memory_evaluator import should_learn
from memory.memory_store import save_memory


load_dotenv()

# ==============================
# EMBEDDINGS
# ==============================
embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL_NAME
)

# ==============================
# VECTORSTORE
# ==============================
vectorstore = Chroma(
    persist_directory=CHROMA_PERSIST_DIR,
    embedding_function=embeddings
)

# ==============================
# CARGA DE PDFs LEGALES (UNA VEZ)
# ==============================
LEGAL_DOCS_PATH = "legal_docs"

pdf_docs = load_pdfs_from_folder(LEGAL_DOCS_PATH)
pdf_chunks = split_documents(pdf_docs)

if pdf_chunks:
    vectorstore.add_documents(pdf_chunks)
    vectorstore.persist()

# ==============================
# LLM
# ==============================
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0
)

# ==============================
# CONVERSACIÓN
# ==============================
print("Asistente de Cobranzas iniciado. Escriba 'SALIR' para finalizar.\n")

while True:
    query = input("Tú: ").strip()

    if query.upper() == "SALIR":
        print("\nBot: Conversación finalizada. Que tenga un buen día.")
        break

    context = retrieve_context(vectorstore, query)
    prompt = build_prompt(context, query)

    response = llm.invoke(prompt)
    print("\nBot:", response.content, "\n")

    # ==========================
    # APRENDIZAJE CONTROLADO
    # ==========================
    decision, reason = should_learn(query, response.content)

    if decision:
        save_memory(vectorstore, query, response.content, reason)

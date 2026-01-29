# 🤖 Bot de Cobranzas – Ecuador

Asistente inteligente de cobranzas enfocado en normativa ecuatoriana, utilizando:
- RAG (Retrieval Augmented Generation)
- Documentos legales en PDF
- Memoria selectiva y controlada
- Modelo LLM vía Groq

---

## 📁 Estructura del proyecto

Bot_cobranzas_v6/
│
├─ src/
│ ├─ main.py
│ ├─ config/
│ │ └─ settings.py
│ ├─ rag/
│ │ └─ pdf_loader.py
| | └─ rag_retriever.py
│ └─ memory/
│ ├─ memory_evaluator.py
│ └─ memory_store.py
│
├─ legal_docs/ # PDFs legales (no incluidos)
├─ requirements.txt
└─ README.md


---

## ⚙️ Requisitos

- Python 3.11
- Cuenta y API Key de Groq
- Windows / Linux / macOS

---

## 🚀 Instalación paso a paso

1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Kairus29/Bot_cobranzas_v6.git
cd Bot_cobranzas_v6

2️⃣ Crear entorno virtual
python -m venv venv

Activar:

Windows: venv\Scripts\activate
Linux / macOS : source venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Configurar variables de entorno
GROQ_API_KEY="Aquí debe ir su API KEY"

5️⃣ Agregar documentos legales (opcional pero recomendado)
Colocar PDFs legales en la carpeta:
legal_docs/

6️⃣ Ejecutar el bot
python src/main.py

## Detalles
- Es un proyecto Academico 
- No es asesoría legal
- Usa fuentes públicas
- Memoria controlada
- No usa datos personales


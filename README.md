# 🧠 Clinic AI Agent

Sistema de **RAG (Retrieval-Augmented Generation)** diseñado para la gestión y consulta inteligente de documentos clínicos y administrativos.

Permite realizar preguntas en lenguaje natural sobre documentos médicos, políticas internas y guías de cobertura, devolviendo respuestas con **fuentes trazables y verificables**.

---

## 🚀 Características

- 📄 Ingesta automática de documentos PDF
- 🧹 Limpieza y normalización de texto
- 🧠 Chunking semántico optimizado para embeddings
- 🔎 Búsqueda vectorial con FAISS
- 📌 Metadatos enriquecidos por documento
- 💬 Chat interactivo con Streamlit
- 📚 Respuestas con fuentes citables
- ⚙️ Pipeline modular listo para producción

---

## 🧱 Arquitectura del Sistema

### Pipeline RAG

```text
PDF Documents
│
▼
Document Loader (PyPDFLoader)
│
▼
Text Cleaning
│
▼
Metadata Enrichment (Category + ID + Source)
│
▼
Text Chunking (LangChain Splitters)
│
▼
Embeddings (HuggingFace)
│
▼
Vector Store (FAISS)
│
▼
Retriever
│
▼
LLM (Gemini / OpenAI)
│
▼
Structured Answer + Sources
│
▼
Streamlit UI
```


---

## 🏗️ Arquitectura del Proyecto
``` text
clinic-ai-agent/
├── app/
│ ├── chains/
│ │ └── rag_chain.py # Cadena RAG completa
│ ├── config/
│ │ ├── settings.py # Configuración global
│ │ └── validator.py # Validación de variables de entorno
│ ├── core/
│ │ ├── exceptions.py # Excepciones personalizadas
│ │ └── logging_config.py # Configuración de logs
│ ├── loaders/
│ │ └── pdf_loader.py # Carga y limpieza de PDFs
│ ├── models/
│ │ ├── cohere_model.py # Integración con Cohere
│ │ └── gemini.py # Integración con Gemini
│ ├── processing/
│ │ ├── chunking.py # Fragmentación de texto
│ │ ├── cleaning.py # Limpieza de texto
│ │ ├── embeddings.py # Generación de embeddings
│ │ └── metadata.py # Enriquecimiento de metadatos
│ ├── prompts/
│ │ └── rag_prompt.py # Templates de prompts
│ ├── retrievers/
│ │ └── retriever.py # Lógica de recuperación
│ ├── services/
│ │ ├── ingestion_service.py # Servicio de ingesta de documentos
│ │ ├── query_service.py # Servicio de consultas
│ │ ├── rag_service.py # Servicio RAG principal
│ │ └── vectorstore_service.py # Servicio de vector store
│ ├── tools/ # Herramientas auxiliares
│ ├── ui/
│ │ ├── components/
│ │ │ ├── chat.py # Componente de chat
│ │ │ ├── footer.py # Pie de página
│ │ │ └── sidebar.py # Barra lateral
│ │ ├── pages/
│ │ │ └── main.py # Página principal
│ │ └── styles/
│ │ └── theme.py # Estilos y temas
│ └── vectorstores/
│ └── faiss_store.py # Implementación FAISS
│
├── data/
│ └── documentos/
│ ├── coberturas/ # Documentos sobre coberturas médicas
│ │ └── guia_coberturas_medicas.pdf
│ ├── consultas/ # Documentos sobre consultas y turnos
│ │ └── faq_consultas_y_turnos.pdf
│ └── politicas/ # Documentos sobre políticas
│ ├── politica_cancelaciones.pdf
│ └── politica_privacidad_pacientes.pdf
│
├── vector_db/
│ └── faiss_index/ # Índice vectorial persistente
│ ├── index.faiss
│ └── index.pkl
│
├── streamlit_app.py # Punto de entrada de la UI
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Tecnologías utilizadas

### 🧠 LLM & Frameworks
- LangChain Core
- LangChain Community
- LangChain Google GenAI
- LangChain OpenAI
- LangChain Cohere

### 🔎 Embeddings & NLP
- HuggingFace Embeddings
- Sentence Transformers
- Transformers

### 📦 Vector Database
- FAISS (faiss-cpu)

### 📄 Document Processing
- PyPDF
- LangChain Text Splitters

### 🖥️ Frontend
- Streamlit

### 🔐 Configuración y Observabilidad
- Python-dotenv
- LangSmith

---

## 📊 Flujo del sistema

1. El usuario carga documentos PDF
2. Se limpian y normalizan los textos
3. Se agregan metadatos (categoría, ID, fuente)
4. Se dividen en chunks semánticos
5. Se generan embeddings
6. Se almacenan en FAISS
7. El usuario realiza una consulta
8. El sistema recupera contexto relevante
9. El LLM genera la respuesta
10. Se devuelven fuentes verificables

---

## 📌 Ejemplo de respuesta

```text
Respuesta:
La política de cancelación indica que ...

Fuentes:
- Política de Cancelaciones
  Categoría: politicas
  Página: 3
```

---


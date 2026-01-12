# Asistente Turístico de Tenerife (RAG) 🌴

Este proyecto implementa un sistema de **Retrieval Augmented Generation (RAG)** para actuar como un asistente turístico inteligente sobre la isla de Tenerife.

## Características
*   **Fuente de Datos**: Documento PDF `TENERIFE.pdf` (Guía oficial o información turística).
*   **Tecnología**: LangChain, OpenAI GPT, ChromaDB.
*   **Interfaz**: Notebook de Jupyter para prototipado y Scripts Python modulares.

## Instalación

1.  Crear entorno virtual:
    ```bash
    python -m venv llm-env
    .\llm-env\Scripts\activate
    ```
2.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Configurar `.env`:
    ```
    OPENAI_API_KEY=tu_clave_aqui
    ```

## Estructura
*   `data/`: Datos crudos (PDF).
*   `notebooks/`: Prototipado (Notebook Driven Development).
*   `src/`: Código fuente modular (Clean Code).

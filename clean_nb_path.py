import json
from pathlib import Path

notebook_path = Path("notebooks/main_demo.ipynb")

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# The clean content for the code cell (single valid path)
clean_code_source = [
    "import os\n",
    "import openai\n",
    "from openai import OpenAI\n",
    "from pathlib import Path\n",
    "\n",
    "# DEBUG: Verificar entorno\n",
    "print(f\"📂 CWD: {os.getcwd()}\")\n",
    "print(f\"📦 OpenAI Version: {openai.__version__}\")\n",
    "\n",
    "client = OpenAI()\n",
    "\n",
    "# Path corregido y validado\n",
    "pdf_path = Path(\"../data/raw/TENERIFE.pdf\")\n",
    "\n",
    "if not pdf_path.exists():\n",
    "    print(f\"❌ No encontrado: {pdf_path}\")\n",
    "else:\n",
    "    print(f\"✅ Archivo encontrado: {pdf_path}\")\n",
    "\n",
    "    # Crear Vector Store\n",
    "    try:\n",
    "        if not hasattr(client, 'beta'):\n",
    "            print(\"❌ La versión de OpenAI instalada no tiene acceso a 'beta'. Actualiza la librería.\")\n",
    "        else:\n",
    "            vector_store = client.beta.vector_stores.create(name=\"Tenerife Guide Store\")\n",
    "            print(f\"📦 Vector Store creado: {vector_store.id}\")\n",
    "            \n",
    "            # Subir archivos\n",
    "            with open(pdf_path, \"rb\") as f:\n",
    "                file_batch = client.beta.vector_stores.file_batches.upload_and_poll(\n",
    "                    vector_store_id=vector_store.id, files=[f]\n",
    "                )\n",
    "            print(f\"📄 Estado de carga: {file_batch.status}\")\n",
    "            print(f\"🔢 Archivos procesados: {file_batch.file_counts}\")\n",
    "    except Exception as e:\n",
    "        print(f\"❌ Error Critical: {e}\")"
]

# Find and update
found = False
for i, cell in enumerate(nb["cells"]):
    source_text = "".join(cell.get("source", []))
    # Identify the cell by its unique components
    if "vector_stores.create" in source_text and "Path" in source_text:
        if cell["cell_type"] == "code":
            nb["cells"][i]["source"] = clean_code_source
            found = True
            break

if found:
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Notebook path logic cleaned.")
else:
    print("Target cell not found for cleaning.")

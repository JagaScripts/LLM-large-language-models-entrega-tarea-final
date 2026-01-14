# Plan de Mejoras y Extras (Roadmap)

Este documento detalla los siguientes pasos para abordar los **Extras/Bonus** identificados en el enunciado de la práctica (Fase 5: Experimentación), así como mejoras futuras propuestas.

## 1. Extras Asignados (Priority: High)
Estos puntos corresponden a la "Fase 5: Experimentación" descrita en las instrucciones originales y son el siguiente paso lógico.

### 🧪 Experimento A: Estrategias de Chunking
**Objetivo**: Validar si cambiar el tamaño del chunk mejora la recuperación.
- [ ] **Acción**: Parametrizar `chunk_size` en la función de ingesta.
- [ ] **Prueba**: Crear 3 Vector Stores distintos:
    - `Small` (256 tokens)
    - `Medium` (1000 tokens) - *Actual*
    - `Large` (4096 tokens)
- [ ] **Medición**: Ejecutar el Dataset de Evaluación contra cada uno y comparar `ctx_precision`.

### 📉 Experimento B: Análisis de Casos Límite ("Best/Worst")
**Objetivo**: Entender dónde falla el modelo.
- [ ] **Acción**: Automatizar la extracción de las 3 peores respuestas (Lowest Scores) del `eval_results.csv`.
- [ ] **Análisis**: Usar el Agente Juez para generar una "Autopsia" de por qué fallaron (ej: falta de contexto, alucinación, ambigüedad).

## 2. Extras Técnicos (Corto Plazo)
- [ ] **Soporte Multi-PDF**: Modificar la Fase 2 para iterar sobre una carpeta `data/raw/*.pdf` e ingestar múltiples guías (ej: Senderismo, Gastronomía, Transporte).
- [ ] **UI con Streamlit**: Sacar el agente del Notebook y crear una interfaz web de chat real usando `streamlit` o `gradio`.
- [ ] **Guardrails Avanzados**: Implementar filtros de seguridad más estrictos para evitar que el agente hable de temas no turísticos (ej: política).

## 3. Mejoras de Negocio (Medio Plazo)
- [ ] **Herramienta de Reservas**: Integrar una nueva `function_tool` que permita "simular" una reserva de hotel o excursión, devolviendo un ticket JSON.
- [ ] **Personalización**: Añadir una "memoria de sesión" para que el agente recuerde el nombre del usuario y sus preferencias (ej: "Me gusta el senderismo") a lo largo de la conversación.

## 4. Analítica Avanzada (Largo Plazo)
- [ ] **Dashboard de Métricas**: Usar los CSV generados para pintar gráficas de evolución de calidad.
- [ ] **Feedbak Loop**: Permitir al usuario votar respuestas para re-entrenar o ajustar prompts.

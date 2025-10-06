import streamlit as st
import requests
import json

# URL del archivo JSON en GitHub RAW
URL_JSON = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPOSITORIO/main/preguntas.json"

@st.cache_data
def cargar_preguntas():
    response = requests.get(URL_JSON)
    return response.json()

preguntas = cargar_preguntas()

st.set_page_config(page_title="Quiz de Atención y Videos Cortos", layout="centered")

st.title("📱 Atención Sostenida y Videos Cortos - Quiz Interactivo")

# Estado persistente
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.mostrando_feedback = False
    st.session_state.correcta = None

indice = st.session_state.indice

# Fin del cuestionario
if indice >= len(preguntas):
    st.success(f"✅ Has completado el quiz. Puntaje final: {st.session_state.puntaje} / {len(preguntas)}")
    st.balloons()
    if st.button("🔄 Reiniciar"):
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.mostrando_feedback = False
        st.session_state.correcta = None
    st.stop()

# Mostrar la pregunta actual
pregunta_actual = preguntas[indice]
st.subheader(f"Pregunta {indice + 1}")
st.write(pregunta_actual["pregunta"])

# Mostrar opciones
opcion_elegida = st.radio("Selecciona una opción:", options=pregunta_actual["opciones"], index=None)

# Botón de enviar
if st.button("Responder") and opcion_elegida is not None:
    correcta = pregunta_actual["opciones"][pregunta_actual["respuesta_correcta"]]
    if opcion_elegida == correcta:
        st.session_state.puntaje += 1
        st.session_state.correcta = True
        st.success("✅ ¡Respuesta correcta!")
    else:
        st.session_state.correcta = False
        st.error(f"❌ Respuesta incorrecta.")
    
    st.info(f"💡 Explicación: {pregunta_actual['explicacion']}")
    st.session_state.mostrando_feedback = True

# Botón para continuar si se mostró feedback
if st.session_state.mostrando_feedback:
    if st.button("Siguiente"):
        st.session_state.indice += 1
        st.session_state.mostrando_feedback = False
        st.session_state.correcta = None

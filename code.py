import streamlit as st

# Lista con las preguntas, opciones, respuestas correctas y explicación
questions = [
    {
        "pregunta": "¿Cuál es una característica clave de los videos cortos en plataformas como TikTok o Instagram Reels?",
        "opciones": [
            "Duración mayor a 10 minutos",
            "Enfoque en contenido educativo largo",
            "Contenido rápido y altamente visual",
            "Transmisiones en vivo de larga duración"
        ],
        "respuesta_correcta": "Contenido rápido y altamente visual",
        "explicacion": "Los videos cortos se caracterizan por ser rápidos, visualmente atractivos y diseñados para captar la atención en pocos segundos."
    },
    {
        "pregunta": "¿Qué efecto puede tener el consumo frecuente de videos cortos en la atención sostenida?",
        "opciones": [
            "Mejora la capacidad de concentración prolongada",
            "No tiene ningún efecto",
            "Puede reducir la capacidad de mantener la atención por largos periodos",
            "Aumenta el interés por leer libros largos"
        ],
        "respuesta_correcta": "Puede reducir la capacidad de mantener la atención por largos periodos",
        "explicacion": "Ver videos cortos constantemente puede afectar negativamente la atención sostenida, ya que el cerebro se acostumbra a estímulos rápidos y constantes."
    },
    {
        "pregunta": "¿Qué mecanismo cerebral se activa frecuentemente al consumir videos cortos con recompensas rápidas?",
        "opciones": [
            "Lóbulo parietal",
            "Corteza visual primaria",
            "Sistema de recompensa dopaminérgico",
            "Cerebelo"
        ],
        "respuesta_correcta": "Sistema de recompensa dopaminérgico",
        "explicacion": "Este sistema libera dopamina cuando se experimenta placer o gratificación, lo cual se activa con la dinámica de recompensas instantáneas de los videos cortos."
    },
    {
        "pregunta": "¿Por qué los algoritmos de plataformas como TikTok promueven videos muy breves?",
        "opciones": [
            "Mantienen al usuario más tiempo en la app",
            "Fomentan la lectura de contenido educativo",
            "Requieren menos espacio de almacenamiento",
            "Cumplen regulaciones de contenido"
        ],
        "respuesta_correcta": "Mantienen al usuario más tiempo en la app",
        "explicacion": "Los videos cortos son altamente adictivos y permiten que los usuarios consuman muchos en poco tiempo, lo que aumenta el tiempo de permanencia en la plataforma."
    },
    {
        "pregunta": "¿Cuál de los siguientes grupos es más vulnerable a la disminución de la atención sostenida por videos cortos?",
        "opciones": [
            "Adultos mayores",
            "Personas con altos niveles de lectura",
            "Niños y adolescentes",
            "Personas mayores de 50 años"
        ],
        "respuesta_correcta": "Niños y adolescentes",
        "explicacion": "El cerebro de niños y adolescentes está en desarrollo, por lo que es más sensible a los efectos de consumo excesivo de contenidos breves y rápidos."
    },
    {
        "pregunta": "¿Cuál de estos es un posible efecto de ver muchos videos cortos en el rendimiento académico?",
        "opciones": [
            "Mejora la retención de información",
            "Disminuye la capacidad de concentración en tareas largas",
            "Aumenta el deseo de estudiar",
            "Mejora la velocidad de lectura"
        ],
        "respuesta_correcta": "Disminuye la capacidad de concentración en tareas largas",
        "explicacion": "El consumo excesivo de videos cortos puede dificultar que el estudiante se enfoque en actividades que requieren atención prolongada, como estudiar o leer."
    },
    {
        "pregunta": "¿Qué tipo de contenido puede ayudar a contrarrestar los efectos negativos de los videos cortos en la atención sostenida?",
        "opciones": [
            "Videos virales",
            "Lectura prolongada y práctica de mindfulness",
            "Series con múltiples episodios",
            "Podcasts cortos de entretenimiento"
        ],
        "respuesta_correcta": "Lectura prolongada y práctica de mindfulness",
        "explicacion": "La lectura y el mindfulness fomentan la atención plena y sostenida, contrarrestando los efectos de la estimulación constante de los videos cortos."
    },
    {
        "pregunta": "¿Qué diferencia clave hay entre los videos cortos y los videos educativos largos en términos de impacto cognitivo?",
        "opciones": [
            "Los videos largos tienen peor calidad de imagen",
            "Los videos cortos son menos entretenidos",
            "Los videos largos promueven una mayor concentración y comprensión",
            "Los videos cortos mejoran la capacidad de análisis"
        ],
        "respuesta_correcta": "Los videos largos promueven una mayor concentración y comprensión",
        "explicacion": "Los videos más largos requieren mayor enfoque y procesan ideas más complejas, lo que puede beneficiar la atención sostenida y la comprensión."
    },
    {
        "pregunta": "¿Cuál de los siguientes hábitos puede ayudar a reducir la dependencia de videos cortos?",
        "opciones": [
            "Establecer tiempos limitados de uso en redes sociales",
            "Usar varias redes sociales al mismo tiempo",
            "Ver más videos cortos antes de dormir",
            "Activar notificaciones constantes"
        ],
        "respuesta_correcta": "Establecer tiempos limitados de uso en redes sociales",
        "explicacion": "Limitar el tiempo de uso permite reducir la exposición y recuperar hábitos de atención más prolongada."
    },
    {
        "pregunta": "¿Qué pueden hacer los padres para ayudar a sus hijos a manejar el consumo de videos cortos?",
        "opciones": [
            "Recompensarlos con más tiempo en pantalla",
            "Establecer reglas claras y fomentar actividades alternativas",
            "Permitirles ver cualquier contenido sin supervisión",
            "Ignorar el tema para evitar discusiones"
        ],
        "respuesta_correcta": "Establecer reglas claras y fomentar actividades alternativas",
        "explicacion": "Es importante establecer límites y promover actividades que fomenten la concentración, como la lectura, el juego al aire libre o la conversación."
    }
]

def main():
    st.title("Trivia sobre Videos Cortos y Atención Sostenida")

    if "index" not in st.session_state:
        st.session_state.index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""

    question = questions[st.session_state.index]

    st.write(f"**Pregunta {st.session_state.index + 1} de {len(questions)}:**")
    st.write(question["pregunta"])

    if not st.session_state.answered:
        choice = st.radio("Selecciona una respuesta:", question["opciones"])
        if st.button("Enviar respuesta"):
            st.session_state.answered = True
            if choice == question["respuesta_correcta"]:
                st.session_state.score += 1
                st.session_state.feedback = f"✅ Correcto! {question['explicacion']}"
            else:
                st.session_state.feedback = f"❌ Incorrecto. {question['explicacion']}"
    else:
        st.write(st.session_state.feedback)
        if st.session_state.index < len(questions) - 1:
            if st.button("Siguiente pregunta"):
                st.session_state.index += 1
                st.session_state.answered = False
                st.session_state.feedback = ""
        else:
            st.write("### ¡Has terminado la trivia!")
            st.write(f"Tu puntaje final es {st.session_state.score} de {len(questions)}")
            if st.button("Reiniciar Trivia"):
                st.session_state.index = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.session_state.feedback = ""

if __name__ == "__main__":
    main()

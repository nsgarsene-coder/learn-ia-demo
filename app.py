import streamlit as st
import time
import random
# --- just the test ---
# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="LearnIA - Apprentissage Adaptatif", page_icon="🧠", layout="wide")

# --- SIMULATION BACKEND (Pas de vraie BDD pour la démo rapide) ---
if 'xp' not in st.session_state:
    st.session_state.xp = 120
if 'level' not in st.session_state:
    st.session_state.level = 3

# --- FONCTIONS SIMULANT L'IA ---
def analyze_course(text, style):
    """Simule l'IA qui analyse et résume"""
    time.sleep(2) # On fait semblant de réfléchir
    summary = f"RESUMÉ GÉNÉRÉ ({style}): \n\nCe cours traite des concepts fondamentaux suivants... " \
              f"L'idée principale est que {text[:50]}... En conclusion, il faut retenir que l'approche {style} " \
              "permet de mieux visualiser ces données complexe."
    return summary

def generate_quiz():
    return [
        {"q": "Quel est le concept clé ?", "options": ["Option A", "Option B", "Option C"], "answer": "Option A"},
        {"q": "Pourquoi cette méthode ?", "options": ["Raison X", "Raison Y", "Raison Z"], "answer": "Raison Y"}
    ]

# --- INTERFACE UTILISATEUR (SIDEBAR) ---
st.sidebar.title("👤 Profil Apprenant")
name = st.sidebar.text_input("Ton Prénom", "Thomas")
style = st.sidebar.selectbox("Ton style d'apprentissage", ["Visuel (Schémas)", "Auditif (Podcast)", "Kinesthésique (Pratique)"])
mode = st.sidebar.radio("Mode", ["Révision Express", "Apprentissage Profond"])

st.sidebar.markdown("---")
st.sidebar.metric(label="Niveau", value=f"Lvl {st.session_state.level}")
st.sidebar.progress(st.session_state.xp % 100)
st.sidebar.caption(f"XP Total: {st.session_state.xp}")

# --- PAGE PRINCIPALE ---
st.title("🧠 LearnIA")
st.markdown(f"Bonjour **{name}** ! Prêt à transformer tes cours ?")

# ÉTAPE 1 : INGESTION
st.header("1. Importe ton cours")
course_input = st.text_area("Colle ton cours ici (ou le texte de tes notes)", height=150, placeholder="La photosynthèse est le processus par lequel...")
uploaded_file = st.file_uploader("Ou upload une image/PDF", type=['png', 'jpg', 'pdf'])

if st.button("🚀 Lancer la Transformation IA"):
    if course_input:
        with st.spinner('Analyse sémantique en cours...'):
            # Simulation de l'IA
            summary = analyze_course(course_input, style)
            st.success("Transformation terminée !")
            
            # ÉTAPE 2 : RÉSULTAT ADAPTATIF
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📄 Résumé Structuré")
                st.info(summary)
                if style == "Visuel (Schémas)":
                    st.image("https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=1000&auto=format&fit=crop", caption="MindMap Générée par IA")
                elif style == "Auditif (Podcast)":
                    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format='audio/mp3')
                    st.caption("Podcast généré : 'Le Prof Cool'")
            
            with col2:
                st.subheader("🎮 Quiz de validation")
                quiz = generate_quiz()
                for i, q in enumerate(quiz):
                    st.write(f"**Question {i+1}:** {q['q']}")
                    user_rep = st.radio(f"Choix {i+1}", q['options'], key=i)
                
                if st.button("Valider le Quiz"):
                    st.balloons()
                    st.session_state.xp += 50
                    st.success("Bravo ! +50 XP gagnés !")

            # ÉTAPE 3 : FEEDBACK ORAL
            st.markdown("---")
            st.subheader("🎤 Mode Professeur (Feedback)")
            st.write("Explique ce que tu as compris à l'oral, l'IA va te corriger.")
            if st.button("🎙️ Enregistrer ma réponse"):
                with st.spinner("Écoute en cours..."):
                    time.sleep(2)
                    st.warning("IA : 'C'est pas mal ! Tu as bien compris le début, mais tu as oublié de préciser le contexte historique.'")
                    st.metric("Ta note", "7/10")

    else:
        st.error("Merci d'entrer du texte pour commencer.")

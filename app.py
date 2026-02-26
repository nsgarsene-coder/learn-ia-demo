import streamlit as st
import time
import random
import sys
from pathlib import Path

# --- CONFIGURATION DU DESIGN ---
sys.path.insert(0, str(Path(__file__).parent / "styles"))
try:
    from learnia_dynamic_colors import initialize_dark_theme, apply_dynamic_theme
except ImportError:
    def apply_dynamic_theme(mode): pass

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="LearnIA - Apprentissage Adaptatif", page_icon="asset_s/icons8-cerveau-64.png", layout="wide")

# --- INJECTION CSS ---
try:
    with open("styles/learnia_custom_styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# --- SIMULATION BACKEND ---
if 'xp' not in st.session_state:
    st.session_state.xp = 120
if 'level' not in st.session_state:
    st.session_state.level = 3

# --- FONCTIONS SIMULANT L'IA ---
def analyze_course(text, style):
    time.sleep(2)
    summary = f"RESUME GENERE ({style}): \n\nCe cours traite des concepts fondamentaux suivants... " \
              f"L'idee principale est que {text[:50]}... En conclusion, il faut retenir que l'approche {style} " \
              "permet de mieux visualiser ces donnees complexe."
    return summary

def generate_quiz(text):
    # Quiz dynamique base sur le contenu
    if "Soleil" in text or "planete" in text:
        return [
            {"q": "Quelle planete possede des anneaux spectaculaires ?", "options": ["Mars", "Saturne", "Jupiter"], "answer": "Saturne"},
            {"q": "Quel pourcentage de la masse du systeme le Soleil contient-il ?", "options": ["50%", "75%", "99,8%"], "answer": "99,8%"}
        ]
    return [
        {"q": "Quel est le concept cle ?", "options": ["Option A", "Option B", "Option C"], "answer": "Option A"},
        {"q": "Pourquoi cette methode ?", "options": ["Raison X", "Raison Y", "Raison Z"], "answer": "Raison Y"}
    ]

# --- INTERFACE UTILISATEUR (SIDEBAR) ---
st.sidebar.image("asset_s/icons8-étudiant-femme-50.png", width=60)
st.sidebar.title("Profil Apprenant")
name = st.sidebar.text_input("Ton Prenom", "Thomas")
style = st.sidebar.selectbox("Ton style d'apprentissage", ["Visuel (Schemas)", "Auditif (Podcast)", "Kinesthesique (Pratique)"])

mode_options = ["Revision Express", "Apprentissage Profond"]
mode_selection = st.sidebar.radio("Mode", mode_options)
mode_key = "revision_express" if mode_selection == "Revision Express" else "apprentissage_profond"

apply_dynamic_theme(mode_key)

st.sidebar.markdown("---")
st.sidebar.metric(label="Niveau", value=f"Lvl {st.session_state.level}")
st.sidebar.progress(st.session_state.xp % 100)
st.sidebar.caption(f"XP Total: {st.session_state.xp}")

# --- PAGE PRINCIPALE ---
st.image("asset_s/icons8-cerveau-64.png", width=80)
st.title("LearnIA")
st.markdown(f"Bonjour **{name}** ! Pret a transformer tes cours ?")

# ETAPE 1 : INGESTION
st.header("1. Importe ton cours")
course_input = st.text_area("Colle ton cours ici (ou le texte de tes notes)", height=150, placeholder="La photosynthese est le processus par lequel...")
uploaded_file = st.file_uploader("Ou upload une image/PDF", type=['png', 'jpg', 'pdf'])

rocket_slot = st.empty()

if st.button("Lancer la Transformation IA"):
    if course_input:
        rocket_slot.image("asset_s/icons8-fusée.gif", width=100)
        
        with st.spinner('Analyse semantique en cours...'):
            summary = analyze_course(course_input, style)
            st.session_state.current_summary = summary
            st.session_state.current_quiz = generate_quiz(course_input)
            st.session_state.transformed = True
            st.success("Transformation terminee !")
        
        rocket_slot.empty()

if st.session_state.get('transformed'):
    # --- ETAPE 2 : RESULTAT ADAPTATIF ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Resume Structure")
        st.info(st.session_state.current_summary)
        if style == "Visuel (Schemas)":
            st.image("https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=1000&auto=format&fit=crop", caption="MindMap Generee par IA")
        elif style == "Auditif (Podcast)":
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format='audio/mp3')
            st.caption("Podcast genere : 'Le Prof Cool'")

    with col2:
        st.subheader("Quiz de validation")
        quiz = st.session_state.current_quiz
        for i, q in enumerate(quiz):
            st.write(f"**Question {i+1}:** {q['q']}")
            st.radio(f"Choix pour Q{i+1}", q['options'], key=f"quiz_{i}")

        if st.button("Valider le Quiz"):
            st.balloons()
            st.session_state.xp += 50
            st.success("Bravo ! +50 XP gagnes !")

    # --- ETAPE 3 : FEEDBACK ORAL ---
    st.markdown("---")
    st.subheader("Mode Professeur (Feedback)")
    st.write("Explique ce que tu as compris a l'oral, l'IA va te corriger.")
    if st.button("Enregistrer ma reponse"):
        with st.spinner("Ecoute en cours..."):
            time.sleep(2)
            st.warning("IA : 'C'est pas mal ! Tu as bien compris le debut, mais tu as oublie de preciser le contexte historique.'")
            st.metric("Ta note", "7/10")
elif not course_input and st.session_state.get('transformed') is None:
    pass

"""
LearnIA - Dynamic Color System Implementation
Système de couleurs dynamiques pour Streamlit

Ce module gère l'application des couleurs dynamiques en fonction du mode
d'apprentissage sélectionné par l'utilisateur.
"""

import streamlit as st
from typing import Dict, Tuple



COLOR_PALETTES = {
    "revision_express": {
        "primary": "#007BFF",      # Bleu Vif
        "primary_dark": "#0056b3",
        "primary_light": "#0084FF",
        "secondary": "#FFC107",    # Jaune/Ambre
        "name": "Révision Express"
    },
    "apprentissage_profond": {
        "primary": "#6F42C1",      # Violet Énergique
        "primary_dark": "#5a32a3",
        "primary_light": "#7d5dd1",
        "secondary": "#FFC107",    # Jaune/Ambre
        "name": "Apprentissage Profond"
    }
}

# Couleurs de base (Thème Sombre)
BASE_COLORS = {
    "bg_primary": "#121212",
    "bg_secondary": "#1E1E1E",
    "bg_tertiary": "#252525",
    "text_primary": "#E0E0E0",
    "text_secondary": "#B0B0B0",
    "text_tertiary": "#808080",
    "border": "#333333",
}



def generate_dynamic_css(mode: str) -> str:
    """
    Génère le CSS dynamique en fonction du mode d'apprentissage sélectionné.
    
    Args:
        mode: Le mode d'apprentissage ('revision_express' ou 'apprentissage_profond')
    
    Returns:
        Une chaîne CSS contenant les variables de couleurs mises à jour.
    """
    palette = COLOR_PALETTES.get(mode, COLOR_PALETTES["revision_express"])
    
    css = f"""
    <style>
    :root {{
        /* Couleurs de Base (Thème Sombre) */
        --bg-primary: {BASE_COLORS['bg_primary']};
        --bg-secondary: {BASE_COLORS['bg_secondary']};
        --bg-tertiary: {BASE_COLORS['bg_tertiary']};
        
        /* Texte */
        --text-primary: {BASE_COLORS['text_primary']};
        --text-secondary: {BASE_COLORS['text_secondary']};
        --text-tertiary: {BASE_COLORS['text_tertiary']};
        
        /* Couleurs d'Accentuation (Dynamiques) */
        --color-primary: {palette['primary']};
        --color-primary-dark: {palette['primary_dark']};
        --color-primary-light: {palette['primary_light']};
        --color-secondary: {palette['secondary']};
        
        /* Bordures et Ombres */
        --border-color: {BASE_COLORS['border']};
        --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.3);
        --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.4);
        --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.5);
        
        /* Espacements */
        --spacing-xs: 4px;
        --spacing-sm: 8px;
        --spacing-md: 16px;
        --spacing-lg: 24px;
        --spacing-xl: 32px;
        
        /* Typographie */
        --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        --font-size-base: 16px;
        --font-size-sm: 14px;
        --font-size-lg: 18px;
        --font-size-xl: 24px;
        --font-size-2xl: 32px;
        
        /* Transitions */
        --transition-fast: 150ms ease-in-out;
        --transition-normal: 300ms ease-in-out;
    }}
    
    /* Thème Sombre - Éléments Globaux */
    body {{
        background-color: var(--bg-primary);
        color: var(--text-primary);
        font-family: var(--font-family);
        font-size: var(--font-size-base);
        line-height: 1.6;
    }}
    
    .stApp {{
        background-color: var(--bg-primary);
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: var(--bg-secondary);
        border-right: 1px solid var(--border-color);
    }}
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
        background-color: var(--bg-secondary);
    }}
    
    /* Cartes */
    .profile-card,
    .mode-card,
    .level-card {{
        background-color: var(--bg-tertiary);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: var(--spacing-md);
        margin-bottom: var(--spacing-md);
        box-shadow: var(--shadow-sm);
        transition: all var(--transition-normal);
    }}
    
    .profile-card:hover,
    .mode-card:hover,
    .level-card:hover {{
        background-color: #2A2A2A;
        box-shadow: var(--shadow-md);
    }}
    
    /* Titre de la Carte */
    .card-title {{
        font-size: var(--font-size-lg);
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: var(--spacing-sm);
        display: flex;
        align-items: center;
        gap: var(--spacing-sm);
    }}
    
    .card-title::before {{
        content: '';
        width: 4px;
        height: 20px;
        background-color: var(--color-primary);
        border-radius: 2px;
    }}
    
    /* Boutons */
    button,
    .stButton > button {{
        background-color: var(--color-primary) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        padding: var(--spacing-md) var(--spacing-lg) !important;
        font-size: var(--font-size-base) !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all var(--transition-fast) !important;
        box-shadow: var(--shadow-sm) !important;
    }}
    
    button:hover,
    .stButton > button:hover {{
        background-color: var(--color-primary-dark) !important;
        box-shadow: var(--shadow-md) !important;
        transform: translateY(-2px) !important;
    }}
    
    button:active,
    .stButton > button:active {{
        transform: translateY(0) !important;
        box-shadow: var(--shadow-sm) !important;
    }}
    
    /* Champs de Saisie */
    textarea,
    input[type="text"],
    input[type="email"],
    input[type="password"],
    select {{
        background-color: var(--bg-tertiary) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
        padding: var(--spacing-md) !important;
        font-family: var(--font-family) !important;
        font-size: var(--font-size-base) !important;
        transition: all var(--transition-fast) !important;
    }}
    
    textarea:focus,
    input[type="text"]:focus,
    input[type="email"]:focus,
    input[type="password"]:focus,
    select:focus {{
        outline: none !important;
        border-color: var(--color-primary) !important;
        box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1) !important;
    }}
    
    /* Barre de Progression */
    .xp-progress-fill {{
        background: linear-gradient(90deg, var(--color-secondary), #FFD700) !important;
    }}
    
    /* Niveau */
    .level-display {{
        color: var(--color-secondary) !important;
    }}
    
    /* Contenu Principal */
    [data-testid="stMainBlockContainer"] {{
        background-color: var(--bg-primary);
        padding: var(--spacing-xl);
    }}
    
    /* Titres */
    h1 {{
        color: var(--text-primary) !important;
        font-size: var(--font-size-2xl) !important;
        font-weight: 700 !important;
    }}
    
    h2 {{
        color: var(--text-primary) !important;
        font-size: var(--font-size-xl) !important;
        font-weight: 600 !important;
    }}
    
    h3 {{
        color: var(--text-secondary) !important;
        font-size: var(--font-size-lg) !important;
        font-weight: 600 !important;
    }}
    
    /* Paragraphes */
    p {{
        color: var(--text-secondary) !important;
    }}
    
    /* Radio Buttons */
    input[type="radio"] {{
        accent-color: var(--color-primary) !important;
    }}
    
    /* Scrollbar */
    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: var(--bg-secondary);
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: var(--color-primary);
        border-radius: 4px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: var(--color-primary-dark);
    }}
    </style>
    """
    
    return css


def apply_dynamic_theme(mode: str) -> None:
    """
    Applique le thème dynamique en fonction du mode sélectionné.
    
    Args:
        mode: Le mode d'apprentissage ('revision_express' ou 'apprentissage_profond')
    """
    css = generate_dynamic_css(mode)
    st.markdown(css, unsafe_allow_html=True)



def get_palette_colors(mode: str) -> Dict[str, str]:
    """
    Retourne la palette de couleurs pour le mode spécifié.
    
    Args:
        mode: Le mode d'apprentissage
    
    Returns:
        Un dictionnaire contenant les couleurs de la palette
    """
    return COLOR_PALETTES.get(mode, COLOR_PALETTES["revision_express"])


def initialize_dark_theme() -> None:
    """
    Initialise le thème sombre de base pour Streamlit.
    """
    st.set_page_config(
        page_title="LearnIA - Apprentissage Adaptatif",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
        theme={
            "primaryColor": "#007BFF",
            "backgroundColor": "#121212",
            "secondaryBackgroundColor": "#1E1E1E",
            "textColor": "#E0E0E0",
            "font": "sans serif"
        }
    )


if __name__ == "__main__":
    # Initialiser le thème
    initialize_dark_theme()
    
    # Simuler la sélection du mode
    mode = st.radio("Choisissez votre mode d'apprentissage:", 
                    options=["revision_express", "apprentissage_profond"],
                    format_func=lambda x: COLOR_PALETTES[x]["name"])
    
    # Appliquer le thème dynamique
    apply_dynamic_theme(mode)
    
    # Afficher les couleurs actuelles
    st.write(f"**Mode actuel:** {COLOR_PALETTES[mode]['name']}")
    st.write(f"**Couleur primaire:** {COLOR_PALETTES[mode]['primary']}")

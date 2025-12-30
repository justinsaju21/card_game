"""
CSS styles for the card selector application.
Clean professional theming with gradients, shadows, and animations.
"""

import uuid
import time

def get_card_styles() -> str:
    """Return CSS styles for card display - PROFESSIONAL EDITION."""
    return """
    <style>
    /* Import Google Fonts - Clean & Professional */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;500;600&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main container styling - Professional dark gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-attachment: fixed;
    }
    
    /* Card container */
    .card-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 30px;
        perspective: 1000px;
    }
    
    /* Card styling - Clean Professional */
    .game-card {
        width: 280px;
        height: 400px;
        background: linear-gradient(145deg, #1e1e2e 0%, #2d2d44 50%, #1a1a2e 100%);
        border-radius: 20px;
        box-shadow: 
            0 25px 60px rgba(0, 0, 0, 0.4),
            0 0 40px rgba(99, 102, 241, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Poppins', sans-serif;
        color: #e0e0e0;
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(99, 102, 241, 0.3);
        animation: cardAppear 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .game-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 
            0 35px 80px rgba(0, 0, 0, 0.5),
            0 0 60px rgba(99, 102, 241, 0.25);
    }
    
    /* Subtle glow accent */
    .game-card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #6366f1, #8b5cf6, #06b6d4, #6366f1);
        border-radius: 22px;
        z-index: -1;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .game-card:hover::before {
        opacity: 0.5;
        animation: borderGlow 3s linear infinite;
    }
    
    @keyframes borderGlow {
        0%, 100% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(30deg); }
    }
    
    /* Card content */
    .card-content {
        z-index: 10;
        text-align: center;
        padding: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    
    .card-name {
        font-size: 1.5rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #ffffff;
        text-shadow: 0 2px 10px rgba(99, 102, 241, 0.5);
        background: linear-gradient(180deg, #ffffff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        text-align: center;
        line-height: 1.4;
        word-wrap: break-word;
    }
    
    /* Card decoration lines */
    .card-decoration {
        position: absolute;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }
    
    .card-decoration::before,
    .card-decoration::after {
        content: '';
        position: absolute;
        background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
        height: 1px;
        width: 60%;
        left: 20%;
    }
    
    .card-decoration::before { top: 40px; }
    .card-decoration::after { bottom: 40px; }
    
    /* Card back (placeholder) */
    .card-back {
        width: 280px;
        height: 400px;
        background: linear-gradient(145deg, #1e1e2e 0%, #2d2d44 100%);
        border-radius: 20px;
        box-shadow: 
            0 20px 60px rgba(0, 0, 0, 0.4),
            inset 0 0 80px rgba(99, 102, 241, 0.05);
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid rgba(99, 102, 241, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .card-back-pattern {
        position: absolute;
        width: 100%;
        height: 100%;
        background: 
            repeating-linear-gradient(
                45deg,
                transparent,
                transparent 10px,
                rgba(99, 102, 241, 0.03) 10px,
                rgba(99, 102, 241, 0.03) 20px
            );
        opacity: 0.8;
    }
    
    .card-back-symbol {
        font-size: 4rem;
        color: rgba(99, 102, 241, 0.3);
        z-index: 1;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.1); }
    }
    
    @keyframes cardAppear {
        0% { 
            opacity: 0; 
            transform: translateY(60px) rotateX(-20deg) scale(0.9); 
        }
        100% { 
            opacity: 1; 
            transform: translateY(0) rotateX(0deg) scale(1); 
        }
    }
    
    /* Discard animation */
    @keyframes discardCard {
        0% { 
            opacity: 1; 
            transform: translateX(0) rotateZ(0deg) scale(1); 
        }
        100% { 
            opacity: 0; 
            transform: translateX(400px) translateY(-50px) rotateZ(30deg) scale(0.5); 
        }
    }
    
    .discarding {
        animation: discardCard 0.5s ease-in forwards !important;
    }
    
    /* Counter styling */
    .deck-counter {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.2));
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 16px;
        padding: 20px 30px;
        text-align: center;
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .counter-number {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(180deg, #6366f1 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .counter-label {
        font-size: 0.85rem;
        color: rgba(255, 255, 255, 0.6);
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 5px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 32px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.5) !important;
    }

    .stButton > button:disabled {
        background: rgba(255, 255, 255, 0.1) !important;
        color: rgba(255, 255, 255, 0.3) !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }
    
    /* Title styling */
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #a5b4fc 50%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 5px;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        text-align: center;
        color: rgba(255, 255, 255, 0.5);
        margin-bottom: 30px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    
    /* Discard pile styling */
    .discard-pile {
        background: rgba(30, 30, 46, 0.8);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(99, 102, 241, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .discard-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 15px;
    }
    
    .discard-item {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.6);
        padding: 10px 14px;
        margin: 6px 0;
        background: rgba(99, 102, 241, 0.1);
        border-radius: 8px;
        border-left: 3px solid #6366f1;
        animation: slideIn 0.3s ease-out;
    }
    
    @keyframes slideIn {
        0% { opacity: 0; transform: translateX(-20px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    
    /* File uploader styling */
    .stFileUploader {
        background: rgba(30, 30, 46, 0.5) !important;
        border-radius: 12px !important;
        border: 2px dashed rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        background: rgba(30, 30, 46, 0.8) !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
        border-radius: 12px !important;
        color: #e0e0e0 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1e2e 0%, #0f0c29 100%);
        border-right: 1px solid rgba(99, 102, 241, 0.2);
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: #e0e0e0;
    }
    
    section[data-testid="stSidebar"] h2 {
        font-family: 'Poppins', sans-serif !important;
        color: #a5b4fc !important;
    }
    </style>
    """


def render_card(card_name: str) -> str:
    """Render HTML for a face-up card with the given name."""
    card_id = f"card-{uuid.uuid4()}"
    timestamp = int(time.time() * 1000)
    
    return f"""
    <div id="{card_id}" class="card-container" data-timestamp="{timestamp}">
        <div class="game-card" style="animation: cardAppear 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;">
            <div class="card-decoration"></div>
            <div class="card-content">
                <div class="card-name">{card_name}</div>
            </div>
        </div>
    </div>
    <script>
        (function() {{
            var card = document.getElementById('{card_id}');
            if (card) {{
                var gameCard = card.querySelector('.game-card');
                if (gameCard) {{
                    gameCard.style.animation = 'none';
                    gameCard.offsetHeight;
                    gameCard.style.animation = 'cardAppear 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) forwards';
                }}
            }}
        }})();
    </script>
    """


def render_card_discarding(card_name: str) -> str:
    """Render HTML for a card being discarded with animation."""
    card_id = f"card-{uuid.uuid4()}"
    timestamp = int(time.time() * 1000)
    
    return f"""
    <div id="{card_id}" class="card-container" data-timestamp="{timestamp}">
        <div class="game-card discarding">
            <div class="card-decoration"></div>
            <div class="card-content">
                <div class="card-name">{card_name}</div>
            </div>
        </div>
    </div>
    <script>
        (function() {{
            var card = document.getElementById('{card_id}');
            if (card) {{
                var gameCard = card.querySelector('.game-card');
                if (gameCard) {{
                    gameCard.style.animation = 'none';
                    gameCard.offsetHeight;
                    gameCard.style.animation = 'discardCard 0.5s ease-in forwards';
                }}
            }}
        }})();
    </script>
    """


def render_card_back() -> str:
    """Render HTML for a card back (placeholder when no card selected)."""
    return """
    <div class="card-container">
        <div class="card-back">
            <div class="card-back-pattern"></div>
            <div class="card-back-symbol">?</div>
        </div>
    </div>
    """


def render_discard_item(card_name: str) -> str:
    """Render HTML for a discard pile item with animation."""
    item_id = f"discard-{uuid.uuid4()}"
    return f"""
    <div id="{item_id}" class="discard-item" style="animation: slideIn 0.3s ease-out forwards;">
        {card_name}
    </div>
    <script>
        (function() {{
            var item = document.getElementById('{item_id}');
            if (item) {{
                item.style.animation = 'none';
                item.offsetHeight;
                item.style.animation = 'slideIn 0.3s ease-out forwards';
            }}
        }})();
    </script>
    """


def render_deck_counter(remaining: int, total: int) -> str:
    """Render HTML for the deck counter."""
    return f"""
    <div class="deck-counter">
        <div class="counter-number">{remaining}</div>
        <div class="counter-label">Cards Left</div>
        <div style="margin-top: 8px; font-size: 0.75rem; color: rgba(255,255,255,0.4);">
            of {total} total
        </div>
    </div>
    """

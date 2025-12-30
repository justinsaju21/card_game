"""
Enhanced Streamlit Card Selector with Deck Management
======================================================
A premium card selector with stateful deck/discard management,
visual theming, file uploads, weighted selection, and sound effects.
"""

import streamlit as st
# Trigger reload for final logic
import random
from typing import Optional

# Local imports
import styles
import importlib
importlib.reload(styles)
from styles import get_card_styles, render_card, render_card_back, render_discard_item, render_deck_counter, render_card_discarding
from audio import get_draw_sound_html
from deck_utils import parse_deck_text, parse_deck_file, get_sample_deck


# =============================================================================
# Page Configuration
# =============================================================================
st.set_page_config(
    page_title="Card Selector Pro",
    page_icon="🎴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
st.markdown(get_card_styles(), unsafe_allow_html=True)


# =============================================================================
# Session State Initialization
# =============================================================================
def init_session_state():
    """Initialize all session state variables."""
    if 'active_deck' not in st.session_state:
        st.session_state.active_deck = []
    if 'discard_pile' not in st.session_state:
        st.session_state.discard_pile = []
    if 'current_card' not in st.session_state:
        st.session_state.current_card = None
    if 'play_sound' not in st.session_state:
        st.session_state.play_sound = False
    if 'deck_loaded' not in st.session_state:
        st.session_state.deck_loaded = False
    if 'total_cards' not in st.session_state:
        st.session_state.total_cards = 0
    if 'show_discard_animation' not in st.session_state:
        st.session_state.show_discard_animation = False
    if 'trigger_draw_animation' not in st.session_state:
        st.session_state.trigger_draw_animation = 0


init_session_state()


# =============================================================================
# Deck Management Functions
# =============================================================================
def load_deck(cards: list):
    """Load a new deck into session state."""
    st.session_state.active_deck = list(cards)
    st.session_state.discard_pile = []
    st.session_state.current_card = None
    st.session_state.deck_loaded = True
    st.session_state.total_cards = len(cards)


def discard_current_card():
    """Discard the current card with animation."""
    if st.session_state.current_card:
        st.session_state.show_discard_animation = True
        return True
    return False


def draw_card():
    """Draw a card from the active deck."""
    if not st.session_state.active_deck:
        return None
    
    # If there's a card currently displayed, move it to history
    if st.session_state.current_card:
        st.session_state.discard_pile.append(st.session_state.current_card)
    
    # Select a new card randomly
    selected_card = random.choice(st.session_state.active_deck)
    
    if selected_card:
        # Remove from active deck and set as current
        st.session_state.active_deck.remove(selected_card)
        st.session_state.current_card = selected_card
        st.session_state.play_sound = True
        st.session_state.trigger_draw_animation += 1  # Trigger animation
    
    return selected_card


def reset_deck():
    """Reset the deck by moving all cards (discarded + current) back to active deck."""
    all_cards_to_return = st.session_state.discard_pile.copy()
    if st.session_state.current_card:
        all_cards_to_return.append(st.session_state.current_card)
    
    if all_cards_to_return:
        st.session_state.active_deck.extend(all_cards_to_return)
        st.session_state.discard_pile = []
        st.session_state.current_card = None
        random.shuffle(st.session_state.active_deck)
        return True
    return False


# =============================================================================
# Main UI Layout
# =============================================================================

# Title Section
st.markdown('<div class="main-title">Card Selector Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Random Selection Made Easy</div>', unsafe_allow_html=True)


# =============================================================================
# Sidebar - Deck Setup
# =============================================================================
with st.sidebar:
    st.markdown("## 📚 Deck Setup")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload Deck File",
        type=['txt', 'csv'],
        help="Upload a .txt or .csv file with card names."
    )
    
    # Manual input
    st.markdown("---")
    st.markdown("### ✍️ Or Enter Manually")
    deck_input = st.text_area(
        "Card List",
        value=get_sample_deck() if not st.session_state.deck_loaded else "",
        height=200,
        help="Enter one card per line."
    )
    
    # Load deck button
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📥 Load Deck", use_container_width=True):
            if uploaded_file is not None:
                # Parse uploaded file with BOM handling
                content = uploaded_file.read().decode('utf-8-sig')
                cards = parse_deck_file(content, uploaded_file.name)
            elif deck_input.strip():
                # Parse manual input
                cards = parse_deck_text(deck_input)
            else:
                cards = []
            
            if cards:
                load_deck(cards)
                st.success(f"Loaded {len(cards)} cards!")
            else:
                st.error("No valid cards found!")
    
    with col2:
        if st.button("📝 Use Sample", use_container_width=True):
            cards = parse_deck_text(get_sample_deck())
            load_deck(cards)
            st.success(f"Loaded sample deck with {len(cards)} cards!")


# =============================================================================
# Main Content Area
# =============================================================================

# Create columns for layout
col_left, col_center, col_right = st.columns([1, 2, 1])

# Left Column - Deck Counter and Actions
with col_left:
    if st.session_state.deck_loaded:
        st.markdown(
            render_deck_counter(
                len(st.session_state.active_deck),
                st.session_state.total_cards
            ),
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Discard button (only shown if there's a current card)
        if st.session_state.current_card and not st.session_state.show_discard_animation:
            if st.button(
                "🗑️ Discard Card",
                use_container_width=True,
                key="discard_btn"
            ):
                if discard_current_card():
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Draw button - disabled if deck is empty OR if there's a current card
        draw_disabled = len(st.session_state.active_deck) == 0 or st.session_state.current_card is not None
        
        # Dynamic button text based on state
        if len(st.session_state.active_deck) == 0:
            button_text = "🎴 Deck Empty!"
        elif st.session_state.current_card is not None:
            button_text = "🗑️ Discard First!"
        else:
            button_text = "🎴 Draw Card"
        
        if st.button(
            button_text,
            disabled=draw_disabled,
            use_container_width=True,
            key="draw_btn"
        ):
            draw_card()
            st.rerun()

# Center Column - Card Display
with col_center:
    if st.session_state.deck_loaded:
        # Check if we're in discarding state
        if st.session_state.show_discard_animation and st.session_state.current_card:
            # Show discarding animation
            st.markdown(
                render_card_discarding(st.session_state.current_card),
                unsafe_allow_html=True
            )
            # Move card to discard pile and clear states
            st.session_state.discard_pile.append(st.session_state.current_card)
            st.session_state.current_card = None
            st.session_state.show_discard_animation = False
            # Wait for animation to complete before rerunning
            import time
            time.sleep(0.7)
            # Trigger a rerun to show the card back
            st.rerun()
            
        elif st.session_state.current_card:
            # Play sound effect
            if st.session_state.play_sound:
                st.markdown(get_draw_sound_html(), unsafe_allow_html=True)
                st.session_state.play_sound = False
            
            # Show the drawn card
            st.markdown(
                render_card(st.session_state.current_card),
                unsafe_allow_html=True
            )
        else:
            # Show card back placeholder
            st.markdown(render_card_back(), unsafe_allow_html=True)
            st.markdown(
                "<p style='text-align: center; color: rgba(255,255,255,0.5); font-style: italic;'>Draw a card to begin...</p>",
                unsafe_allow_html=True
            )
    else:
        st.markdown(render_card_back(), unsafe_allow_html=True)
        st.markdown(
            "<p style='text-align: center; color: rgba(255,255,255,0.5); font-style: italic;'>Load a deck from the sidebar to start</p>",
            unsafe_allow_html=True
        )

# Right Column - Discard Pile
with col_right:
    if st.session_state.deck_loaded:
        st.markdown('<div class="discard-pile">', unsafe_allow_html=True)
        st.markdown('<div class="discard-title">🗑️ Discard Pile</div>', unsafe_allow_html=True)
        
        if st.session_state.discard_pile:
            # Show last 10 discarded cards
            for card in reversed(st.session_state.discard_pile[-10:]):
                st.markdown(f'<div class="discard-item">{card}</div>', unsafe_allow_html=True)
            
            if len(st.session_state.discard_pile) > 10:
                st.markdown(
                    f'<div class="discard-item" style="color: rgba(255,255,255,0.3);">... and {len(st.session_state.discard_pile) - 10} more</div>',
                    unsafe_allow_html=True
                )
        else:
            st.markdown(
                '<div class="discard-item" style="font-style: italic;">No cards discarded yet</div>',
                unsafe_allow_html=True
            )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Reset button
        reset_disabled = len(st.session_state.discard_pile) == 0 and st.session_state.current_card is None
        if st.button(
            "🔄 Reset & Shuffle",
            disabled=reset_disabled,
            use_container_width=True
        ):
            if reset_deck():
                st.balloons()
                st.rerun()


# =============================================================================
# Footer Info
# =============================================================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: rgba(255,255,255,0.4); font-size: 0.85rem;">
        <p>💡 <strong>Tips:</strong> Upload a deck file or use the sample deck to get started.</p>
        <p>Format: One <code>CardName</code> per line.</p>
    </div>
    """,
    unsafe_allow_html=True
)

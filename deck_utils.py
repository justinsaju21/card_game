"""
Deck management utilities for the card selector application.
Handles parsing, weighting, and random selection.
"""

import random
from typing import Tuple, Dict, List, Optional
from io import StringIO


def parse_card_line(line: str) -> Optional[str]:
    """
    Parse a single card line.
    
    Args:
        line: A single line from the deck input
        
    Returns:
        The card name or None if invalid
    """
    line = line.strip()
    if not line or line.startswith('#'):  # Skip empty lines and comments
        return None
    
    # Weights are no longer supported, so we treat the entire line as the card name
    # Even if it contains a pipe, we include it as part of the name
    return line


def parse_deck_text(text: str) -> List[str]:
    """
    Parse deck text input.
    
    Args:
        text: Multi-line text with card names
        
    Returns:
        List of card names
    """
    cards = []
    
    for line in text.split('\n'):
        card_name = parse_card_line(line)
        if card_name:
            cards.append(card_name)
    
    return cards


def parse_deck_file(file_content: str, filename: str) -> List[str]:
    """
    Parse a deck file (CSV or TXT).
    
    Args:
        file_content: String content of the file
        filename: Name of the file for format detection
        
    Returns:
        List of card names
    """
    # Normalize line endings
    file_content = file_content.replace('\r\n', '\n').replace('\r', '\n')
    
    if filename.lower().endswith('.csv'):
        cards = []
        # CSV format: assume first column is card name
        for line in file_content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split(',')
            card_name = parts[0].strip().strip('"').strip("'")
            if card_name:
                cards.append(card_name)
        return cards
    else:
        # TXT format: simple line parsing
        return parse_deck_text(file_content)


def random_card_choice(cards: List[str]) -> Optional[str]:
    """
    Select a random card from the list.
    
    Args:
        cards: List of available card names
        
    Returns:
        Selected card name
    """
    if not cards:
        return None
    
    return random.choice(cards)


def get_sample_deck() -> str:
    """Return a sample deck for demonstration."""
    return """# Fantasy Card Deck
# Enter one card name per line

Goblin Scout
Forest Sprite
Stone Golem
River Serpent
Shadow Assassin
Fire Elemental
Ice Mage
Thunder Knight
Dragon Rider
Phoenix Lord
Crystal Guardian
Void Walker
Ancient Dragon
God of Thunder
"""

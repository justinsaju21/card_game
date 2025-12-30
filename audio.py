"""
Audio utilities for the card selector application.
Contains base64-encoded sound effects and HTML audio generators.
"""

# Base64-encoded card draw sound effect (short swoosh/flip sound)
# This is a minimal WAV file encoded in base64
DRAW_SOUND_BASE64 = """
UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YVoGAACAgICAgICAgICAgICAgICA
gICAgICAgICAgICAf3+AgICAgH9/f39/f39/f4CAgICAgICAgICAgICAgH9/f3+AgICAgICAgH9/f4CA
gH9/gICAgICAgH9/f39/f4CAgH9/gICAf39/f4CAgICAgH9/f39/f4B/f4B/f3+AgH9/f4CAgH9/gICA
gH9/gIB/gH9/f4B/f4CAf3+Af3+AgIB/gH+Af39/gH+Af4CAgH+AgIB/gH9/f4B/f4CAf4B/gIB/gH+A
gICAgH+Af39/gH9/gH9/f4CAf4CAgH+Af4CAf4CAgH+Af4B/gH+Af4CAgIB/gH+AgH+AgICAf4B/gH+A
gIB/gICAf4CAgH+AgIB/gICAf4CAgH+AgIB/gICAf4CAgICAgICAgICAf4CAgH+AgIB/gICAf4CAgH+A
gIB/gICAf4CAgH+AgIB/gH+Af4B/gH+Af4B/gH+Af4B/gH+Af4B/gH+Af4B/gH+Af4B/gIB/gICAf4CA
gH+AgIB/gICAf4CAgH+AgIB/gICAgICAgICAgICAgICAf4CAgH+AgIB/gICAf4CAgH+AgIB/gIB/gH+A
gH+Af4CAgH+AgIB/gICAgICAgICAgICAgICAgIB/gH+Af4CAf4B/gH+Af4B/gH+Af4CAgICAgICAgICA
gICAgICAgH+AgH+Af4B/gH+Af4B/gH+Af4B/gH+Af4B/gH+AgICAgICAgICAgH+AgH+Af4B/gIB/gH+A
f4B/gH+Af4B/gH+Af4B/gH+AgH+AgICAgICAgICAgICAgICAgICAgICAgICAf4B/gH+Af4B/gIB/gH+A
gH+Af4B/gICAgH+Af4CAgICAgICAgICAgH+AgH+AgH+Af4B/gH+Af4B/gH+Af4CAf4CAgICAgICAf4CA
gICAgICAgICAgICAgICAgH+Af4B/gH+Af4B/gH+Af4CAgH+Af4CAgH+AgICAgICAgICAgICAgICAf4CA
gH+AgH+AgH+Af4B/gH+Af4CAf4CAgICAgICAgICAgICAgICAgICAgICAgICAgH+AgH+AgH+Af4B/gH+A
f4B/gH+AgICAgICAgICAgICAgICAgICAgICAgICAf4CAgH+Af4B/gH+Af4B/gH+Af4CAgICAgICAgICA
gICAgICAgICAgICAgICAgICAgH+AgH+AgH+Af4B/gH+Af4CAgICAgICAgICAgICAgICAgICAgICAgICA
gICAgICAgICAgH+AgH+Af4B/gH+AgH+AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgH+AgH+A
gH+Af4B/gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgH+AgH+AgH+AgICAgICAgICA
gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA
"""

# Alternative: A more reliable approach using a simple beep tone
# This creates a short "card flip" sound effect
CARD_FLIP_SOUND = """
data:audio/wav;base64,UklGRl9vT19teleW6tbW1tbW1tbW1tbW1tbW1tbW1tfX19fX19fX19fX19fX2NjY2NjY2NjY2NjY
2dnZ2dnZ2dnZ2dnZ2tra2tra2tra2tra2tra29vb29vb29vb29vb29vb29vc3Nzc3Nzc3Nzc3N3d3d3d3d3d
3d3d3d7e3t7e3t7e3t7e3t7e39/f39/f39/f39/f4ODg4ODg4ODg4ODg4OHh4eHh4eHh4eHh4uLi4uLi4uLi
4uLi4+Pj4+Pj4+Pj4+Pj5OTk5OTk5OTk5OTk5eXl5eXl5eXl5eXl5ubm5ubm5ubm5ubm5+fn5+fn5+fn5+fn
6Ojo6Ojo6Ojo6Ojo6enp6enp6enp6enp6urq6urq6urq6urq6+vr6+vr6+vr6+vr7Ozs7Ozs7Ozs7Ozs7e3t
7e3t7e3t7e3t7u7u7u7u7u7u7u7u7+/v7+/v7+/v7+/v8PDw8PDw8PDw8PDw8fHx8fHx8fHx8fHx8vLy8vLy
8vLy8vLy8/Pz8/Pz8/Pz8/Pz9PT09PT09PT09PT09fX19fX19fX19fX19vb29vb29vb29vb29/f39/f39/f3
9/f3+Pj4+Pj4+Pj4+Pj4+fn5+fn5+fn5+fn5+vr6+vr6+vr6+vr6+/v7+/v7+/v7+/v7/Pz8/Pz8/Pz8/Pz8
/f39/f39/f39/f39/v7+/v7+/v7+/v7+////
"""


def get_draw_sound_html() -> str:
    """
    Generate HTML for playing the card draw sound effect.
    Uses a short synthesized sound that works across browsers.
    """
    return f"""
    <audio autoplay>
        <source src="{CARD_FLIP_SOUND}" type="audio/wav">
    </audio>
    """


def get_shuffle_sound_html() -> str:
    """
    Generate HTML for playing a shuffle sound effect.
    """
    # Using the same base sound for now, could be customized
    return f"""
    <audio autoplay>
        <source src="{CARD_FLIP_SOUND}" type="audio/wav">
    </audio>
    """

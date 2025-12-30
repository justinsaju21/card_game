# 🎴 Card Selector Pro

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cardgame-gn3aenokejqqn9wsd7odfn.streamlit.app/)

A premium, interactive card selection tool designed for flawless deck management and a high-end user experience. Built with Python and Streamlit, featuring custom CSS 3D animations and immersive sound effects.

---

## ✨ Features

- **🎯 Precision Selection:** Randomly draw cards with a state-of-the-art 3D flip animation.
- **📚 Deck Management:** 
  - **Manual Entry:** Paste your list directly into the sidebar.
  - **File Upload:** Support for `.txt` and `.csv` files.
  - **Sample Decks:** Get started instantly with pre-loaded examples.
- **🗑️ Discard System:** Automatically tracks drawn cards in a reverse-chronological discard pile.
- **🔄 Intelligent Reset:** Shuffle discarded cards back into the deck with a celebratory visual effect.
- **🎵 Immersive Audio:** Strategic sound cues for drawing and UI interactions.
- **📱 Fully Responsive:** Works perfectly on Desktop, Tablet, and Mobile.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/) Enhanced with Vanilla CSS (3D Transforms & Keyframes).
- **Backend:** Python 3.x
- **Animation:** CSS3 animations for tactile feedback.
- **Deployment:** Streamlit Cloud.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/justinsaju21/card_game.git
   cd card_game
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

---

## 📖 How to Use

1. **Setup your Deck:** Use the sidebar to either upload a `.txt` file (one card name per line) or type your list manually.
2. **Draw:** Click the **🎴 Draw Card** button to flip a card.
3. **Discard:** Once finished with a card, click **🗑️ Discard Card** to move it to history.
4. **Reset:** Use the **🔄 Reset & Shuffle** button to return all cards to the active deck and start fresh.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/justinsaju21/card_game/issues).

---

*Built with ❤️ by [Justin Saju](https://github.com/justinsaju21)*

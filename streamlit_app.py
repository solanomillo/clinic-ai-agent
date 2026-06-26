# streamlit_app.py
import sys
from pathlib import Path

# Agregar el directorio raíz al path
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))

from app.ui.pages import main

if __name__ == "__main__":
    main.main()
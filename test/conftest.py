"""Ensure project root is on sys.path so that `import scripts.*` works when
pytest runs from within nested CI containers or IDEs with different working
directories."""
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

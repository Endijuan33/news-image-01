import os
import shutil

# Entry image: THE WORLD front page for Friday 13 November 2026 — lead
# story Hormuz plus six verified stories. The program only copies the
# committed image bytes, so both runs write exactly the same file.
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"),
    os.path.join(OUT, "entry.png"),
)

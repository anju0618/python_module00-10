#!/usr/bin/env python3

import sys
from importlib.metadata import version

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd  # type: ignore
    HAS_DEPENDENCIES = True
except ImportError:
    HAS_DEPENDENCIES = False


def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    requirements = ["pandas", "numpy"]
    for lib in requirements:
        try:
            print(f"[OK] {lib} ({version(lib)})")
        except Exception:
            return False

    print("Data manipulation ready")
    print("Numerical computation ready")
    print("Visualization ready")

    try:
        print(f"[OK] matplotlib ({version('matplotlib')})")
    except Exception:
        return False
    return True


def generate_42_graph() -> None:
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    ascii_mask = np.array([
        [0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],  # noqa
        [0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],  # noqa
        [1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0],  # noqa
        [1,1,0,1,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0],  # noqa
        [1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0],  # noqa
        [1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],  # noqa
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],  # noqa
        [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0],  # noqa
        [0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],  # noqa
        [0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],  # noqa
        [0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],  # noqa
        [0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # noqa
        [0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]   # noqa
    ], dtype=np.int32)

    height, width = ascii_mask.shape
    raw_x = np.random.uniform(0, width, size=1000)
    raw_y = np.random.uniform(0, height, size=1000)
    df = pd.DataFrame({"x": raw_x, "y": raw_y})

    df["mask_x"] = df["x"].astype(int).clip(0, width - 1)
    df["mask_y"] = df["y"].astype(int).clip(0, height - 1)

    def is_in_42(row: pd.Series) -> bool:
        y_idx = int(row["mask_y"])
        x_idx = int(row["mask_x"])
        return bool(ascii_mask[y_idx, x_idx] == 1)

    df["is_42"] = df.apply(is_in_42, axis=1)
    df_42 = df[df["is_42"]]
    df_bg = df[~df["is_42"]].sample(frac=0.1)

    plt.figure(figsize=(10, 5), facecolor='black')
    ax = plt.axes()
    ax.set_facecolor('black')

    plt.scatter(df_42["x"], -df_42["y"], color="lime", s=15,
                alpha=0.8, label="Project: 42")
    plt.scatter(df_bg["x"], -df_bg["y"], color="#00FF00", s=2, alpha=0.2)

    title_str = "MATRIX ANALYSIS OUTPUT: VISUALIZING PROJECT 42"
    plt.title(title_str, color="white", fontsize=14)
    plt.axis('off')

    plt.savefig("matrix_analysis.png", facecolor='black')
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    if not HAS_DEPENDENCIES:
        print("Welcome to the Real World of Data Engineering")
        print("\n[ERROR] Missing dependencies!")
        print("To install using pip, run:")
        print("    pip install -r requirements.txt")
        print("To install using Poetry, run:")
        print("    poetry install")
        sys.exit(1)

    if check_dependencies():
        generate_42_graph()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

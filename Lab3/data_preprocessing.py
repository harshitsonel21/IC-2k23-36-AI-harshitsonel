"""Small EDA and preprocessing workflow using the supplied placement dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def main():
    path = Path("datasets/placement.csv")
    df = pd.read_csv(path)
    print("Shape:", df.shape)
    print("\nHead:\n", df.head())
    print("\nInfo:")
    print(df.info())
    print("\nMissing values:\n", df.isna().sum())
    print("\nSummary:\n", df.describe())
    df["attendance"] = df["attendance"].fillna(df["attendance"].median())
    print("\nPlacement counts:\n", df["placed"].value_counts())
    ax = df.plot.scatter(x="hours_studied", y="attendance", c="placed",
                         colormap="viridis", title="Study hours vs attendance")
    ax.figure.tight_layout()
    ax.figure.savefig("Lab3/placement_scatter.png")
    print("Saved Lab3/placement_scatter.png")

if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("data/cac_2024.csv")
    target = 150.0
    avg = round(df["CAC"].mean(), 2)
    print("Quarterly CAC (2024):")
    print(df.to_string(index=False))
    print(f"Average CAC 2024: {avg}")
    print(f"Industry Target: {target}")
    gap = round(avg - target, 2)
    print(f"Gap to target: {gap}")

    # Plot 1: Trend
    plt.figure()
    plt.plot(df["Quarter"], df["CAC"], marker="o")
    plt.title("Customer Acquisition Cost (CAC) — 2024 Trend")
    plt.xlabel("Quarter")
    plt.ylabel("CAC")
    for i, v in enumerate(df["CAC"]):
        plt.text(i, v, f"{v}", ha="center", va="bottom")
    plt.savefig("figures/cac_trend_2024.png", bbox_inches="tight", dpi=200)
    plt.close()

    # Plot 2: Average vs Target
    plt.figure()
    bars = ["Avg 2024 CAC", "Industry Target"]
    values = [avg, target]
    plt.bar(bars, values)
    plt.title("Average CAC vs Industry Target (2024)")
    plt.ylabel("Cost")
    for i, v in enumerate(values):
        plt.text(i, v, f"{v}", ha="center", va="bottom")
    plt.savefig("figures/cac_vs_target_2024.png", bbox_inches="tight", dpi=200)
    plt.close()

if __name__ == "__main__":
    main()
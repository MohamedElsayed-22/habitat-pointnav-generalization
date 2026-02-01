import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("habitat-lab/tb/replication_Gibson/tb.csv")
experiment = "Baseline_Replication"
steps = df["Step"].to_numpy()
values = df["Value"].to_numpy()

# EMA smoothing
alpha = 0.1   
ema = pd.Series(values).ewm(alpha=alpha).mean().to_numpy()

plt.figure(figsize=(6, 4))
plt.plot(steps, ema)

plt.xlabel("Training Steps (Xe6)")
plt.ylabel("SPL")
plt.title(f"PointGoal Navigation Performance (SPL) - {experiment}")
plt.grid(True)

plt.gca().xaxis.set_major_formatter(
    FuncFormatter(lambda x, _: f"{x/1e6:.0f}")
)

plt.tight_layout()
plt.savefig(f"docs/{experiment}_spl_curve.png", dpi=300)
plt.show()

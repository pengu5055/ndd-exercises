import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cmasher as cmr
from scipy.stats import norm

# Use custom style
mpl.style.use("./ma-style.mplstyle")
colors = cmr.take_cmap_colors("cmr.tropical", 8, cmap_range=(0, 0.85))

gauss1 = norm(loc=3, scale=1)
gauss2 = norm(loc=7, scale=1)

x = np.linspace(0, 10, 1000)
y1 = gauss1.pdf(x)
y2 = gauss2.pdf(x)

fig, ax = plt.subplots()
ax.set_title("Threshold value between two measurement peaks")
ax.plot(x, y1, color=colors[0], label="Particle 1")
ax.plot(x, y2, color=colors[3], label="Particle 2")
ax.fill_between(x, y1, y2, where=y1>y2, color=colors[0], alpha=0.3, label="Efficiency")
ax.fill_between(x, 0, y2, where=y2<y1, color=colors[6], alpha=0.3, label="False Positive")
ax.fill_between(x, 0, y1, where=y1<y2, color=colors[7], alpha=0.3, label="False Negative")

ax.axvline(x=5, color="black", linestyle="--", label="Threshold\nvalue")
# ax.set_xlabel("Feature")
# ax.set_ylabel("Density")
ax.axis('off')
ax.set_ylim(0, 0.75)
ax.legend(frameon=False, loc="upper left")

plt.tight_layout()
plt.savefig("threshold.pdf", dpi=500)
plt.show()

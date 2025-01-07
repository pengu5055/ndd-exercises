import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cmasher as cmr

# Use custom style
mpl.style.use("./ma-style.mplstyle")
colors = cmr.take_cmap_colors("cmr.tropical", 8, cmap_range=(0, 0.85))

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, 100)
data = np.linspace(0, 9, 10)
measurements = 2 * data + np.random.normal(0, 2, data.shape)

# Plot
fig, ax = plt.subplots()
ax.set_title("Fitting a linear model to data")
ax.plot(x, 2*x, color="black", ls=":", label="True model", lw=1.5, zorder=1, alpha=0.5)
ax.errorbar(data, measurements, yerr=np.std(measurements), capsize=5, fmt="o", color=colors[0], label="Measurements", zorder=2)
ax.scatter(data, measurements, color=colors[2], zorder=3)

# Annotate all points with $\sigma$ to hammer home the point
for i in range(len(data)):
    ax.annotate("$\sigma$", (data[i]+.25, measurements[i]+.25), fontsize=12, color=colors[0])

# Change tick labels to abstract
ax.set_xticks(data)
ax.tick_params(axis='x', which='major', labelsize=12, width=1, length=6)
ax.tick_params(axis='x', which='minor', tick1On=False, tick2On=False)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.5))
ax.xaxis.set_minor_formatter(plt.FuncFormatter(lambda x, _: f"$\Delta x$" if x not in [-0.5, 9.5] and x < 9.5 else ""))
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"$x_{int(x)}$"))
ax.get_yaxis().set_visible(False)
ax.spines[["left", "right", "top", "bottom"]].set_visible(False)
ax.legend(frameon=False, loc="upper left")

plt.tight_layout()
plt.savefig("linearfit.pdf", dpi=500)
plt.show()

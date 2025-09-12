import matplotlib.pyplot as plt

# Data: (Color Name, Hex, Psychology, Ideal Use)
colors_data = [
    ("Blue", "#1f77b4", "Trust, reliability, calmness, professionalism", "Finance, healthcare, tech, corporate sites"),
    ("Red", "#d62728", "Urgency, excitement, passion", "CTAs, sales, food, sports"),
    ("Green", "#2ca02c", "Growth, nature, health, prosperity", "Sustainability, wellness, finance"),
    ("Yellow", "#ffbf00", "Optimism, warmth, creativity", "Youth brands, highlights, cheerful CTAs"),
    ("Orange", "#ff7f0e", "Friendliness, enthusiasm, affordability", "Ecommerce, entertainment, CTAs"),
    ("Purple", "#9467bd", "Creativity, luxury, spirituality", "Beauty, wellness, premium services"),
    ("Pink", "#e377c2", "Compassion, romance, youthfulness", "Fashion, causes, youth products"),
    ("Black", "#000000", "Sophistication, power, elegance", "Luxury, bold minimalism"),
    ("White", "#ffffff", "Cleanliness, simplicity, openness", "Minimalist, modern, health"),
    ("Gray", "#7f7f7f", "Neutrality, balance, professionalism", "Corporate, tech backgrounds"),
    ("Brown", "#8c564b", "Earthiness, stability, warmth", "Organic food, handmade products"),
    ("Teal", "#17becf", "Balance, calmness, creativity", "Wellness, tech, travel")
]

# Create figure
fig, ax = plt.subplots(figsize=(12, 9))
ax.axis('off')

# Column headers
ax.text(0.25, len(colors_data) + 0.5, "Color", fontsize=14, fontweight="bold", ha="center")
ax.text(2.5, len(colors_data) + 0.5, "Psychology", fontsize=14, fontweight="bold", ha="center")
ax.text(6.5, len(colors_data) + 0.5, "Ideal Web Uses", fontsize=14, fontweight="bold", ha="center")

# Rows
for i, (name, hex_color, psychology, usage) in enumerate(colors_data):
    y = len(colors_data) - i
    # Color swatch
    ax.add_patch(plt.Rectangle((0, y - 0.4), 0.5, 0.8, color=hex_color, ec="black"))
    # Texts
    ax.text(0.6, y, name, fontsize=12, fontweight="bold", va="center")
    ax.text(2.5, y, psychology, fontsize=10, va="center", wrap=True)
    ax.text(6.5, y, usage, fontsize=10, va="center", wrap=True)

plt.tight_layout()
plt.show()

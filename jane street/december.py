import numpy as np
import plotly.graph_objects as go

def simulate_vectorized(j_thresh, s_low, s_high, n=1_00_000):
    k = (np.sqrt(5) - 1) / 2
    
    # 1. Generate random throws
    j1 = np.random.rand(n)
    s1 = np.random.rand(n)
    s_reroll = np.random.rand(n)
    j_reroll = np.random.rand(n)

    # 2. Spears' Strategy based on J's "leak" (j1)
    current_s_thresh = np.where(j1 < k, s_low, s_high)
    
    # 3. Final Scores
    s_final = np.where(s1 >= current_s_thresh, s1, s_reroll)
    j_final = np.where(j1 >= j_thresh, j1, j_reroll)

    # 4. Win Rate (J > S)
    wins = np.sum(j_final > s_final)
    return wins / n

# --- Data Generation ---
k_nash = (np.sqrt(5) - 1) / 2
resolution = 40

# Define ranges for Spears' Low and High thresholds
x = np.linspace(0.4, 0.7, resolution)  # s_low
y = np.linspace(0.55, 0.85, resolution) # s_high
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

print("Simulating grid...")
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = simulate_vectorized(j_thresh=k_nash, s_low=X[i, j], s_high=Y[i, j])

# --- Plotting with Plotly ---

# 1. The Surface Plot
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis', opacity=0.9)])

# 2. Add the "Original Strategy" Point for comparison
orig_high = k_nash + k_nash**4 / 2
orig_win_rate = simulate_vectorized(k_nash, 0.5, orig_high, n=500_000)

fig.add_trace(go.Scatter3d(
    x=[0.5], 
    y=[orig_high], 
    z=[orig_win_rate],
    mode='markers',
    marker=dict(size=10, color='red', symbol='circle'),
    name='Original Strategy'
))

# 3. Layout and Labels
fig.update_layout(
    title=f'Java-lin Win Rate (Rotatable)<br>Java-lin fixed at Nash: {k_nash:.3f}',
    scene=dict(
        xaxis_title='Spears Low Threshold (s_low)',
        yaxis_title='Spears High Threshold (s_high)',
        zaxis_title='Java-lin Win Rate',
        # Optional: Set camera angle or aspect ratio here
    ),
    width=900,
    height=700,
    margin=dict(l=65, r=50, b=65, t=90)
)

# Show the plot
fig.show()
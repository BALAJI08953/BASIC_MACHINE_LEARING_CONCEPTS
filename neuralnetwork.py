
import numpy as np
rng = np.random.default_rng(0)
t = rng.uniform(0.5, 3 * np.pi, 400)

X = np.r_[
    np.c_[t * np.cos(t), t * np.sin(t)],
    np.c_[-t * np.cos(t), -t * np.sin(t)]
] / 10

y = np.r_[
    np.zeros(400),
    np.ones(400)
][:, None]

sizes = [2, 24, 24, 24, 24, 24, 24, 1]

W = [
    rng.normal(0, np.sqrt(1 / a), (a, b))
    for a, b in zip(sizes, sizes[1:])
]
B = [np.zeros(n) for n in sizes[1:]]
for step in range(2001):

    h = [X]

    for i in range(len(W)):
        z = h[-1] @ W[i] + B[i]

        h.append(
            np.tanh(z)
            if i < len(W) - 1
            else 1 / (1 + np.exp(-z))
        )

    d = (h[-1] - y) / len(X)

    for i in reversed(range(len(W))):
        gW, gB = h[i].T @ d, d.sum(0)

        if i:
            d = (d @ W[i].T) * (1 - h[i]**2)

        W[i] -= 0.3 * gW
        B[i] -= 0.3 * gB

    if step % 500 == 0:
        print(
            step,
            "accuracy",
            ((h[-1] > 0.5) == y).mean()
        )

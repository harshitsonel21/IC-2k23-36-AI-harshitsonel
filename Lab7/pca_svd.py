"""PCA dimensionality reduction and SVD reconstruction demo."""
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def main():
    rng = np.random.default_rng(42)
    X = rng.normal(size=(100, 5))
    X[:, 4] = 0.7 * X[:, 0] - 0.2 * X[:, 1] + rng.normal(0, 0.1, 100)
    X_scaled = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2, random_state=42)
    reduced = pca.fit_transform(X_scaled)
    print("Original shape:", X.shape)
    print("Reduced shape:", reduced.shape)
    print("Explained variance ratio:", pca.explained_variance_ratio_)
    U, S, Vt = np.linalg.svd(X_scaled, full_matrices=False)
    reconstructed = (U[:, :2] * S[:2]) @ Vt[:2, :]
    print("Rank-2 reconstruction MSE:", np.mean((X_scaled - reconstructed) ** 2))

if __name__ == "__main__":
    main()

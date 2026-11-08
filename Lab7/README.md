# Lab 7: Explainable AI, Adversarial AI, PCA/SVD and Advanced Applications

## Aim / Problem Statement
Explore dimensionality reduction using PCA/SVD and understand the FGSM perturbation principle. The included FGSM script is a toy vector demonstration, not a trained image-classification attack.

## Algorithm
PCA: standardize features and project them to two principal components. SVD: compute a rank-2 approximation. FGSM: calculate the input gradient of a classification loss and perturb the input by epsilon times the gradient sign.

## How to run
```bash
python Lab7/pca_svd.py
python Lab7/fgsm_demo.py
```

## Results / Output
Run the program and record the actual console output and generated files here. Add screenshots/graphs from your execution.

## Performance Analysis
Report applicable metrics such as accuracy, precision, recall, F1-score, execution time, and/or solution path cost. Do not insert estimated values.

## Learning Outcomes
Understand dimensionality reduction, singular-value decomposition, gradient-based adversarial perturbations, and the distinction between a toy demo and a full image-model experiment.

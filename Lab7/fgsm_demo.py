"""Minimal FGSM demonstration on a toy differentiable model (not a real image classifier)."""
import torch
from torch import nn

def main():
    torch.manual_seed(1)
    model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 2))
    x = torch.rand(1, 4, requires_grad=True)
    label = torch.tensor([0])
    loss = nn.CrossEntropyLoss()(model(x), label)
    model.zero_grad()
    loss.backward()
    epsilon = 0.05
    perturbed = torch.clamp(x + epsilon * x.grad.sign(), 0, 1).detach()
    print("Original input:", x.detach())
    print("Perturbed input:", perturbed)
    print("L-infinity perturbation:", (perturbed - x.detach()).abs().max().item())

if __name__ == "__main__":
    main()

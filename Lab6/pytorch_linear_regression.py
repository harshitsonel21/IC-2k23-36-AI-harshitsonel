"""Linear regression using PyTorch tensors and autograd."""
import torch
from torch import nn

def main():
    torch.manual_seed(7)
    x = torch.arange(1, 11, dtype=torch.float32).view(-1, 1)
    y = 3.0 * x + 2.0
    model = nn.Linear(1, 1)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(500):
        prediction = model(x)
        loss = loss_fn(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch+1}: loss={loss.item():.6f}")

    print("Learned weight:", model.weight.item())
    print("Learned bias:", model.bias.item())
    print("Prediction for x=11:", model(torch.tensor([[11.0]])).item())
    torch.save(model.state_dict(), "models/linear_regression.pt")

if __name__ == "__main__":
    main()

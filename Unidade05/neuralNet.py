import torch
import torch.nn as nn

# Definindo o modelo da rede neural
class NeuralNet(nn.Module):
    def __init__(self,input_size):
        super().__init__()
        self.linear_stack = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Dropout(0.25),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, x):
        logits = self.linear_stack(x)
        return logits
import torch

from kaiwu.torch_plugin import RestrictedBoltzmannMachine
from kaiwu.classical import SimulatedAnnealingOptimizer
from torch.optim import SGD


if __name__ == "__main__":
    USE_QPU = False
    NUM_READS = 100
    SAMPLE_SIZE = 17

    sampler = SimulatedAnnealingOptimizer()
    sample_kwargs = {}
    h_range = j_range = None
    num_nodes = 50
    num_visible = 20
    num_edges = 100
    x = 1 - 2.0 * torch.randint(0, 2, (SAMPLE_SIZE, num_visible))

    # Instantiate the model
    rbm = RestrictedBoltzmannMachine(
        num_visible,
        num_nodes - num_visible,
    )

    # Instantiate the optimizer
    opt_rbm = SGD(rbm.parameters())

    # Example of one iteration in a training loop
    # Generate a sample set from the model
    x = rbm.get_hidden(x)
    s = rbm.sample(sampler)
    opt_rbm.zero_grad()
    # Compute the objective---this objective yields the same gradient as the negative
    # log likelihood of the model
    objective = rbm.objective(x, s)
    # Backpropgate gradients
    print("call backward")
    objective.backward()
    print("after backward")
    # Update model weights with a step of stochastic gradient descent
    opt_rbm.step()
    print(objective)

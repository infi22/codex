"""Training routines and configuration stubs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Protocol


class Model(Protocol):
    """Protocol describing the interface expected by the trainer."""

    def forward(self, batch: Any) -> Any: ...


class Optimizer(Protocol):
    """Protocol describing optimizer behavior."""

    def step(self) -> None: ...
    def zero_grad(self) -> None: ...


@dataclass
class TrainingConfig:
    """Configuration for training loops."""

    epochs: int
    learning_rate: float
    checkpoint_dir: str


def train(
    model: Model,
    optimizer: Optimizer,
    data_loader: Callable[[], Any],
    config: TrainingConfig,
) -> None:
    """Placeholder training loop.

    Future versions will integrate logging, checkpointing, gradient
    accumulation, and early stopping based on validation metrics.
    """

    for _ in range(config.epochs):
        for batch in data_loader():
            _ = model.forward(batch)
            optimizer.zero_grad()
            optimizer.step()

"""Orchestration entrypoints for data, training, and evaluation."""

from __future__ import annotations

from typing import Callable

from . import data, evaluation, training


def run_experiment(
    dataset_config: data.DatasetConfig,
    data_source: data.DataSource,
    training_config: training.TrainingConfig,
    trainer: Callable[..., None] = training.train,
) -> evaluation.Metrics:
    """Placeholder experiment runner.

    This will eventually wire together data loading, model initialization,
    training, and evaluation. For now it demonstrates the intended control
    flow and types between components.
    """

    _ = data.load_dataset(dataset_config, data_source)
    trainer(None, None, lambda: [], training_config)  # type: ignore[arg-type]
    return evaluation.Metrics(accuracy=0.0, latency_ms=0.0, safety_score=0.0)

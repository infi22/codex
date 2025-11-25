"""Smoke tests for the pipeline scaffolding."""

from src import data, evaluation, pipeline, training


def test_run_experiment_returns_metrics() -> None:
    class DummySource:
        def load(self):
            return []

    metrics = pipeline.run_experiment(
        dataset_config=data.DatasetConfig(name="dummy", version="0.1"),
        data_source=DummySource(),
        training_config=training.TrainingConfig(
            epochs=1, learning_rate=0.001, checkpoint_dir="/tmp/checkpoints"
        ),
    )

    assert isinstance(metrics, evaluation.Metrics)

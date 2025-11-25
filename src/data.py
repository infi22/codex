"""Data loading and preprocessing utilities.

This module will house dataset readers, schema validation, preprocessing
pipelines, and dataset versioning utilities to support reproducible
experiments.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Protocol


class DataSource(Protocol):
    """Protocol describing a loadable dataset source."""

    def load(self) -> Iterable[dict]:
        """Load raw records from the underlying source."""


@dataclass
class DatasetConfig:
    """Configuration for dataset loading and preprocessing."""

    name: str
    version: str
    split: str = "train"


def load_dataset(config: DatasetConfig, source: DataSource) -> Iterable[dict]:
    """Placeholder loader that will connect configuration and source objects.

    In future iterations this will perform validation, logging, and
    instrumentation to track dataset versions.
    """

    return source.load()

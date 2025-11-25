"""Evaluation utilities for comparing runs to baselines."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass
class Metrics:
    """Container for key evaluation metrics."""

    accuracy: float
    latency_ms: float
    safety_score: float


@dataclass
class Baseline:
    """Baseline metrics to compare against."""

    name: str
    metrics: Metrics


def compare_to_baseline(current: Metrics, baseline: Baseline) -> Mapping[str, float]:
    """Return metric deltas relative to a baseline."""

    return {
        "accuracy_delta": current.accuracy - baseline.metrics.accuracy,
        "latency_delta": current.latency_ms - baseline.metrics.latency_ms,
        "safety_delta": current.safety_score - baseline.metrics.safety_score,
    }

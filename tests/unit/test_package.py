import importlib

import pytest

import gold_intel

LAYERS = ["core", "data", "features", "backtest", "risk", "journal", "ml", "agents"]


def test_version_is_set() -> None:
    assert gold_intel.__version__ and gold_intel.__version__ != "0.0.0+unknown"


@pytest.mark.parametrize("layer", LAYERS)
def test_architecture_layers_are_importable(layer: str) -> None:
    module = importlib.import_module(f"gold_intel.{layer}")
    assert module.__doc__, f"gold_intel.{layer} should document its responsibility"

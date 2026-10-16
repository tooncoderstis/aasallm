"""Smoke test paket aasallm (Fase 0)."""

import aasallm
import aasallm.np
import aasallm.serve
import aasallm.torch


def test_version() -> None:
    assert aasallm.__version__ == "0.1.0"


def test_subpackage_docstrings() -> None:
    assert aasallm.np.__doc__
    assert aasallm.torch.__doc__
    assert aasallm.serve.__doc__

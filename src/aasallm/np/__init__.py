"""Implementasi NumPy murni — rujukan kebenaran setiap rumus (ADR-0001).

Setiap operasi (dot product, matmul, softmax, LayerNorm, attention, ...) ditulis
eksplisit mengikuti rumus buku, tanpa framework, agar dapat diaudit baris-per-baris.
"""

from aasallm.np import vectors
from aasallm.np.vectors import (
    add,
    as_vector,
    cosine_similarity,
    dot,
    hadamard,
    norm_l2,
    scale,
)

__all__ = [
    "add",
    "as_vector",
    "cosine_similarity",
    "dot",
    "hadamard",
    "norm_l2",
    "scale",
    "vectors",
]

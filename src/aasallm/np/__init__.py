"""Implementasi NumPy murni — rujukan kebenaran setiap rumus (ADR-0001).

Setiap operasi (dot product, matmul, softmax, LayerNorm, attention, ...) ditulis
eksplisit mengikuti rumus buku, tanpa framework, agar dapat diaudit baris-per-baris.
"""

from aasallm.np import matrices, vectors
from aasallm.np.matrices import (
    flops_matmul,
    identity,
    matadd,
    matmul,
    matvec,
    transpose,
)
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
    "flops_matmul",
    "hadamard",
    "identity",
    "matadd",
    "matmul",
    "matrices",
    "matvec",
    "norm_l2",
    "scale",
    "transpose",
    "vectors",
]

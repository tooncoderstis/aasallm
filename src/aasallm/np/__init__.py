"""Implementasi NumPy murni — rujukan kebenaran setiap rumus (ADR-0001).

Setiap operasi (dot product, matmul, softmax, LayerNorm, attention, ...) ditulis
eksplisit mengikuti rumus buku, tanpa framework, agar dapat diaudit baris-per-baris.
"""

from aasallm.np import matrices, probability, vectors
from aasallm.np.matrices import (
    flops_matmul,
    identity,
    matadd,
    matmul,
    matvec,
    transpose,
)
from aasallm.np.probability import (
    conditional_probability,
    cumulative_sum,
    expected_value,
    normal_pdf,
    sample_categorical,
    std,
    uniform,
    validate_distribution,
    variance,
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
    "conditional_probability",
    "cosine_similarity",
    "cumulative_sum",
    "dot",
    "expected_value",
    "flops_matmul",
    "hadamard",
    "identity",
    "matadd",
    "matmul",
    "matrices",
    "matvec",
    "norm_l2",
    "normal_pdf",
    "probability",
    "sample_categorical",
    "scale",
    "std",
    "transpose",
    "uniform",
    "validate_distribution",
    "variance",
    "vectors",
]

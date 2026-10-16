"""Implementasi NumPy murni — rujukan kebenaran setiap rumus (ADR-0001).

Setiap operasi (dot product, matmul, softmax, LayerNorm, attention, ...) ditulis
eksplisit mengikuti rumus buku, tanpa framework, agar dapat diaudit baris-per-baris.
"""

from aasallm.np import information, matrices, probability, vectors
from aasallm.np.information import (
    bits_per_byte,
    cross_entropy,
    entropy,
    kl_divergence,
    mean_negative_log_likelihood,
    perplexity,
)
from aasallm.np.information import (
    information as self_information,
)
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
    "bits_per_byte",
    "conditional_probability",
    "cosine_similarity",
    "cross_entropy",
    "cumulative_sum",
    "dot",
    "entropy",
    "expected_value",
    "flops_matmul",
    "hadamard",
    "identity",
    "information",
    "kl_divergence",
    "matadd",
    "matmul",
    "matrices",
    "matvec",
    "mean_negative_log_likelihood",
    "norm_l2",
    "normal_pdf",
    "perplexity",
    "probability",
    "sample_categorical",
    "scale",
    "self_information",
    "std",
    "transpose",
    "uniform",
    "validate_distribution",
    "variance",
    "vectors",
]

"""Implementasi NumPy murni — rujukan kebenaran setiap rumus (ADR-0001).

Setiap operasi (dot product, matmul, softmax, LayerNorm, attention, ...) ditulis
eksplisit mengikuti rumus buku, tanpa framework, agar dapat diaudit baris-per-baris.
"""

from aasallm.np import bpe, calculus, embedding, information, matrices, probability, vectors
from aasallm.np.bpe import encode as bpe_encode
from aasallm.np.bpe import split_symbols, train_bpe
from aasallm.np.calculus import (
    central_difference,
    gradient_descent_step,
    linear_backward,
    numerical_derivative,
    numerical_gradient,
    relu,
    relu_derivative,
    sigmoid,
    sigmoid_derivative,
    tanh_derivative,
)
from aasallm.np.embedding import (
    embed_one_hot,
    embedding_lookup,
    embedding_parameters,
    one_hot,
    one_hot_matrix,
    tied_logits,
)
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
    "bpe",
    "bpe_encode",
    "calculus",
    "central_difference",
    "conditional_probability",
    "cosine_similarity",
    "cross_entropy",
    "cumulative_sum",
    "dot",
    "embed_one_hot",
    "embedding",
    "embedding_lookup",
    "embedding_parameters",
    "entropy",
    "expected_value",
    "flops_matmul",
    "gradient_descent_step",
    "hadamard",
    "identity",
    "information",
    "kl_divergence",
    "linear_backward",
    "matadd",
    "matmul",
    "matrices",
    "matvec",
    "mean_negative_log_likelihood",
    "norm_l2",
    "normal_pdf",
    "numerical_derivative",
    "numerical_gradient",
    "one_hot",
    "one_hot_matrix",
    "perplexity",
    "probability",
    "relu",
    "relu_derivative",
    "sample_categorical",
    "scale",
    "self_information",
    "sigmoid",
    "sigmoid_derivative",
    "split_symbols",
    "std",
    "tanh_derivative",
    "tied_logits",
    "train_bpe",
    "transpose",
    "uniform",
    "validate_distribution",
    "variance",
    "vectors",
]

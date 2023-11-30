#!/usr/bin/python3
"""
This module multiplies 2 matrix with numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)

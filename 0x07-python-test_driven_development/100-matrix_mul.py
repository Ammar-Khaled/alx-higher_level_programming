#!/usr/bin/python3
"""This module multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")

    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    
    len_row_a = len(m_a[0])
    len_row_b = len(m_b[0])

    for l in m_a:
        if type(l) != list:
            raise TypeError("m_a must be a list of lists")
        
        if len(l) == 0:
            raise TypeError("m_a can't be empty")
        
        if len(l) != len_row_a:
            raise TypeError("each row of m_a must be of the same size")
        
        for e in l:
            if type(e) != int and type(e) != float:
               raise TypeError("m_a should contain only integers or floats") 
        
    for l in m_b:
        if type(l) != list:
            raise TypeError("m_b must be a list of lists")
        
        if len(l) == 0:
            raise TypeError("m_b can't be empty")
        
        if len(l) != len_row_b:
            raise TypeError("each row of m_b must be of the same size")

        for e in l:
            if type(e) != int and type(e) != float:
               raise TypeError("m_b should contain only integers or floats")
            
    # if m_a and m_b can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
       
    ans_idx = -1
    ans = []

    # for each row in m_a
    for row_a in m_a:

        ans_idx += 1
        ans.append([])
        col_idx = -1

        for it in range(len(m_b[0])):
            entry = 0
            col_idx += 1
            for j in range(len(m_b)):
                entry += row_a[j] * m_b[j][col_idx]
            ans[ans_idx].append(entry)

    return ans


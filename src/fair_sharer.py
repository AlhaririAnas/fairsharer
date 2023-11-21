def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """
    
    for i in range(0, num_iterations):
        max_value_idx = values.index(max(values))        
        right_neighbourMax_idx = max_value_idx + 1
        left_neighbourMax_idx = max_value_idx -1
        
        
        if max_value_idx == len(values) - 1: #When max-value has the last position in list
            right_neighbourMax_idx = 0
            
        if max_value_idx == 0: #When max-value has the first position in list
                left_neighbourMax_idx = -1
                

        
        values[left_neighbourMax_idx] += values[max_value_idx] * share
        values[right_neighbourMax_idx] += values[max_value_idx] * share
        values[max_value_idx] -= values[max_value_idx] * share * 2

    
    return values

print(fair_sharer([0, 1000, 800, 0], 1))
print(fair_sharer([0, 1000, 800, 0], 2))

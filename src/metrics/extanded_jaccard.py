
def extanded_jaccard(solution_matrix_1, solution_matrix_2):
    updated_solution_matrix_1 = list()
    for i in solution_matrix_1:
        if i not in solution_matrix_2:
            updated_solution_matrix_1.extend(i)

    return list(set(updated_solution_matrix_1))

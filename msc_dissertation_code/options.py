import os
from multiprocessing import Pool

from msc_dissertation_code.constructive_algorithms import (room_criteria_map,
                                                           surgery_criteria_map)
from msc_dissertation_code.handlers import Problem
from msc_dissertation_code.solution.solution_utils import solver


def solve_one(filename, surg_alg, room_alg):
    """Solve one problem."""
    problem = Problem(filename)
    solution = solver(surg_alg,
                      room_alg,
                      problem.capacity,
                      problem.rooms,
                      problem.durations)
    problem.solutions.append(solution)

    return problem


def solve_one_with_all(filename):
    """Solve one problem with all possible algorithms."""
    workload = []
    problem = Problem(filename)

    for surg_alg in room_criteria_map.values():
        for room_alg in surgery_criteria_map.values():
            workload.append([surg_alg,
                             room_alg,
                             problem.capacity,
                             problem.rooms,
                             problem.durations])

    with Pool() as pool:
        solutions = pool.map(solver, workload)

    problem.solutions.extend(solutions)

    return problem


def solve_all_with_all_algs(base_dir):
    """Solve all the problems with all the possible algorithms."""
    problems_list = []

    for file_ in os.listdir(base_dir):

        if file_.startswith('.'):
            continue

        problem = solve_one_with_all(os.path.join(base_dir, file_))
        problems_list.append(problem)

    return problems_list

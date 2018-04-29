from msc_dissertation_code.solution.evaluator import evaluator


class Solution:
    """Responsible of holding all the necessary information that corresponds
    to a solution.
    """

    def __init__(self, room_criteria_alg_name, surg_criteria_alg_name,
                       sol_dict, overtime, idletime, makespan):
        self.room_criteria_alg_name = room_criteria_alg_name
        self.surgery_criteria_alg_name = surg_criteria_alg_name
        self.solution_dict = sol_dict
        self.overtime = overtime
        self.idletime = idletime
        self.makespan = makespan

    def to_dict(self):
        return self.__dict__


def solver(surgery_criteria, room_criteria, capacity, rooms, durations):
    """Solve a particular problem with particular algorithms.

    Args:
        surgery_criteria(class): a class that represents the algorithm
            that sorts the surgeries in a certain order.
        room_criteria (class): a class that represents the algorithm
            that assigns the surgeries into rooms.
        capacity (int): number of minutes the can a room be occupied.
        rooms (int): number of rooms can be booked.
        durations (list): a list of the estimated surgeries durations.
    Returns:
        (Solution)
    """
    surg = surgery_criteria(durations)
    sorted_durations = surg.sort()
    room_alg = room_criteria(sorted_durations, rooms, capacity)
    sol = room_alg.run()
    overtime, idletime, makespan = evaluator(sol,
                                             sorted_durations,
                                             rooms,
                                             capacity)

    return Solution(room_criteria.name,
                    surgery_criteria.name,
                    sol,
                    overtime,
                    idletime,
                    makespan)

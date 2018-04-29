def _calc_durations(solution, durations, rooms):
    total_durations = [0] * rooms

    for idr, r in enumerate(rooms):
        for ids, s in enumerate(solution[idr]):

            if solution[idr][ids] == -1:
                total_durations[idr] = None
            else:
                surg = solution[idr][ids]
                total_durations[idr] += durations[surg]

    return total_durations


def _calc_overtime(total_durations, capacity):
    overtime = []

    for d in total_durations:

        if not d:
            overtime.append(0)
        else:
            result = capacity - d
            if result >= 0:
                overtime.append(0)
            else:
                overtime.append(result)

    # Overtime per room.
    return sum(overtime) / len(overtime)


def _calc_idletime(total_durations, capacity):
    idletime = []

    for d in total_durations:

        if not d:
            idletime.append(capacity)
        else:
            result = capacity - d
            if result > 0:
                idletime.append(result)
            else:
                idletime.append(0)

    # Idletime per room
    return sum(idletime) / len(idletime)


def _calc_makespan(total_durations):
    return max(total_durations)


def evaluator(solution, durations, rooms, capacity):
    total_durations = _calc_durations(solution, durations, rooms)
    return (_calc_overtime(total_durations, capacity),
            _calc_idletime(total_durations, capacity),
            _calc_makespan(total_durations))
__all__ = ['FirstFit', 'BestFit']


from msc_dissertation_code.constructive_algorithms.criteria import BaseCriteria


class BaseRoomCriteria(BaseCriteria):
    """Base Room Criteria abstract class.

    The class will be used in order to create the constructive algorithms,
    that they will determine the surgery allocation to the rooms.
    """

    def __init__(self, durations, rooms, capacity=480):
        super().__init__(durations)
        self.rooms = rooms
        self.cap = [capacity] * rooms
        self.sol = [[] for _ in range(rooms)]

    def run(self):
        pass


class FirstFit(BaseRoomCriteria):
    """First Fit Algorithm.

    The algorithm tries to find the room in which the surgery best fits.
    In case the room is not found - overtime is created - the algorithm
    tries to find the room in which, if the surgery is assigned, it will create
    the least amount of overtime.
    """

    @staticmethod
    def _overtime_room(cap):
        """Find the room with the smallest amount of overtime.

        Args:
            cap (list): a list of integers.
        Returns:
            ic (int): the index of the room with the min overtime.
        """
        min_value = max(cap)

        # Return the first room that has the minimum value.
        for ic, c in enumerate(cap):
            if c == min_value:
                return ic

    def run(self):
        """Run the algorithm.

        Returns:
            sol (list): a list of lists that corresponds to the solution.
        """
        for ids, s in enumerate(self.durations):
            for idr, r in enumerate(self.rooms):

                if self.cap[idr] - s >= 0:
                    self.sol[idr].append(ids)
                    self.cap[idr] -= r
                    break
            else:

                # Overtime capacity list.
                overtime_cap = [
                    self.cap[room] - s for room in range(self.rooms)
                ]
                min_room = self._overtime_room(overtime_cap)
                # Assign the un-scheduled surgery to the room that has the
                # minimum amount of overtime.
                self.sol[min_room].append(ids)
                self.cap[min_room] -= self.durations[ids]

        return self.sol


class BestFit(BaseRoomCriteria):
    """Best Fit Algorithm.

    The algorithm tries to find the room in which, if the surgery is placed,
    it will create the least amount of overtime.
    """

    def run(self):
        """Run the algorithm.

        Returns:
            sol (list): a list of lists that corresponds to the solution.
        """
        for ids, s in enumerate(self.durations):

            temp_durs = []

            for idr, r in enumerate(self.rooms):

                temp_durs.append(self.cap[idr] - s)

            best_room = temp_durs.index(max(temp_durs))
            self.sol[best_room].append(ids)
            self.cap[best_room] -= s

        return self.sol


# TODO
class WorstFit(BaseRoomCriteria):
    pass


# TODO
class RandomFit(BaseRoomCriteria):
    pass

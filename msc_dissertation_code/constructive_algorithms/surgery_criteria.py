__all__ = ['FCFS', 'SPT', 'LPT', 'LOHI', 'HILO', 'Valley', 'Hill']


from msc_dissertation_code.constructive_algorithms.criteria import BaseCriteria


class DurationsCriteria(BaseCriteria):
    """Base Surgery Criteria abstract class.

    The class will be used in order to create the sorting algorithms, that they
    will sort the surgeries' durations into a particular sequence.
    """

    def sort(self):
        pass


class FCFS(DurationsCriteria):
    """First Come First Served algorithm.

    The algorithm returns the surgeries in the exact way they come.
    """

    def sort(self):
        """Sort the surgeries' durations.

        Returns:
            (list)
        """
        return self.durations


class SPT(FCFS):
    """Shortest Processing Time.

    The algorithm sorts the surgeries from the shortest to the longest surgery.
    """

    def sort(self):
        """Sort the surgeries' durations.

        Returns:
            (list)
        """
        return sorted(super().sort())


class LPT(FCFS):
    """Longest Processing Time Algorithm.

    The algorithm shorts the surgeries from the longest to the shortest.
    """

    def sort(self):
        """Sort the surgeries' durations.

        Returns:
            (list)
        """
        return sorted(super().sort(), reverse=True)


class LOHI(DurationsCriteria):
    """Low And Hi Values Algorithm.

    The class generates a list of surgeries with a low and high values, starting
    with low, high and continues like that.
    """

    def __init__(self, durations):
        super().__init__(durations)
        self.durs = sorted(self.durations)

    def sort(self):
        """Sort the surgeries' durations.

        Returns:
            output (list)
        """
        output = []
        i = 0
        while len(output) < len(self.durs):
            output.append(self.durs[i])
            if len(output) == len(self.durs):
                break

            output.append(self.durs[len(self.durs) - 1 - i])
            i += 1

        return output


class HILO(LOHI):
    """Hi And Low Values Algorithm.

    The class generates a list of surgeries with high and low values, starting
    with high, low and continues like that.
    """

    def __init__(self, durations):
        super().__init__(durations)
        self.durs = sorted(self.durations, reverse=True)


class Valley(DurationsCriteria):
    """Valley Algorithm.

    High values in the beginning and in the end of the list, low values
    in the middle.
    """

    def sort(self):
        """Sort the surgeries' durations.

        Returns:
            (list)
        """
        durs = sorted(self.durations, reverse=True)
        return durs[::2] + sorted(durs[1::2])


class Hill(DurationsCriteria):
    """Hill Algorithm.

    Low values in the beginning and in the end of the list, high values
    in the middle.
    """

    def sort(self):
        """Sort the surgeries' durations.

        Returns:
            (list)
        """
        durs = sorted(self.durations)
        return durs[::2] + sorted(durs[1::2], reverse=True)

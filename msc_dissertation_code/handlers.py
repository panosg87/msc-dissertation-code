import math


class Problem:
    """The class represents the a problem.

    It is responsible of parsing the TXT file and holding all the necessary
    parameters.

    An example of a TXT file: 1_ordays_5_load_0,8_1.txt
    """

    def __init__(self, filename):
        self.filename = filename
        self.rooms = filename.split('_')[2]
        self.load = float(filename.split('_')[4].replace(',', '.'))
        # TODO: parse the capacity from the file.
        # The capacity is to all the files 480. However, this should be parsed
        # from the file.
        self.capacity = 480
        self.solutions = []
        self.raw_parameters = self._parse_file()
        self.durations = self._calc_stats()

    @staticmethod
    def _read_file(filename):
        """Read a TXT file.

        Returns:
            (list): the lines of the file.
        """
        with open(filename, 'r') as f:
            lines = f.readlines()
        return [line.split() for line in lines]

    @staticmethod
    def _get_file_elements(lines):
        """Get elements from the file.

        Args:
            lines (list): corresponds to lines of the TXT file.
        Returns:
            parameters (list) corresponds to the parameters parsed
                from the TXT file.
        """
        parameters = []
        for line_num, line in enumerate(lines):
            if any(x in line for x in ['P1', 'P2', 'P3']):
                parameters = lines[line_num + 1:]
                break
        for elem, param in enumerate(parameters):
            parameters[elem] = [float(i) for i in param[1:4]]
        return parameters

    def _parse_file(self):
        lines = self._read_file(self.filename)
        return self._get_file_elements(lines)

    @staticmethod
    def _calc_mean(m, s, g):
        """Calculate the estimated duration, in minutes.

        The three parameters corresponds to the 3-paramater
        log normal distribution.

        Args:
             m (float)
             s (float)
             g (float)
        """
        return g + (math.e ** (m + (s ** 2) / 2))

    def _calc_stats(self):
        """Calculate estimated surgeries' durations.

        Returns:
            (list): a list of float values.
        """
        return [self._calc_mean(
            row[0], row[1], row[2]) for row in self.raw_parameters]

    # TODO
    def export_solution(self):
        pass
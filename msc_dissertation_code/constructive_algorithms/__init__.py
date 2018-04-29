from msc_dissertation_code.constructive_algorithms.room_criteria import *
from msc_dissertation_code.constructive_algorithms.surgery_criteria import *


surgery_criteria_map = {
    'FCFS': FCFS,
    'SPT': SPT,
    'LPT': LPT,
    'LOHI': LOHI,
    'HILO': HILO,
    'Valley': Valley,
    'Hill': Hill
}

room_criteria_map = {
    'First Fit': FirstFit,
    'Best Fit': BestFit
}
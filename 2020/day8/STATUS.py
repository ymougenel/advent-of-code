#!/usr/bin/env python3

from enum import Enum

class STATUS(Enum):
    IDLE = 6
    READY = 1
    RUNNING = 2
    INFINITE_LOOP = 3
    TERMINATED_OK = 4
    TERMINATED_KO = 5
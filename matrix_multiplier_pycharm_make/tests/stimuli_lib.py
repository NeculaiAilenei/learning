import os
from random import getrandbits
import cocotb
from cocotb.handle import SimHandleBase
from cocotb.triggers import RisingEdge

class matrix_multiplier_stimuli:
    def __init__(self):
        self.NUM_SAMPLES = 3000
        self.DATA_WIDTH = int(cocotb.top.DATA_WIDTH)
        self.A_ROWS = int(cocotb.top.A_ROWS)
        self.B_COLUMNS = int(cocotb.top.B_COLUMNS)
        self.A_COLUMNS_B_ROWS = int(cocotb.top.A_COLUMNS_B_ROWS)
        # Initial values
        cocotb.top.valid_i.value = 0
        cocotb.top.a_i.value = self.create_a(lambda x: 0)
        cocotb.top.b_i.value = self.create_b(lambda x: 0)

    def create_matrix(self, func, rows, cols):
        return [func(self.DATA_WIDTH) for row in range(rows) for col in range(cols)]

    def create_a(self,func):
        return self.create_matrix(func, self.A_ROWS, self.A_COLUMNS_B_ROWS)

    def create_b(self, func):
        return self.create_matrix(func, self.A_COLUMNS_B_ROWS, self.B_COLUMNS)

    def gen_a(self, func=getrandbits):
        """Generate random matrix data for A"""
        for _ in range(self.NUM_SAMPLES):
            yield self.create_a(func)

    def gen_b(self, func=getrandbits):
        """Generate random matrix data for B"""
        for _ in range(self.NUM_SAMPLES):
            yield self.create_b(func)

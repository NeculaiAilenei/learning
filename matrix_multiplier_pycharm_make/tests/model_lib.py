import math
from cocotb.binary import BinaryValue
from cocotb.handle import SimHandleBase
from typing import List

class matrix_multiplier_model:
    def __init__(self, dut : SimHandleBase):
        self.dut = dut

    def model(self, a_matrix: List[int], b_matrix: List[int]) -> List[int]:
        """Transaction-level model of the matrix multipler as instantiated"""
        A_ROWS = self.dut.A_ROWS.value
        A_COLUMNS_B_ROWS = self.dut.A_COLUMNS_B_ROWS.value
        B_COLUMNS = self.dut.B_COLUMNS.value
        DATA_WIDTH = self.dut.DATA_WIDTH.value
        return [
            BinaryValue(
                sum(
                    [
                        a_matrix[(i * A_COLUMNS_B_ROWS) + n]
                        * b_matrix[(n * B_COLUMNS) + j]
                        for n in range(A_COLUMNS_B_ROWS)
                    ]
                ),
                n_bits=(DATA_WIDTH * 2) + math.ceil(math.log2(A_COLUMNS_B_ROWS)),
                bigEndian=False,
            )
            for i in range(A_ROWS)
            for j in range(B_COLUMNS)
        ]

import cocotb
from cocotb.handle import SimHandleBase
from model_lib import matrix_multiplier_model
from monitor_lib import DataValidMonitor

class MatrixMultiplierTester:
    """
    Reusable checker of a matrix_multiplier instance

    Args
        matrix_multiplier_entity: handle to an instance of matrix_multiplier
    """

    def __init__(self, matrix_multiplier_entity: SimHandleBase):
        self.dut = matrix_multiplier_entity

        self.input_mon = DataValidMonitor(
            clk=self.dut.clk_i,
            valid=self.dut.valid_i,
            datas=dict(A=self.dut.a_i, B=self.dut.b_i),
        )

        self.output_mon = DataValidMonitor(
            clk=self.dut.clk_i, valid=self.dut.valid_o, datas=dict(C=self.dut.c_o)
        )

        self.checker = matrix_multiplier_model(self.dut)

        self._checker = None

    def start(self) -> None:
        """Starts monitors, model, and checker coroutine"""
        if self._checker is not None:
            raise RuntimeError("Monitor already started")
        self.input_mon.start()
        self.output_mon.start()
        self._checker = cocotb.start_soon(self._check())

    def stop(self) -> None:
        """Stops everything"""
        if self._checker is None:
            raise RuntimeError("Monitor never started")
        self.input_mon.stop()
        self.output_mon.stop()
        self._checker.kill()
        self._checker = None

    async def _check(self) -> None:
        while True:
            actual = await self.output_mon.values.get()
            expected_inputs = await self.input_mon.values.get()
            expected = self.checker.model(
                a_matrix=expected_inputs["A"], b_matrix=expected_inputs["B"]
            )
            assert actual["C"] == expected


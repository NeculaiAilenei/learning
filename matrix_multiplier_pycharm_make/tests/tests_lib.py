import cocotb
from cocotb.handle import SimHandleBase
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from tester_lib import MatrixMultiplierTester
from stimuli_lib import matrix_multiplier_stimuli

class matrix_multiplier_tests:
    def __init__(self, matrix_multiplier_tests_entity: SimHandleBase):
        self.dut = matrix_multiplier_tests_entity
        cocotb.start_soon(Clock(self.dut.clk_i, 10, units="ns").start())
        self.stimuli = matrix_multiplier_stimuli()
        self.stimuli.NUM_SAMPLES = 1000
        self.tester = MatrixMultiplierTester(self.dut)

    async def test_1(self):
        self.dut._log.info("Initialize and reset")
        self.dut.reset_i.value = 1
        for _ in range(3):
            await RisingEdge(self.dut.clk_i)
        self.dut.reset_i.value = 0
        self.tester.start()
        self.dut._log.info("Test multiplication operations")

        # Generate stimuli
        # Do multiplication operations
        for i, (A, B) in enumerate(zip(self.stimuli.gen_a(), self.stimuli.gen_b())):
            await RisingEdge(self.dut.clk_i)
            self.dut.a_i.value = A
            self.dut.b_i.value = B
            self.dut.valid_i.value = 1
            await RisingEdge(self.dut.clk_i)
            self.dut.valid_i.value = 0
            if i % 100 == 0:
                self.dut._log.info(f"{i} / {self.stimuli.NUM_SAMPLES}")
        await RisingEdge(self.dut.clk_i)
        self.tester.stop()

    async def test_2(self):
        self.dut._log.info("Initialize and reset")
        self.dut.reset_i.value = 1
        for _ in range(3):
            await RisingEdge(self.dut.clk_i)
        self.dut.reset_i.value = 0
        self.tester.start()
        self.dut._log.info("Test multiplication operations")

        # Generate stimuli
        # Do multiplication operations
        for i, (A, B) in enumerate(zip(self.stimuli.gen_a(), self.stimuli.gen_b())):
            await RisingEdge(self.dut.clk_i)
            self.dut.a_i.value = A
            self.dut.b_i.value = B
            self.dut.valid_i.value = 1
            await RisingEdge(self.dut.clk_i)
            self.dut.valid_i.value = 0
            if i % 100 == 0:
                self.dut._log.info(f"{i} / {self.stimuli.NUM_SAMPLES}")
        await RisingEdge(self.dut.clk_i)
        self.tester.stop()

import cocotb
from pycharm import *
from tests_lib import matrix_multiplier_tests

@cocotb.test()
async def multiply_test_1(dut):
    """Test multiplication of many matrices."""
    tests = matrix_multiplier_tests(dut)
    await tests.test_1()

@cocotb.test()
async def multiply_test_2(dut):
    """Test multiplication of many matrices."""
    tests = matrix_multiplier_tests(dut)
    await tests.test_2()

@cocotb.test()
async def multiply_test_3(dut):
    """Test multiplication of many matrices."""
    tests = matrix_multiplier_tests(dut)
    await tests.test_2()

if __name__ == "__main__":
    sys.exit(run_tb())
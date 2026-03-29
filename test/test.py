import cocotb
from cocotb.triggers import Timer

def expected_f(a, b, c):
    return (a & b) | (1 - c)

def expected_y(c):
    return 1 - c

@cocotb.test()
async def test_lab2_logic(dut):
    dut.ena.value = 1
    dut.uio_in.value = 0
    dut.rst_n.value = 1

    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                value = (c << 2) | (b << 1) | a
                dut.ui_in.value = value

                await Timer(1, units="ns")

                f_out = int(dut.uo_out.value) & 0x1
                y_out = (int(dut.uo_out.value) >> 1) & 0x1

                exp_f = expected_f(a, b, c)
                exp_y = expected_y(c)

                assert f_out == exp_f, (
                    f"F mismatch for A={a}, B={b}, C={c}: "
                    f"got {f_out}, expected {exp_f}"
                )

                assert y_out == exp_y, (
                    f"Y mismatch for A={a}, B={b}, C={c}: "
                    f"got {y_out}, expected {exp_y}"
                )

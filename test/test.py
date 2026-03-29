import cocotb
from cocotb.triggers import Timer


def expected_x(a, b, c):
    return (a & b) | (1 - c)


def expected_y(c):
    return 1 - c


@cocotb.test()
async def test_lab2_logic(dut):
    dut.ena.value = 1
    dut.uio_in.value = 0
    dut.rst_n.value = 1
    dut.ui_in.value = 0

    await Timer(20, unit="ns")

    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                value = (c << 2) | (b << 1) | a
                dut.ui_in.value = value

                await Timer(20, unit="ns")

                out_str = str(dut.uo_out.value).lower()

                assert "x" not in out_str, (
                    f"Output still unknown for A={a}, B={b}, C={c}: {out_str}"
                )
                assert "z" not in out_str, (
                    f"Output still high-Z for A={a}, B={b}, C={c}: {out_str}"
                )

                out_val = int(dut.uo_out.value)
                x = out_val & 0b1
                y = (out_val >> 1) & 0b1

                exp_x = expected_x(a, b, c)
                exp_y = expected_y(c)

                assert x == exp_x, (
                    f"x wrong for A={a}, B={b}, C={c}. Got {x}, expected {exp_x}"
                )
                assert y == exp_y, (
                    f"y wrong for A={a}, B={b}, C={c}. Got {y}, expected {exp_y}"
                )

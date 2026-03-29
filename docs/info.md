## How it works

This project implements the Lab 2 combinational logic function:

- F = AB + C'
- Y = C'

Inputs:
- A = ui_in[0]
- B = ui_in[1]
- C = ui_in[2]

Outputs:
- F is mapped to uo_out[0]
- Y is mapped to uo_out[1]

The design is purely combinational and does not require the Tiny Tapeout clock.

## How to test

Apply the three inputs A, B, and C on ui_in[0], ui_in[1], and ui_in[2].

Expected outputs:
- Y = NOT(C)
- F = (A AND B) OR NOT(C)

Truth table:

| A | B | C | Y=C' | F=AB+C' |
|---|---|---|------|---------|
| 0 | 0 | 0 | 1    | 1       |
| 0 | 0 | 1 | 0    | 0       |
| 0 | 1 | 0 | 1    | 1       |
| 0 | 1 | 1 | 0    | 0       |
| 1 | 0 | 0 | 1    | 1       |
| 1 | 0 | 1 | 0    | 0       |
| 1 | 1 | 0 | 1    | 1       |
| 1 | 1 | 1 | 0    | 1       |

## External hardware

No external hardware required.

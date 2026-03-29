module tt_um_yourgithub_lab2_logic (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // Bidirectional inputs
    output wire [7:0] uio_out,  // Bidirectional outputs
    output wire [7:0] uio_oe,   // Bidirectional output enables
    input  wire       ena,      // Always high when design is enabled
    input  wire       clk,      // Clock
    input  wire       rst_n     // Active-low reset
);

    // Lab 2 input mapping
    wire A = ui_in[0];
    wire B = ui_in[1];
    wire C = ui_in[2];

    // Required logic
    wire Y = ~C;
    wire F = (A & B) | (~C);

    // Output mapping
    assign uo_out[0] = F;
    assign uo_out[1] = Y;
    assign uo_out[7:2] = 6'b000000;

    // No bidirectional pins used
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Consume otherwise-unused inputs to avoid warnings
    wire _unused = &{ena, clk, rst_n, uio_in, ui_in[7:3], 1'b0};

endmodule

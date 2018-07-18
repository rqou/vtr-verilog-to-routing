module test(input a, input b, output o_and, output o_or, output o_xor, input clk);

// assign o_and = a & b;
// assign o_or = a | b;
// assign o_xor = a ^ b;

always @(posedge clk) begin
    o_and = a & b;
    o_or = a | b;
    o_xor = a ^ b;
end

endmodule

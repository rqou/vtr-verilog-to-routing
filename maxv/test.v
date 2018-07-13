module test(input a, input b, output o_and, output o_or, output o_xor);

assign o_and = a & b;
assign o_or = a | b;
assign o_xor = a ^ b;

endmodule

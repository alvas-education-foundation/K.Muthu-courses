// Code your testbench here
// or browse Examples
module stimulus;
reg [15:0] in;
wire [4:0] out;
count_0 c0(out,in);
initial
begin
  $dumpfile("dump1.vcd");
  $dumpvars(1,stimulus);
  
in=16'h0000;
#100;
  
in=16'hAFAF;
#100;

in=16'h8BD0;
#100;
  
in=16'hFFFF;
#200;
  
end
  
  initial $monitor($time," - Input=%b ___ No of zeroes=%d",in,out);
  
endmodule

// Code your design here
module count_0(out,in);
input [15:0] in;
output reg [4:0] out;
integer i;
always@(in)
begin
  out=0;
  for(i=0;i<16;i=i+1)
    if (in[i]==1'b0)
      out=out+1;
end
endmodule
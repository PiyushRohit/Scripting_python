module bcd_counter(
  output reg [3:0] count,
  input up,
  input down,
  input clk,
  input reset
);

always @(posedge clk) begin
  if (reset)
    count <= 0;
  else begin
    if (up) begin
      if (count == 9)
        count <= 0;
      else
        count <= count + 1;
    end else if (down) begin
      if (count == 0)
        count <= 9;
      else
        count <= count - 1;
    end
  end
end

endmodule

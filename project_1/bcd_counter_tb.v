module bcd_counter_tb();

  reg clk = 0, up = 0, down = 0, reset = 0;
  wire [3:0] count;

  bcd_counter uut(count, up, down, clk, reset);

  // Generate clock with 10 time unit period
  always #5 clk = ~clk;

  initial begin
    // Enable waveform dump for GTKWave
    $dumpfile("counter.vcd");
    $dumpvars(0, bcd_counter_tb);

    // Monitor all changes live in the console
    $monitor("Time = %0t | clk = %b | reset = %b | up = %b | down = %b | count = %d",
              $time, clk, reset, up, down, count);

    // Test sequence
    $display("----- Applying Reset -----");
    reset = 1; #10;
    reset = 0;
    $display("----- Begin Up Counting -----");
    up = 1;
    repeat(12) #10;  // Should wrap from 9 → 0 and go up again

    $display("----- Begin Down Counting -----");
    up = 0;
    down = 1;
    repeat(12) #10;  // Should wrap from 0 → 9 and go down again

    $display("----- Test up = down = 1 (conflicting input) -----");
    down = 1; up = 1; #20;
    down = 0; up = 0; #10;

    $display("----- Simulation Complete -----");
    $finish;
  end

endmodule

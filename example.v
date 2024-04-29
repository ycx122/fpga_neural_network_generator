
module top_network(
    // Top module interface ports
     input clk,
     input rst,
     input [255:0] data_in_top,
     input data_in_top_vaild,
     output data_in_top_ready,
     output [79:0] data_out_top,
     output data_out_top_vaild,
     input data_out_top_ready
);

// Intermediate wires
wire [1023:0] data_out_layer1;
wire data_out_layer1_vaild;
wire data_out_layer1_ready;
wire [1023:0] data_out_layer2;
wire data_out_layer2_vaild;
wire data_out_layer2_ready;
wire [79:0] data_out_layer3;
wire data_out_layer3_vaild;
wire data_out_layer3_ready;
wire [79:0] data_out_layer4;
wire data_out_layer4_vaild;
wire data_out_layer4_ready;
wire [79:0] data_out_layer5;
wire data_out_layer5_vaild;
wire data_out_layer5_ready;


// Instances of connected layers
fc #(
            .INPUT_WIDTH(8),
            .INPUT_NUM(32),
            .OUTPUT_WIDTH(16),
            .OUTPUT_NUM(64),
            .WEIGHT("weight_1.txt")

        ) fc_layer1 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_in_top),
             .data_in_vaild(data_in_top_vaild),     
             .data_in_ready(data_in_top_ready),             
             .data_out(data_out_layer1),
             .data_out_vaild(data_out_layer1_vaild),     
             .data_out_ready(data_out_layer1_ready)      
             
            // ...
        );
        relu #(
            .INPUT_WIDTH(16),
            .INPUT_NUM(64)

        ) relu_layer2 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer1),
             .data_in_vaild(data_out_layer1_vaild),     
             .data_in_ready(data_out_layer1_ready),   
             .data_out(data_out_layer2),
             .data_out_vaild(data_out_layer2_vaild),     
             .data_out_ready(data_out_layer2_ready)   
             
            // ...
        );
        fc #(
            .INPUT_WIDTH(16),
            .INPUT_NUM(64),
            .OUTPUT_WIDTH(8),
            .OUTPUT_NUM(10),
            .WEIGHT("weight_3.txt")

        ) fc_layer3 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer2),
             .data_in_vaild(data_out_layer2_vaild),     
             .data_in_ready(data_out_layer2_ready),             
             .data_out(data_out_layer3),
             .data_out_vaild(data_out_layer3_vaild),     
             .data_out_ready(data_out_layer3_ready)      
             
            // ...
        );
        relu #(
            .INPUT_WIDTH(8),
            .INPUT_NUM(10)

        ) relu_layer4 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer3),
             .data_in_vaild(data_out_layer3_vaild),     
             .data_in_ready(data_out_layer3_ready),   
             .data_out(data_out_layer4),
             .data_out_vaild(data_out_layer4_vaild),     
             .data_out_ready(data_out_layer4_ready)   
             
            // ...
        );
        fc #(
            .INPUT_WIDTH(8),
            .INPUT_NUM(10),
            .OUTPUT_WIDTH(8),
            .OUTPUT_NUM(10),
            .WEIGHT("weight_5.txt")

        ) fc_layer5 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer4),
             .data_in_vaild(data_out_layer4_vaild),     
             .data_in_ready(data_out_layer4_ready),             
             .data_out(data_out_layer5),
             .data_out_vaild(data_out_layer5_vaild),     
             .data_out_ready(data_out_layer5_ready)      
             
            // ...
        );
        relu #(
            .INPUT_WIDTH(8),
            .INPUT_NUM(10)

        ) relu_layer6 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer5),
             .data_in_vaild(data_out_layer5_vaild),     
             .data_in_ready(data_out_layer5_ready),   
             .data_out(data_out_top),
             .data_out_vaild(data_out_top_vaild),     
             .data_out_ready(data_out_top_ready)   
             
            // ...
        );
        

endmodule

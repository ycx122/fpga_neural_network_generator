
module top_network(
    // Top module interface ports
     input clk,
     input rst,
     input [31:0] data_in_top,
     input data_in_top_vaild,
     output data_in_top_ready,
     output [319:0] data_out_top,
     output data_out_top_vaild,
     input data_out_top_ready
);

// Intermediate wires
wire [287:0] data_out_layer1;
wire data_out_layer1_vaild;
wire data_out_layer1_ready;
wire [31:0] data_out_layer2;
wire data_out_layer2_vaild;
wire data_out_layer2_ready;
wire [31:0] data_out_layer3;
wire data_out_layer3_vaild;
wire data_out_layer3_ready;
wire [2591:0] data_out_layer4;
wire data_out_layer4_vaild;
wire data_out_layer4_ready;
wire [31:0] data_out_layer5;
wire data_out_layer5_vaild;
wire data_out_layer5_ready;
wire [2591:0] data_out_layer6;
wire data_out_layer6_vaild;
wire data_out_layer6_ready;
wire [863:0] data_out_layer7;
wire data_out_layer7_vaild;
wire data_out_layer7_ready;


// Instances of connected layers
cov_ram #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(1),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(9),
            .INIT_FILE("weight_1.txt"),
            .PIC_X(81),
            .PIC_Y(81),
            .MARTIX_LEN(3),
            .PADDING(2),
            .STRIDE(1)

        ) cov_ram_layer1 (
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
        cov #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(9),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(1),
            .COV_KERNEL("weight_2.txt")

        ) cov_layer2 (
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
        relu #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(1)

        ) relu_layer3 (
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
        cov_ram #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(1),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(81),
            .INIT_FILE("weight_4.txt"),
            .PIC_X(81),
            .PIC_Y(81),
            .MARTIX_LEN(9),
            .PADDING(0),
            .STRIDE(8)

        ) cov_ram_layer4 (
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
        pool #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(81),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(1),
            .POOL_METHOD(max)

        ) pool_layer5 (
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
        cov_ram #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(1),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(81),
            .INIT_FILE("weight_6.txt"),
            .PIC_X(9),
            .PIC_Y(9),
            .MARTIX_LEN(9),
            .PADDING(0),
            .STRIDE(1)

        ) cov_ram_layer6 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer5),
             .data_in_vaild(data_out_layer5_vaild),     
             .data_in_ready(data_out_layer5_ready),             
             .data_out(data_out_layer6),
             .data_out_vaild(data_out_layer6_vaild),     
             .data_out_ready(data_out_layer6_ready)      
             
            // ...
        );
        fc #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(81),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(27),
            .WEIGHT("weight_7.txt")

        ) fc_layer7 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer6),
             .data_in_vaild(data_out_layer6_vaild),     
             .data_in_ready(data_out_layer6_ready),             
             .data_out(data_out_layer7),
             .data_out_vaild(data_out_layer7_vaild),     
             .data_out_ready(data_out_layer7_ready)      
             
            // ...
        );
        fc #(
            .INPUT_WIDTH(32),
            .INPUT_NUM(27),
            .OUTPUT_WIDTH(32),
            .OUTPUT_NUM(10),
            .WEIGHT("weight_8.txt")

        ) fc_layer8 (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in(data_out_layer7),
             .data_in_vaild(data_out_layer7_vaild),     
             .data_in_ready(data_out_layer7_ready),             
             .data_out(data_out_top),
             .data_out_vaild(data_out_top_vaild),     
             .data_out_ready(data_out_top_ready)      
             
            // ...
        );
        

endmodule

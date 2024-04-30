class NetworkGenerator:
    def __init__(self):
        self.layers = []

    def add_layer(self, input_width, input_num, output_width, output_num,layer_code):
        layer_params = {
            'input_width': input_width,
            'input_num': input_num,
            'output_width': output_width,
            'output_num': output_num,
            "layer_code":layer_code
        }
        self.layers.append(layer_params)

    def add_fc_layer(self, input_width, input_num, output_width, output_num):
        layer_params = {
            'input_width': input_width,
            'input_num': input_num,
            'output_width': output_width,
            'output_num': output_num,
            "layer_code":'fc'
        }
        self.layers.append(layer_params)

    def add_relu_layer(self, input_width, input_num):
        layer_params = {
            'input_width': input_width,
            'input_num': input_num,
            'output_width': input_width,
            'output_num': input_num,
            "layer_code":'relu'
        }
        self.layers.append(layer_params)   

    def add_cov_ram(self, input_width, input_num,output_width,output_num,pic_x,pic_y,martix_len,need_init,padding,stride):
        layer_params = {
            'input_width': input_width,
            'input_num': input_num,
            'output_width': output_width,
            'output_num': output_num,
            'pic_x':pic_x,
            'pic_y':pic_y,
            'martix_len':martix_len,
            'need_init':need_init,
            'padding':padding,
            'stride':stride,
            "layer_code":'cov_ram'
        }
        self.layers.append(layer_params)   

    def add_cov_layer(self, input_width, input_num, output_width, output_num):
        layer_params = {
            'input_width': input_width,
            'input_num': input_num,
            'output_width': output_width,
            'output_num': output_num,
            "layer_code":'cov'
        }
        self.layers.append(layer_params)

    def add_pool_layer(self, input_width, input_num, output_width, pool_method):
        layer_params = {
            'input_width': input_width,
            'input_num': input_num,
            'output_width': output_width,
            'output_num': 1,
            'pool_method':pool_method,
            "layer_code":'pool'
        }
        self.layers.append(layer_params)


    def generate_fc_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name, weight_file):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

        input_vaild = f"data_out_{prev_instance_name}_vaild" if prev_instance_name else "data_in_top_vaild"
        input_ready = f"data_out_{prev_instance_name}_ready" if prev_instance_name else "data_in_top_ready"

        output_vaild = f"data_out_{instance_name}_vaild" if next_instance_name else "data_out_top_vaild"
        output_ready = f"data_out_{instance_name}_ready" if next_instance_name else "data_out_top_ready"

        return f"""fc #(
            .INPUT_WIDTH({layer_params['input_width']}),
            .INPUT_NUM({layer_params['input_num']}),
            .OUTPUT_WIDTH({layer_params['output_width']}),
            .OUTPUT_NUM({layer_params['output_num']}),
            .WEIGHT("{weight_file}")

        ) fc_{instance_name} (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in({input_wire}),
             .data_in_vaild({input_vaild}),     
             .data_in_ready({input_ready}),             
             .data_out({output_wire}),
             .data_out_vaild({output_vaild}),     
             .data_out_ready({output_ready})      
             
            // ...
        );
        """

    def generate_pool_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

        input_vaild = f"data_out_{prev_instance_name}_vaild" if prev_instance_name else "data_in_top_vaild"
        input_ready = f"data_out_{prev_instance_name}_ready" if prev_instance_name else "data_in_top_ready"

        output_vaild = f"data_out_{instance_name}_vaild" if next_instance_name else "data_out_top_vaild"
        output_ready = f"data_out_{instance_name}_ready" if next_instance_name else "data_out_top_ready"

        return f"""pool #(
            .INPUT_WIDTH({layer_params['input_width']}),
            .INPUT_NUM({layer_params['input_num']}),
            .OUTPUT_WIDTH({layer_params['output_width']}),
            .OUTPUT_NUM({layer_params['output_num']}),
            .POOL_METHOD({layer_params['pool_method']})

        ) pool_{instance_name} (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in({input_wire}),
             .data_in_vaild({input_vaild}),     
             .data_in_ready({input_ready}),             
             .data_out({output_wire}),
             .data_out_vaild({output_vaild}),     
             .data_out_ready({output_ready})      
             
            // ...
        );
        """

    def generate_cov_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name, weight_file):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

        input_vaild = f"data_out_{prev_instance_name}_vaild" if prev_instance_name else "data_in_top_vaild"
        input_ready = f"data_out_{prev_instance_name}_ready" if prev_instance_name else "data_in_top_ready"

        output_vaild = f"data_out_{instance_name}_vaild" if next_instance_name else "data_out_top_vaild"
        output_ready = f"data_out_{instance_name}_ready" if next_instance_name else "data_out_top_ready"

        return f"""cov #(
            .INPUT_WIDTH({layer_params['input_width']}),
            .INPUT_NUM({layer_params['input_num']}),
            .OUTPUT_WIDTH({layer_params['output_width']}),
            .OUTPUT_NUM({layer_params['output_num']}),
            .COV_KERNEL("{weight_file}")

        ) cov_{instance_name} (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in({input_wire}),
             .data_in_vaild({input_vaild}),     
             .data_in_ready({input_ready}),             
             .data_out({output_wire}),
             .data_out_vaild({output_vaild}),     
             .data_out_ready({output_ready})      
             
            // ...
        );
        """

    def generate_cov_ram_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name, weight_file):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

        input_vaild = f"data_out_{prev_instance_name}_vaild" if prev_instance_name else "data_in_top_vaild"
        input_ready = f"data_out_{prev_instance_name}_ready" if prev_instance_name else "data_in_top_ready"

        output_vaild = f"data_out_{instance_name}_vaild" if next_instance_name else "data_out_top_vaild"
        output_ready = f"data_out_{instance_name}_ready" if next_instance_name else "data_out_top_ready"

        return f"""cov_ram #(
            .INPUT_WIDTH({layer_params['input_width']}),
            .INPUT_NUM({layer_params['input_num']}),
            .OUTPUT_WIDTH({layer_params['output_width']}),
            .OUTPUT_NUM({layer_params['output_num']}),
            .INIT_FILE("{weight_file}"),
            .PIC_X({layer_params['pic_x']}),
            .PIC_Y({layer_params['pic_y']}),
            .MARTIX_LEN({layer_params['martix_len']}),
            .PADDING({layer_params['padding']}),
            .STRIDE({layer_params['stride']})

        ) cov_ram_{instance_name} (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in({input_wire}),
             .data_in_vaild({input_vaild}),     
             .data_in_ready({input_ready}),             
             .data_out({output_wire}),
             .data_out_vaild({output_vaild}),     
             .data_out_ready({output_ready})      
             
            // ...
        );
        """

    def generate_relu_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

        input_vaild = f"data_out_{prev_instance_name}_vaild" if prev_instance_name else "data_in_top_vaild"
        input_ready = f"data_out_{prev_instance_name}_ready" if prev_instance_name else "data_in_top_ready"

        output_vaild = f"data_out_{instance_name}_vaild" if next_instance_name else "data_out_top_vaild"
        output_ready = f"data_out_{instance_name}_ready" if next_instance_name else "data_out_top_ready"

        return f"""relu #(
            .INPUT_WIDTH({layer_params['input_width']}),
            .INPUT_NUM({layer_params['input_num']})

        ) relu_{instance_name} (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in({input_wire}),
             .data_in_vaild({input_vaild}),     
             .data_in_ready({input_ready}),   
             .data_out({output_wire}),
             .data_out_vaild({output_vaild}),     
             .data_out_ready({output_ready})   
             
            // ...
        );
        """

    def generate_top_module(self):
        instances = []
        wires = []
        weights_files = []

        for i, params in enumerate(self.layers):
            weight_file = f"weight_{i+1}.txt"
            weights_files.append(weight_file)
            
            if params["layer_code"]== 'fc' :
                prev_instance_name = f"layer{i}" if i > 0 else ""
                next_instance_name = f"layer{i+2}" if i < len(self.layers) - 1 else ""
            
                instances.append(self.generate_fc_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name, weight_file))

            if params["layer_code"]== 'pool' :
                prev_instance_name = f"layer{i}" if i > 0 else ""
                next_instance_name = f"layer{i+2}" if i < len(self.layers) - 1 else ""
            
                instances.append(self.generate_pool_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name))

            if params["layer_code"]== 'cov' :
                prev_instance_name = f"layer{i}" if i > 0 else ""
                next_instance_name = f"layer{i+2}" if i < len(self.layers) - 1 else ""
            
                instances.append(self.generate_cov_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name, weight_file))

            if params["layer_code"]== 'relu' :
                prev_instance_name = f"layer{i}" if i > 0 else ""
                next_instance_name = f"layer{i+2}" if i < len(self.layers) - 1 else ""

                instances.append(self.generate_relu_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name))

            if params["layer_code"]== 'cov_ram' :
                prev_instance_name = f"layer{i}" if i > 0 else ""
                next_instance_name = f"layer{i+2}" if i < len(self.layers) - 1 else ""             

                if params['need_init']==True :
                    instances.append(self.generate_cov_ram_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name , weight_file))
                else :
                    instances.append(self.generate_cov_ram_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name , ''))

            if i < len(self.layers) - 1:  # Add intermediate wires between layers
                wire_width = params['output_width'] * params['output_num']
                wires.append(f"wire [{wire_width-1}:0] data_out_layer{i+1};\n")
                wires.append(f"wire data_out_layer{i+1}_vaild;\n")
                wires.append(f"wire data_out_layer{i+1}_ready;\n")



        top_io_width = self.layers[0]['input_width'] * self.layers[0]['input_num']
        output_port = f"output [{self.layers[-1]['output_width'] * self.layers[-1]['output_num'] - 1}:0] data_out_top"
        
        top_module = f"""
module top_network(
    // Top module interface ports
     input clk,
     input rst,
     input [{top_io_width-1}:0] data_in_top,
     input data_in_top_vaild,
     output data_in_top_ready,
     {output_port},
     output data_out_top_vaild,
     input data_out_top_ready
);

// Intermediate wires
{"".join(wires)}

// Instances of connected layers
{"".join(instances)}

endmodule
"""
        return top_module

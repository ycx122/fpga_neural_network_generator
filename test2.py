class FullyConnectedNetworkGenerator:
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

    def generate_fc_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name, weight_file):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

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
             .data_out({output_wire})
             
            // ...
        );
        """

    def generate_relu_instance(self, layer_params, instance_name, prev_instance_name, next_instance_name, weight_file):
        input_wire = f"data_out_{prev_instance_name}" if prev_instance_name else "data_in_top"
        output_wire = f"data_out_{instance_name}" if next_instance_name else "data_out_top"

        return f"""relu #(
            .INPUT_WIDTH({layer_params['input_width']}),
            .INPUT_NUM({layer_params['input_num']}),
            .OUTPUT_WIDTH({layer_params['output_width']}),
            .OUTPUT_NUM({layer_params['output_num']})
            )

        ) relu_{instance_name} (
            // Define the connections for each instance
             .clk(clk),
             .rst(rst),
             .data_in({input_wire}),
             .data_out({output_wire})
             
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
            
            if params["layer_code"]== 'relu' :
                prev_instance_name = f"layer{i}" if i > 0 else ""
                next_instance_name = f"layer{i+2}" if i < len(self.layers) - 1 else ""
            
                instances.append(self.generate_relu_instance(params, f"layer{i+1}", prev_instance_name, next_instance_name, weight_file))

            if i < len(self.layers) - 1:  # Add intermediate wires between layers
                wire_width = params['output_width'] * params['output_num']
                wires.append(f"wire [{wire_width-1}:0] data_out_layer{i+1};\n")

        top_io_width = self.layers[0]['input_width'] * self.layers[0]['input_num']
        output_port = f"output [{self.layers[-1]['output_width'] * self.layers[-1]['output_num'] - 1}:0] data_out_top"
        
        top_module = f"""
module top_network(
    // Top module interface ports
     input clk,
     input rst,
     input [{top_io_width-1}:0] data_in_top,
     {output_port}
);

// Intermediate wires
{"".join(wires)}

// Instances of fully connected layers
{"".join(instances)}

endmodule
"""
        return top_module

# Usage
network_generator = FullyConnectedNetworkGenerator()
network_generator.add_layer(8, 32, 16, 64,"fc")   # Adding first layer
network_generator.add_layer(16, 64, 16, 64,"relu")   # Adding first layer
network_generator.add_layer(16, 64, 8, 10,"fc")   # Adding second layer
network_generator.add_layer(8, 10, 8, 10,"relu")   # Adding first layer
verilog_code = network_generator.generate_top_module()

print(verilog_code)

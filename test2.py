import verilog_generator
# Usage
network_generator = verilog_generator.NetworkGenerator()
network_generator.add_fc_layer(8, 32, 16, 64)   # Adding first layer
network_generator.add_relu_layer(16, 64)   # Adding first layer
network_generator.add_fc_layer(16, 64, 8, 10)   # Adding second layer
network_generator.add_relu_layer(8, 10)   # Adding first layer
network_generator.add_fc_layer(8, 10, 8, 10)   # Adding second layer
network_generator.add_relu_layer(8, 10)   # Adding first layer
verilog_code = network_generator.generate_top_module()

print(verilog_code)

with open('example.v', 'w') as f:
    f.writelines(verilog_code)
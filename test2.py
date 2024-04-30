import verilog_generator
# Usage
network_generator = verilog_generator.NetworkGenerator()
network_generator.add_cov_ram(32,1,32,9,81,81,3,True,2,1) #储存输入图片
network_generator.add_cov_layer(32, 9, 32, 1)             #增加卷积层
network_generator.add_relu_layer(32, 1)                   #增加relu层
network_generator.add_cov_ram(32,1,32,81,81,81,9,True,0,8)#储存卷积结果
network_generator.add_pool_layer(32,81,32,'max')          #池化层
network_generator.add_cov_ram(32,1,32,81,9,9,9,True,0,1)  #储存池化结果
network_generator.add_fc_layer(32, 81, 32, 27)            #全连接层1
network_generator.add_fc_layer(32, 27, 32, 10)            #全连接层2
verilog_code = network_generator.generate_top_module()    #生成verilog

print(verilog_code)

with open('example.v', 'w') as f:
    f.writelines(verilog_code)
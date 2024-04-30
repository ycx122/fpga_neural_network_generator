# 神经网络硬件加速器生成器
欢迎来到神经网络硬件加速器生成器的GitHub页面！

这个项目旨在通过一个Python脚本来描述并生成整个神经网络模型的verilog hdl代码。通过生成top文件调用使用Verilog实现基本的数字电路元件库，来快速部署和测试简单的神经网络。

## 特性
卷积处理元件 (Convolutional Processing Elements, PE): 使用Verilog描述的卷积PE，针对进行图像相关操作的神经网络层设计。
激活单元 (RLU Units): 可以执行ReLU等常见激活函数的硬件单元。
全连接层单元 （Fully Connected Layer Units）： 用于构建网络中的全连接层的硬件单元。
握手协议: 所有的基础单元都采用统一的握手协议，保证了不同单元之间的无缝连接与通信。
自动化网络构建: 利用Python脚本根据用户定义的网络结构自动生成顶层模块代码，实现快速部署。
## 如何使用
`import verilog_generator`

## 目录结构
`test2.py` 示例

`verilog_generator.py` 生成顶层文件的库

库文件还在建设之中

## 快速开始
请参照以下指南来快速开始使用本项目：

运行test2.py，查看输出

`python3 test2.py`

输出结果放在example.v中

## 贡献
我们欢迎任何形式的贡献，无论是新功能的提议、问题报告还是拉取请求。 如果你想为项目贡献代码，请遵循以下步骤：

Fork仓库并创建你的分支：git checkout -b new-feature-branch
提交你的修改：git commit -am 'Add some feature'
推送到分支：git push origin new-feature-branch
提交拉取请求。
许可证
本项目采用MIT许可证。

希望这个项目能够帮助你在硬件层面上更好地理解和实践神经网络！

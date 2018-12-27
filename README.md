# InterfaceTestYhz
框架：接口测试框架

### 思想：
    该接口自动化框架运用了模块化的思想，将单个模块封装，然后集中处理的原理

### 使用方法：
    运行 main.py 

### 框架介绍
    case        // 用例存放
    common      // 公共方法封装
    config      // 配置文件
    data        // 数据交互封装，解决main压力
    logs        // 日志，待完善
    report      // 报告，待完善
    unil        // 基本模块封装
    run_main    // 运行主方法
    测试数据     // 测试 mock 用
    
1.0.1-SNAPSHOT 更新内容 2018/12/23
-----------------------------------------------------
    1.重新定义config
    2.调整 run_main 运行结构
    3.log系统待完善
    4.html 报告待完善

    目前已知bug：
    1. 保存文件时只能保存到当前文件，否则会导致判断是否运行里面只有一条数据，即写入的时候只写入最后一条，导致无法获取详细数据
    
1.0.0-SNAPSHOT 更新内容 
-----------------------------------------------------
    1.程序已经调试成功，第一版正式上线
    2.excel根据格式写入信息，或自行在config里进行调整
    3.运行main.py即可，测试完成后自动发送邮件
    4.具体信息在config里进行编写   


  
此框架为个人实际所用，仅供测试使用，禁止用于商业用途

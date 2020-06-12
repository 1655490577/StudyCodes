# python版接口自动化测试框架（基础入门版）

## 博客及公众号
- 更多测试分享，请访问[**博客**](https://www.cnblogs.com/uncleyong/p/10530261.html)：https://www.cnblogs.com/uncleyong/p/10530261.html
- 更多测试干货，请关注：**微信公众号：全栈测试笔记**
- ![微信公众号：全栈测试笔记](https://files-cdn.cnblogs.com/files/uncleyong/qzcsbj.bmp)


## 设计思路
- 基础入门版，略


## 目录结构介绍
- bin：可执行文件，程序入口
- conf：配置文件，各种路径配置、ip、端口等
- lib：工具库
- reprot：测试报告
- test_case：测试用例
- log：日志文件
- README.md：说明文件


## 主要技术栈
- requests
- unittest


## 使用说明
- 略


## 待优化功能
- **数据初始化**：比如要登录，保证有正确的账号，新增数据，要保证被新增的数据不存在；其实，业务数据基本上在流程测试过程中就依赖获取到了
- **关联**：依赖数据存全局变量
- **数据分离**：比如，把测试数据抽离到excel中


## 更新历史
- 略


## 参与贡献




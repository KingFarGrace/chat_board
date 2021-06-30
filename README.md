# chat_board
a chat board system

### 目录结构

+ config：存放配置文件（具体说明待扩充，下同）
+ model：model层，存放模型文件
+ template：view层，存放模板（视图）文件
+ view：controller层，存放路由文件及接口方法文件
+ util：存放工具类及常用工具方法
+ test：存放测试文件，包括单元测试及接口测试

跨站脚本（xss）
漏洞成因：用户输入或一些用户可控参数未经处理地输出到页面上
漏洞实现：在xss页面的搜索框中输入“<a href="https://www.baidu.com">百度</a> ”，下方本应出现简单的文本内容变为超链接，诱导正常用户点击进入到其他网站
漏洞解决需要更改的文件：xss.html
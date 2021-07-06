# 系统漏洞描述

### 跨站脚本（XSS）

+ 漏洞成因：用户输入或一些用户可控参数未经处理地输出到页面上
+ 漏洞实现：在xss页面的输入框中输入“<a href="https://www.baidu.com">百度</a> ”更改用户签名，上方本应出现简单的文本内容变为超链接，诱导正常用户点击进入到其他网站
+ 漏洞解决步骤：更改 xss.html 中修改页面标签元素的方法，改为flask中的{{参数}}方法，会将搜索框中输入的内容不转义而全部显示

### 跨站点请求伪造（CSRF）

+ 漏洞成因：用户信任网站a并登录，浏览器存在cookie时打开恶意网站b，b伪造用户向a发送请求
+ 漏洞实现：先在index页面登录账号，再到csrf页面下，点击“csrf漏洞”，转跳到 csrf_hack 页面，依靠浏览器已保存的cookie发送转账请求（项目处于csrf保护状态）
+ 漏洞解决步骤：更改app.py中的CsrfProtect(app)，并把html中带有表单提交的地方添加csrf_token语句即可
  如：<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
+ 需要更改的文件：app.py admin.html csrf.html encrypy.html fileDownload.html fileUpload.html index.html sqlPush.html ultravires.html xss.html（validate.html中 添加 {{
  form.csrf_token() }} ）（待扩充）

### HTTP 请求头注入
+ 漏洞成因：WEB程序代码中把用户提交的参数未做过滤直接输出到HTTP响应头里，导致攻击者可以利用该漏洞来注入到HTTP响应头中实现攻击
+ 漏洞实现：使用外部工具（burpsuite）对请求进行抓包，修改响应头里的字段
+ 漏洞解决步骤：提交请求时将请求中的cookie与session对比，不同则丢弃返回错误

### 目标遍历漏洞

+ 漏洞成因：服务器对于用户发来的url请求不加以限制，使得用户可以任意访问服务器上的目录，从而窃取敏感数据。

+ 漏洞实现：在`nginx.conf`中作如下设置即可实现目录遍历漏洞。

  ```
  location / {
  	autoindex on;
  }
  ```

+ 漏洞解决步骤：将上述配置修改为`autoindex off;`

### SQL 注入

+ 漏洞成因：对用户输入数据的合法性没有判断或过滤不严，在web应用程序中事先定义好的查询语句的结尾上添加额外的SQL语句，在管理员不知情的情况下实现非法操作，以此来实现欺骗数据库服务器执行非授权的任意查询，从而进一步得到相应的数据信息
+ 漏洞实现：后端使用原生sql语句，在sql注入界面，当用户id输入为 '' or 1=1# 时会登录成功，因为#在mysql中也是注释符，输入之后就相当于 select * from login_url where id='' or
  1=1
+ 漏洞解决步骤：flask-sqlalchemy自带ORM，可以防护SQL注入，使用其自带的查询语句即可

### 文件上传

+ 漏洞成因：上传文件的时，未对上传的文件进行严格的验证和过滤
+ 漏洞实现：后端未进行文件验证和过滤操作，可接受来自于前端的任意文件或脚本
+ 漏洞解决步骤：定义pdf文件的配置文件pdfconfig，对上传的文件惊醒验证过滤操作，限制其只能为pdf文件

### 文件下载

+ 漏洞成因：文件下载采用get方法传输数据，没有对下载的文件做限制，直接通过路径对文件进行下载，恶意用户就可以利用这种方式下载服务器的各种文件
+ 漏洞实现：前端传入的参数是文件的路径，在上方输入网址：http://127.0.0.1:port/download?filepath=(本地文件路径)即可下载本地文件
+ 漏洞解决步骤：前端传入的数据仅仅为文件名，后端拼接可下载的pdf文件路径与文件名

### 日志不全

+ 漏洞成因：开发者没有在程序内引入/编写日志，对于某些系统异常或遭受到的攻击没有办法追踪定位，以至于无法解决。
+ 漏洞实现：不使用python内置库logging编写日志即可实现漏洞（其他第三方日志库同理），本程序内只要在入口文件`app.py`中将导入的日志配置类`logconfig`注释掉即可实现漏洞。
+ 漏洞解决步骤：对后端的每一个可调用方法的不同逻辑分支均编写相对应的日志，准确描述该操作的时间，操作的目标，操作的结果以及输出的内容，分层调用的方法则在每一层添加逻辑关系相连的日志，最终在日志文件中输出操作栈。

### 渗透测试漏洞

1. 身份验证漏洞
    + 漏洞成因：程序对于用户敏感信息（如密码）没有加以限制，使得用户有意或者无意的设置了过于简单的密码，最终被攻击者暴力破解。
    + 漏洞实现：对于前端表单数据，在后端不设置相对应的验证器就可以实现漏洞，本程序中，在`views.form.register_form`中取消类变量`password`定义中的验证器赋值部分即可。
    + 漏洞解决步骤：在`views.form.register_form`中添加对`password`变量的验证器，限定用户只能设置8-16位包含大小写字母和数字的密码。
2. 越权访问漏洞
    + 漏洞成因：程序中没有鉴权模块或过滤器，仅在前端做了限制，使得用户可以通过直接修改url发起get请求进入任意页面。
    + 漏洞实现：仅在模板文件中的表单部分限制用户输入，而在后端不设置鉴权逻辑，从而当用户修改url时，可以向后端发起任意请求并访问任意路由。
    + 漏洞解决步骤：在`route.py`文件中的`horizon`（水平越权漏洞）和`vertical`（垂直越权漏洞）两个路由中，把注释掉的鉴权逻辑启用，并把缺陷代码注释掉，即可修复漏洞。
3. 敏感数据明文传输
    + 漏洞成因：程序中没有实现对敏感数据的加密保护，使得前端发给后端的请求中可以直接看到敏感数据，降低了安全性。
    + 漏洞实现：`index.html` 页面中的登录模块存在此漏洞。
    + 漏洞解决步骤：使用RSA非对称加密对程序中的敏感数据进行加密（如用户登录密码）。前端使用`jsencrypt`库对表单数据进行加密（加密公钥由后端提供），后端使用`pycryptodome`库对数据进行解密（解密私钥由脚本产生并保存在程序内部），从而实现在传输过程中对敏感信息进行保护。本程序中的`router.encrypt`路由中实现了完整的加密传输过程。
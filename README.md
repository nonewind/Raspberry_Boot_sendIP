# 树莓派开机主动发送自己的局域网ip/外网ip到你的微信

- 之前因为第一次开机树莓派连接不上遇到了很多问题，不知道是我的问题还是电脑的问题 所幸，看到了大神写了一个Raspberry开机发送自己的IP到mail 所以就突发奇想 我要发送到Wechat上！

- 使用[berryconda](https://github.com/jjhelmus/berryconda) 基于 py3.6

- 利用方糖server酱 进行微信消息推送 具体请查阅[http://sc.ftqq.com/3.version]

## 操作步骤

- 下载目录下的 boot_getIP_send_Wechat.py 到你的 Raspberry 
- 进入方糖的[http://sc.ftqq.com/3.version] 登陆拿到你的key 并将code中的key替换成你的
- 远程连接Raspberry 
- 输入 sudo nano /etc/rc.local 
- 在 exit 0 之前加入一行执行代码  eg: python /绝对路径/boot_getIP_send_Wechat.py >> /绝对路径/log.log 2>&1  保存并退出
- 重启树莓派 等待15s 看看手机微信！

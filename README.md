# PT Auto Sign

NexusPHP PT 站点自动签到脚本

## 安装依赖

```bash
pip install toml requests
```

## 配置

复制 `config.example.toml` 为 `config.toml`，填入你的站点信息：

```toml
[global]
user_agent = "Mozilla/5.0 ..."

[sites.SITENAME]
cookie = "从浏览器复制的完整 cookie"
home_url = "https://site.com/index.php"
sign_url = "https://site.com/attendance.php"
```

### 获取 Cookie

登录 PT 站点后，按 F12 打开开发者工具，在 Network 中刷新页面，点击任意请求，复制 Request Headers 中的 `Cookie` 值。

## 运行

```bash
python pt_sign.py
```

## 定时任务 (Linux crontab)

```bash
crontab -e
```

每天早上 6 点签到：

```
0 6 * * * cd /path/to/pt-auto-sign && /usr/bin/python3 pt_sign.py >> /path/to/pt-auto-sign/sign.log 2>&1
```

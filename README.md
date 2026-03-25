# PT Auto Sign

NexusPHP PT 站点自动签到脚本

## 安装依赖

```bash
pip install toml requests
```

## 配置

复制 `config.example.toml` 为 `config.toml`。

### 站点配置

```toml
[global]
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# 有签到页的站点
[sites.站点名称]
cookie = "c_secure_uid=xxx; c_secure_pass=xxx"
home_url = "https://site.com/index.php"
sign_url = "https://site.com/attendance.php"

# 无签到页的站点（仅访问主页）
[sites.另一个站点]
cookie = "c_secure_uid=xxx"
home_url = "https://site2.com/index.php"

# 使用 Authorization 的站点
[sites.OAUTH站点]
authorization = "Bearer xxxxx"
home_url = "https://site3.com/index.php"
sign_url = "https://site3.com/attendance.php"
```

### 获取 Cookie / Authorization

登录 PT 站点后，按 F12 打开开发者工具，在 Network 中刷新页面，点击任意请求：

- 复制 Request Headers 中的 `Cookie`
- 或复制 `Authorization` 值

## 运行

```bash
python pt_sign.py
```

## 定时任务 (Linux crontab)

```bash
crontab -e
```

每天早上 6 点执行：

```
0 6 * * * cd /path/to/pt-auto-sign && /usr/bin/python3 pt_sign.py >> sign.log 2>&1
```

外部控制何时执行及随机延迟。

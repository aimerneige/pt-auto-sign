#!/usr/bin/env python3
"""
NexusPHP PT 站点自动签到脚本
配置文件格式: config.toml
"""

import toml
import requests
import re
import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def load_config(config_path: str = "config.toml") -> dict:
    """加载配置文件"""
    if not os.path.exists(config_path):
        logger.error(f"配置文件 {config_path} 不存在")
        sys.exit(1)
    return toml.load(config_path)


def sign_in(session: requests.Session, site_name: str, site_config: dict, headers: dict) -> str:
    """执行签到"""
    url = site_config["sign_url"]
    data = {"action": "addbonus"}

    try:
        r = session.post(url, headers=headers, data=data, timeout=30)
        r.encoding = "utf-8"

        msg = re.search(r"今天签到您获得(.*?)点魔力值", r.text)
        if msg:
            return f"签到成功: 获得 {msg.group(1)} 魔力值"

        if "已经签到过了" in r.text or "今天已经签到" in r.text:
            return "今日已签到"

        return f"签到结果未知: {r.text[:200]}"
    except Exception as e:
        return f"签到失败: {e}"


def check_cookie(session: requests.Session, site_name: str, site_config: dict, headers: dict) -> bool:
    """检查 cookie 是否有效"""
    try:
        r = session.get(site_config["home_url"], headers=headers, timeout=30)
        r.encoding = "utf-8"
        return bool(re.search(r"欢迎", r.text))
    except:
        return False


def run_single_site(site_name: str, site_config: dict, global_headers: dict):
    """处理单个站点"""
    logger.info(f"开始处理站点: {site_name}")

    session = requests.Session()
    headers = {
        "User-Agent": global_headers.get("user_agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"),
        "Cookie": site_config["cookie"],
    }

    if not check_cookie(session, site_name, site_config, headers):
        logger.warning(f"[{site_name}] Cookie 可能已失效，跳过签到")
        return

    result = sign_in(session, site_name, site_config, headers)
    logger.info(f"[{site_name}] {result}")


def main():
    config = load_config()
    global_headers = config.get("global", {})

    sites = config.get("sites", {})

    for site_name, site_config in sites.items():
        run_single_site(site_name, site_config, global_headers)

    logger.info("所有站点处理完成")


if __name__ == "__main__":
    main()

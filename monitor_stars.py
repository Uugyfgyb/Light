import requests
import time
import sys

def get_repo_stars(repo_full_name):
    """获取指定仓库的 Star 数量"""
    url = f"https://api.github.com/repos/{repo_full_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("stargazers_count", 0)
    except Exception as e:
        print(f"获取 Star 数量失败: {e}")
        return None

def monitor_stars(repo_full_name, threshold, interval=60):
    """
    监控 Star 数量
    :param repo_full_name: 仓库全名
    :param threshold: 触发通知的 Star 数量阈值
    :param interval: 检查间隔（秒），默认 60 秒
    """
    print(f"开始监控 {repo_full_name}，目标阈值: {threshold}，检查间隔: {interval}秒")
    
    while True:
        current_stars = get_repo_stars(repo_full_name)
        if current_stars is not None:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 当前 Star 数量: {current_stars}")
            
            if current_stars >= threshold:
                print(f"🎉 恭喜！{repo_full_name} 的 Star 数量已达到阈值 {threshold}！")
                # 这里可以扩展通知方式，例如发送邮件、飞书/钉钉机器人等
                send_notification(repo_full_name, current_stars)
                break
        
        time.sleep(interval)

def send_notification(repo, stars):
    """
    发送通知的占位函数
    用户可以根据需要在此处集成具体的通知 API（如 Webhook）
    """
    print(f"【通知】仓库 {repo} 已达成目标，当前 Star 数: {stars}")

if __name__ == "__main__":
    # 默认配置
    REPO = "Uugyfgyb/Light"
    THRESHOLD = 10  # 默认阈值为 10，您可以根据需要修改
    INTERVAL = 300  # 默认每 5 分钟检查一次
    
    # 允许通过命令行参数覆盖
    if len(sys.argv) > 1:
        THRESHOLD = int(sys.argv[1])
    
    monitor_stars(REPO, THRESHOLD, INTERVAL)

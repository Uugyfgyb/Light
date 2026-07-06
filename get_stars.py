import requests
import sys

def get_repo_stars(repo_full_name):
    """
    获取指定 GitHub 仓库的 Star 数量
    :param repo_full_name: 仓库全名 (例如 'Uugyfgyb/Light')
    """
    url = f"https://api.github.com/repos/{repo_full_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        stars = data.get("stargazers_count", 0)
        print(f"仓库 '{repo_full_name}' 的 Star 数量为: {stars}")
        return stars
    except requests.exceptions.RequestException as e:
        print(f"获取数据时出错: {e}")
        return None

if __name__ == "__main__":
    # 默认查询当前仓库，也可以通过命令行参数指定其他仓库
    target_repo = sys.argv[1] if len(sys.argv) > 1 else "Uugyfgyb/Light"
    get_repo_stars(target_repo)

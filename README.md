# HearthstoneQueue-PeerToPeer-NoServer

# 自动化《炉石传说》排队工具

## 功能概述
HearthstoneQueueCloudless 是一个自动化工具，通过监测在线笔记本网站的个人主页帖子标题变化，实现自动开启《炉石传说》的排队功能。

### 主要功能

#### 监测帖子标题
- 持续监测指定网址的第一个帖子的标题变化。

#### 自动排队
- 一旦发现标题变化，自动启动《炉石传说》的排队功能。

#### 远程控制
- 在下班或放学途中，让电脑自动进入游戏开始排队。

## 环境配置

### 先决条件
确保已安装Python和相关库。使用以下命令安装依赖：

```bash
pip install -r requirements.txt

## 配置文件

编辑 `config.json` 文件。填入你的 Cookie 信息，并输入你的战网安装目录中 `Battle.net.exe` 的绝对路径。

```json
{
    "cookie": "你的Cookie",
    "battle_net_path": "C:\\Program Files (x86)\\Battle.net\\Battle.net.exe"
}

# HearthstoneQueue-PeerToPeer-NoServer

## 自动化《炉石传说》排队工具

### 功能概述
通过监测在线笔记本网站 [http://www.xnote.cn/note/](http://www.xnote.cn/note/) 个人主页上第一个帖子的标题变化，通过手机远程自动开启电脑上《炉石传说》的排队功能。

### 使用步骤

1. **注册账号**
   在网站 [http://www.xnote.cn/note/](http://www.xnote.cn/note/) 上注册一个账号。

2. **配置环境**
   确保你的计算机上已安装 Python。  
   在命令行中输入以下命令以安装所需的依赖：
   ```bash
   pip install -r requestment.txt

3.  **编辑配置文件**
   打开 config.json 文件，填写以下信息：

   ```bash
   Cookie: 输入你在网站上的 Cookie 信息。
   Battle.net 路径: 填入你的战网安装目录内的 Battle.net.exe 的绝对路径。
   ```
4.  **启动程序**
   完成上述步骤后，使用```python main.py```启动程序，它将持续监测帖子标题变化，并在发现变化时自动启动《炉石传说》的排队功能。

### 注意事项
请确保你的电脑在监测期间保持开机状态。
监测频率及其他参数可根据需求自行调整。

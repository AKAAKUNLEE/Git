以下是 **QuickCookie** 项目的 `README.md` 文件内容，详细介绍了项目的功能、使用方法、安装步骤以及扩展功能。

---

# QuickCookie

**QuickCookie** 是一款基于Python的工具，能够快速获取全网视频平台的cookie。它支持多平台操作，提供简单易用的命令行工具，并将cookie保存为本地JSON文件，方便后续使用。

## 功能特点

- **多平台支持**：默认支持Bilibili、YouTube、优酷等视频平台，可轻松扩展。
- **快速获取**：使用Selenium自动化工具，快速获取目标平台的cookie。
- **保存为JSON**：将获取的cookie保存为结构化JSON文件，便于后续处理。
- **命令行支持**：通过命令行参数指定目标平台，操作简单易用。

## 安装步骤

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/QuickCookie.git
cd QuickCookie
```

### 2. 安装依赖

确保你已经安装了Python 3.x，然后运行以下命令安装依赖：

```bash
pip install -r requirements.txt
```

### 3. 下载ChromeDriver

1. 下载与Chrome浏览器版本匹配的 [ChromeDriver](https://sites.google.com/chromium.org/driver/)。
2. 将 `quickcookie.py` 文件中的 `/path/to/chromedriver` 替换为ChromeDriver的实际路径。

## 使用方法

### 命令行

运行以下命令获取指定平台的cookie：

```bash
python quickcookie.py --platform <platform_name>
```

支持的平台：`bilibili`、`youtube`、`youku`。

例如，获取Bilibili的cookie：

```bash
python quickcookie.py --platform bilibili
```

### 输出结果

获取的cookie会保存在 `cookies/` 目录下，文件名为 `{platform}_cookies.json`。例如：

- `cookies/bilibili_cookies.json`
- `cookies/youtube_cookies.json`

## 示例输出

`cookies/bilibili_cookies.json` 文件内容示例：

```json
[
    {
        "name": "SESSDATA",
        "value": "1234567890abcdef",
        "domain": ".bilibili.com",
        "path": "/",
        "expires": 1698765432,
        "httpOnly": true,
        "secure": true
    },
    ...
]
```

## 扩展功能

### 1. 添加新平台

在 `quickcookie.py` 文件的 `PLATFORMS` 字典中添加新平台。例如：

```python
PLATFORMS["iqiyi"] = "https://www.iqiyi.com"
```

### 2. 处理登录

如果需要登录才能获取cookie，可以使用Selenium模拟登录操作。例如：

```python
# 查找登录按钮并点击
driver.find_element(By.CLASS_NAME, "login-button").click()
```

### 3. GUI支持

可以使用Tkinter或PyQt为工具添加图形界面。

## 注意事项

1. **合法性**：使用本工具时，请确保遵守相关法律法规，并获得用户的明确同意。
2. **反爬虫机制**：部分平台可能有反爬虫机制，需进一步处理验证码等问题。
3. **更新ChromeDriver**：确保ChromeDriver与Chrome浏览器的版本一致。

## 贡献

欢迎提交Issue或Pull Request，帮助改进本项目！

## 许可证

本项目采用 [MIT License](LICENSE)。


# 🐍 pystudy

> 一份从零开始的 Python 学习记录 —— 覆盖基础语法、面向对象、模块包、数据分析、网络爬虫，直到 Web 开发与 AI 应用落地。

这个仓库不是某个单一项目，而是我学习 Python 全过程的**代码笔记**：每个文件都围绕一个具体知识点写成，注释详尽，可以直接运行。

---

## 📌 仓库亮点

| 模块 | 一句话说明 |
| --- | --- |
| [🧠 AI应用](./AI应用/) | Streamlit 搭建 AI 对话应用的 4 个演进版本（非流式 → 流式 → 提示词工程 → 多会话持久化） |
| [🌐 Web应用](./Web应用/) | ⭐ **「汉字谜盒」** —— FastAPI + 大模型实现的汉字字谜游戏，完整前后端，[点此查看详细文档](./Web应用/README.md) |
| [🕷 爬虫](./爬虫/) | requests + lxml/XPath 实战，抓取 TMDB 电影榜单并落盘 CSV |
| [📊 数据分析](./数据分析/) | Jupyter 笔记本：pandas 数据处理 + matplotlib 可视化的完整练习 |
| [🧱 面向对象](./面向对象/) | 从类与对象到封装/继承/多态，附一个命令行图书管理系统 |
| [📦 module](./module/) | 自定义模块与包的导入机制、`__all__` 与 `__name__` 的用法 |

---

## 🗂 目录结构

```
pystudy/
├── 📄 *.py                 # 根目录：Python 基础语法练习（22 个独立脚本）
│
├── 🧠 AI应用/              # Streamlit + 大模型对话应用
│   ├── ai_partner_1.py     #   最小闭环：聊天界面 + 非流式输出
│   ├── ai_partner_2.py     #   进阶：stream=True 流式打字机效果
│   ├── ai_partner_3.py     #   进阶：侧边栏 + 提示词工程（角色扮演）
│   ├── ai_partner_4.py     #   完整版：多会话管理 + JSON 持久化
│   ├── streamlit入门.py    #   Streamlit 常用组件总览
│   ├── 文件操作入门.py      #   open() 读写、with 语句、相对/绝对路径
│   ├── json模块入门.py      #   json.dump/load、ensure_ascii=False
│   ├── 阿里云百炼api调用.py  #   纯控制台版大模型 API 调用
│   ├── resources/          #   示例素材（图片/音频/视频/文本）
│   └── sessions/           #   ai_partner_4.py 落盘的会话记录
│
├── 🌐 Web应用/             # ⭐ FastAPI + AI 字谜游戏「汉字谜盒」
│   ├── README.md           #   👈 完整项目文档（安装/配置/接口/FAQ）
│   ├── main.py             #   FastAPI 主程序：6 个接口 + 全局异常处理
│   ├── FastAPI入门.py      #   27 行最小 FastAPI 示例
│   ├── static/             #   原生前端：index.html / style.css / app.js
│   └── sessions/           #   会话存档（JSON）
│
├── 🕷 爬虫/                # 网络爬虫实战
│   ├── 网络机器人入门.py    #   requests 发请求，抓取 TIOBE 榜单
│   ├── 网页解析.py         #   lxml + XPath 解析本地 HTML
│   ├── Xpath语法.py        #   XPath 语法专项练习
│   ├── 案例-电影榜单1.py   #   实战：抓取 TMDB Top Rated → CSV（单页）
│   ├── 案例-电影榜单2.py   #   实战：翻页抓取 + 正则提取
│   ├── csv入门.py          #   CSV 读写两种方式
│   ├── resources/          #   待解析的 HTML 与图片素材
│   └── csv_data/           #   爬取结果（movie_list*.csv）
│
├── 📊 数据分析/            # pandas + matplotlib（Jupyter）
│   ├── Jupyter入门.ipynb           #  Notebook 基本操作
│   ├── pandas入门.ipynb            #  DataFrame 构造与统计聚合
│   ├── pandas-DataFrame与Series.ipynb  # 4 种构造法与常用属性
│   ├── 数据读取与写入.ipynb         #  read_csv、iloc vs loc、布尔过滤
│   ├── 数据清洗.ipynb              #  缺失值 / 重复值 / 异常值
│   ├── 数据排序与分组.ipynb         #  sort_values、groupby、agg
│   ├── Matplotlib入门.ipynb        #  折线图 + 中文显示配置
│   ├── Matplotlib图表.ipynb        #  子图、柱状图、饼图、savefig
│   ├── top300电影榜单分析.ipynb     #  综合实战：2×2 子图看板
│   ├── TMDB-TOP300电影榜单数据统计.py # 上述 Notebook 的脚本版（含类型注解）
│   └── data/                       #  movies.csv、sales.csv 等数据源
│
├── 🧱 面向对象/            # 面向对象编程
│   ├── 类和对象.py          #   类的定义与实例化
│   ├── 实例方法.py          #   __init__ 与 self
│   ├── 实例属性与类属性.py   #   两者区别与查找顺序
│   ├── 魔法方法.py          #   __str__、__repr__ 等
│   ├── 案例.py              #   综合小案例
│   └── 面向对象高级/         #   封装 / 继承 / 多态 / 鸭子类型
│       └── 图书管理系统.py   #   命令行版图书借阅系统（ABC 抽象类 + JSON 存储）
│
├── 📦 module/              # 模块与包
│   ├── main.py             #   模块导入的几种写法
│   ├── my_fun.py           #   自定义模块，演示 __all__ 与 __name__
│   ├── 导入包中的模块.py    #   包的导入方式
│   └── utils/              #   自定义包（含 __init__.py）
│
└── 📄 根目录脚本            # Python 基础语法专项
    ├── 数据类型.py、数据容器-列表/元组/字典/集合/字符串.py
    ├── 函数基础.py、函数进阶.py
    ├── 异常.py、导入模块.py、match模式匹配.py
    ├── zip函数.py、join函数 和 sort函数.py、sort()与lambda 匿名函数.py
    ├── defaultdict调用.py、数值交换.py、for循环打印乘法表.py、打印国际象棋.py
    └── 练习01.py ~ 练习03.py   # LeetCode 风格算法题（atoi、最长回文子串、盛水容器）
```

---

## ⚙️ 环境要求

| 项目 | 版本 / 说明 |
| --- | --- |
| Python | **3.12**（`__pycache__` 中可见 `cpython-312`） |
| 编辑器 | PyCharm（仓库含 `.idea/`）或任意支持 Python 的 IDE |

### 第三方依赖

不同模块用到的库不同，按需安装即可：

```bash
# 🌐 Web 应用
pip install fastapi uvicorn openai pydantic

# 🧠 AI 应用（Streamlit 版）
pip install streamlit openai

# 🕷 爬虫
pip install requests lxml

# 📊 数据分析
pip install pandas matplotlib jupyter
```

> 仓库目前**没有** `requirements.txt`，因为各模块依赖差异较大、互相独立。建议按需安装，或进入某个子项目目录后单独固化依赖。

---

## 🚀 快速开始

### 想看完整项目？从这里开始

```bash
cd Web应用
python main.py
# 浏览器打开 http://localhost:8000
```

这是仓库里**唯一一个完整的前后端项目** —— 「汉字谜盒」AI 字谜游戏。运行前需配置大模型 API Key，详见 **[Web应用/README.md](./Web应用/README.md)**。

### 想按顺序学？推荐这条路线

```
第 1 站  根目录 *.py              Python 语法地基（数据类型、容器、函数、异常）
   ↓
第 2 站  面向对象/                 类与对象 → 封装 / 继承 / 多态 → 图书管理系统
   ↓
第 3 站  module/                  模块与包的导入机制
   ↓
第 4 站  爬虫/                     requests 抓取 → XPath 解析 → CSV 落盘
   ↓
第 5 站  数据分析/                 pandas 清洗 → 分组聚合 → matplotlib 可视化
   ↓
第 6 站  AI应用/                  大模型 API → Streamlit 界面 → 多会话应用
   ↓
第 7 站  Web应用/                 FastAPI 后端 → 前后端联调 → AI 产品化
```

每一步的产物都会成为下一步的输入：爬虫抓来的 `movie_list.csv` 正是数据分析模块的素材，数据分析用到的 `movies.csv` 又与爬虫实战呼应。

---

## 💡 学习心得

记录几个踩过的坑，供后来者参考：

1. **相对路径的坑** —— `Web应用/` 和 `AI应用/` 中的资源路径都是相对的，必须在对应目录下运行脚本，否则会报文件不存在。更稳妥的做法是用 `os.path.join(os.path.dirname(__file__), "static")` 基于文件位置拼绝对路径。

2. **`iloc` 与 `loc` 的边界差异** —— `iloc` 按行号切片**不含**结束位置，`loc` 按行标签切片**包含**结束位置，初学者极易混淆。

3. **中文处理三件套** —— 写 JSON 用 `ensure_ascii=False`，读 CSV 注意 `utf-8-sig`，matplotlib 中文要设置 `plt.rcParams['font.sans-serif']`。

4. **`__name__ == "__main__"` 的价值** —— 既是模块测试代码的开关，也是 FastAPI 项目区分"直接启动"与"被导入"的标准写法。

5. **从 Streamlit 到 FastAPI** —— Streamlit 适合快速验证 AI 想法，但要做出可定制的产品界面，还是需要 FastAPI 提供接口 + 自己写前端。仓库里两条路线都走了一遍。

---

## ⚠️ 注意事项

- **`sessions/` 目录**：`Web应用/sessions/` 与 `AI应用/sessions/` 存放的是真实对话记录，建议在 `.gitignore` 中排除，避免上传个人信息。
- **API Key 安全**：所有涉及大模型的脚本都通过环境变量 `DASHSCOPE_API_KEY` 读取密钥，**切勿硬编码进代码**。上传到 GitHub 前请确认没有明文密钥。
- **大文件**：`AI应用/resources/` 中有 20 MB 的音频和 35 MB 的视频，提交前请评估是否必要，或考虑使用 Git LFS。
- **爬虫合规**：`爬虫/` 中的代码仅供学习，实际抓取请遵守目标网站的 `robots.txt` 及相关法律法规，控制请求频率。

---

## 📄 许可

学习用途代码，可自由参考。部分数据源来自公开网站，版权归原作者所有。

---

<div align="center">

**如果这个项目对你有帮助，欢迎点个 ⭐ Star**

*持续更新中...*

</div>

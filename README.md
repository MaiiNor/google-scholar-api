# 🔍 Google Scholar API - OpenClaw Skill

[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/MaiiNor/google-scholar-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![SerpAPI](https://img.shields.io/badge/SerpAPI-Integrated-orange)](https://serpapi.com)

**通过 SerpAPI 实现的 Google Scholar 学术搜索工具 - 为研究人员和学生提供强大的论文搜索和下载功能**

## 🎯 为什么选择这个工具？

Google Scholar 没有官方 API，手动搜索和下载论文效率低下。这个工具可以：

- ✅ **批量搜索**：一次搜索获取大量相关论文
- ✅ **智能过滤**：按年份、引用数、相关性排序
- ✅ **自动下载**：一键下载可用的 PDF 文件
- ✅ **结构化数据**：获取标题、作者、摘要、引用等完整信息
- ✅ **集成 OpenClaw**：在 AI 助手中直接使用学术搜索功能

## ✨ 核心特性

### 🔍 高级搜索功能
- **多关键词搜索**：支持复杂查询和布尔运算符
- **高级过滤**：按年份、作者、期刊、引用数过滤
- **排序选项**：相关性、日期、引用数排序
- **分页支持**：获取大量搜索结果

### 📄 论文管理
- **批量下载**：自动下载多篇论文的 PDF
- **元数据提取**：提取标题、作者、摘要、DOI 等信息
- **引用分析**：分析论文的引用次数和趋势
- **本地存储**：结构化保存搜索结果和下载文件

### 🔧 开发者友好
- **Python API**：简单的函数调用接口
- **命令行工具**：方便的命令行界面
- **配置灵活**：支持环境变量和配置文件
- **错误处理**：完善的错误处理和重试机制

### 📊 数据导出
- **JSON 导出**：结构化数据导出
- **CSV 导出**：表格格式，便于分析
- **BibTeX 导出**：引用管理格式
- **Markdown 报告**：生成可读性强的报告

## 🚀 快速开始

### 安装方法

#### 方法1：作为 OpenClaw 技能安装
```bash
# 从 GitHub 安装
openclaw skills install https://github.com/MaiiNor/google-scholar-api

# 或从本地目录安装
openclaw skills install ./google-scholar-api
```

#### 方法2：作为 Python 包使用
```bash
# 克隆仓库
git clone https://github.com/MaiiNor/google-scholar-api.git
cd google-scholar-api

# 安装依赖
pip install -r scripts/requirements.txt

# 设置 API 密钥
export SERP_API_KEY="your_serpapi_key_here"
```

#### 方法3：直接运行脚本
```bash
# 下载脚本
curl -O https://raw.githubusercontent.com/MaiiNor/google-scholar-api/main/scripts/google_scholar_search.py

# 运行搜索
python google_scholar_search.py "artificial intelligence"
```

### 基本使用

#### 1. 简单搜索
```bash
# 搜索论文
python scripts/google_scholar_search.py "machine learning"

# 指定数量
python scripts/google_scholar_search.py "deep learning" --num 20

# 按年份过滤
python scripts/google_scholar_search.py "transformer" --year 2020
```

#### 2. 高级搜索
```bash
# 多关键词搜索
python scripts/google_scholar_search.py "attention mechanism" "natural language processing"

# 布尔搜索
python scripts/google_scholar_search.py "GAN OR generative adversarial network"

# 作者搜索
python scripts/google_scholar_search.py "author:Yoshua Bengio"
```

#### 3. 下载论文
```bash
# 搜索并下载
python scripts/google_scholar_search.py "reinforcement learning" --download

# 指定下载目录
python scripts/google_scholar_search.py "computer vision" --download --output ./papers/

# 限制下载数量
python scripts/google_scholar_search.py "quantum computing" --download --limit 10
```

## 📖 详细使用指南

### API 密钥配置

#### 获取 SerpAPI 密钥
1. 访问 [SerpAPI 官网](https://serpapi.com)
2. 注册账号（免费计划：100次搜索/月）
3. 在仪表板获取 API 密钥

#### 配置密钥
```bash
# 方法1：环境变量（推荐）
export SERP_API_KEY="your_serpapi_key_here"

# 方法2：配置文件
echo 'SERP_API_KEY="your_serpapi_key_here"' > ~/.google_scholar_config

# 方法3：Python 代码中设置
import os
os.environ["SERP_API_KEY"] = "your_serpapi_key_here"
```

### 搜索参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `--num` | 结果数量 (1-100) | `--num 50` |
| `--start` | 起始位置 | `--start 10` |
| `--year` | 年份过滤 | `--year 2023` |
| `--sort` | 排序方式 | `--sort date` |
| `--download` | 下载 PDF | `--download` |
| `--output` | 输出目录 | `--output ./papers/` |
| `--limit` | 下载限制 | `--limit 5` |
| `--format` | 输出格式 | `--format json` |
| `--verbose` | 详细输出 | `--verbose` |

### 输出格式

#### JSON 格式（默认）
```json
{
  "search_parameters": {
    "q": "machine learning",
    "num": 10
  },
  "search_information": {
    "total_results": 5340000,
    "time_taken": 0.8
  },
  "organic_results": [
    {
      "position": 1,
      "title": "Machine Learning: A Probabilistic Perspective",
      "link": "https://dl.acm.org/doi/10.5555/123456",
      "snippet": "A comprehensive introduction to machine learning...",
      "publication_info": {
        "summary": "Kevin P. Murphy, 2012"
      },
      "resources": [
        {
          "title": "PDF",
          "link": "https://example.com/paper.pdf",
          "file_format": "PDF"
        }
      ],
      "inline_links": {
        "cited_by": {
          "total": 12543
        }
      }
    }
  ]
}
```

#### CSV 格式
```bash
# 导出为 CSV
python scripts/google_scholar_search.py "data science" --format csv --output results.csv
```

#### BibTeX 格式
```bash
# 导出为 BibTeX
python scripts/google_scholar_search.py "neural networks" --format bibtex --output references.bib
```

### Python API 使用

#### 基本搜索
```python
from google_scholar_search import GoogleScholarSearch

# 初始化搜索器
searcher = GoogleScholarSearch(api_key="your_key")

# 简单搜索
results = searcher.search("artificial intelligence", num=10)

# 处理结果
for paper in results["organic_results"]:
    print(f"标题: {paper['title']}")
    print(f"作者: {paper['publication_info']['summary']}")
    print(f"引用: {paper['inline_links']['cited_by']['total']}")
    print(f"链接: {paper['link']}")
    print("-" * 50)
```

#### 批量下载
```python
from google_scholar_search import GoogleScholarSearch

searcher = GoogleScholarSearch()

# 搜索并下载
results = searcher.search(
    query="quantum machine learning",
    num=20,
    download=True,
    output_dir="./quantum_papers/"
)

print(f"找到 {results['search_information']['total_results']} 篇论文")
print(f"下载了 {len(results['downloaded_files'])} 个 PDF 文件")
```

#### 高级功能
```python
from google_scholar_search import GoogleScholarSearch

searcher = GoogleScholarSearch()

# 1. 按年份过滤
results_2023 = searcher.search("transformer", year=2023)

# 2. 按引用数排序
results_sorted = searcher.search("attention", sort="cited_by")

# 3. 获取作者的所有论文
author_papers = searcher.search("author:Geoffrey Hinton")

# 4. 复合搜索
complex_search = searcher.search(
    query="(GAN OR \"generative adversarial network\") AND image",
    num=50,
    year=2022
)
```

## 🔧 集成示例

### 与 OpenClaw 集成
```python
# 在 OpenClaw 技能中使用
def handle_google_scholar_request(query, user):
    """处理 Google Scholar 搜索请求"""
    from google_scholar_search import GoogleScholarSearch
    
    searcher = GoogleScholarSearch()
    results = searcher.search(query, num=5)
    
    response = f"🔍 搜索 '{query}' 的结果:\n\n"
    for i, paper in enumerate(results["organic_results"][:5], 1):
        response += f"{i}. **{paper['title']}**\n"
        response += f"   作者: {paper['publication_info']['summary']}\n"
        response += f"   引用: {paper['inline_links']['cited_by']['total']}\n"
        response += f"   链接: {paper['link']}\n\n"
    
    return response
```

### 与学术工作流集成
```python
import pandas as pd
from google_scholar_search import GoogleScholarSearch

def create_literature_review(topic, output_file="literature_review.md"):
    """创建文献综述"""
    searcher = GoogleScholarSearch()
    
    # 搜索相关论文
    papers = searcher.search(topic, num=30, year=2020)
    
    # 创建 DataFrame 进行分析
    df = pd.DataFrame([
        {
            "title": p["title"],
            "authors": p["publication_info"]["summary"],
            "citations": p["inline_links"]["cited_by"]["total"],
            "year": p["publication_info"]["summary"].split(",")[-1].strip(),
            "link": p["link"]
        }
        for p in papers["organic_results"]
    ])
    
    # 生成 Markdown 报告
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# 文献综述: {topic}\n\n")
        f.write(f"## 搜索统计\n")
        f.write(f"- 总论文数: {len(df)}\n")
        f.write(f"- 平均引用数: {df['citations'].mean():.1f}\n")
        f.write(f"- 最新年份: {df['year'].max()}\n\n")
        
        f.write(f"## 高引用论文\n")
        top_cited = df.nlargest(10, "citations")
        for _, row in top_cited.iterrows():
            f.write(f"### {row['title']}\n")
            f.write(f"- 作者: {row['authors']}\n")
            f.write(f"- 引用: {row['citations']}\n")
            f.write(f"- 链接: {row['link']}\n\n")
    
    print(f"文献综述已保存到: {output_file}")
    return df
```

### 自动化研究助手
```python
import schedule
import time
from google_scholar_search import GoogleScholarSearch
from datetime import datetime

def daily_research_update():
    """每日研究更新"""
    searcher = GoogleScholarSearch()
    
    # 关注的研究主题
    topics = [
        "large language models",
        "multimodal AI",
        "AI safety",
        "reinforcement learning"
    ]
    
    today = datetime.now().strftime("%Y-%m-%d")
    report = f"# 每日研究更新 ({today})\n\n"
    
    for topic in topics:
        # 搜索最近一周的论文
        results = searcher.search(
            query=topic,
            num=5,
            sort="date"
        )
        
        report += f"## {topic}\n"
        for paper in results["organic_results"]:
            report += f"- **{paper['title']}**\n"
            report += f"  {paper['snippet'][:100]}...\n"
            report += f"  [链接]({paper['link']})\n\n"
    
    # 保存报告
    filename = f"research_update_{today}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"研究更新已保存: {filename}")

# 每天上午9点运行
schedule.every().day.at("09:00").do(daily_research_update)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## 📁 项目结构

```
google-scholar-api/
├── README.md                 # 本文档
├── SKILL.md                  # OpenClaw 技能定义
├── INSTALL.md                # 安装指南
├── LICENSE                   # MIT 许可证
├── .gitignore               # Git 忽略文件
├── scripts/                 # 脚本目录
│   ├── google_scholar_search.py  # 主搜索脚本
│   ├── config_example.py         # 配置示例
│   └── requirements.txt          # Python 依赖
├── references/              # 参考文档
│   ├── api_guide.md             # API 使用指南
│   └── usage_examples.md        # 使用示例
├── examples/               # 示例目录
│   ├── basic_search.py         # 基础搜索示例
│   ├── batch_download.py       # 批量下载示例
│   └── data_analysis.py        # 数据分析示例
└── tests/                  # 测试目录
    ├── test_search.py          # 搜索功能测试
    └── test_download.py        # 下载功能测试
```

## 🐛 故障排除

### 常见问题

#### Q1: API 密钥无效
```bash
# 检查环境变量
echo $SERP_API_KEY

# 测试 API 密钥
python -c "import os; print('Key length:', len(os.getenv('SERP_API_KEY', '')))"

# 获取新的 API 密钥
# 访问: https://serpapi.com/manage-api-key
```

#### Q2: 搜索返回空结果
```bash
# 检查查询语句
python scripts/google_scholar_search.py "test query" --verbose

# 尝试简单查询
python scripts/google_scholar_search.py "machine learning"

# 检查网络连接
curl -I https://serpapi.com
```

#### Q3: PDF 下载失败
```bash
# 检查下载目录权限
ls -la ./downloads/

# 尝试手动下载
curl -O https://example.com/paper.pdf

# 使用代理（如果需要）
export HTTP_PROXY="http://proxy:port"
python scripts/google_scholar_search.py "query" --download
```

#### Q4: 速率限制
```bash
# 查看剩余配额
# 访问: https://serpapi.com/manage-api-key

# 添加延迟
python scripts/google_scholar_search.py "query" --delay 2

# 分批搜索
for term in "AI" "ML" "DL"; do
    python scripts/google_scholar_search.py "$term" --num 10
    sleep 5
done
```

### 调试模式
```bash
# 启用详细输出
python scripts/google_scholar_search.py "test" --verbose --debug

# 查看原始 API 响应
python scripts/google_scholar_search.py "test" --raw-response

# 记录日志
python scripts/google_scholar_search.py "test" 2>&1 | tee search.log
```

## 📊 性能优化

### 搜索优化
```python
from google_scholar_search import GoogleScholarSearch
import concurrent.futures

def parallel_search(queries, max_workers=3):
    """并行搜索多个查询"""
    searcher = GoogleScholarSearch()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(searcher.search, query, num=10): query
            for query in queries
        }
        
        results = {}
        for future in concurrent.futures.as_completed(futures):
            query = futures[future]
            try:
                results[query] = future.result()
            except Exception as e:
                print(f"搜索 '{query}' 失败: {e}")
    
    return results

# 并行搜索多个主题
topics = ["neural networks", "computer vision", "natural language processing"]
all_results = parallel_search(topics)
```

### 缓存机制
```python
from google_scholar_search import GoogleScholarSearch
import pickle
import hashlib
import os

class CachedScholarSearch(GoogleScholarSearch):
    """带缓存的搜索器"""
    
    def __init__(self, cache_dir="./cache", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def search(self, query, **kwargs):

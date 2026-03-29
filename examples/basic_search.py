#!/usr/bin/env python3
"""
基础搜索示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.google_scholar_search import GoogleScholarSearch

def main():
    """基础搜索示例"""
    # 初始化搜索器（会自动读取环境变量 SERP_API_KEY）
    searcher = GoogleScholarSearch()
    
    # 简单搜索
    print("🔍 搜索 'machine learning'...")
    results = searcher.search("machine learning", num=5)
    
    print(f"找到 {results['search_information']['total_results']} 篇相关论文")
    print(f"获取了 {len(results['organic_results'])} 篇论文信息\n")
    
    # 显示结果
    for i, paper in enumerate(results['organic_results'], 1):
        print(f"{i}. {paper['title']}")
        print(f"   作者: {paper['publication_info']['summary']}")
        if 'cited_by' in paper.get('inline_links', {}):
            print(f"   引用: {paper['inline_links']['cited_by']['total']}")
        print(f"   链接: {paper['link']}")
        print()

if __name__ == "__main__":
    main()

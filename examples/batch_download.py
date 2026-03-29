#!/usr/bin/env python3
"""
批量下载示例
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.google_scholar_search import GoogleScholarSearch

def main():
    """批量下载示例"""
    searcher = GoogleScholarSearch()
    
    # 创建下载目录
    download_dir = "./downloaded_papers"
    os.makedirs(download_dir, exist_ok=True)
    
    # 搜索并下载
    print("📥 搜索并下载 'deep learning' 相关论文...")
    results = searcher.search(
        query="deep learning",
        num=10,
        download=True,
        output_dir=download_dir,
        limit=5  # 只下载前5个可用的PDF
    )
    
    print(f"\n✅ 完成!")
    print(f"搜索到 {len(results['organic_results'])} 篇论文")
    
    if 'downloaded_files' in results:
        print(f"成功下载 {len(results['downloaded_files'])} 个PDF文件:")
        for filepath in results['downloaded_files']:
            print(f"  - {os.path.basename(filepath)}")
    
    print(f"\n文件保存在: {os.path.abspath(download_dir)}")

if __name__ == "__main__":
    main()

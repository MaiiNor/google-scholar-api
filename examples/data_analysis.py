#!/usr/bin/env python3
"""
数据分析示例
"""

import sys
import os
import json
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.google_scholar_search import GoogleScholarSearch

def analyze_search_results(results, topic):
    """分析搜索结果"""
    print(f"\n📊 分析结果: {topic}")
    print("=" * 50)
    
    papers = results['organic_results']
    
    # 基本统计
    print(f"论文数量: {len(papers)}")
    
    # 引用统计
    citations = []
    for paper in papers:
        if 'cited_by' in paper.get('inline_links', {}):
            citations.append(paper['inline_links']['cited_by']['total'])
    
    if citations:
        print(f"平均引用数: {sum(citations)/len(citations):.1f}")
        print(f"最高引用: {max(citations)}")
        print(f"最低引用: {min(citations)}")
    
    # 年份分析（简单提取）
    years = []
    for paper in papers:
        summary = paper.get('publication_info', {}).get('summary', '')
        # 尝试提取年份（最后4位数字）
        import re
        year_match = re.search(r'\b(19|20)\d{2}\b', summary)
        if year_match:
            years.append(int(year_match.group()))
    
    if years:
        print(f"最新年份: {max(years)}")
        print(f"最早年份: {min(years)}")
    
    # 保存分析结果
    analysis = {
        "topic": topic,
        "total_papers": len(papers),
        "citation_stats": {
            "average": sum(citations)/len(citations) if citations else 0,
            "max": max(citations) if citations else 0,
            "min": min(citations) if citations else 0
        },
        "year_stats": {
            "latest": max(years) if years else None,
            "earliest": min(years) if years else None
        },
        "analysis_date": datetime.now().isoformat()
    }
    
    # 保存为JSON
    output_file = f"analysis_{topic.replace(' ', '_')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    
    print(f"\n分析结果已保存到: {output_file}")
    
    return analysis

def main():
    """主函数"""
    searcher = GoogleScholarSearch()
    
    # 搜索多个主题
    topics = [
        "artificial intelligence",
        "machine learning", 
        "deep learning"
    ]
    
    all_analyses = {}
    
    for topic in topics:
        print(f"\n🔍 搜索: {topic}")
        results = searcher.search(topic, num=15)
        analysis = analyze_search_results(results, topic)
        all_analyses[topic] = analysis
    
    # 生成比较报告
    print("\n" + "=" * 50)
    print("📈 主题比较报告")
    print("=" * 50)
    
    for topic, analysis in all_analyses.items():
        print(f"\n{topic}:")
        print(f"  论文数: {analysis['total_papers']}")
        print(f"  平均引用: {analysis['citation_stats']['average']:.1f}")
        print(f"  最新年份: {analysis['year_stats']['latest']}")

if __name__ == "__main__":
    main()

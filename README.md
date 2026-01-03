# Douban Top250 Movie Analysis

使用 Python 对豆瓣 Top250 电影数据进行分析与可视化。

## 项目简介

本项目基于爬取的豆瓣 Top250 电影数据，
对电影评分、上映年代等信息进行统计分析，
并使用 matplotlib 进行可视化展示。

## 技术栈

- Python 3
- pandas
- matplotlib

## 项目结构

```text
douban-top250-analysis/
├── analysis/
│   └── analysis.py
├── data/
│   └── douban_top250.csv
├── output/
│   └── *.png
└── README.md
数据分析结果
评分分布

Top10 高分电影

使用方法
bash
复制代码
python analysis/analysis.py
运行后生成图表保存在 output/ 目录。
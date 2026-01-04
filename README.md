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

## 数据分析结果

### 1️⃣ 电影评分分布

展示豆瓣 Top250 电影的整体评分分布情况。

![Rating Distribution](output/rating_distribution.png)

---

### 2️⃣ 各年代电影数量分布

按年代统计电影数量。

![Movies by Decade](output/movies_by_decade.png)

---

### 3️⃣ Top10 高分电影

评分最高的 10 部电影如下：

![Top10 Movies](output/top10_movies.png)

---

### 4️⃣ 电影上映年份趋势

Top250 电影在不同年份的分布趋势。

![Movies by Year](output/movies_by_year.png)

<p align="center">
  <img src="output/top10_movies.png" width="600">
</p>


使用方法
bash
复制代码
python analysis/analysis.py
运行后生成图表保存在 output/ 目录。
import pandas as pd
import matplotlib.pyplot as plt
import os


def main():
    # ======================
    # 0️⃣ 准备输出目录
    # ======================
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # ======================
    # 1️⃣ 读取数据
    # ======================
    df = pd.read_csv("data/douban_top250.csv")
    df["rating"] = df["rating"].astype(float)
    df["year"] = df["year"].astype(int)

    # ======================
    # 2️⃣ 评分分布
    # ======================
    plt.figure()
    df["rating"].hist(bins=20)
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/rating_distribution.png")
    plt.close()

    # ======================
    # 3️⃣ 各年代电影数量
    # ======================
    df["decade"] = df["year"] // 10 * 10
    decade_count = df["decade"].value_counts().sort_index()

    plt.figure()
    decade_count.plot(kind="bar")
    plt.title("Movies by Decade")
    plt.xlabel("Decade")
    plt.ylabel("Number of Movies")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/movies_by_decade.png")
    plt.close()

    # ======================
    # 4️⃣ Top10 高分电影
    # ======================
    top10 = df.sort_values(by="rating", ascending=False).head(10)

    plt.figure()
    plt.barh(top10["title"], top10["rating"])
    plt.xlabel("Rating")
    plt.title("Top 10 Highest Rated Movies")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/top10_movies.png")
    plt.close()

    # ======================
    # 5️⃣ 年份趋势
    # ======================
    year_count = df["year"].value_counts().sort_index()

    plt.figure()
    plt.plot(year_count.index, year_count.values)
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.title("Movies Released by Year")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/movies_by_year.png")
    plt.close()

    print("✅ 所有图表已保存到 output/ 目录")


if __name__ == "__main__":
    main()

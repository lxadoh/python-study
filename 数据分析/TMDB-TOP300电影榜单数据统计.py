import pandas as pd
import matplotlib
matplotlib.use('TkAgg')   # 切换后端为TkAgg
import matplotlib.pyplot as plt
from matplotlib.axes import Axes


# 常量
MOVIES_FILE = 'data/movies.csv'
OUTPUT_FILE = 'data/TMDB-TOP300.png'


def load_data() -> pd.DataFrame:
    """
    加载电影数据
    :return: 电影数据DataFrame
    """
    # int64 不支持空值
    # Int64 支持空值
    # float64 支持空值
    data = pd.read_csv(
        MOVIES_FILE,
        usecols=['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言'],
        dtype={'年份': 'Int64'}
    )
    return data


def plot_year_count(axes: Axes, data: pd.DataFrame):
    """
    统计每一年上映的电影数量的变化 (折线图)
    :param axes: 子图对象
    :param data: 电影数据
    """
    # 1. 缺失值,异常值处理
    data['年份'] = data['年份'].fillna(data['上映时间'].str[:4])

    # 2. 分组统计
    year_count = data.groupby('年份')['年份'].count()

    # 3. 组装数据
    # x轴
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x_year = [i for i in range(min_year, max_year + 1)]
    # y轴
    y_year = [year_count.get(i, 0) for i in x_year]  # get(i, 0)表示如果i在year_count中则返回year_count[i]，否则返回0

    # 4. 绘制折线图
    axes.plot(x_year, y_year, color='green')
    axes.set_title('每年上映的电影数量变化', fontsize=16)
    axes.set_xlabel('年份', fontsize=14)
    axes.set_ylabel('电影数量', fontsize=14)

    axes.set_xticks(x_year[::10])  # 设置x轴刻度
    y_ticks = [i for i in range(0, max(y_year) + 3, 3)]  # 设置y轴刻度
    axes.set_yticks(y_ticks)


def plot_language_count(axes: Axes, data: pd.DataFrame):
    """
    统计对比不同语言的电影数量 (柱状图)
    :param axes: 子图对象
    :param data: 电影数据
    """
    # 1. 分组统计
    language_count = data.groupby('语言')['语言'].count()

    # 2. 组装数据
    x_language = language_count.index.tolist()  # x轴
    y_language = language_count.values.tolist()  # y轴

    # 3. 绘制柱状图
    axes.bar(x_language, y_language, color='g', width=0.7)
    axes.set_title('不同语言的电影数量对比', fontsize=16)
    axes.set_xlabel('语言', fontsize=14)
    axes.set_ylabel('电影数量', fontsize=14)
    axes.tick_params(axis='x', rotation=45)  # 旋转x轴刻度
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格


def plot_type_count(axes: Axes, data: pd.DataFrame):
    """
    统计不同类型电影数量 (柱状图)
    :param axes: 子图对象
    :param data: 电影数据
    """
    # 1. 分组统计
    type_count = {}
    for type_list in data['类型'].str.split(','):
        for type_name in type_list:
            if type_name in type_count:
                type_count[type_name] += 1
            else:
                type_count[type_name] = 1
    x_type = list(type_count.keys())  # x轴
    y_type = list(type_count.values())  # y轴

    # 2. 绘制柱状图
    axes.bar(x_type, y_type, color='g', width=0.7)
    axes.set_title('不同类型的电影数量对比', fontsize=16)
    axes.set_xlabel('类型', fontsize=14)
    axes.set_ylabel('电影数量', fontsize=14)
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格


def plot_score_distribution(axes: Axes, data: pd.DataFrame):
    """
    统计对比各个评分的电影占比 (饼状图)
    :param axes: 子图对象
    :param data: 电影数据
    """
    # 1. 分组统计
    score_count = data.groupby('评分')['评分'].count()

    # 2. 合并小数据
    total = score_count.sum()
    large_scores = score_count[score_count >= total * 0.02]  # 大数据, 比例大于等于2%
    small_scores = score_count[score_count < total * 0.02]  # 小数据, 比例小于2%
    # shape()表示矩阵的行数和列数 shape[0]表示行数 shape[1]表示列数
    if small_scores.shape[0] > 0:
        large_scores['其他'] = small_scores.sum()

    scores = large_scores.index.tolist()  # 评分列表
    scores_values = large_scores.values.tolist()  # 评分数量列表

    # 3. 绘制饼状图
    # startangle=140表示从140度开始绘制 autopct='%1.1f%%'表示显示百分比 pctdistance=0.75表示scores_values与圆心的距离
    axes.pie(scores_values, labels=scores, autopct='%1.1f%%', pctdistance=0.75, startangle=140)
    axes.set_title('各个评分的电影占比', fontsize=16)
    axes.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.1))


def main():
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 创建子图
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    fig.suptitle('TMDB-TOP300电影榜单数据统计', fontsize=23)  # 添加画布标题
    # 调整子图之间的间距，wspace为水平间距，hspace为垂直间距
    fig.subplots_adjust(wspace=0.2, hspace=0.4)

    # 获取子图
    axes1: Axes = axes[0][0]
    axes2: Axes = axes[0][1]
    axes3: Axes = axes[1][0]
    axes4: Axes = axes[1][1]

    # 加载数据
    data = load_data()

    # 绘制图表
    plot_year_count(axes1, data)            # 1. 每年上映的电影数量变化 (折线图)
    plot_language_count(axes2, data)        # 2. 不同语言的电影数量对比 (柱状图)
    plot_type_count(axes3, data)            # 3. 不同类型的电影数量对比 (柱状图)
    plot_score_distribution(axes4, data)    # 4. 各个评分的电影占比 (饼状图)

    # 保存图片
    plt.savefig(OUTPUT_FILE)

    # 显示图表
    plt.show()


if __name__ == '__main__':
    main()

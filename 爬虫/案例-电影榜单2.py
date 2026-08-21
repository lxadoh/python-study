import requests
from lxml import html
import csv


# 常量
MOVIE_LIST_FILE = "csv_data/movie_list.csv"
# 电影榜单url
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated" # 电影榜单的url（第一页）
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items" # 电影榜单的url（第2页之后）


# 定义函数，保存电影详情到csv文件
def save_all_movies(all_movies):
    with open(MOVIE_LIST_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['电影名', '年份', '上映时间', '标签', '时长', '评分', '语言', '导演', '标语', '描述'])
        writer.writeheader() # 写入表头
        writer.writerows(all_movies) # 写入多行数据  参数: 一个字典列表



# 定义函数，获得电影详情
def get_movie_info(movie_info_url):
    # 1.发送请求，获得数据
    movie_response = requests.get(movie_info_url,timeout=60)
    print(f"发送请求{movie_info_url},获得电影详情数据...")
    # 2. 解析数据，提取电影详情
    movie_document = html.fromstring(movie_response.text)
    # 3. 解析电影
    movie_names = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()') # 电影名称
    movie_years = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()') # 电影年份
    movie_datas = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="release"]/text()') # 电影上映时间
    movie_tags = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="genres"]/a/text()') # 电影标签
    movie_cost_times = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()') # 电影时长
    movie_scores = movie_document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent') # 电影评分
    movie_languages = movie_document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()') # 电影语言
    movie_directors = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()') # 电影导演
    # movie_authors = movie_document.xpath('')
    movie_slogans = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()') # 电影标语
    movie_descriptions = movie_document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()') # 电影描述

    # 4. 返回电影详情 - 字典
    movie_info = {
        '电影名': movie_names[0].strip() if movie_names else '',
        '年份': movie_years[0].strip() if movie_years else '',
        '上映时间': movie_datas[0].strip() if movie_datas else '',
        '标签': ",".join(movie_tags) if movie_tags else '',
        '时长': movie_cost_times[0].strip() if movie_cost_times else '',
        '评分': movie_scores[0].strip() if movie_scores else '',
        '语言': movie_languages[0].strip() if movie_languages else '',
        '导演': movie_directors[0].strip() if movie_directors else '',
        '标语': movie_slogans[0].strip() if movie_slogans else '',
        '描述': movie_descriptions[0].strip() if movie_descriptions else '',
    }

    return movie_info

# 主函数
def main():
    all_movies = [] # 所有电影详情列表
    for page_num in range(1, 6):
        # 1. 发送请求，获得高分电影榜单数据
        if page_num == 1:
            response = requests.get(TMDB_TOP_URL_1,timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-02-21&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                     timeout=60)
        print("发送请求,获得TMDB高分电影榜单数据")

        # 2. 解析数据，提取电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath('//div[@class="w-full overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-colors hover:border-gray-300"]')

        # 3. 遍历电影列表，获得电影列表
        for movie in movie_list:
            movie_urls = movie.xpath('./div/div/a/@href')
            if movie_urls:
                # 电影详情url
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    # 4. 保存电影详情到csv文件
    print("获取到所有电影详情，保存到测试csv文件中")
    save_all_movies(all_movies)


if __name__ == '__main__':
    main()
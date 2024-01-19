import feedparser

blog_rss_url = 'https://bartlebytypewriter.tistory.com/rss'
rss_feed = feedparser.parse(blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = ""

MAX_POST_NUM = 5

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """### HI THERE!!

<!--
**2fireontree/2fireontree** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

[![*'s github stats](https://github-readme-stats.vercel.app/api?username=younghwangit)](https://github.com/younghwangit)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=younghwangit&layout=compact)](https://github.com/younghwangit/github-readme-stats)

"""
readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)

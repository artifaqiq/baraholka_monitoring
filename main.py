import urllib.request
import psycopg2

max = 10

# nice_urls = []
#
# for x in range(3500, 40000000):
#     url = "http://baraholka.onliner.by/viewtopic.php?t={}".format(x)
#     doc = str(urllib.request.urlopen(url).read())
#     count = doc.count("<div class=\"b-msgpost-txt\">")
#     if count > max:
#         nice_urls.append(url)
#         print(" ========= {} : {}".format(count, url))
#     else: print("{} : {}".format(count, url))
#
#     if x % 1000 == 0:
#         f = open("i.txt", "w")
#
#         f.write(str(x))
#         f.close()
#
# for nice_url in nice_urls:
#     print(nice_url)







try:
    conn = psycopg2.connect("dbname='baraholka_onliner' user='baraholka_monitoring' host='localhost' password='12345678'")
except:
    print(" ### Unable to connect to database")
    exit()


data = {
    'url': "http://url.html",
    'count_comments': 5,
    'ups' : 20,
    'description' : "Description",
    'cost' : "122r",
    'date' : "12.12.12222",
    'section': "Мотоциклы"
}

cur = conn.cursor()

cur.execute("""INSERT INTO goods (url, count_comments, cost, description, date, ups, section)\
            VALUES ('{url}', {count_comments}, '{cost}', '{description}', '{date}', {ups}, '{section}')""".format(**data))

conn.commit()



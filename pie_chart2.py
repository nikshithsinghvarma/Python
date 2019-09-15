from sqlite3 import connect
def search2(webdb):
    con = connect(webdb)
    cur = con.cursor()
    while True:
        keyword = input('Enter keyword: ')
        cur.execute("SELECT DISTINCT Keywords.Url, Ranks.rank FROM Keywords, Ranks WHERE Keywords.Url = Ranks.Url AND Keywords.Word = 'Paris' ORDER BY Ranks.rank DESC")
        print('{:15}{:4}'.format('URL', 'RANK'))
        for url, rank in cur:
            print('{:15}{:4}'.format(url, rank))


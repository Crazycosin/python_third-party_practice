import datetime
import pony.orm as pny

database = pny.Database('sqlite', 'music.sqlite', create_db=True)


########################################################################
class Artist(database.Entity):
     """
     使用 Pony ORM 创建表 Artist
     """
     name = pny.Required(str)
     albums = pny.Set("Album")


########################################################################
class Album(database.Entity):
     """
     使用 Pony ORM 创建表 Album
     """
     artist = pny.Required(Artist)
     title = pny.Required(str)
     release_date = pny.Required(datetime.date)
     publisher = pny.Required(str)
     media_type = pny.Required(str)

def create_db():
    #打开调试模式 
    pny.sql_debug(True)
    #映射模型数据库 
    #如果它们不存在，则创建表 
    database.generate_mapping(create_tables=True)


# ----------------------------------------------------------------------
@pny.db_session
def add_data():
    """"""

    new_artist = Artist(name=u"Newsboys")
    bands = [u"MXPX", u"Kutless", u"Thousand Foot Krutch"]
    for band in bands:
        artist = Artist(name=band)

    album = Album(artist=new_artist,
                title=u"Read All About It",
                release_date=datetime.date(1988, 12, 1),
                publisher=u"Refuge",
                media_type=u"CD")

    albums = [{"artist": new_artist,
                "title": "Hell is for Wimps",
                "release_date": datetime.date(1990, 7, 31),
                "publisher": "Sparrow",
                "media_type": "CD"
                },
            {"artist": new_artist,
                "title": "Love Liberty Disco",
                "release_date": datetime.date(1999, 11, 16),
                "publisher": "Sparrow",
                "media_type": "CD"
                },
            {"artist": new_artist,
                "title": "Thrive",
                "release_date": datetime.date(2002, 3, 26),
                "publisher": "Sparrow",
                "media_type": "CD"}
            ]

    for album in albums:
          a = Album(**album)


def update_data_test():
    with pny.db_session:
        band = Artist.get(name='Newsboys')
        print(band.name)
        for record in band.albums:
            print(record.title)
        # 修改数据 
        band_name = Artist.get(name='Kutless')
        band_name.name = 'Beach Boys'


def delete_data_test():
    with pny.db_session:
        band = Artist.get(name="MXPX")
        band.delete()



if __name__ == "__main__":
    create_db()
    add_data()

    #  use db_session as a context manager
    with pny.db_session:
        a = Artist(name="Skillet")
    update_data_test()
    result = pny.select(i.name for i in Artist)
    delete_data_test()
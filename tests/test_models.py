from src.models import GoogleAlbum, GoogleAlbums


def test_album_model() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
        product_url="album_product_url",
    )
    assert album.id == "album_id"
    assert album.title == "album_title"
    assert album.product_url == "album_product_url"


def test_album_model_by_alias() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
        productUrl="album_product_url",
    )
    assert album.id == "album_id"
    assert album.title == "album_title"
    assert album.product_url == "album_product_url"


def test_albums_model() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
        product_url="album_product_url",
    )
    albums = GoogleAlbums(albums=[album], next_page_token="next_page_token")
    assert albums.albums == [album]
    assert albums.next_page_token == "next_page_token"


def test_albums_model_by_alias() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
        productUrl="album_product_url",
    )
    albums = GoogleAlbums(albums=[album], nextPageToken="next_page_token")
    assert albums.albums == [album]
    assert albums.next_page_token == "next_page_token"

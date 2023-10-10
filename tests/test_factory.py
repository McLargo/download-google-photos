from src.factory import GoogleAlbumsFactory
from src.models import GoogleAlbum, GoogleAlbums


def test_is_album() -> None:
    albums_instance = GoogleAlbumsFactory.build()
    assert isinstance(albums_instance, GoogleAlbums)
    assert isinstance(albums_instance.albums, list)
    assert isinstance(albums_instance.albums[0], GoogleAlbum)
    assert isinstance(albums_instance.next_page_token, str)

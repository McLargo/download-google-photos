from src.factory import GoogleAlbumsFactory, GoogleMediaItemsFactory
from src.models import (
    GoogleAlbum,
    GoogleAlbums,
    GoogleMediaItem,
    GoogleMediaItems,
)


def test_is_albums() -> None:
    albums_instance = GoogleAlbumsFactory.build()
    assert isinstance(albums_instance, GoogleAlbums)
    assert isinstance(albums_instance.albums, list)
    assert isinstance(albums_instance.albums[0], GoogleAlbum)
    assert isinstance(albums_instance.next_page_token, str)


def test_is_media_items() -> None:
    media_items_instance = GoogleMediaItemsFactory.build()
    assert isinstance(media_items_instance, GoogleMediaItems)
    assert isinstance(media_items_instance.media_items, list)
    assert isinstance(media_items_instance.media_items[0], GoogleMediaItem)
    assert isinstance(media_items_instance.next_page_token, str)

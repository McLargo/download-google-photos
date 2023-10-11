from faker import Faker

from src.factory import (
    DEFAULT_ALBUMS_SIZE,
    DEFAULT_MEDIA_ITEMS_SIZE,
    GoogleAlbumFactory,
    GoogleAlbumsFactory,
    GoogleMediaItemFactory,
    GoogleMediaItemsFactory,
    get_google_albums,
    get_google_media_items,
)
from src.models import (
    GoogleAlbum,
    GoogleAlbums,
    GoogleMediaItem,
    GoogleMediaItems,
)


def test_is_album() -> None:
    albums_instance = GoogleAlbumFactory.build()
    assert isinstance(albums_instance, GoogleAlbum)
    assert isinstance(albums_instance.title, str)
    assert isinstance(albums_instance.id, str)


def test_is_albums() -> None:
    albums_instance = GoogleAlbumsFactory.build()
    assert isinstance(albums_instance, GoogleAlbums)
    assert isinstance(albums_instance.albums, list)
    assert isinstance(albums_instance.albums[0], GoogleAlbum)
    assert albums_instance.next_page_token is None


def test_is_media_item() -> None:
    media_item_instance = GoogleMediaItemFactory.build()
    assert isinstance(media_item_instance, GoogleMediaItem)
    assert isinstance(media_item_instance.media_item_id, str)
    assert isinstance(media_item_instance.product_url, str)
    assert isinstance(media_item_instance.base_url, str)
    assert isinstance(media_item_instance.filename, str)


def test_is_media_items() -> None:
    media_items_instance = GoogleMediaItemsFactory.build()
    assert isinstance(media_items_instance, GoogleMediaItems)
    assert isinstance(media_items_instance.media_items, list)
    assert isinstance(media_items_instance.media_items[0], GoogleMediaItem)


def test_get_google_albums() -> None:
    albums: GoogleAlbums = get_google_albums()
    assert isinstance(albums, GoogleAlbums)
    assert isinstance(albums.albums, list)
    assert isinstance(albums.albums[0], GoogleAlbum)
    assert len(albums.albums) == DEFAULT_ALBUMS_SIZE
    assert albums.next_page_token is None


def test_get_google_albums_with_parameters() -> None:
    custom_albums_size = 10
    fake = Faker()
    next_page_token = fake.pystr()
    albums: GoogleAlbumsFactory = get_google_albums(
        albums_size=custom_albums_size,
        next_page_token=next_page_token,
    )
    assert isinstance(albums, GoogleAlbums)
    assert isinstance(albums.albums, list)
    assert isinstance(albums.albums[0], GoogleAlbum)
    assert len(albums.albums) == custom_albums_size
    assert isinstance(albums.next_page_token, str)
    assert albums.next_page_token == next_page_token


def test_get_google_media_items() -> None:
    media_items: GoogleMediaItems = get_google_media_items()
    assert isinstance(media_items, GoogleMediaItems)
    assert isinstance(media_items.media_items, list)
    assert isinstance(media_items.media_items[0], GoogleMediaItem)
    assert len(media_items.media_items) == DEFAULT_MEDIA_ITEMS_SIZE


def test_get_google_media_items_with_parameters() -> None:
    custom_media_items_size = 15
    media_items: GoogleMediaItemsFactory = get_google_media_items(
        media_items_size=custom_media_items_size,
    )
    assert isinstance(media_items, GoogleMediaItems)
    assert isinstance(media_items.media_items, list)
    assert isinstance(media_items.media_items[0], GoogleMediaItem)
    assert len(media_items.media_items) == custom_media_items_size

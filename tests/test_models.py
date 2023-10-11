from src.models import (
    GoogleAlbum,
    GoogleAlbums,
    GoogleMediaItem,
    GoogleMediaItems,
)


def test_google_album_model() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
    )
    assert album.id == "album_id"
    assert album.title == "album_title"


def test_google_album_model_by_alias() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
    )
    assert album.id == "album_id"
    assert album.title == "album_title"


def test_google_albums_model() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
    )
    albums = GoogleAlbums(albums=[album], next_page_token="next_page_token")
    assert albums.albums == [album]
    assert albums.next_page_token == "next_page_token"


def test_google_albums_model_by_alias() -> None:
    album = GoogleAlbum(
        id="album_id",
        title="album_title",
    )
    albums = GoogleAlbums(albums=[album], nextPageToken="next_page_token")
    assert albums.albums == [album]
    assert albums.next_page_token == "next_page_token"


def test_google_media_item_model() -> None:
    media_item = GoogleMediaItem(
        media_item_id="media_item_id",
        base_url="media_item_base_url",
        product_url="media_item_product_url",
        filename="media_item_filename",
    )
    assert media_item.media_item_id == "media_item_id"
    assert media_item.base_url == "media_item_base_url"
    assert media_item.product_url == "media_item_product_url"
    assert media_item.filename == "media_item_filename"


def test_google_media_item_model_by_alias() -> None:
    media_item = GoogleMediaItem(
        id="media_item_id",
        baseUrl="media_item_baseUrl",
        productUrl="media_item_productUrl",
        filename="media_item_filename",
    )
    assert media_item.media_item_id == "media_item_id"
    assert media_item.base_url == "media_item_baseUrl"
    assert media_item.product_url == "media_item_productUrl"
    assert media_item.filename == "media_item_filename"


def test_google_media_items_model():
    media_item = GoogleMediaItem(
        media_item_id="media_item_id",
        base_url="media_item_base_url",
        product_url="media_item_product_url",
        filename="media_item_filename",
    )
    media_items = GoogleMediaItems(
        media_items=[media_item],
    )
    assert media_items.media_items == [media_item]


def test_google_media_items_model_by_alias():
    media_item = GoogleMediaItem(
        id="media_item_id",
        baseUrl="media_item_baseUrl",
        productUrl="media_item_productUrl",
        filename="media_item_filename",
    )
    media_items = GoogleMediaItems(
        media_items=[media_item],
    )
    assert media_items.media_items == [media_item]

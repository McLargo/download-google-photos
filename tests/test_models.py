import pytest

from src.models import (
    GoogleAlbum,
    GoogleAlbums,
    GoogleMediaItem,
    GoogleMediaItems,
)

pytestmark = pytest.mark.unit


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
        base_url="media_item_base_url",
        filename="media_item_filename",
        mime_type="media_item_mime_type",
    )
    assert media_item.base_url == "media_item_base_url"
    assert media_item.filename == "media_item_filename"
    assert media_item.mime_type == "media_item_mime_type"


def test_google_media_item_download_url_no_http() -> None:
    media_item = GoogleMediaItem(
        base_url="media_item_base_url",
        filename="media_item_filename",
        mime_type="media_item_mime_type",
    )
    with pytest.raises(ValueError, match="Expected an http base_url"):
        media_item.download_url()


def test_google_media_item_download_url_mime_type_image() -> None:
    media_item = GoogleMediaItem(
        base_url="http://media_item_base_url",
        filename="media_item_filename",
        mime_type="image/jpeg",
    )
    assert media_item.download_url() == "http://media_item_base_url=d"


def test_google_media_item_download_url_mime_type_video() -> None:
    media_item = GoogleMediaItem(
        base_url="http://media_item_base_url",
        filename="media_item_filename",
        mime_type="video/mp4",
    )
    assert media_item.download_url() == "http://media_item_base_url=dv"


def test_google_media_item_download_url_mime_type_invalid() -> None:
    media_item = GoogleMediaItem(
        base_url="http://media_item_base_url",
        filename="media_item_filename",
        mime_type="invalid",
    )
    with pytest.raises(ValueError, match="Unknown mime type"):
        media_item.download_url()


def test_google_media_item_model_by_alias() -> None:
    media_item = GoogleMediaItem(
        id="media_item_id",
        baseUrl="media_item_baseUrl",
        filename="media_item_filename",
        mimeType="media_item_mimeType",
    )
    assert media_item.base_url == "media_item_baseUrl"
    assert media_item.filename == "media_item_filename"
    assert media_item.mime_type == "media_item_mimeType"


def test_google_media_items_model():
    media_item = GoogleMediaItem(
        base_url="media_item_base_url",
        filename="media_item_filename",
        mime_type="media_item_mime_type",
    )
    media_items = GoogleMediaItems(
        media_items=[media_item],
    )
    assert media_items.media_items == [media_item]


def test_google_media_items_model_by_alias():
    media_item = GoogleMediaItem(
        id="media_item_id",
        baseUrl="media_item_baseUrl",
        filename="media_item_filename",
        mimeType="media_item_mimeType",
    )
    media_items = GoogleMediaItems(
        media_items=[media_item],
    )
    assert media_items.media_items == [media_item]

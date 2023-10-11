import pytest

from src.mocks import (
    MockExecuteAlbums,
    MockExecuteMediaItems,
    MockGooglePhotosLibrary,
    MockListAlbums,
    MockSearchMediaItems,
)
from src.models import GoogleAlbums, GoogleMediaItems

pytestmark = pytest.mark.unit


def test_mock_execute_albums() -> None:
    albums: dict = MockExecuteAlbums().execute()
    assert isinstance(albums, dict)

    google_albums: GoogleAlbums = GoogleAlbums.model_validate(albums)
    assert isinstance(google_albums, GoogleAlbums)


def test_mock_list_album() -> None:
    albums: MockExecuteAlbums = MockListAlbums().list()
    assert isinstance(albums, MockExecuteAlbums)


def test_mock_execute_media_items() -> None:
    media_items: dict = MockExecuteMediaItems().execute()
    assert isinstance(media_items, dict)

    google_media_items: GoogleMediaItems = GoogleMediaItems.model_validate(
        media_items,
    )
    assert isinstance(google_media_items, GoogleMediaItems)


def test_mock_search_media_items() -> None:
    media_items: MockExecuteMediaItems = MockSearchMediaItems().search()
    assert isinstance(media_items, MockExecuteMediaItems)


def test_mock_google_photos_library_album() -> None:
    albums: MockListAlbums = MockGooglePhotosLibrary().albums()
    assert isinstance(albums, MockListAlbums)


def test_mock_google_photos_library_media_items() -> None:
    media_items: MockSearchMediaItems = MockGooglePhotosLibrary().mediaItems()
    assert isinstance(media_items, MockSearchMediaItems)

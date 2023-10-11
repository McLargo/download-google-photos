from unittest.mock import Mock, patch

import pytest
from googleapiclient.errors import HttpError

from src.factory import get_google_albums
from src.google_photos import GooglePhotos
from src.models import GoogleAlbum, GoogleMediaItem

pytestmark = pytest.mark.unit


def test_get_albums() -> None:
    google_photos: GooglePhotos = GooglePhotos(mock_photos_library=True)
    albums: list[GoogleAlbum] = google_photos.get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)


@patch("src.mocks.MockExecuteAlbums.execute")
def test_get_albums_with_token(mock_execute) -> None:
    mock_execute.side_effect = [
        get_google_albums(next_page_token="next_page_token").model_dump(),
        get_google_albums().model_dump(),
    ]
    google_photos: GooglePhotos = GooglePhotos(mock_photos_library=True)
    albums: list[GoogleAlbum] = google_photos.get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)


def test_get_media_items_by_album_id() -> None:
    google_photos: GooglePhotos = GooglePhotos(mock_photos_library=True)
    media_items: list[
        GoogleMediaItem
    ] = google_photos.get_media_items_by_album_id("album_id")
    assert isinstance(media_items, list)
    assert isinstance(media_items[0], GoogleMediaItem)


@patch("src.google_photos.build")
@patch("src.google_photos.GooglePhotos._get_credentials")
def test_build_error(mock_credentials, mock_build) -> None:
    mock_credentials.return_value = Mock()
    http_error: HttpError = HttpError(
        resp=Mock(status=500),
        content=b"Boom!",
    )
    mock_build.side_effect = http_error
    with pytest.raises(HttpError):
        GooglePhotos()

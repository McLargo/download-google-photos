from unittest.mock import Mock, patch

import pytest
from googleapiclient.errors import HttpError

from src.google_photos import GooglePhotos
from src.models import GoogleAlbum, GoogleMediaItem


def test_get_albums() -> None:
    google_photos: GooglePhotos = GooglePhotos(mock_photos_library=True)
    albums: list[GoogleAlbum] = google_photos.get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)


# TODO: add test_get_albums_with_pagination


def test_get_media_items_by_album_id() -> None:
    google_photos: GooglePhotos = GooglePhotos(mock_photos_library=True)
    media_items: list[
        GoogleMediaItem
    ] = google_photos.get_media_items_by_album_id("album_id")
    assert isinstance(media_items, list)
    assert isinstance(media_items[0], GoogleMediaItem)


@patch("src.google_photos.build")
def test_build_error(mock_build) -> None:
    http_error: HttpError = HttpError(
        resp=Mock(status=500),
        content=b"Boom!",
    )
    mock_build.side_effect = http_error
    with pytest.raises(HttpError):
        GooglePhotos()

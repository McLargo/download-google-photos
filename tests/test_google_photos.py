from unittest.mock import Mock, patch

import pytest
from googleapiclient.errors import HttpError

from src.factory import albums_factory, media_items_factory
from src.google_photos import GooglePhotos
from src.models import GoogleAlbum, GoogleMediaItem


@patch("src.google_photos.build")
def test_get_albums(mock_build) -> None:
    mock_build.return_value.albums.return_value.list.return_value.execute.return_value = (  # noqa: E501
        albums_factory.model_dump()
    )
    google_photos: GooglePhotos = GooglePhotos()
    albums: list[GoogleAlbum] = google_photos.get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)


@patch("src.google_photos.build")
def test_get_media_items_by_album_id(mock_build) -> None:
    mock_build.return_value.mediaItems.return_value.search.return_value.execute.return_value = (  # noqa: E501
        media_items_factory.model_dump()
    )
    google_photos: GooglePhotos = GooglePhotos()
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

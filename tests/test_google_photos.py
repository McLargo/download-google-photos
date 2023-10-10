from unittest.mock import Mock, patch

import pytest
from googleapiclient.errors import HttpError

from src.google_photos import GooglePhotos
from src.models import GoogleAlbum


def test_get_albums() -> None:
    albums: list[GoogleAlbum] = GooglePhotos().get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)


@patch("src.google_photos.build")
def test_build_error(mock_build) -> None:
    http_error: HttpError = HttpError(
        resp=Mock(status=500),
        content=b"Boom!",
    )
    mock_build.side_effect = http_error
    with pytest.raises(HttpError):
        GooglePhotos()

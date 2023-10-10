from src.mocks import MockGooglePhotos
from src.models import GoogleAlbum, GoogleMediaItem


def test_mock_google_photos_get_albums() -> None:
    mock_google_photos_instance = MockGooglePhotos()
    albums = mock_google_photos_instance.get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)


def test_mock_google_photos_get_media_items_by_album_id() -> None:
    mock_google_photos_instance = MockGooglePhotos()
    media_items = mock_google_photos_instance.get_media_items_by_album_id(
        "album_id",
    )
    assert isinstance(media_items, list)
    assert isinstance(media_items[0], GoogleMediaItem)

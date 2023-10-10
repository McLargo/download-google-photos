from src.mocks import GooglePhotosMock
from src.models import GoogleAlbum


def test_google_photos_mock_get_albums() -> None:
    google_photos_mock_instance = GooglePhotosMock()
    albums = google_photos_mock_instance.get_albums()
    assert isinstance(albums, list)
    assert isinstance(albums[0], GoogleAlbum)

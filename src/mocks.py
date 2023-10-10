from src.factory import GoogleAlbumsFactory
from src.models import GoogleAlbum


class GooglePhotosMock:
    def get_albums(self) -> list[GoogleAlbum]:
        albums = GoogleAlbumsFactory.build()
        return albums.albums

from src.factory import albums_factory, media_items_factory
from src.models import GoogleAlbum, GoogleMediaItem


# TODO: review if this is ever used in tests. if not, remove
class MockGooglePhotos:
    def get_albums(self) -> list[GoogleAlbum]:
        return albums_factory.albums

    def get_media_items_by_album_id(
        self,
        album_id: str,
    ) -> list[GoogleMediaItem]:
        return media_items_factory.media_items

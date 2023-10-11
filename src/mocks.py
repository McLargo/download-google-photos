from src.factory import get_google_albums, get_google_media_items


class MockExecuteAlbums:
    def execute(self) -> dict:
        return get_google_albums().model_dump()


class MockListAlbums:
    def list(*args, **kwargs) -> MockExecuteAlbums:
        return MockExecuteAlbums()


class MockExecuteMediaItems:
    def execute(self) -> dict:
        return get_google_media_items().model_dump()


class MockSearchMediaItems:
    def search(*args, **kwargs) -> MockExecuteMediaItems:
        return MockExecuteMediaItems()


class MockGooglePhotosLibrary:
    def albums(self) -> MockListAlbums:
        return MockListAlbums()

    def mediaItems(self) -> MockSearchMediaItems:
        return MockSearchMediaItems()

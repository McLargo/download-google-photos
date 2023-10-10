from polyfactory.factories.pydantic_factory import ModelFactory

from src.models import GoogleAlbums, GoogleMediaItems


class GoogleAlbumsFactory(ModelFactory[GoogleAlbums]):
    __model__ = GoogleAlbums


class GoogleMediaItemsFactory(ModelFactory[GoogleMediaItems]):
    __model__ = GoogleMediaItems


albums_factory = GoogleAlbumsFactory.build()
media_items_factory = GoogleMediaItemsFactory.build()

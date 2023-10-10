from polyfactory.factories.pydantic_factory import ModelFactory

from src.models import GoogleAlbums


class GoogleAlbumsFactory(ModelFactory[GoogleAlbums]):
    __model__ = GoogleAlbums

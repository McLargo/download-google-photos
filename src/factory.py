from typing import Optional

from faker import Faker
from polyfactory.factories.pydantic_factory import ModelFactory

from src.models import (
    GoogleAlbum,
    GoogleAlbums,
    GoogleMediaItem,
    GoogleMediaItems,
)

DEFAULT_LOCALE = "es_ES"
DEFAULT_ALBUMS_SIZE = 5
DEFAULT_MEDIA_ITEMS_SIZE = 10


class EsESFaker:
    __faker__ = Faker(locale=DEFAULT_LOCALE)


class GoogleAlbumFactory(EsESFaker, ModelFactory[GoogleAlbum]):
    __model__ = GoogleAlbum

    @classmethod
    def title(cls) -> str:
        return f"{cls.__faker__.first_name()} en {cls.__faker__.country()} ({cls.__faker__.year()})"  # noqa: E501


class GoogleAlbumsFactory(ModelFactory[GoogleAlbums]):
    __model__ = GoogleAlbums

    next_page_token = None


class GoogleMediaItemFactory(EsESFaker, ModelFactory[GoogleMediaItem]):
    __model__ = GoogleMediaItem

    @classmethod
    def product_url(cls) -> str:
        return cls.__faker__.image_url()


class GoogleMediaItemsFactory(ModelFactory[GoogleMediaItems]):
    __model__ = GoogleMediaItems


def get_google_albums(
    albums_size: int = DEFAULT_ALBUMS_SIZE,
    next_page_token: Optional[str] = None,
) -> GoogleAlbums:
    albums = GoogleAlbumFactory.batch(size=albums_size)
    return GoogleAlbumsFactory().build(
        albums=albums,
        next_page_token=next_page_token,
    )


def get_google_media_items(
    media_items_size: int = DEFAULT_MEDIA_ITEMS_SIZE,
) -> GoogleMediaItems:
    media_items = GoogleMediaItemFactory.batch(size=media_items_size)
    return GoogleMediaItemsFactory().build(media_items=media_items)

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class GoogleAlbum(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str


class GoogleAlbums(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    albums: list[GoogleAlbum]
    next_page_token: Optional[str] = Field(default=None, alias="nextPageToken")


class GoogleMediaItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    product_url: str = Field(alias="productUrl")
    filename: str


class GoogleMediaItems(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    media_items: list[GoogleMediaItem] = Field(alias="mediaItems")

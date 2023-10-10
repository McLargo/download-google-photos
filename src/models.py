from pydantic import BaseModel, ConfigDict, Field


class GoogleAlbum(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    product_url: str = Field(alias="productUrl")


class GoogleAlbums(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    albums: list[GoogleAlbum]
    next_page_token: str = Field(alias="nextPageToken")


class GoogleMediaItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    media_item_id: str = Field(alias="id")
    description: str
    product_url: str = Field(alias="productUrl")
    filename: str


class GoogleMediaItems(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    media_items: list[GoogleMediaItem]
    next_page_token: str = Field(alias="nextPageToken")

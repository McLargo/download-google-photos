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

from __future__ import annotations

from typing import Any
from typing import List  # noqa: UP035
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Links(BaseModel):
    mu: str
    raw: str


class MdCover(BaseModel):
    vol: str
    w: int
    h: int
    b2key: str


class Relates(BaseModel):
    title: str
    slug: str
    hid: str
    md_covers: List[MdCover]  # noqa: UP006


class Recommendation(BaseModel):
    up: int
    down: int
    total: int
    relates: Relates


class MdTitle(BaseModel):
    title: str
    lang: str


class MdGenres(BaseModel):
    name: str
    type: Optional[str]  # noqa: UP007
    slug: str
    group: str


class MdComicMdGenre(BaseModel):
    md_genres: MdGenres


class MdCover1(BaseModel):
    vol: Any
    w: int
    h: int
    b2key: str


class MuPublishers(BaseModel):
    title: str
    slug: str


class MuComicPublisher(BaseModel):
    mu_publishers: MuPublishers


class MuCategories(BaseModel):
    title: str
    slug: str


class MuComicCategory(BaseModel):
    mu_categories: MuCategories
    positive_vote: int
    negative_vote: int


class MuComics(BaseModel):
    mu_comic_publishers: List[MuComicPublisher]  # noqa: UP006
    licensed_in_english: Any
    mu_comic_categories: List[MuComicCategory]  # noqa: UP006


class Comic(BaseModel):
    id: int
    hid: str
    title: str
    country: str
    status: int
    links: Links
    last_chapter: str
    chapter_count: int
    demographic: Any
    user_follow_count: int
    follow_rank: int
    follow_count: int
    desc: str
    parsed: str
    slug: str
    mismatch: Any
    year: int
    bayesian_rating: str
    rating_count: int
    content_rating: str
    translation_completed: bool
    chapter_numbers_reset_on_new_volume_manual: bool
    final_chapter: Any
    final_volume: Any
    noindex: bool
    adsense: bool
    login_required: bool
    recommendations: List[Recommendation]  # noqa: UP006
    relate_from: List  # noqa: UP006
    is_english_title: Any
    md_titles: List[MdTitle]  # noqa: UP006
    md_comic_md_genres: List[MdComicMdGenre]  # noqa: UP006
    md_covers: List[MdCover1]  # noqa: UP006
    mu_comics: MuComics
    iso639_1: str
    lang_name: str
    lang_native: str


class MdGroups(BaseModel):
    title: str
    slug: str


class MdChaptersGroup(BaseModel):
    md_groups: MdGroups


class FirstChapter(BaseModel):
    vol: Any
    title: Any
    chap: str
    hid: str
    lang: str
    created_at: str
    up_count: int
    group_name: List[str]  # noqa: UP006
    md_chapters_groups: List[MdChaptersGroup]  # noqa: UP006


class Artist(BaseModel):
    name: str
    slug: str


class Author(BaseModel):
    name: str
    slug: str


class Model(BaseModel):
    comic: Optional[Comic] = None  # noqa: UP007
    first_chapters: Optional[List[FirstChapter]] = Field(  # noqa: UP006, UP007
        None,
        alias="firstChapters",
    )
    artists: Optional[List[Artist]] = None  # noqa: UP006, UP007
    authors: Optional[List[Author]] = None  # noqa: UP006, UP007
    lang_list: Optional[List[str]] = Field(None, alias="langList")  # noqa: UP006, UP007
    recommendable: Optional[bool] = None  # noqa: UP007
    demographic: Optional[Any] = None  # noqa: UP007
    english_link: Optional[Any] = Field(None, alias="englishLink")  # noqa: UP007
    mature_content: Optional[bool] = Field(None, alias="matureContent")  # noqa: UP007
    selector_position: Optional[str] = None  # noqa: UP007
    check_vol2_chap1: Optional[bool] = Field(  # noqa: UP007
        None,
        alias="checkVol2Chap1",
    )

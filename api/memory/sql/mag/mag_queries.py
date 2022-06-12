from typing import Dict, List, Literal

import pandas as pd

from api.memory.sql.mag.mag_schema import (
    Affiliations,
    Authors,
    FieldOfStudyChildren,
    FieldOfStudyExtendedAttributes,
    FieldsOfStudy,
    PaperAuthorAffiliations,
    PaperFieldsOfStudy,
    PaperResources,
    Papers,
    PaperUrls,
)
from api.memory.sql.omni_config_sql import session


def select_mag_id(mag_id: List[int]):
    if not mag_id:
        return None
    else:
        return mag_id[0]


def fetch_fields_of_study(fieldofstudyid: List[int]) -> pd.DataFrame:

    query = (
        session.query(
            FieldsOfStudy.fieldofstudyid,
            FieldsOfStudy.rank,
            FieldsOfStudy.displayname,
            FieldsOfStudy.maintype,
            FieldsOfStudy.level,
            FieldsOfStudy.papercount,
            FieldsOfStudy.paperfamilycount,
            FieldsOfStudy.citationcount,
        )
        .filter(FieldsOfStudy.fieldofstudyid.in_(fieldofstudyid))
        .all()
    )
    return pd.DataFrame(
        query,
        columns=[
            "fieldofstudyid",
            "rank",
            "displayname",
            "maintype",
            "level",
            "papercount",
            "paperfamilycount",
            "citationcount",
        ],
    )


def fetch_field_of_study_children(fieldofstudyid: int) -> List[int]:
    query = (
        session.query(
            FieldOfStudyChildren.fieldofstudyid,
            FieldOfStudyChildren.childfieldofstudyid,
        )
        .filter(FieldOfStudyChildren.fieldofstudyid == fieldofstudyid)
        .all()
    )
    return [x[1] for x in query]


def fetch_fields_of_study_level_0() -> List[int]:
    query = (
        session.query(FieldsOfStudy.fieldofstudyid)
        .filter(FieldsOfStudy.level == 0)
        .all()
    )
    return [x[0] for x in query]


def fetch_fields_of_study_containing_subword(subword: str) -> List[int]:
    if len(subword) < 4:
        return []

    query = (
        session.query(FieldsOfStudy.fieldofstudyid)
        .filter(FieldsOfStudy.displayname.contains(subword))
        .all()
    )
    return [x[0] for x in query]


def fetch_authors_of_field_of_study2(fieldofstudyid: int) -> List[int]:
    """Same function but using join. exemple : 41350136"""

    query = (
        session.query(Authors.authorid)
        .join(
            PaperAuthorAffiliations,
            PaperAuthorAffiliations.AuthorId == Authors.authorid,
        )
        .join(
            PaperFieldsOfStudy,
            PaperFieldsOfStudy.paperid == PaperAuthorAffiliations.PaperId,
        )
        .filter(PaperFieldsOfStudy.fieldofstudyid == fieldofstudyid)
        # .order_by(Authors.citationcount.desc()) # order by decreases the performances...
        .limit(100000)
        .all()
    )
    return [x[0] for x in query]


def fetch_mag_authors_from_articles(
    mag_paper_ids: List[int],
) -> Dict[int, Dict[int, str]]:
    # mag_ids: List of the (MAG) ids of the articles
    # return Dict of Dict of form: mag_paper_id -> (mag_author_id -> author_name)

    query = (
        session.query(
            Authors.authorid,
            Authors.displayname,
            PaperAuthorAffiliations.PaperId,
            PaperAuthorAffiliations.AuthorId,
        )
        .join(
            PaperAuthorAffiliations,
            PaperAuthorAffiliations.AuthorId == Authors.authorid,
        )
        .filter(PaperAuthorAffiliations.PaperId.in_(mag_paper_ids))
    )

    # if only_french:
    #     query = query.filter(Affiliations.iso3166code == "FR")

    query = query.all()

    res: Dict[int, Dict[int, str]] = {id: {} for id in mag_paper_ids}
    for mag_author_id, author_name, mag_paper_id, _ in query:
        res[mag_paper_id][mag_author_id] = author_name

    return res


def fetch_authors_by_ids(mag_author_ids: List[int]) -> pd.DataFrame:

    query = (
        session.query(
            Authors.authorid,
            Authors.displayname,
            Authors.lastknownaffiliationid,
            Authors.citationcount,
            Authors.papercount,
            Affiliations.displayname,
            Affiliations.latitude,
            Affiliations.longitude,
            Affiliations.iso3166code,
            Affiliations.officialpage,
            Affiliations.wikipage,
        )
        .join(
            Affiliations, Affiliations.affiliationid == Authors.lastknownaffiliationid
        )
        .filter(Authors.authorid.in_(mag_author_ids))
    )

    # if only_french:
    #     query = query.filter(Affiliations.iso3166code == "FR")
    query = query.all()
    return pd.DataFrame(
        query,
        columns=[
            "authorid",
            "authorname",
            "lastknownaffiliationid",
            "citationcount",
            "papercount",
            "affiliationname",
            "latitude",
            "longitude",
            "iso3166code",
            "officialpage",
            "wikipage",
        ],
    )


def fetch_github(mag_paper_ids: List[int]) -> Dict[int, List[str]]:
    # Returns: mag_paper_id -> list of github urls

    query = (
        session.query(PaperResources.paperid, PaperResources.resourceurl)
        .filter(PaperResources.paperid.in_(mag_paper_ids))
        .filter(PaperResources.resourceurl.contains("github"))
    )

    query = query.all()

    github_urls: Dict[int, List[str]] = {
        mag_paper_id: [] for mag_paper_id in mag_paper_ids
    }
    for mag_paper_id, github_url in query:
        github_urls[mag_paper_id].append(github_url)
    return github_urls


def _fetch_top_github_snippet_():

    subquery = (
        session.query(PaperResources.paperid)
        .join(Papers)
        .filter(PaperResources.resourceurl.contains("github"))
        .order_by(Papers.CitationCount.desc())
        .limit(50)
        .subquery()
    )
    query = (
        session.query(
            PaperResources.resourceurl,
            Papers.CitationCount,
            Papers.PaperTitle,
            Papers.Year,
        )
        .join(PaperResources, PaperResources.paperid == Papers.PaperId)
        .filter(Papers.PaperId.in_(subquery))
        .order_by(Papers.CitationCount.desc())
        .all()
    )
    return pd.DataFrame(
        query, columns=["resourceurl", "citationcount", "title", "year"]
    )


def fetch_authors(subword: str) -> pd.DataFrame:
    """Too long : 300secondes"""

    subquery = (
        session.query(Authors.authorid)
        .filter(Authors.displayname.contains(subword))
        .limit(100)
        .subquery()
    )
    query = (
        session.query(
            Authors.authorid,
            Authors.displayname,
            Authors.citationcount,
            Affiliations.displayname,
        )
        .join(
            Affiliations, Affiliations.affiliationid == Authors.lastknownaffiliationid
        )
        .filter(Authors.authorid.in_(subquery))
        .all()
    )
    return pd.DataFrame(
        query, columns=["authorid", "displayname", "citationcount", "affiliationname"]
    )


def fetch_main_papers_of_field_of_study(fieldofstudyid: int) -> pd.DataFrame:

    query = (
        session.query(
            Papers.PaperId,
            Papers.PaperTitle,
            Papers.Year,
            Papers.CitationCount,
            PaperAuthorAffiliations.OriginalAuthor,
        )
        .join(PaperFieldsOfStudy, PaperFieldsOfStudy.paperid == Papers.PaperId)
        .join(
            PaperAuthorAffiliations, PaperAuthorAffiliations.PaperId == Papers.PaperId
        )
        .filter(PaperFieldsOfStudy.fieldofstudyid == fieldofstudyid)
        .filter(PaperAuthorAffiliations.AuthorSequenceNumber == 1)
        .order_by(Papers.CitationCount.desc())
        .limit(10)
        .all()
    )
    return pd.DataFrame(
        query, columns=["paperid", "title", "year", "citationcount", "OriginalAuthor"]
    )


def fetch_resources_field_of_study(fieldofstudyid: int) -> pd.DataFrame:

    query = (
        session.query(
            PaperResources.resourceurl,
            PaperResources.resourcetype,
            Papers.CitationCount,
            Papers.PaperTitle,
            Papers.Year,
        )
        .join(PaperFieldsOfStudy, PaperFieldsOfStudy.paperid == PaperResources.paperid)
        .join(Papers, Papers.PaperId == PaperResources.paperid)  # facultative
        .filter(PaperFieldsOfStudy.fieldofstudyid == fieldofstudyid)
        .order_by(Papers.CitationCount.desc())
        .limit(10)
        .all()
    )
    return pd.DataFrame(
        query, columns=["resourceurl", "resourcetype", "citationcount", "title", "year"]
    )


def fetch_fields_of_study_by_ids_slow(mag_ids: List[List[int]]) -> pd.DataFrame:
    """Deprecated because too slow"""
    mag_ids_clean = [
        select_mag_id(ids) for ids in mag_ids if select_mag_id(ids) is not None
    ]

    results = (
        session.query(
            PaperFieldsOfStudy.paperid,
            FieldsOfStudy.displayname,
            FieldsOfStudy.fieldofstudyid,
            FieldsOfStudy.level,
        )
        .join(
            PaperFieldsOfStudy,
            PaperFieldsOfStudy.fieldofstudyid == FieldsOfStudy.fieldofstudyid,
        )
        .filter(PaperFieldsOfStudy.paperid.in_(mag_ids_clean))
        .filter(FieldsOfStudy.level > 1)
    ).all()
    session.close()

    df = pd.DataFrame(
        results, columns=["mag_id", "fieldofstudy", "fieldofstudyid", "level"]
    )

    # df.to_csv("fos.csv")

    return df


def fetch_fields_of_study_by_ids(mag_ids: List[List[int]]) -> pd.DataFrame:
    # Same thing as above but with 2 queries

    mag_ids_clean = [
        select_mag_id(ids) for ids in mag_ids if select_mag_id(ids) is not None
    ]

    results = (
        session.query(
            PaperFieldsOfStudy.paperid, PaperFieldsOfStudy.fieldofstudyid
        ).filter(PaperFieldsOfStudy.paperid.in_(mag_ids_clean))
    ).all()
    session.close()

    df_mag_ids_fieldofstudyid = pd.DataFrame(
        results, columns=["mag_id", "fieldofstudyid"]
    )

    list_fields_of_study_id = [
        int(x) for x in df_mag_ids_fieldofstudyid["fieldofstudyid"]
    ]

    results = (
        session.query(
            FieldsOfStudy.displayname, FieldsOfStudy.fieldofstudyid, FieldsOfStudy.level
        )
        .filter(FieldsOfStudy.fieldofstudyid.in_(list_fields_of_study_id))
        .filter(FieldsOfStudy.level > 1)
    ).all()
    session.close()

    df_fields = pd.DataFrame(
        results, columns=["fieldofstudy", "fieldofstudyid", "level"]
    )

    # merge the two dataframes
    df = df_mag_ids_fieldofstudyid.merge(df_fields, how="left", on="fieldofstudyid")

    # remove rows with containg nan, that appeared with the version with all fields
    df = df.dropna()

    return df


def fetch_wiki_fields_of_studies(fieldofstudyid: List[int]) -> Dict[int, str]:

    query = (
        session.query(
            FieldOfStudyExtendedAttributes.fieldofstudyid,
            FieldOfStudyExtendedAttributes.attributevalue,
        )
        .filter(FieldOfStudyExtendedAttributes.fieldofstudyid.in_(fieldofstudyid))
        .filter(FieldOfStudyExtendedAttributes.attributetype == 2)
        .all()
    )
    # retourne un dict `filed of study id`` -> `wiki URL``
    return {row[0]: row[1] for row in query}


DocType = Literal[
    "Book",
    "BookChapter",
    "Conference",
    "Dataset",
    "Journal",
    "Patent",
    "Repository",
    "Thesis",
]


def fetch_doctypes_by_ids(mag_ids: List[List[int]]) -> Dict[str, List[DocType]]:
    mag_ids_clean = [
        select_mag_id(ids) for ids in mag_ids if select_mag_id(ids) is not None
    ]

    results = (
        session.query(Papers.DocType, Papers.PaperId)
        .filter(Papers.PaperId.in_(mag_ids_clean))
        .all()
    )
    session.close()

    res: Dict[str, List[DocType]] = {}
    for doctype, magId in results:
        magId = str(magId)
        if magId not in res:
            res[magId] = []
        res[magId].append(doctype)
    return res


def fetch_paper_urls(mag_ids: List[int]) -> Dict[int, str]:
    # the 'int' in the input and the output represent magId

    results = (
        session.query(PaperUrls.SourceUrl, PaperUrls.PaperId)
        .filter(PaperUrls.PaperId.in_(mag_ids))
        .all()
    )
    session.close()

    query_result = {magId: paper_url for paper_url, magId in results}
    res = {}
    for magId in mag_ids:
        if magId in query_result:
            res[magId] = query_result[magId]
        else:
            res[magId] = "None"
    return res


# def fetch_similar_articles(magId: str) -> List[str]:
#     """
#     Get the id of the N most cited articles.
#     """
#     engine = get_engine_articles()
#     Session = sessionmaker(bind=engine)

#     # 1. Get list of MAG ids
#
#     query = (
#         session.query(PaperRecommendations.recommendedpaperid)
#         .filter(PaperRecommendations.paperid == magId)
#         .order_by(PaperRecommendations.score.desc())
#     )
#     similar_articles_mag_id = [str(article.recommendedpaperid) for article in query]
#     session.close()

#     # 2. Get list of S2Orc ids
#     # TODO: faire des jointures et ordonner par score
#
#     query = session.query(ArticleS2ORC.paper_id).filter(
#         ArticleS2ORC.mag_id.in_(similar_articles_mag_id)
#     )
#     similar_articles_s2orc_id = [str(article.id) for article in query]
#     session.close()
#     # This step divise by 2 the number of similar articles

#     return similar_articles_s2orc_id

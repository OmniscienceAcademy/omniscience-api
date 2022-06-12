# type: ignore
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Affiliations(Base):
    __tablename__ = "affiliations"
    affiliationid = Column(BigInteger, primary_key=True)
    rank = Column(Integer)
    normalizedname = Column(String)
    displayname = Column(String)
    gridid = Column(String)
    officialpage = Column(String)
    wikipage = Column(String)
    papercount = Column(BigInteger)
    paperfamilycount = Column(BigInteger)
    citationcount = Column(BigInteger)
    iso3166code = Column(String)  # language code FR, EN, ...
    latitude = Column(Float)
    longitude = Column(Float)
    createddate = Column(DateTime)

    authors = relationship("Authors")
    paperauthoraffiliations = relationship("PaperAuthorAffiliations")


class AuthorExtendedAttributes(Base):
    __tablename__ = "authorextendedattributes"
    virtual_column = Column(String, primary_key=True)
    authorid = Column(BigInteger, ForeignKey("authors.authorid"))
    attributetype = Column(Integer)
    attributevalue = Column(String)


class Authors(Base):
    __tablename__ = "authors"
    authorid = Column(BigInteger, primary_key=True)
    rank = Column(Integer)
    normalizedname = Column(String)
    displayname = Column(String)
    lastknownaffiliationid = Column(
        BigInteger, ForeignKey("affiliations.affiliationid")
    )
    papercount = Column(BigInteger)
    paperfamilycount = Column(BigInteger)
    citationcount = Column(BigInteger)
    createddate = Column(DateTime)

    authorsextendedattributes = relationship("AuthorExtendedAttributes")
    paperauthoraffiliations = relationship("PaperAuthorAffiliations")


class ConferenceInstances(Base):
    __tablename__ = "conferenceinstances"
    conferenceinstanceid = Column(BigInteger, primary_key=True)
    normalizedname = Column(String)
    displayname = Column(String)
    conferenceseriesid = Column(
        BigInteger, ForeignKey("conferenceseries.conferenceseriesid")
    )
    location = Column(String)
    officialurl = Column(String)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    abstractregistrationdate = Column(DateTime)
    submissiondeadlinedate = Column(DateTime)
    notificationduedate = Column(DateTime)
    finalversionduedate = Column(DateTime)
    papercount = Column(BigInteger)
    paperfamilycount = Column(BigInteger)
    citationcount = Column(BigInteger)
    latitude = Column(Float)
    longitude = Column(Float)
    createddate = Column(DateTime)

    papers = relationship("Papers")


class ConferenceSeries(Base):
    __tablename__ = "conferenceseries"
    conferenceseriesid = Column(BigInteger, primary_key=True)
    rank = Column(Integer)
    normalizedname = Column(String)
    displayname = Column(String)
    papercount = Column(BigInteger)
    paperfamilycount = Column(BigInteger)
    citationcount = Column(BigInteger)
    createddate = Column(DateTime)

    papers = relationship("Papers")
    conferenceinstances = relationship("ConferenceInstances")


class EntityRelatedEntities(Base):
    __tablename__ = "entityrelatedentities"
    virtual_column = Column(String, primary_key=True)
    entityid = Column(BigInteger)
    entitytype = Column(String)
    relatedentityid = Column(BigInteger)
    relatedentitytype = Column(String)
    relatedtype = Column(Integer)
    score = Column(Float)


class FieldOfStudyChildren(Base):
    __tablename__ = "fieldofstudychildren"
    virtual_column = Column(String, primary_key=True)
    fieldofstudyid = Column(BigInteger, ForeignKey("fieldsofstudy.fieldofstudyid"))
    childfieldofstudyid = Column(BigInteger)


class RelatedFieldOfStudy(Base):
    __tablename__ = "relatedfieldofstudy"
    virtual_column = Column(String, primary_key=True)
    fieldofstudyid1 = Column(BigInteger, ForeignKey("fieldsofstudy.fieldofstudyid"))
    type1 = Column(String)
    fieldofstudyid2 = Column(BigInteger)
    type2 = Column(String)
    rank = Column(Float)


class FieldOfStudyExtendedAttributes(Base):
    __tablename__ = "fieldofstudyextendedattributes"
    virtual_column = Column(String, primary_key=True)
    fieldofstudyid = Column(BigInteger, ForeignKey("fieldsofstudy.fieldofstudyid"))
    attributetype = Column(Integer)
    attributevalue = Column(String)


class FieldsOfStudy(Base):
    __tablename__ = "fieldsofstudy"
    fieldofstudyid = Column(BigInteger, primary_key=True)
    rank = Column(Integer)
    normalizedname = Column(String)
    displayname = Column(String)
    maintype = Column(String)
    level = Column(Integer)
    papercount = Column(BigInteger)
    paperfamilycount = Column(BigInteger)
    citationcount = Column(BigInteger)
    createddate = Column(DateTime)

    fieldofstudyextendedattributes = relationship("FieldOfStudyExtendedAttributes")
    fieldofstudychildren = relationship("FieldOfStudyChildren")
    paperfieldsofstudy = relationship("PaperFieldsOfStudy")
    relatedfieldofstudy = relationship("RelatedFieldOfStudy")


class Journals(Base):
    __tablename__ = "journals"
    journalid = Column(BigInteger, primary_key=True)
    rank = Column(Integer)
    normalizedname = Column(String)
    displayname = Column(String)
    issn = Column(String)
    publisher = Column(String)
    webpage = Column(String)
    papercount = Column(BigInteger)
    paperfamilycount = Column(BigInteger)
    citationcount = Column(BigInteger)
    createddate = Column(DateTime)

    papers = relationship("Papers")


class PaperAuthorAffiliations(Base):
    """Warning partially corrupted database"""

    __tablename__ = "paperauthoraffiliations"

    virtual_column = Column(String, primary_key=True)
    PaperId = Column(BigInteger, ForeignKey("papers.PaperId"))
    AuthorId = Column(BigInteger, ForeignKey("authors.authorid"))
    AffiliationId = Column(DOUBLE_PRECISION, ForeignKey("affiliations.affiliationid"))
    AuthorSequenceNumber = Column(BigInteger)
    OriginalAuthor = Column(String)
    OriginalAffiliation = Column(String)


class PaperCitationContexts(Base):
    __tablename__ = "papercitationcontexts"
    virtual_column = Column(String, primary_key=True)
    PaperId = Column(BigInteger, ForeignKey("papers.PaperId"))
    PaperReferenceId = Column(BigInteger)
    CitationContext = Column(String)


class PaperExtendedAttributes(Base):
    __tablename__ = "paperextendedattributes"
    virtual_column = Column(String, primary_key=True)
    paperid = Column(BigInteger, ForeignKey("papers.PaperId"))
    attributetype = Column(Integer)
    attributevalue = Column(String)


class PaperFieldsOfStudy(Base):
    __tablename__ = "paperfieldsofstudy"
    virtual_column = Column(String, primary_key=True)
    paperid = Column(BigInteger, ForeignKey("papers.PaperId"))
    fieldofstudyid = Column(BigInteger, ForeignKey("fieldsofstudy.fieldofstudyid"))
    score = Column(Float)


class PaperMesh(Base):
    __tablename__ = "papermesh"
    virtual_column = Column(String, primary_key=True)
    paperid = Column(BigInteger, ForeignKey("papers.PaperId"))
    descriptorui = Column(String)
    descriptorname = Column(String)
    qualifierui = Column(String)
    qualifiername = Column(String)
    ismajortopic = Column(Boolean)


class PaperRecommendations(Base):
    __tablename__ = "paperrecommendations"
    virtual_column = Column(String, primary_key=True)
    paperid = Column(BigInteger, ForeignKey("papers.PaperId"))
    recommendedpaperid = Column(BigInteger)
    score = Column(Float)


class PaperReferences(Base):
    __tablename__ = "paperreferences"
    virtual_column = Column(String, primary_key=True)
    paperid = Column(BigInteger, ForeignKey("papers.PaperId"))
    paperreferenceid = Column(BigInteger)  # ?


class PaperResources(Base):
    __tablename__ = "paperresources"
    virtual_column = Column(String, primary_key=True)
    paperid = Column(BigInteger, ForeignKey("papers.PaperId"))
    resourcetype = Column(Integer)
    resourceurl = Column(String)
    sourceurl = Column(String)
    relationshiptype = Column(Integer)


class Papers(Base):
    """Warning partially corrupted database"""

    __tablename__ = "papers"
    PaperId = Column(BigInteger, primary_key=True)
    Rank = Column(BigInteger)
    Doi = Column(String)
    DocType = Column(String)
    PaperTitle = Column(String)
    OriginalTitle = Column(String)
    BookTitle = Column(String)
    Year = Column(DOUBLE_PRECISION)
    Date = Column(String)
    OnlineDate = Column(String)
    Publisher = Column(String)
    JournalId = Column(DOUBLE_PRECISION, ForeignKey("journals.journalid"))
    ConferenceSeriesId = Column(
        DOUBLE_PRECISION, ForeignKey("conferenceseries.conferenceseriesid")
    )
    ConferenceInstanceId = Column(
        DOUBLE_PRECISION, ForeignKey("conferenceinstances.conferenceinstanceid")
    )
    Volume = Column(DOUBLE_PRECISION)
    Issue = Column(DOUBLE_PRECISION)
    FirstPage = Column(String)
    LastPage = Column(String)
    ReferenceCount = Column(BigInteger)
    CitationCount = Column(BigInteger)
    EstimatedCitation = Column(BigInteger)
    OriginalVenue = Column(String)
    FamilyId = Column(DOUBLE_PRECISION)
    FamilyRank = Column(DOUBLE_PRECISION)
    DocSubTypes = Column(String)
    CreatedDate = Column(String)

    paperauthoraffiliations = relationship("PaperAuthorAffiliations")
    papercitationcontexts = relationship("PaperCitationContexts")
    paperextendedattributes = relationship("PaperExtendedAttributes")
    paperfieldsofstudy = relationship("PaperFieldsOfStudy")
    papermesh = relationship("PaperMesh")
    paperrecommendations = relationship("PaperRecommendations")
    paperreferences = relationship("PaperReferences")
    paperresources = relationship("PaperResources")
    paperurls = relationship("PaperUrls")


class PaperUrls(Base):
    __tablename__ = "paperurls"
    virtual_column = Column(String, primary_key=True)
    PaperId = Column(BigInteger, ForeignKey("papers.PaperId"))
    SourceType = Column(DOUBLE_PRECISION)
    SourceUrl = Column(String)
    LanguageCode = Column(String)

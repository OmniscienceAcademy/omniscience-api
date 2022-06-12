SELECT authors.displayname AS authors_displayname,
    authors.citationcount AS authors_citationcount
FROM authors
WHERE authors.authorid IN(
        SELECT paperauthoraffiliations."AuthorId"
        FROM paperauthoraffiliations
        WHERE paperauthoraffiliations."PaperId" IN(
                SELECT paperfieldsofstudy.paperid
                FROM paperfieldsofstudy
                WHERE paperfieldsofstudy.fieldofstudyid = % (fieldofstudyid_1) s
            )
    ) not run but ok:
SELECT paperauthoraffiliations."AuthorId"
FROM paperauthoraffiliations
WHERE paperauthoraffiliations."PaperId" IN(
        SELECT paperfieldsofstudy.paperid
        FROM paperfieldsofstudy
        WHERE paperfieldsofstudy.fieldofstudyid = % (fieldofstudyid_1) s
    )

-- shitty
SELECT authors.displayname AS authors_displayname,
    authors.citationcount AS authors_citationcount,
    authors.papercount AS authors_papercount,
    authors.lastknownaffiliationid AS authors_lastknownaffiliationid,
    authors.rank AS authors_rank
FROM (
        authors
        JOIN paperauthoraffiliations ON paperauthoraffiliations."AuthorId" = authors.authorid
        JOIN paperfieldsofstudy ON paperfieldsofstudy.paperid = paperauthoraffiliations."PaperId"
    )
WHERE paperfieldsofstudy.fieldofstudyid = 2780680706

-- good !
SELECT t.displayname AS authors_displayname
FROM (
	select *
	from
        authors
        JOIN paperauthoraffiliations ON paperauthoraffiliations."AuthorId" = authors.authorid
        JOIN paperfieldsofstudy ON paperfieldsofstudy.paperid = paperauthoraffiliations."PaperId"
	WHERE paperfieldsofstudy.fieldofstudyid = 2780680706
	LIMIT 100
    ) as t

# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['BasicRoutesTests::test_faiss_articles_with_infos 1'] = {
    'faiss_articles': [
        {
            'faiss_score': 0.7593238353729248,
            'nb_inbound_citations': 0,
            'paper_id': 9403319,
            'similarity': 0.7593238353729248,
            'title': 'WHOLE-WHEAT BREAD.',
            'year': 1918
        },
        {
            'faiss_score': 0.7072782516479492,
            'nb_inbound_citations': 0,
            'paper_id': 82204618,
            'similarity': 0.7072782516479492,
            'title': 'Bread cereals and bread.',
            'year': 1954
        },
        {
            'faiss_score': 0.6727426535123198,
            'nb_inbound_citations': 1,
            'paper_id': 161037686,
            'similarity': 0.6607014536857605,
            'title': 'Breads white and brown. Their place in thought and social history.',
            'year': 1956
        },
        {
            'faiss_score': 0.6008145809173584,
            'nb_inbound_citations': 0,
            'paper_id': 70465457,
            'similarity': 0.6008145809173584,
            'title': 'Breads brown and wholemeal',
            'year': 1983
        },
        {
            'faiss_score': 0.5332241654396057,
            'nb_inbound_citations': 0,
            'paper_id': 127926128,
            'similarity': 0.5332241654396057,
            'title': 'Double-Layered Flat Breads',
            'year': 1996
        }
    ]
}

snapshots['BasicRoutesTests::test_get_article_by_id 1'] = {
    'authors': [
        [
            2274101767,
            'F. Roy'
        ]
    ],
    'github_urls': [
    ],
    'id': 153662531,
    'journalName': 'European Journal of Housing Policy',
    'language': 'un',
    'magId': 1967659097,
    'n_author': [
        0
    ],
    'nbInCitations': 2,
    'nbOutCitations': 0,
    'paperAbstract': 'The collapse of the former Soviet Union and the subsequent transition process has transformed the political, social and economic landscape in central and eastern Europe, the Balkans and Russia. Reforms of the existing regulatory and institutional framework have created the basis for continued economic expansion. The resulting rising incomes of households have become one of the main drivers for prosperous banking markets. To benefit from this positive trend, many banks have opted for an expansion into mortgage lending. The objective of this paper is therefore to analyse how these countries have managed to convert the positive economic development into better housing for their citizens (including the access to mortgage credit). The paper sets out the criteria which are considered essential for the development of primary mortgage markets and compares these with mortgage market development, starting with an outline of the situation before the beginning of the transition process, including an analysis of what has enabled the emergence of the mortgage markets and finishing by an overview of the present situation. The paper concludes with an assessment of the progress made since the start of the transition process, thereby providing an outlook for the further development of mortgage markets, in particular in view of the current turbulence in the international financial markets.',
    'pdfUrls': [
        'https://EconPapers.repec.org/RePEc:taf:eurjhp:v:8:y:2008:i:2:p:133-160'
    ],
    'question': '',
    's2Url': 'https://api.semanticscholar.org/CorpusID:153662531',
    'similar_articles': [
        158839382,
        53316827,
        169173037,
        55665522,
        155891158
    ],
    'similar_articles_not_cited_by_us': [
    ],
    'tags': [
        {
            'color': 'white',
            'tag': 'test'
        }
    ],
    'title': 'Mortgage Markets in Central and Eastern Europe – A Review of Past Experiences and Future Perspectives',
    'tldr': '',
    'top_articles_cited': [
    ],
    'top_articles_citing': [
    ],
    'venue': None,
    'year': 2008
}

snapshots['BasicRoutesTests::test_get_articles 1'] = {
    18988104: {
        'SourceUrl': 'https://www.sciencedirect.com/science/article/pii/S0899825606000169#!',
        'abstract': " A commonly held belief in economics is that an individual's preferences that are revealed by her choices must be complete. This paper takes issue with this position by showing that one may be able to distinguish between indifference and indecisiveness of an agent upon observing her choice behavior. We relax the standard Weak Axiom of Revealed Preferences (WARP) and show that a potent theory of individual choice (with and without risk) can be founded on this weaker axiom when it is coupled with some other standard postulates. The most notable features here are that an agent is allowed to be indifferent between certain alternatives and indecisive about others. Moreover, an outside observer can identify which of these actually occur upon examining the (observable) choice behavior of the decision maker. As an application, we also show how our theory may be able to cope with the classical preference reversal phenomenon.",
        'first_name': [
            'K.',
            'E.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
            1928848,
            59450432,
            16466404
        ],
        'journal': 'Games Econ. Behav.',
        'last_name': [
            'Eliaz',
            'Ok'
        ],
        'mag_authors': {
            494257986: 'Efe A. Ok',
            1990884168: 'Kfir Eliaz'
        },
        'mag_id': [
            2041332986
        ],
        'n_author': [
            0,
            1
        ],
        'nb_inbound_citations': 71,
        'nb_outbound_citations': 33,
        'outbound_citations': [
            153846912,
            3050113,
            18248965,
            156429446,
            150703369,
            154864907,
            14575375,
            1928848,
            153687316,
            16798614,
            122059798,
            23002905,
            120998684,
            120754207,
            153816098,
            144363176,
            153573933,
            153965105,
            152869298,
            56097847,
            59450432,
            154394056,
            2167374,
            152525523,
            156348375,
            46966243,
            16466404,
            154066538,
            25323884,
            358900,
            144558711,
            198882552,
            54652
        ],
        'paper_id': 18988104,
        'question': 'How can we relax the Weak Axiom of Revealed Preference',
        's2_url': 'https://api.semanticscholar.org/CorpusID:18988104',
        'title': 'Indifference or indecisiveness? Choice-theoretic foundations of incomplete preferences',
        'tldr': 'We relax the Weak Axiom of Revealed Preferences (WARP) and show that a potent theory of individual choice (with and without risk) can be founded on this weaker axiom.',
        'venue': 'Games Econ. Behav.',
        'year': 2006
    },
    144551922: {
        'SourceUrl': 'https://growkudos.com/publications/10.1111%252Fj.1470-6431.2009.00821.x/reader',
        'abstract': 'Drawing from the literature on the analytics of government, the paper discusses marketing as a form of government, elaborating and illustrating the many ways in which consumer choice is shaped, modified and directed in the market through practices and techniques of consumer marketing. The aim is to critically reflect upon and render problematic the individualistic ideas of the green consumer as a powerful market force and to provoke discussion on the conceptualization – and construction – of consumer subjectivity and social problems in marketing. Taking examples particularly from the fashion and clothing industry, the paper discusses the ways in which marketing activities come to shape consumer conduct by operating through the choice of individuals who freely pursue their needs and desires, and by working on the environment within which this freedom of choice is exercised. The paper contributes to the literature on green consumerism by systematically interrogating and elaborating on the modes and practices of marketing thought and expertise through which consumers and consumption are rendered intelligible and actionable in the market.',
        'first_name': [
            'J.',
            'A.',
            'K.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'International Journal of Consumer Studies',
        'last_name': [
            'Moisander',
            'Markkula',
            'ErÃ¤ranta'
        ],
        'mag_authors': {
            102105129: 'Kirsi Eräranta',
            2091417843: 'Johanna Moisander',
            2092075466: 'Annu Markkula'
        },
        'mag_id': [
            2032360494
        ],
        'n_author': [
            0,
            1,
            2
        ],
        'nb_inbound_citations': 0,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 144551922,
        's2_url': 'https://api.semanticscholar.org/CorpusID:144551922',
        'title': 'Construction of consumer choice in the market: challenges for environmental policy',
        'venue': None,
        'year': 2010
    },
    144555080: {
        'SourceUrl': 'https://www.tandfonline.com/doi/full/10.1111/j.1533-8525.1993.tb00132.x',
        'abstract': 'This article seeks to advance "new structuralist" theory by considering the effects of positional power and class on individual earnings. We contend that positional power, that is the power wielded by workers employed in industries in an interdependent economy, confers upon workers the potential to disrupt system-wide production and creates leverage to demand higher earnings from employers. We demonstrate that positional power, in particular the per worker volume of goods and services received from other industries (or upstream production), increases workers\' earnings net of sociodemographic variables and other plausible structural sources of earnings determination. We suggest that the threat of disrupting upstream production holds greater earnings potential than disrupting downstream production because of the profit realization problems associated with the former. We also show that the positive effects of positional power are not evenly distributed across the class structure, but rather are concentrated among non-owning classes who display a social control function in the labor process. We discuss the implications of our research for future new structuralist research.',
        'first_name': [
            'M.',
            'K.T.',
            'D.S.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'Sociological Quarterly',
        'last_name': [
            'Wallace',
            'Leicht',
            'Grant'
        ],
        'mag_authors': {
            244314973: 'Kevin T. Leicht',
            2170494988: 'Don Grant',
            2894382954: 'Michael Wallace'
        },
        'mag_id': [
            2029764453
        ],
        'n_author': [
            0,
            1,
            2
        ],
        'nb_inbound_citations': 4,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 144555080,
        's2_url': 'https://api.semanticscholar.org/CorpusID:144555080',
        'title': 'POSITIONAL POWER, CLASS, AND INDIVIDUAL EARNINGS INEQUALITY: Advancing New Structuralist Explanations',
        'venue': None,
        'year': 1993
    },
    146157251: {
        'SourceUrl': 'None',
        'abstract': 'The United States ranks low on many measures of population health. In addressing this societal problem, nonprofit health conversion foundations are emerging as important, local social entrepreneurs. We investigated the processes by which these organizations create and implement locally situated innovative approaches to promote health and wellness. Using an inductive, qualitative approach, we identified central themes by which conversion foundations, as social entrepreneurs, developed collaborative solutions to health. We found that they defined the social problem, generated social capital in the community, and educated potential partners. These mechanisms helped build a groundwork for collaboration among community actors. Conversion foundations then convened partners with complementary competencies to develop creative solutions. This research contributes to the literature on social entrepreneurship and nonprofits by expanding understanding of how foundations can foster community collaborations to develop innovative solutions to social problems. Further, this study sheds light on the activities and processes of nonprofit health conversion foundations as actors with the potential to improve population health.',
        'first_name': [
            'K.',
            'J.',
            'K.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'Nonprofit Management and Leadership',
        'last_name': [
            'Heinze',
            'Banaszak-Holl',
            'Babiak'
        ],
        'mag_authors': {
            1239146254: 'Jane Banaszak-Holl',
            2017508887: 'Kathryn L. Heinze',
            2077487816: 'Kathy Babiak'
        },
        'mag_id': [
            2598979897,
            2233350825,
            2599334988
        ],
        'n_author': [
            0,
            1,
            2
        ],
        'nb_inbound_citations': 1,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 146157251,
        's2_url': 'https://api.semanticscholar.org/CorpusID:146157251',
        'title': 'Social Entrepreneurship in Communities: Examining the Collaborative Processes of Health Conversion Foundations Social Entrepreneurship Processes',
        'venue': None,
        'year': 2016
    },
    153662531: {
        'SourceUrl': 'https://EconPapers.repec.org/RePEc:taf:eurjhp:v:8:y:2008:i:2:p:133-160',
        'abstract': 'The collapse of the former Soviet Union and the subsequent transition process has transformed the political, social and economic landscape in central and eastern Europe, the Balkans and Russia. Reforms of the existing regulatory and institutional framework have created the basis for continued economic expansion. The resulting rising incomes of households have become one of the main drivers for prosperous banking markets. To benefit from this positive trend, many banks have opted for an expansion into mortgage lending. The objective of this paper is therefore to analyse how these countries have managed to convert the positive economic development into better housing for their citizens (including the access to mortgage credit). The paper sets out the criteria which are considered essential for the development of primary mortgage markets and compares these with mortgage market development, starting with an outline of the situation before the beginning of the transition process, including an analysis of what has enabled the emergence of the mortgage markets and finishing by an overview of the present situation. The paper concludes with an assessment of the progress made since the start of the transition process, thereby providing an outlook for the further development of mortgage markets, in particular in view of the current turbulence in the international financial markets.',
        'first_name': [
            'F.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'European Journal of Housing Policy',
        'last_name': [
            'Roy'
        ],
        'mag_authors': {
            2274101767: 'Friedemann Roy'
        },
        'mag_id': [
            1967659097
        ],
        'n_author': [
            0
        ],
        'nb_inbound_citations': 2,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 153662531,
        's2_url': 'https://api.semanticscholar.org/CorpusID:153662531',
        'title': 'Mortgage Markets in Central and Eastern Europe – A Review of Past Experiences and Future Perspectives',
        'venue': None,
        'year': 2008
    },
    153666201: {
        'SourceUrl': 'https://ssrn.com/abstract=181828',
        'abstract': "Congress may soon restrict joint and several liability for cleanup of contaminated sites under Superfund. We explore whether this change would discourage settlements and is therefore likely to increase the program's already high litigation costs per site. Recent theoretical research by Kornhauser and Revesz finds that joint and several liability may either encourage or discourage settlement, depending on the correlation of outcomes at trial across defendants. We extend their two-defendant model to a richer framework with N defendants. This extension allows us to test the theoretical model empirically using data on Superfund litigation. We find that joint and several liability does not discourage settlements and may even encourage them. Our results support the model's predictions about the effects of several variables, such as the degree of correlation in trial outcomes. Copyright 2000 by the University of Chicago.",
        'first_name': [
            'H.F.',
            'H.A.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'The Journal of Legal Studies',
        'last_name': [
            'Chang',
            'Sigman'
        ],
        'mag_authors': {
            2092886149: 'Hilary Sigman',
            2131369551: 'Howard F. Chang'
        },
        'mag_id': [
            1704893522,
            2951810696
        ],
        'n_author': [
            0,
            1
        ],
        'nb_inbound_citations': 16,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 153666201,
        'question': 'How do settlements affect cleanup of contaminated sites?',
        's2_url': 'https://api.semanticscholar.org/CorpusID:153666201',
        'title': 'Incentives to Settle Under Joint and Several Liability: An Empirical Analysis of Superfund Litigation',
        'tldr': 'Congress may soon restrict joint and several liability for cleanup of contaminated sites under Superfund. We explore whether this change would discourage settlements.',
        'venue': None,
        'year': 2000
    },
    153666223: {
        'SourceUrl': 'https://econpapers.repec.org/article/cupbjposi/v_3a10_3ay_3a1980_3ai_3a03_3ap_3a317-339_5f00.htm',
        'abstract': "Critics of the American House of Representatives frequently cite, in one form or another, a national model of representation as a basis for criticizing both the House and the behaviour of some of its individual members. One of the more familiar criticisms, for example, is that members of the House are so motivated by local or regional concerns and interests that representation in some meaningful national form is rendered almost impossible.' So widely is this characterization shared that it is hardly ever asked whether or not members of the House behave in ways that would be consistent and meaningful in terms of a national model of representation.2 This question is an important one. Representation is supposed to be a principal function of the legislature, and yet many of the critics of Congress view the presidency as having a special ability in the area of national representation. The Congress, after all, is selected on the basis of essentially local rather than national elections so that there can be no assurance as to how much members of Congress will be influenced by national concerns and directions of opinion. The president, on the other hand, is the only officer elected by the whole nation, and only the presidency is chosen by elections that have a truly national focus and character. In this sense the presidency is uniquely responsible to a national constituency. With the presidency's national constituency and orientation in",
        'first_name': [
            'J.',
            'B.',
            'T.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'British Journal of Political Science',
        'last_name': [
            'Schwarz',
            'Fenmore',
            'Volgy'
        ],
        'mag_authors': {
            176803166: 'Barton Fenmore',
            2157829243: 'John E. Schwarz',
            2506934156: 'Thomas J. Volgy'
        },
        'mag_id': [
            1993489756
        ],
        'n_author': [
            0,
            1,
            2
        ],
        'nb_inbound_citations': 0,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 153666223,
        's2_url': 'https://api.semanticscholar.org/CorpusID:153666223',
        'title': 'Liberal and Conservative Voting in the House of Representatives: A National Model of Representation',
        'venue': None,
        'year': 1980
    },
    153667575: {
        'SourceUrl': 'http://www.sciencedirect.com/science/article/pii/S0969593109000055',
        'abstract': 'This study investigates the respective influences of price and country of origin as extrinsic cues on consumer evaluations of wine quality when all intrinsic cues are experienced through sensory perceptions, and then compares these results with those of a survey employing identical intrinsic and extrinsic cues. Taste testing experiments were conducted (NÂ =Â 263) using Chardonnay and a three (COO) by three (price) by three (acid level) conjoint analysis fractional factorial design. Price and COO were both found to be more important contributors to perception of wine quality than taste. The study advances our understanding of the influence of extrinsic cues to dominant quality assessment and shows conjoint analysis to be a credible means of measuring consumer reactions to specific wine attributes.',
        'first_name': [
            'R.',
            'P.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'International Business Review',
        'last_name': [
            'Veale',
            'Quester'
        ],
        'mag_authors': {
            723010404: 'Pascale G. Quester',
            2114307796: 'Roberta Veale'
        },
        'mag_id': [
            1987820526
        ],
        'n_author': [
            0,
            1
        ],
        'nb_inbound_citations': 28,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 153667575,
        'question': 'How do price and COO affect perception of wine quality?',
        's2_url': 'https://api.semanticscholar.org/CorpusID:153667575',
        'title': 'Do consumer expectations match experience? Predicting the influence of price and country of origin on perceptions of product quality',
        'tldr': 'Price and COO were found to be more important contributors to perception of wine quality than taste.',
        'venue': None,
        'year': 2009
    },
    153669883: {
        'SourceUrl': 'https://we.clmconsulting.pl/index.php/we/article/view/52',
        'abstract': 'The importance of the study of the dynamics of the movement of financial flows of the banking system using wavelet analysis methodology is emphasized. The expediency of simultaneous wavelet analysis in terms of the overall dynamics of incoming and outgoing cash flows of the banking system and individual components of such flows is shown. It is noted that it can more fully develop signs of reciprocity between the studied data rows. The analysis of the stability of the domestic banking system based on wavelet analysis is conducted. The presence of a significant correlation between the analyzed data rows during the economic crisis in Ukraine is found. Lack of effectiveness of the stable functioning of the banking system is specified.',
        'first_name': [
            'N.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': None,
        'last_name': [
            'Pogorelenko'
        ],
        'mag_authors': {
            2668515644: 'Nataliia Pogorelenko'
        },
        'mag_id': [
            1959289354
        ],
        'n_author': [
            0
        ],
        'nb_inbound_citations': 0,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 153669883,
        's2_url': 'https://api.semanticscholar.org/CorpusID:153669883',
        'title': 'WAVELET TRANSFORMATION OF TIME SERIES OF DATA IN DISCLOSURE OF INWARD AND OUTWARD FLOW DYNAMICS OF BANKING SYSTEM OF UKRAINE',
        'venue': None,
        'year': 2015
    },
    154671520: {
        'SourceUrl': 'https://econpapers.repec.org/article/blareesec/v_3a18_3ay_3a1990_3ai_3a4_3ap_3a403-430.htm',
        'abstract': 'Commercial real estate makes up a relatively small percentage of most institutional portfolios, even though the existing literature has consistently reported attractive risk-return characteristics that would suggest much larger allocations. This discrepancy has been explained by a perceived lack of comparability between return series calculated for real estate and those calculated for other asset classes. Just as investors actively involved in the futures markets do not consider individual common stocks to be traded continuously, those active in the stock market do not consider real estate to be traded continuously. In both cases, adjustments to reported returns are necessary to achieve a degree of comparability. This study makes such adjustments, using sales data from properties that help comprise the National Council of Real Estate Investment Fiduciaries / Frank Russell Company (NCREIF/FRC) Index to generate a "transaction-driven" commercial real estate return series. Examination of the risk-return characteristics of this series shows that it is quite different from traditionally reported real estate return series and far more consistent with risk-return characteristics that have been reported for other asset classes. Copyright American Real Estate and Urban Economics Association.',
        'first_name': [
            'M.',
            'R.',
            'D.'
        ],
        'github_urls': [
        ],
        'inbound_citations': [
        ],
        'journal': 'Real Estate Economics',
        'last_name': [
            'Miles',
            'Cole',
            'Guilkey'
        ],
        'mag_authors': {
            732950256: 'David K. Guilkey',
            2129477670: 'Rebel A. Cole',
            2230800165: 'Mike Miles'
        },
        'mag_id': [
            2125497831
        ],
        'n_author': [
            0,
            1,
            2
        ],
        'nb_inbound_citations': 25,
        'nb_outbound_citations': 0,
        'outbound_citations': [
        ],
        'paper_id': 154671520,
        'question': '',
        's2_url': 'https://api.semanticscholar.org/CorpusID:154671520',
        'title': 'A Different Look at Commercial Real Estate Returns',
        'tldr': 'This study uses sales data from properties that help comprise the National Council of Real Estate Investment Fiduciaries (NCREIF/FRC) Index to generate a "transaction-driven" commercial real estate return series. Examination of the risk-return characteristics of this series shows that it is quite different from traditionally reported real estate return series.',
        'venue': None,
        'year': 1990
    }
}

snapshots['BasicRoutesTests::test_get_field_of_study_children 1'] = {
    'child_fields_of_study': [
        {
            'citationcount': 9435,
            'displayname': 'Focal firm',
            'fieldofstudyid': 2991807362,
            'level': 2,
            'maintype': None,
            'papercount': 564,
            'paperfamilycount': 538,
            'rank': 14810
        },
        {
            'citationcount': 155577,
            'displayname': 'Vertical integration',
            'fieldofstudyid': 181169782,
            'level': 2,
            'maintype': None,
            'papercount': 10989,
            'paperfamilycount': 9979,
            'rank': 11612
        },
        {
            'citationcount': 1352,
            'displayname': 'Supply market',
            'fieldofstudyid': 2993335673,
            'level': 2,
            'maintype': None,
            'papercount': 275,
            'paperfamilycount': 270,
            'rank': 16018
        },
        {
            'citationcount': 50607,
            'displayname': 'Firm offer',
            'fieldofstudyid': 25328781,
            'level': 2,
            'maintype': None,
            'papercount': 1342,
            'paperfamilycount': 1328,
            'rank': 13002
        },
        {
            'citationcount': 87568,
            'displayname': 'Strategic group',
            'fieldofstudyid': 2775988158,
            'level': 2,
            'maintype': None,
            'papercount': 728,
            'paperfamilycount': 705,
            'rank': 12450
        },
        {
            'citationcount': 2508,
            'displayname': 'International sourcing',
            'fieldofstudyid': 2993752005,
            'level': 2,
            'maintype': None,
            'papercount': 173,
            'paperfamilycount': 160,
            'rank': 15815
        },
        {
            'citationcount': 4437,
            'displayname': 'Vertical market',
            'fieldofstudyid': 2781407128,
            'level': 2,
            'maintype': None,
            'papercount': 356,
            'paperfamilycount': 325,
            'rank': 15083
        },
        {
            'citationcount': 241859,
            'displayname': 'Absorptive capacity',
            'fieldofstudyid': 2777724570,
            'level': 2,
            'maintype': None,
            'papercount': 8505,
            'paperfamilycount': 7913,
            'rank': 11626
        },
        {
            'citationcount': 1539,
            'displayname': 'Market pull',
            'fieldofstudyid': 2994545535,
            'level': 2,
            'maintype': None,
            'papercount': 199,
            'paperfamilycount': 193,
            'rank': 16215
        },
        {
            'citationcount': 74754,
            'displayname': 'Export performance',
            'fieldofstudyid': 2778269237,
            'level': 2,
            'maintype': None,
            'papercount': 6831,
            'paperfamilycount': 6203,
            'rank': 12452
        },
        {
            'citationcount': 30354,
            'displayname': 'Free entry',
            'fieldofstudyid': 2781090088,
            'level': 2,
            'maintype': 'medicine.symptom',
            'papercount': 1711,
            'paperfamilycount': 1396,
            'rank': 13236
        },
        {
            'citationcount': 318154,
            'displayname': 'Theory of the firm',
            'fieldofstudyid': 78173224,
            'level': 2,
            'maintype': None,
            'papercount': 4485,
            'paperfamilycount': 3893,
            'rank': 11093
        },
        {
            'citationcount': 90496,
            'displayname': 'Network effect',
            'fieldofstudyid': 96219163,
            'level': 2,
            'maintype': None,
            'papercount': 5543,
            'paperfamilycount': 4831,
            'rank': 12262
        },
        {
            'citationcount': 35400,
            'displayname': 'Firm strategy',
            'fieldofstudyid': 2988675013,
            'level': 2,
            'maintype': None,
            'papercount': 1559,
            'paperfamilycount': 1494,
            'rank': 13382
        },
        {
            'citationcount': 22182,
            'displayname': 'Corporate innovation',
            'fieldofstudyid': 2992878125,
            'level': 2,
            'maintype': None,
            'papercount': 1020,
            'paperfamilycount': 941,
            'rank': 13802
        },
        {
            'citationcount': 18574,
            'displayname': 'Industry life cycle',
            'fieldofstudyid': 2992834503,
            'level': 2,
            'maintype': None,
            'papercount': 404,
            'paperfamilycount': 371,
            'rank': 13976
        },
        {
            'citationcount': 14755,
            'displayname': 'Environmental innovation',
            'fieldofstudyid': 2994513015,
            'level': 2,
            'maintype': None,
            'papercount': 847,
            'paperfamilycount': 802,
            'rank': 14300
        },
        {
            'citationcount': 13390,
            'displayname': 'Technological diversity',
            'fieldofstudyid': 2993980804,
            'level': 2,
            'maintype': None,
            'papercount': 220,
            'paperfamilycount': 209,
            'rank': 14424
        },
        {
            'citationcount': 71383,
            'displayname': 'Complementary assets',
            'fieldofstudyid': 2776598745,
            'level': 2,
            'maintype': None,
            'papercount': 766,
            'paperfamilycount': 695,
            'rank': 12795
        },
        {
            'citationcount': 17724,
            'displayname': 'Complementary good',
            'fieldofstudyid': 125258956,
            'level': 2,
            'maintype': None,
            'papercount': 1219,
            'paperfamilycount': 1058,
            'rank': 13861
        },
        {
            'citationcount': 13268,
            'displayname': 'Strategic renewal',
            'fieldofstudyid': 2993515431,
            'level': 2,
            'maintype': None,
            'papercount': 479,
            'paperfamilycount': 461,
            'rank': 14366
        },
        {
            'citationcount': 27953,
            'displayname': 'First-mover advantage',
            'fieldofstudyid': 196276664,
            'level': 2,
            'maintype': None,
            'papercount': 1767,
            'paperfamilycount': 1575,
            'rank': 13488
        },
        {
            'citationcount': 892,
            'displayname': 'U-form',
            'fieldofstudyid': 6292241,
            'level': 2,
            'maintype': None,
            'papercount': 35,
            'paperfamilycount': 31,
            'rank': 16733
        },
        {
            'citationcount': 71292,
            'displayname': 'Humanitarian Logistics',
            'fieldofstudyid': 205548138,
            'level': 2,
            'maintype': None,
            'papercount': 9177,
            'paperfamilycount': 9140,
            'rank': 12345
        },
        {
            'citationcount': 448,
            'displayname': 'Small manufacturing enterprises',
            'fieldofstudyid': 2989175194,
            'level': 2,
            'maintype': None,
            'papercount': 122,
            'paperfamilycount': 119,
            'rank': 16916
        },
        {
            'citationcount': 13133,
            'displayname': 'Technology acquisition',
            'fieldofstudyid': 2986845788,
            'level': 2,
            'maintype': None,
            'papercount': 610,
            'paperfamilycount': 587,
            'rank': 14298
        },
        {
            'citationcount': 290,
            'displayname': 'Coordination cost',
            'fieldofstudyid': 2993413512,
            'level': 2,
            'maintype': None,
            'papercount': 105,
            'paperfamilycount': 96,
            'rank': 17248
        },
        {
            'citationcount': 15847,
            'displayname': 'Industrial dynamics',
            'fieldofstudyid': 2991982731,
            'level': 2,
            'maintype': None,
            'papercount': 817,
            'paperfamilycount': 728,
            'rank': 14135
        },
        {
            'citationcount': 13504,
            'displayname': 'Bilateral monopoly',
            'fieldofstudyid': 2778747415,
            'level': 2,
            'maintype': None,
            'papercount': 541,
            'paperfamilycount': 465,
            'rank': 14042
        },
        {
            'citationcount': 764,
            'displayname': 'Value migration',
            'fieldofstudyid': 2777649027,
            'level': 2,
            'maintype': None,
            'papercount': 99,
            'paperfamilycount': 96,
            'rank': 16827
        },
        {
            'citationcount': 273188,
            'displayname': 'Dynamic capabilities',
            'fieldofstudyid': 2780504989,
            'level': 2,
            'maintype': None,
            'papercount': 7155,
            'paperfamilycount': 6845,
            'rank': 11523
        },
        {
            'citationcount': 26015,
            'displayname': 'Export marketing',
            'fieldofstudyid': 2992406444,
            'level': 2,
            'maintype': None,
            'papercount': 883,
            'paperfamilycount': 865,
            'rank': 13751
        },
        {
            'citationcount': 307,
            'displayname': 'Innovation game',
            'fieldofstudyid': 2778852234,
            'level': 2,
            'maintype': None,
            'papercount': 106,
            'paperfamilycount': 93,
            'rank': 17229
        },
        {
            'citationcount': 2341,
            'displayname': 'Strategic pricing',
            'fieldofstudyid': 2994353288,
            'level': 2,
            'maintype': None,
            'papercount': 275,
            'paperfamilycount': 256,
            'rank': 15658
        },
        {
            'citationcount': 130589,
            'displayname': 'Collusion',
            'fieldofstudyid': 2781198186,
            'level': 2,
            'maintype': None,
            'papercount': 12843,
            'paperfamilycount': 11275,
            'rank': 11693
        },
        {
            'citationcount': 7315,
            'displayname': 'Small and medium size enterprises',
            'fieldofstudyid': 2986666693,
            'level': 2,
            'maintype': None,
            'papercount': 870,
            'paperfamilycount': 852,
            'rank': 14717
        },
        {
            'citationcount': 195005,
            'displayname': 'Manufacturing firms',
            'fieldofstudyid': 2988214486,
            'level': 2,
            'maintype': None,
            'papercount': 10583,
            'paperfamilycount': 9687,
            'rank': 11652
        },
        {
            'citationcount': 33252,
            'displayname': 'Systems of innovation',
            'fieldofstudyid': 2991945585,
            'level': 2,
            'maintype': None,
            'papercount': 1184,
            'paperfamilycount': 1063,
            'rank': 13496
        },
        {
            'citationcount': 1087,
            'displayname': 'Market shaping',
            'fieldofstudyid': 3020775184,
            'level': 2,
            'maintype': None,
            'papercount': 89,
            'paperfamilycount': 88,
            'rank': 16886
        },
        {
            'citationcount': 247,
            'displayname': 'Strategy of Technology',
            'fieldofstudyid': 2778264142,
            'level': 2,
            'maintype': None,
            'papercount': 93,
            'paperfamilycount': 93,
            'rank': 17314
        },
        {
            'citationcount': 5574,
            'displayname': 'Technology trajectory',
            'fieldofstudyid': 2781416404,
            'level': 2,
            'maintype': None,
            'papercount': 95,
            'paperfamilycount': 92,
            'rank': 15185
        },
        {
            'citationcount': 15978,
            'displayname': 'Technology innovation',
            'fieldofstudyid': 2989454216,
            'level': 2,
            'maintype': None,
            'papercount': 6663,
            'paperfamilycount': 6615,
            'rank': 13096
        },
        {
            'citationcount': 5549,
            'displayname': 'Entry cost',
            'fieldofstudyid': 2992352532,
            'level': 2,
            'maintype': None,
            'papercount': 287,
            'paperfamilycount': 239,
            'rank': 14998
        },
        {
            'citationcount': 9550,
            'displayname': 'Industrial Evolution',
            'fieldofstudyid': 2780575846,
            'level': 2,
            'maintype': None,
            'papercount': 525,
            'paperfamilycount': 488,
            'rank': 14502
        },
        {
            'citationcount': 286451,
            'displayname': 'Product innovation',
            'fieldofstudyid': 75434695,
            'level': 2,
            'maintype': None,
            'papercount': 15131,
            'paperfamilycount': 14393,
            'rank': 11278
        },
        {
            'citationcount': 14872,
            'displayname': 'Market entry strategy',
            'fieldofstudyid': 2779303836,
            'level': 2,
            'maintype': None,
            'papercount': 408,
            'paperfamilycount': 399,
            'rank': 14385
        },
        {
            'citationcount': 42198,
            'displayname': 'Knowledge spillover',
            'fieldofstudyid': 2776936074,
            'level': 2,
            'maintype': None,
            'papercount': 2066,
            'paperfamilycount': 1857,
            'rank': 13183
        },
        {
            'citationcount': 14845,
            'displayname': 'Industry dynamics',
            'fieldofstudyid': 2992788863,
            'level': 2,
            'maintype': None,
            'papercount': 719,
            'paperfamilycount': 598,
            'rank': 14193
        },
        {
            'citationcount': 77788,
            'displayname': 'Innovation system',
            'fieldofstudyid': 2781395336,
            'level': 2,
            'maintype': None,
            'papercount': 8105,
            'paperfamilycount': 7744,
            'rank': 12388
        },
        {
            'citationcount': 53964,
            'displayname': 'Dominant design',
            'fieldofstudyid': 2776228155,
            'level': 2,
            'maintype': None,
            'papercount': 684,
            'paperfamilycount': 639,
            'rank': 12835
        },
        {
            'citationcount': 75,
            'displayname': 'Schumpeterian rent',
            'fieldofstudyid': 2780319827,
            'level': 2,
            'maintype': None,
            'papercount': 9,
            'paperfamilycount': 8,
            'rank': 19358
        },
        {
            'citationcount': 10749,
            'displayname': 'Patent statistics',
            'fieldofstudyid': 2992246763,
            'level': 2,
            'maintype': None,
            'papercount': 333,
            'paperfamilycount': 302,
            'rank': 14419
        },
        {
            'citationcount': 21505,
            'displayname': 'Resource slack',
            'fieldofstudyid': 2779366248,
            'level': 2,
            'maintype': None,
            'papercount': 123,
            'paperfamilycount': 114,
            'rank': 13719
        },
        {
            'citationcount': 30243,
            'displayname': 'Technological distance',
            'fieldofstudyid': 2994217397,
            'level': 2,
            'maintype': None,
            'papercount': 159,
            'paperfamilycount': 140,
            'rank': 13666
        },
        {
            'citationcount': 11275,
            'displayname': 'Fixed fee',
            'fieldofstudyid': 3019835526,
            'level': 2,
            'maintype': None,
            'papercount': 391,
            'paperfamilycount': 343,
            'rank': 14346
        },
        {
            'citationcount': 24759,
            'displayname': 'Industry evolution',
            'fieldofstudyid': 2984381091,
            'level': 2,
            'maintype': None,
            'papercount': 644,
            'paperfamilycount': 590,
            'rank': 13574
        },
        {
            'citationcount': 15024,
            'displayname': 'Market selection',
            'fieldofstudyid': 2994106226,
            'level': 2,
            'maintype': None,
            'papercount': 511,
            'paperfamilycount': 459,
            'rank': 14044
        },
        {
            'citationcount': 338045,
            'displayname': 'Market structure',
            'fieldofstudyid': 155739000,
            'level': 2,
            'maintype': None,
            'papercount': 22515,
            'paperfamilycount': 19845,
            'rank': 10854
        },
        {
            'citationcount': 14334,
            'displayname': 'Spin offs',
            'fieldofstudyid': 2992649737,
            'level': 2,
            'maintype': None,
            'papercount': 1312,
            'paperfamilycount': 1235,
            'rank': 14178
        },
        {
            'citationcount': 11527,
            'displayname': 'Conglomerate merger',
            'fieldofstudyid': 105138414,
            'level': 2,
            'maintype': None,
            'papercount': 618,
            'paperfamilycount': 587,
            'rank': 14164
        },
        {
            'citationcount': 18987,
            'displayname': 'Cannibalization',
            'fieldofstudyid': 2777538425,
            'level': 2,
            'maintype': None,
            'papercount': 1155,
            'paperfamilycount': 1017,
            'rank': 13925
        },
        {
            'citationcount': 12209,
            'displayname': 'Green innovation',
            'fieldofstudyid': 2993150066,
            'level': 2,
            'maintype': None,
            'papercount': 999,
            'paperfamilycount': 965,
            'rank': 14487
        },
        {
            'citationcount': 12462,
            'displayname': 'Technology life cycle',
            'fieldofstudyid': 2776155606,
            'level': 2,
            'maintype': None,
            'papercount': 478,
            'paperfamilycount': 457,
            'rank': 14352
        },
        {
            'citationcount': 31039,
            'displayname': 'Unbundling',
            'fieldofstudyid': 7668479,
            'level': 2,
            'maintype': None,
            'papercount': 2999,
            'paperfamilycount': 2648,
            'rank': 13166
        },
        {
            'citationcount': 1391,
            'displayname': 'Market innovation',
            'fieldofstudyid': 2993307950,
            'level': 2,
            'maintype': None,
            'papercount': 296,
            'paperfamilycount': 290,
            'rank': 16029
        }
    ]
}

snapshots['BasicRoutesTests::test_get_fields_of_study_by_ids 1'] = {
    'fields_of_study': [
    ]
}

snapshots['BasicRoutesTests::test_get_fields_of_study_level_0 1'] = {
    'fields_of_study': [
        {
            'citationcount': 7698406,
            'displayname': 'History',
            'fieldofstudyid': 95457728,
            'level': 0,
            'maintype': None,
            'papercount': 3097099,
            'paperfamilycount': 3091672,
            'rank': 6861
        },
        {
            'citationcount': 41055475,
            'displayname': 'Geology',
            'fieldofstudyid': 127313418,
            'level': 0,
            'maintype': None,
            'papercount': 7477171,
            'paperfamilycount': 7385241,
            'rank': 5736
        },
        {
            'citationcount': 37140130,
            'displayname': 'Economics',
            'fieldofstudyid': 162324750,
            'level': 0,
            'maintype': None,
            'papercount': 3202713,
            'paperfamilycount': 2962526,
            'rank': 6154
        },
        {
            'citationcount': 22526545,
            'displayname': 'Geography',
            'fieldofstudyid': 205649164,
            'level': 0,
            'maintype': None,
            'papercount': 4609709,
            'paperfamilycount': 4587281,
            'rank': 6312
        },
        {
            'citationcount': 256551992,
            'displayname': 'Chemistry',
            'fieldofstudyid': 185592680,
            'level': 0,
            'maintype': None,
            'papercount': 18790051,
            'paperfamilycount': 17968615,
            'rank': 4358
        },
        {
            'citationcount': 4921107,
            'displayname': 'Philosophy',
            'fieldofstudyid': 138885662,
            'level': 0,
            'maintype': None,
            'papercount': 2033276,
            'paperfamilycount': 2028434,
            'rank': 7306
        },
        {
            'citationcount': 31064699,
            'displayname': 'Sociology',
            'fieldofstudyid': 144024400,
            'level': 0,
            'maintype': None,
            'papercount': 4564777,
            'paperfamilycount': 4543235,
            'rank': 6138
        },
        {
            'citationcount': 185322865,
            'displayname': 'Materials science',
            'fieldofstudyid': 192562407,
            'level': 0,
            'maintype': None,
            'papercount': 31579038,
            'paperfamilycount': 30128218,
            'rank': 4151
        },
        {
            'citationcount': 86082547,
            'displayname': 'Mathematics',
            'fieldofstudyid': 33923547,
            'level': 0,
            'maintype': None,
            'papercount': 7156607,
            'paperfamilycount': 6843843,
            'rank': 5138
        },
        {
            'citationcount': 349139576,
            'displayname': 'Biology',
            'fieldofstudyid': 86803240,
            'level': 0,
            'maintype': None,
            'papercount': 14081062,
            'paperfamilycount': 13983960,
            'rank': 4437
        },
        {
            'citationcount': 162535676,
            'displayname': 'Computer science',
            'fieldofstudyid': 41008148,
            'level': 0,
            'maintype': None,
            'papercount': 27782833,
            'paperfamilycount': 26577017,
            'rank': 4252
        },
        {
            'citationcount': 22672082,
            'displayname': 'Political science',
            'fieldofstudyid': 17744445,
            'level': 0,
            'maintype': None,
            'papercount': 6930265,
            'paperfamilycount': 6862906,
            'rank': 6012
        },
        {
            'citationcount': 85052577,
            'displayname': 'Engineering',
            'fieldofstudyid': 127413603,
            'level': 0,
            'maintype': 'business.industry',
            'papercount': 12712030,
            'paperfamilycount': 12431023,
            'rank': 4882
        },
        {
            'citationcount': 119844018,
            'displayname': 'Psychology',
            'fieldofstudyid': 15744967,
            'level': 0,
            'maintype': None,
            'papercount': 8403733,
            'paperfamilycount': 8354942,
            'rank': 5214
        },
        {
            'citationcount': 38920422,
            'displayname': 'Environmental science',
            'fieldofstudyid': 39432304,
            'level': 0,
            'maintype': None,
            'papercount': 6428703,
            'paperfamilycount': 6355668,
            'rank': 5852
        },
        {
            'citationcount': 27854476,
            'displayname': 'Business',
            'fieldofstudyid': 144133560,
            'level': 0,
            'maintype': None,
            'papercount': 5592205,
            'paperfamilycount': 5454207,
            'rank': 6104
        },
        {
            'citationcount': 93609574,
            'displayname': 'Physics',
            'fieldofstudyid': 121332964,
            'level': 0,
            'maintype': None,
            'papercount': 9361155,
            'paperfamilycount': 8861679,
            'rank': 5144
        },
        {
            'citationcount': 320117955,
            'displayname': 'Medicine',
            'fieldofstudyid': 71924100,
            'level': 0,
            'maintype': 'business.industry',
            'papercount': 29748536,
            'paperfamilycount': 29566906,
            'rank': 4138
        },
        {
            'citationcount': 5073818,
            'displayname': 'Art',
            'fieldofstudyid': 142362112,
            'level': 0,
            'maintype': 'media_common.quotation_subject',
            'papercount': 3873308,
            'paperfamilycount': 3868291,
            'rank': 6782
        }
    ]
}

snapshots['BasicRoutesTests::test_get_main_papers_of_field_of_study 1'] = {
    'main_papers': [
        {
            'OriginalAuthor': 'Richard M. Cyert',
            'citationcount': 6578,
            'paperid': 3122794957,
            'title': 'a behavioral theory of the firm',
            'year': 1963.0
        },
        {
            'OriginalAuthor': 'Richard Michael Cyert',
            'citationcount': 5218,
            'paperid': 2028436159,
            'title': 'a behavioral theory of the firm',
            'year': 1963.0
        },
        {
            'OriginalAuthor': 'Nitin Nohria',
            'citationcount': 1429,
            'paperid': 1973033485,
            'title': 'is slack good or bad for innovation',
            'year': 1996.0
        },
        {
            'OriginalAuthor': 'L. J. Bourgeois',
            'citationcount': 1377,
            'paperid': 2007893250,
            'title': 'on the measurement of organizational slack',
            'year': 1981.0
        },
        {
            'OriginalAuthor': 'Jitendra Vir Singh',
            'citationcount': 1064,
            'paperid': 1990866741,
            'title': 'performance slack and risk taking in organizational decision making',
            'year': 1986.0
        },
        {
            'OriginalAuthor': 'Gerard George',
            'citationcount': 726,
            'paperid': 3123640796,
            'title': 'slack resources and the performance of privately held firms',
            'year': 2005.0
        },
        {
            'OriginalAuthor': 'Justin Tan',
            'citationcount': 675,
            'paperid': 3121953586,
            'title': 'organizational slack and firm performance during economic transitions two studies from an emerging economy',
            'year': 2003.0
        },
        {
            'OriginalAuthor': 'Glenn B. Voss',
            'citationcount': 507,
            'paperid': 2134595776,
            'title': 'the effects of slack resources and environmentalthreat on product exploration and exploitation',
            'year': 2008.0
        },
        {
            'OriginalAuthor': 'Erwin Danneels',
            'citationcount': 485,
            'paperid': 2077260204,
            'title': 'organizational antecedents of second order competences',
            'year': 2008.0
        },
        {
            'OriginalAuthor': 'Yuri Mishina',
            'citationcount': 448,
            'paperid': 2048055926,
            'title': 'are more resources always better for growth resource stickiness in market and product expansion',
            'year': 2004.0
        }
    ]
}

snapshots['BasicRoutesTests::test_get_resources_field_of_study 1'] = {
    'resources': [
        {
            'citationcount': 297,
            'resourcetype': 2,
            'resourceurl': 'http://cep.lse.ac.uk/pubs/download/data1178.zip',
            'title': 'carbon taxes path dependency and directed technical change evidence from the auto industry',
            'year': 2016.0
        },
        {
            'citationcount': 154,
            'resourcetype': 4,
            'resourceurl': 'https://github.com/PABalland/EconGeo%5BGoogle',
            'title': 'smart specialization policy in the european union relatedness knowledge complexity and regional diversification',
            'year': 2019.0
        },
        {
            'citationcount': 147,
            'resourcetype': 4,
            'resourceurl': 'https://github.com/michaelewens/SDC-to-Compustat-Mapping/blob/master/README.md',
            'title': 'r d and the incentives from merger and acquisition activity',
            'year': 2013.0
        },
        {
            'citationcount': 117,
            'resourcetype': 4,
            'resourceurl': 'https://github.com/ivan-brugere/Bitcoin-Transaction-Network-Extraction',
            'title': 'analyzing the bitcoin network the first four years',
            'year': 2016.0
        },
        {
            'citationcount': 95,
            'resourcetype': 4,
            'resourceurl': 'http://www.princeton.edu/~reddings/code/Pswitch_code.zip',
            'title': 'multi product firms and product switching',
            'year': 2006.0
        },
        {
            'citationcount': 82,
            'resourcetype': 1,
            'resourceurl': 'http://pvidealab.berkeley.edu/innovation_in_PV_industry.html',
            'title': 'an innovation focused roadmap for a sustainable global photovoltaic industry',
            'year': 2014.0
        },
        {
            'citationcount': 73,
            'resourcetype': 4,
            'resourceurl': 'https://github.com/ethereum/wiki/',
            'title': 'trading real world assets on blockchain an application of trust free transaction systems in the market for lemons',
            'year': 2017.0
        },
        {
            'citationcount': 73,
            'resourcetype': 4,
            'resourceurl': 'https://github.com/ethereum/mist',
            'title': 'trading real world assets on blockchain an application of trust free transaction systems in the market for lemons',
            'year': 2017.0
        },
        {
            'citationcount': 66,
            'resourcetype': 4,
            'resourceurl': 'http://www.princeton.edu/~reddings/code/Pswitch_code.zip',
            'title': 'multi product firms and product switching',
            'year': 2006.0
        },
        {
            'citationcount': 63,
            'resourcetype': 4,
            'resourceurl': 'https://github.com/mtu-most/most-PMPY',
            'title': 'open source self replicating 3 d printer factory for small business manufacturing',
            'year': 2016.0
        }
    ]
}

snapshots['BasicRoutesTests::test_search_fields_of_study 1'] = {
    'fields_of_study': [
        {
            'citationcount': 3969,
            'displayname': 'Supply-side economics',
            'fieldofstudyid': 2779356393,
            'level': 2,
            'maintype': None,
            'papercount': 276,
            'paperfamilycount': 255,
            'rank': 15385
        },
        {
            'citationcount': 984,
            'displayname': 'Common good (economics)',
            'fieldofstudyid': 2779462423,
            'level': 2,
            'maintype': None,
            'papercount': 183,
            'paperfamilycount': 176,
            'rank': 16380
        },
        {
            'citationcount': 32549,
            'displayname': 'Post-Keynesian economics',
            'fieldofstudyid': 56777670,
            'level': 2,
            'maintype': None,
            'papercount': 4654,
            'paperfamilycount': 4337,
            'rank': 13047
        },
        {
            'citationcount': 9559,
            'displayname': 'Chicago school of economics',
            'fieldofstudyid': 2779041668,
            'level': 2,
            'maintype': None,
            'papercount': 178,
            'paperfamilycount': 167,
            'rank': 14568
        },
        {
            'citationcount': 74,
            'displayname': 'Structuralist economics',
            'fieldofstudyid': 2776606059,
            'level': 2,
            'maintype': None,
            'papercount': 14,
            'paperfamilycount': 14,
            'rank': 19041
        },
        {
            'citationcount': 60,
            'displayname': 'Quantum economics',
            'fieldofstudyid': 2780814561,
            'level': 3,
            'maintype': None,
            'papercount': 28,
            'paperfamilycount': 21,
            'rank': 18657
        },
        {
            'citationcount': 694314,
            'displayname': 'Service (economics)',
            'fieldofstudyid': 44161491,
            'level': 2,
            'maintype': 'media_common.quotation_subject',
            'papercount': 102609,
            'paperfamilycount': 99669,
            'rank': 9952
        },
        {
            'citationcount': 52,
            'displayname': 'Analysis economics',
            'fieldofstudyid': 2910177048,
            'level': 2,
            'maintype': None,
            'papercount': 14,
            'paperfamilycount': 13,
            'rank': 19016
        },
        {
            'citationcount': 79,
            'displayname': 'Entrepreneurial economics',
            'fieldofstudyid': 2778832405,
            'level': 3,
            'maintype': None,
            'papercount': 36,
            'paperfamilycount': 35,
            'rank': 18395
        },
        {
            'citationcount': 2566881,
            'displayname': 'Competition (economics)',
            'fieldofstudyid': 2780693313,
            'level': 2,
            'maintype': None,
            'papercount': 306792,
            'paperfamilycount': 287782,
            'rank': 8685
        },
        {
            'citationcount': 2975078,
            'displayname': 'Mathematical economics',
            'fieldofstudyid': 144237770,
            'level': 1,
            'maintype': None,
            'papercount': 202063,
            'paperfamilycount': 187484,
            'rank': 8585
        },
        {
            'citationcount': 10371,
            'displayname': 'Computational economics',
            'fieldofstudyid': 2776142066,
            'level': 2,
            'maintype': None,
            'papercount': 836,
            'paperfamilycount': 683,
            'rank': 14419
        },
        {
            'citationcount': 59868,
            'displayname': 'Happiness economics',
            'fieldofstudyid': 2778046797,
            'level': 3,
            'maintype': None,
            'papercount': 264,
            'paperfamilycount': 247,
            'rank': 12949
        },
        {
            'citationcount': 309696,
            'displayname': 'Preference (economics)',
            'fieldofstudyid': 2779413570,
            'level': 2,
            'maintype': None,
            'papercount': 17075,
            'paperfamilycount': 15383,
            'rank': 11005
        },
        {
            'citationcount': 2347689,
            'displayname': 'Positive economics',
            'fieldofstudyid': 118084267,
            'level': 1,
            'maintype': None,
            'papercount': 141449,
            'paperfamilycount': 136063,
            'rank': 9005
        },
        {
            'citationcount': 15,
            'displayname': 'Infrastructure and economics',
            'fieldofstudyid': 2777509107,
            'level': 2,
            'maintype': None,
            'papercount': 9,
            'paperfamilycount': 8,
            'rank': 19847
        },
        {
            'citationcount': 13920,
            'displayname': 'Marxian economics',
            'fieldofstudyid': 2778365179,
            'level': 4,
            'maintype': None,
            'papercount': 591,
            'paperfamilycount': 550,
            'rank': 14127
        },
        {
            'citationcount': 47076,
            'displayname': 'Simulations and games in economics education',
            'fieldofstudyid': 14642086,
            'level': 4,
            'maintype': None,
            'papercount': 3476,
            'paperfamilycount': 3465,
            'rank': 12742
        },
        {
            'citationcount': 49374,
            'displayname': 'Pharmacoeconomics',
            'fieldofstudyid': 2776738588,
            'level': 2,
            'maintype': None,
            'papercount': 4503,
            'paperfamilycount': 4486,
            'rank': 12886
        },
        {
            'citationcount': 69981,
            'displayname': 'Heterodox economics',
            'fieldofstudyid': 508532215,
            'level': 4,
            'maintype': None,
            'papercount': 6425,
            'paperfamilycount': 6319,
            'rank': 12391
        },
        {
            'citationcount': 6798,
            'displayname': 'Islamic economics',
            'fieldofstudyid': 2779703888,
            'level': 3,
            'maintype': None,
            'papercount': 3055,
            'paperfamilycount': 2864,
            'rank': 13830
        },
        {
            'citationcount': 17058,
            'displayname': 'Peace economics',
            'fieldofstudyid': 155631102,
            'level': 3,
            'maintype': 'medicine.medical_specialty',
            'papercount': 2495,
            'paperfamilycount': 2484,
            'rank': 13615
        },
        {
            'citationcount': 108,
            'displayname': 'Heterogeneity in economics',
            'fieldofstudyid': 2778391221,
            'level': 2,
            'maintype': None,
            'papercount': 7,
            'paperfamilycount': 7,
            'rank': 19242
        },
        {
            'citationcount': 9043,
            'displayname': 'Behavioural economics',
            'fieldofstudyid': 2993770480,
            'level': 2,
            'maintype': None,
            'papercount': 1389,
            'paperfamilycount': 1299,
            'rank': 14369
        },
        {
            'citationcount': 78006,
            'displayname': 'Urban economics',
            'fieldofstudyid': 145940883,
            'level': 2,
            'maintype': None,
            'papercount': 6856,
            'paperfamilycount': 6457,
            'rank': 12322
        },
        {
            'citationcount': 45295,
            'displayname': 'Regional economics',
            'fieldofstudyid': 2776858744,
            'level': 2,
            'maintype': None,
            'papercount': 5732,
            'paperfamilycount': 5478,
            'rank': 12795
        },
        {
            'citationcount': 278603,
            'displayname': 'Shock (economics)',
            'fieldofstudyid': 49034341,
            'level': 2,
            'maintype': None,
            'papercount': 31385,
            'paperfamilycount': 26304,
            'rank': 10986
        },
        {
            'citationcount': 161913,
            'displayname': 'Classical economics',
            'fieldofstudyid': 167562979,
            'level': 1,
            'maintype': None,
            'papercount': 26123,
            'paperfamilycount': 25724,
            'rank': 11287
        },
        {
            'citationcount': 32335,
            'displayname': 'Trough (economics)',
            'fieldofstudyid': 32239851,
            'level': 2,
            'maintype': None,
            'papercount': 4738,
            'paperfamilycount': 4617,
            'rank': 12925
        },
        {
            'citationcount': 10836,
            'displayname': 'Network economics',
            'fieldofstudyid': 2777926032,
            'level': 2,
            'maintype': None,
            'papercount': 632,
            'paperfamilycount': 585,
            'rank': 14248
        },
        {
            'citationcount': 385388,
            'displayname': 'Reproduction (economics)',
            'fieldofstudyid': 2779250656,
            'level': 2,
            'maintype': None,
            'papercount': 48171,
            'paperfamilycount': 47171,
            'rank': 10582
        },
        {
            'citationcount': 1143,
            'displayname': 'Dental economics',
            'fieldofstudyid': 2910405091,
            'level': 3,
            'maintype': None,
            'papercount': 545,
            'paperfamilycount': 545,
            'rank': 15624
        },
        {
            'citationcount': 576694,
            'displayname': 'Equity (economics)',
            'fieldofstudyid': 5148918,
            'level': 2,
            'maintype': None,
            'papercount': 48460,
            'paperfamilycount': 46810,
            'rank': 10364
        },
        {
            'citationcount': 56138,
            'displayname': 'Distortion (economics)',
            'fieldofstudyid': 97835835,
            'level': 2,
            'maintype': None,
            'papercount': 5410,
            'paperfamilycount': 4637,
            'rank': 12540
        },
        {
            'citationcount': 131933,
            'displayname': 'Experimental economics',
            'fieldofstudyid': 18619997,
            'level': 2,
            'maintype': None,
            'papercount': 6267,
            'paperfamilycount': 5265,
            'rank': 12062
        },
        {
            'citationcount': 2325,
            'displayname': 'Mineral economics',
            'fieldofstudyid': 71053439,
            'level': 3,
            'maintype': None,
            'papercount': 381,
            'paperfamilycount': 380,
            'rank': 15483
        },
        {
            'citationcount': 478296,
            'displayname': 'Welfare economics',
            'fieldofstudyid': 549774020,
            'level': 1,
            'maintype': None,
            'papercount': 146970,
            'paperfamilycount': 145213,
            'rank': 9874
        },
        {
            'citationcount': 13270,
            'displayname': 'Depreciation (economics)',
            'fieldofstudyid': 95383336,
            'level': 5,
            'maintype': None,
            'papercount': 1041,
            'paperfamilycount': 981,
            'rank': 14014
        },
        {
            'citationcount': 65555,
            'displayname': 'Learning-by-doing (economics)',
            'fieldofstudyid': 2781192542,
            'level': 2,
            'maintype': None,
            'papercount': 4556,
            'paperfamilycount': 4196,
            'rank': 12482
        },
        {
            'citationcount': 2686323,
            'displayname': 'Consumption (economics)',
            'fieldofstudyid': 1374810,
            'level': 2,
            'maintype': None,
            'papercount': 272807,
            'paperfamilycount': 256013,
            'rank': 8756
        },
        {
            'citationcount': 172839,
            'displayname': 'Applied economics',
            'fieldofstudyid': 149615983,
            'level': 2,
            'maintype': None,
            'papercount': 14786,
            'paperfamilycount': 14550,
            'rank': 11510
        },
        {
            'citationcount': 88049,
            'displayname': 'Rural economics',
            'fieldofstudyid': 557418111,
            'level': 4,
            'maintype': None,
            'papercount': 13952,
            'paperfamilycount': 13929,
            'rank': 11906
        },
        {
            'citationcount': 1941,
            'displayname': 'Rule of three (economics)',
            'fieldofstudyid': 2776125116,
            'level': 2,
            'maintype': None,
            'papercount': 147,
            'paperfamilycount': 146,
            'rank': 16203
        },
        {
            'citationcount': 709597,
            'displayname': 'Asset (economics)',
            'fieldofstudyid': 201049251,
            'level': 2,
            'maintype': None,
            'papercount': 75380,
            'paperfamilycount': 67478,
            'rank': 10035
        },
        {
            'citationcount': 168,
            'displayname': 'Test economics',
            'fieldofstudyid': 2986173549,
            'level': 4,
            'maintype': None,
            'papercount': 23,
            'paperfamilycount': 23,
            'rank': 18122
        },
        {
            'citationcount': 135287,
            'displayname': 'New institutional economics',
            'fieldofstudyid': 116006206,
            'level': 2,
            'maintype': None,
            'papercount': 4680,
            'paperfamilycount': 4365,
            'rank': 11927
        },
        {
            'citationcount': 267101,
            'displayname': 'Dominance (economics)',
            'fieldofstudyid': 143057031,
            'level': 2,
            'maintype': None,
            'papercount': 25585,
            'paperfamilycount': 24268,
            'rank': 11044
        },
        {
            'citationcount': 74673,
            'displayname': 'Managerial economics',
            'fieldofstudyid': 152430570,
            'level': 3,
            'maintype': None,
            'papercount': 3500,
            'paperfamilycount': 3445,
            'rank': 12364
        },
        {
            'citationcount': 3663087,
            'displayname': 'Labour economics',
            'fieldofstudyid': 145236788,
            'level': 1,
            'maintype': None,
            'papercount': 346330,
            'paperfamilycount': 326906,
            'rank': 8448
        },
        {
            'citationcount': 2294882,
            'displayname': 'Distribution (economics)',
            'fieldofstudyid': 39735319,
            'level': 2,
            'maintype': 'business.industry',
            'papercount': 276995,
            'paperfamilycount': 265429,
            'rank': 8836
        },
        {
            'citationcount': 126,
            'displayname': 'Post-autistic economics',
            'fieldofstudyid': 2776119178,
            'level': 3,
            'maintype': None,
            'papercount': 32,
            'paperfamilycount': 29,
            'rank': 18285
        },
        {
            'citationcount': 12156,
            'displayname': 'Break-even (economics)',
            'fieldofstudyid': 86223996,
            'level': 2,
            'maintype': None,
            'papercount': 965,
            'paperfamilycount': 922,
            'rank': 14182
        },
        {
            'citationcount': 684,
            'displayname': 'Fundamental theorems of welfare economics',
            'fieldofstudyid': 2779047909,
            'level': 3,
            'maintype': None,
            'papercount': 61,
            'paperfamilycount': 49,
            'rank': 17046
        },
        {
            'citationcount': 399739,
            'displayname': 'Health economics',
            'fieldofstudyid': 524218345,
            'level': 3,
            'maintype': None,
            'papercount': 25579,
            'paperfamilycount': 25258,
            'rank': 10883
        },
        {
            'citationcount': 4101,
            'displayname': 'Drawdown (economics)',
            'fieldofstudyid': 2779623740,
            'level': 3,
            'maintype': None,
            'papercount': 615,
            'paperfamilycount': 505,
            'rank': 15104
        },
        {
            'citationcount': 754,
            'displayname': 'Historical school of economics',
            'fieldofstudyid': 187741664,
            'level': 3,
            'maintype': None,
            'papercount': 71,
            'paperfamilycount': 71,
            'rank': 16961
        },
        {
            'citationcount': 18729,
            'displayname': 'Constitutional economics',
            'fieldofstudyid': 56720970,
            'level': 3,
            'maintype': None,
            'papercount': 3797,
            'paperfamilycount': 3721,
            'rank': 13277
        },
        {
            'citationcount': 19466,
            'displayname': 'Household economics',
            'fieldofstudyid': 2779723664,
            'level': 2,
            'maintype': None,
            'papercount': 610,
            'paperfamilycount': 535,
            'rank': 13882
        },
        {
            'citationcount': 1659013,
            'displayname': 'Value (economics)',
            'fieldofstudyid': 2776535242,
            'level': 2,
            'maintype': None,
            'papercount': 247990,
            'paperfamilycount': 235018,
            'rank': 9029
        },
        {
            'citationcount': 654,
            'displayname': 'Measurement in economics',
            'fieldofstudyid': 2778719853,
            'level': 3,
            'maintype': None,
            'papercount': 89,
            'paperfamilycount': 68,
            'rank': 16855
        },
        {
            'citationcount': 250,
            'displayname': 'Pharmaco economics',
            'fieldofstudyid': 3019626525,
            'level': 2,
            'maintype': None,
            'papercount': 69,
            'paperfamilycount': 69,
            'rank': 17637
        },
        {
            'citationcount': 828529,
            'displayname': 'Profit (economics)',
            'fieldofstudyid': 181622380,
            'level': 2,
            'maintype': None,
            'papercount': 102186,
            'paperfamilycount': 99896,
            'rank': 9820
        },
        {
            'citationcount': 56,
            'displayname': 'Binary economics',
            'fieldofstudyid': 2779634359,
            'level': 4,
            'maintype': None,
            'papercount': 18,
            'paperfamilycount': 18,
            'rank': 18871
        },
        {
            'citationcount': 46,
            'displayname': 'Causation in economics',
            'fieldofstudyid': 2780156244,
            'level': 2,
            'maintype': None,
            'papercount': 7,
            'paperfamilycount': 6,
            'rank': 19663
        },
        {
            'citationcount': 16685,
            'displayname': 'Thermoeconomics',
            'fieldofstudyid': 148234320,
            'level': 3,
            'maintype': None,
            'papercount': 543,
            'paperfamilycount': 537,
            'rank': 13706
        },
        {
            'citationcount': 1306092,
            'displayname': 'Elasticity (economics)',
            'fieldofstudyid': 113027937,
            'level': 2,
            'maintype': None,
            'papercount': 123860,
            'paperfamilycount': 121034,
            'rank': 9318
        },
        {
            'citationcount': 5569,
            'displayname': 'Regulatory economics',
            'fieldofstudyid': 2781367065,
            'level': 2,
            'maintype': None,
            'papercount': 229,
            'paperfamilycount': 203,
            'rank': 15042
        },
        {
            'citationcount': 8685,
            'displayname': 'Feminist economics',
            'fieldofstudyid': 540898589,
            'level': 2,
            'maintype': None,
            'papercount': 772,
            'paperfamilycount': 751,
            'rank': 14545
        },
        {
            'citationcount': 10,
            'displayname': 'Evolution of microeconomics',
            'fieldofstudyid': 2776858244,
            'level': 2,
            'maintype': None,
            'papercount': 1,
            'paperfamilycount': 1,
            'rank': 21516
        },
        {
            'citationcount': 1804013,
            'displayname': 'Socioeconomics',
            'fieldofstudyid': 45355965,
            'level': 1,
            'maintype': None,
            'papercount': 372620,
            'paperfamilycount': 369495,
            'rank': 8826
        },
        {
            'citationcount': 4238981,
            'displayname': 'Production (economics)',
            'fieldofstudyid': 2778348673,
            'level': 2,
            'maintype': None,
            'papercount': 782700,
            'paperfamilycount': 758688,
            'rank': 7959
        },
        {
            'citationcount': 243069,
            'displayname': 'Multiplier (economics)',
            'fieldofstudyid': 124584101,
            'level': 2,
            'maintype': None,
            'papercount': 37752,
            'paperfamilycount': 35859,
            'rank': 10675
        },
        {
            'citationcount': 34122,
            'displayname': 'New classical macroeconomics',
            'fieldofstudyid': 177591768,
            'level': 2,
            'maintype': None,
            'papercount': 830,
            'paperfamilycount': 761,
            'rank': 13154
        },
        {
            'citationcount': 254389,
            'displayname': 'Robustness (economics)',
            'fieldofstudyid': 2778193179,
            'level': 2,
            'maintype': None,
            'papercount': 17493,
            'paperfamilycount': 15199,
            'rank': 11313
        },
        {
            'citationcount': 1646428,
            'displayname': 'Macroeconomics',
            'fieldofstudyid': 139719470,
            'level': 1,
            'maintype': None,
            'papercount': 115986,
            'paperfamilycount': 110937,
            'rank': 9319
        },
        {
            'citationcount': 15428,
            'displayname': 'Agent-based computational economics',
            'fieldofstudyid': 2777618053,
            'level': 2,
            'maintype': None,
            'papercount': 495,
            'paperfamilycount': 393,
            'rank': 14184
        },
        {
            'citationcount': 2636003,
            'displayname': 'Financial economics',
            'fieldofstudyid': 106159729,
            'level': 1,
            'maintype': None,
            'papercount': 190067,
            'paperfamilycount': 184685,
            'rank': 8788
        },
        {
            'citationcount': 41833,
            'displayname': 'Consumer economics',
            'fieldofstudyid': 197902972,
            'level': 4,
            'maintype': None,
            'papercount': 3684,
            'paperfamilycount': 3662,
            'rank': 12902
        },
        {
            'citationcount': 285,
            'displayname': 'Definitions of economics',
            'fieldofstudyid': 184853033,
            'level': 5,
            'maintype': None,
            'papercount': 39,
            'paperfamilycount': 37,
            'rank': 17798
        },
        {
            'citationcount': 1555712,
            'displayname': 'International economics',
            'fieldofstudyid': 18547055,
            'level': 1,
            'maintype': None,
            'papercount': 218987,
            'paperfamilycount': 205298,
            'rank': 9126
        },
        {
            'citationcount': 1053,
            'displayname': 'Recursive economics',
            'fieldofstudyid': 58397932,
            'level': 5,
            'maintype': None,
            'papercount': 55,
            'paperfamilycount': 54,
            'rank': 16656
        },
        {
            'citationcount': 13142,
            'displayname': 'Normative economics',
            'fieldofstudyid': 2779637282,
            'level': 3,
            'maintype': None,
            'papercount': 539,
            'paperfamilycount': 471,
            'rank': 13987
        },
        {
            'citationcount': 385790,
            'displayname': 'Keynesian economics',
            'fieldofstudyid': 165556158,
            'level': 1,
            'maintype': None,
            'papercount': 60132,
            'paperfamilycount': 56898,
            'rank': 10411
        },
        {
            'citationcount': 44193,
            'displayname': 'Hysteresis (economics)',
            'fieldofstudyid': 2776379925,
            'level': 2,
            'maintype': None,
            'papercount': 4270,
            'paperfamilycount': 3871,
            'rank': 12789
        },
        {
            'citationcount': 329,
            'displayname': 'Nursing economics',
            'fieldofstudyid': 2910156750,
            'level': 3,
            'maintype': None,
            'papercount': 159,
            'paperfamilycount': 159,
            'rank': 16827
        },
        {
            'citationcount': 248898,
            'displayname': 'Behavioral economics',
            'fieldofstudyid': 109574028,
            'level': 2,
            'maintype': None,
            'papercount': 14975,
            'paperfamilycount': 13344,
            'rank': 11433
        },
        {
            'citationcount': 163989,
            'displayname': 'Institutional economics',
            'fieldofstudyid': 177821555,
            'level': 2,
            'maintype': None,
            'papercount': 10959,
            'paperfamilycount': 10187,
            'rank': 11672
        },
        {
            'citationcount': 7783,
            'displayname': 'Overheating (economics)',
            'fieldofstudyid': 117785501,
            'level': 2,
            'maintype': None,
            'papercount': 3331,
            'paperfamilycount': 3291,
            'rank': 13691
        },
        {
            'citationcount': 1190,
            'displayname': 'Pluralism in economics',
            'fieldofstudyid': 2781053042,
            'level': 5,
            'maintype': None,
            'papercount': 153,
            'paperfamilycount': 135,
            'rank': 16475
        },
        {
            'citationcount': 756,
            'displayname': 'Hard landing (economics)',
            'fieldofstudyid': 2777913741,
            'level': 3,
            'maintype': None,
            'papercount': 144,
            'paperfamilycount': 119,
            'rank': 16607
        },
        {
            'citationcount': 209874,
            'displayname': 'Business economics',
            'fieldofstudyid': 529859519,
            'level': 2,
            'maintype': None,
            'papercount': 23700,
            'paperfamilycount': 23577,
            'rank': 11320
        },
        {
            'citationcount': 15440,
            'displayname': 'Bioeconomics',
            'fieldofstudyid': 2778148510,
            'level': 2,
            'maintype': None,
            'papercount': 973,
            'paperfamilycount': 912,
            'rank': 14157
        },
        {
            'citationcount': 918,
            'displayname': 'Software economics',
            'fieldofstudyid': 2982913966,
            'level': 4,
            'maintype': None,
            'papercount': 73,
            'paperfamilycount': 73,
            'rank': 16645
        },
        {
            'citationcount': 12254,
            'displayname': 'Convexity in economics',
            'fieldofstudyid': 190607053,
            'level': 5,
            'maintype': None,
            'papercount': 544,
            'paperfamilycount': 541,
            'rank': 14060
        },
        {
            'citationcount': 583,
            'displayname': 'Qualitative economics',
            'fieldofstudyid': 150655782,
            'level': 2,
            'maintype': None,
            'papercount': 43,
            'paperfamilycount': 40,
            'rank': 17090
        },
        {
            'citationcount': 3860,
            'displayname': 'Teaching economics',
            'fieldofstudyid': 2992565346,
            'level': 4,
            'maintype': None,
            'papercount': 851,
            'paperfamilycount': 822,
            'rank': 14758
        },
        {
            'citationcount': 860,
            'displayname': 'Ricardian economics',
            'fieldofstudyid': 2776315787,
            'level': 3,
            'maintype': None,
            'papercount': 118,
            'paperfamilycount': 113,
            'rank': 16586
        },
        {
            'citationcount': 48725,
            'displayname': 'Stimulus (economics)',
            'fieldofstudyid': 2779990827,
            'level': 2,
            'maintype': None,
            'papercount': 7942,
            'paperfamilycount': 6950,
            'rank': 12539
        },
        {
            'citationcount': 5103657,
            'displayname': 'Microeconomics',
            'fieldofstudyid': 175444787,
            'level': 1,
            'maintype': None,
            'papercount': 300588,
            'paperfamilycount': 273942,
            'rank': 8174
        },
        {
            'citationcount': 11139,
            'displayname': 'Neo-Keynesian economics',
            'fieldofstudyid': 27747137,
            'level': 5,
            'maintype': None,
            'papercount': 675,
            'paperfamilycount': 664,
            'rank': 14255
        },
        {
            'citationcount': 1476987,
            'displayname': 'Agricultural economics',
            'fieldofstudyid': 48824518,
            'level': 1,
            'maintype': None,
            'papercount': 331143,
            'paperfamilycount': 320649,
            'rank': 8946
        },
        {
            'citationcount': 19,
            'displayname': 'Criticisms of neoclassical economics',
            'fieldofstudyid': 2776929239,
            'level': 2,
            'maintype': None,
            'papercount': 5,
            'paperfamilycount': 5,
            'rank': 20271
        },
        {
            'citationcount': 63454,
            'displayname': 'Philosophy and economics',
            'fieldofstudyid': 124339740,
            'level': 2,
            'maintype': None,
            'papercount': 7227,
            'paperfamilycount': 7142,
            'rank': 12372
        },
        {
            'citationcount': 118464,
            'displayname': 'Education economics',
            'fieldofstudyid': 527016502,
            'level': 4,
            'maintype': None,
            'papercount': 13419,
            'paperfamilycount': 13256,
            'rank': 11773
        },
        {
            'citationcount': 5310,
            'displayname': 'Pharmaceutical economics',
            'fieldofstudyid': 2908547366,
            'level': 2,
            'maintype': None,
            'papercount': 231,
            'paperfamilycount': 230,
            'rank': 15378
        },
        {
            'citationcount': 17827,
            'displayname': 'Hoarding (economics)',
            'fieldofstudyid': 2776504597,
            'level': 2,
            'maintype': None,
            'papercount': 1941,
            'paperfamilycount': 1713,
            'rank': 13761
        },
        {
            'citationcount': 9030,
            'displayname': 'Conflict economics',
            'fieldofstudyid': 118061837,
            'level': 3,
            'maintype': 'medicine.medical_specialty',
            'papercount': 631,
            'paperfamilycount': 610,
            'rank': 14551
        },
        {
            'citationcount': 9425,
            'displayname': 'Real estate economics',
            'fieldofstudyid': 2779631092,
            'level': 3,
            'maintype': None,
            'papercount': 242,
            'paperfamilycount': 217,
            'rank': 14531
        },
        {
            'citationcount': 504,
            'displayname': 'Participatory economics',
            'fieldofstudyid': 2776744804,
            'level': 4,
            'maintype': None,
            'papercount': 44,
            'paperfamilycount': 44,
            'rank': 17278
        },
        {
            'citationcount': 907,
            'displayname': 'Consumer unit (economics)',
            'fieldofstudyid': 2778664729,
            'level': 3,
            'maintype': None,
            'papercount': 53,
            'paperfamilycount': 51,
            'rank': 16589
        },
        {
            'citationcount': 729618,
            'displayname': 'Neoclassical economics',
            'fieldofstudyid': 133425853,
            'level': 1,
            'maintype': None,
            'papercount': 70943,
            'paperfamilycount': 68592,
            'rank': 9975
        },
        {
            'citationcount': 2618378,
            'displayname': 'Investment (macroeconomics)',
            'fieldofstudyid': 2776577366,
            'level': 2,
            'maintype': None,
            'papercount': 345149,
            'paperfamilycount': 322349,
            'rank': 8635
        },
        {
            'citationcount': 20694,
            'displayname': 'Bertrand paradox (economics)',
            'fieldofstudyid': 60312476,
            'level': 5,
            'maintype': None,
            'papercount': 829,
            'paperfamilycount': 806,
            'rank': 13751
        },
        {
            'citationcount': 2492284,
            'displayname': 'Natural resource economics',
            'fieldofstudyid': 175605778,
            'level': 1,
            'maintype': None,
            'papercount': 288255,
            'paperfamilycount': 279856,
            'rank': 8792
        },
        {
            'citationcount': 8017,
            'displayname': 'AP Macroeconomics',
            'fieldofstudyid': 201915964,
            'level': 3,
            'maintype': None,
            'papercount': 453,
            'paperfamilycount': 451,
            'rank': 14656
        },
        {
            'citationcount': 25757,
            'displayname': 'Complexity economics',
            'fieldofstudyid': 24511565,
            'level': 5,
            'maintype': None,
            'papercount': 1678,
            'paperfamilycount': 1652,
            'rank': 13529
        },
        {
            'citationcount': 157,
            'displayname': 'Non-equilibrium economics',
            'fieldofstudyid': 2776157074,
            'level': 5,
            'maintype': None,
            'papercount': 26,
            'paperfamilycount': 22,
            'rank': 18314
        },
        {
            'citationcount': 47432,
            'displayname': 'Leakage (economics)',
            'fieldofstudyid': 2777042071,
            'level': 2,
            'maintype': None,
            'papercount': 5986,
            'paperfamilycount': 5615,
            'rank': 12658
        },
        {
            'citationcount': 15872,
            'displayname': 'Family economics',
            'fieldofstudyid': 2780000394,
            'level': 2,
            'maintype': None,
            'papercount': 704,
            'paperfamilycount': 641,
            'rank': 14002
        },
        {
            'citationcount': 1644415,
            'displayname': 'Capital (economics)',
            'fieldofstudyid': 91760546,
            'level': 2,
            'maintype': None,
            'papercount': 193845,
            'paperfamilycount': 180776,
            'rank': 9132
        },
        {
            'citationcount': 29758,
            'displayname': 'Socialist economics',
            'fieldofstudyid': 43003075,
            'level': 2,
            'maintype': None,
            'papercount': 4988,
            'paperfamilycount': 4814,
            'rank': 12906
        },
        {
            'citationcount': 691,
            'displayname': 'Applied information economics',
            'fieldofstudyid': 67493897,
            'level': 5,
            'maintype': None,
            'papercount': 26,
            'paperfamilycount': 26,
            'rank': 17181
        },
        {
            'citationcount': 168,
            'displayname': 'Disequilibrium macroeconomics',
            'fieldofstudyid': 2778926449,
            'level': 3,
            'maintype': None,
            'papercount': 41,
            'paperfamilycount': 34,
            'rank': 17958
        },
        {
            'citationcount': 143121,
            'displayname': 'Depression (economics)',
            'fieldofstudyid': 2776867660,
            'level': 2,
            'maintype': None,
            'papercount': 20911,
            'paperfamilycount': 20344,
            'rank': 11508
        },
        {
            'citationcount': 90176,
            'displayname': 'Ecological economics',
            'fieldofstudyid': 176445938,
            'level': 3,
            'maintype': None,
            'papercount': 4146,
            'paperfamilycount': 3953,
            'rank': 12409
        },
        {
            'citationcount': 61572,
            'displayname': 'Neuroeconomics',
            'fieldofstudyid': 188660851,
            'level': 2,
            'maintype': None,
            'papercount': 1943,
            'paperfamilycount': 1757,
            'rank': 13104
        },
        {
            'citationcount': 69546,
            'displayname': 'Organizational economics',
            'fieldofstudyid': 516990006,
            'level': 2,
            'maintype': None,
            'papercount': 875,
            'paperfamilycount': 784,
            'rank': 12610
        },
        {
            'citationcount': 3390534,
            'displayname': 'Public economics',
            'fieldofstudyid': 100001284,
            'level': 1,
            'maintype': None,
            'papercount': 323938,
            'paperfamilycount': 309776,
            'rank': 8518
        },
        {
            'citationcount': 136083,
            'displayname': 'Energy economics',
            'fieldofstudyid': 13882206,
            'level': 2,
            'maintype': None,
            'papercount': 9616,
            'paperfamilycount': 9440,
            'rank': 11693
        },
        {
            'citationcount': 2017367,
            'displayname': 'Environmental economics',
            'fieldofstudyid': 134560507,
            'level': 1,
            'maintype': None,
            'papercount': 265792,
            'paperfamilycount': 260874,
            'rank': 8907
        },
        {
            'citationcount': 6051,
            'displayname': 'Sports economics',
            'fieldofstudyid': 2993414410,
            'level': 3,
            'maintype': None,
            'papercount': 970,
            'paperfamilycount': 797,
            'rank': 14605
        },
        {
            'citationcount': 2753563,
            'displayname': 'Demographic economics',
            'fieldofstudyid': 4249254,
            'level': 1,
            'maintype': None,
            'papercount': 258154,
            'paperfamilycount': 233763,
            'rank': 8765
        },
        {
            'citationcount': 29475,
            'displayname': 'Personnel economics',
            'fieldofstudyid': 85289506,
            'level': 3,
            'maintype': None,
            'papercount': 1969,
            'paperfamilycount': 1867,
            'rank': 13335
        },
        {
            'citationcount': 571,
            'displayname': 'AP Microeconomics',
            'fieldofstudyid': 3804391,
            'level': 2,
            'maintype': None,
            'papercount': 122,
            'paperfamilycount': 122,
            'rank': 16585
        },
        {
            'citationcount': 92725,
            'displayname': 'Mainstream economics',
            'fieldofstudyid': 6358003,
            'level': 3,
            'maintype': None,
            'papercount': 9343,
            'paperfamilycount': 9017,
            'rank': 12067
        },
        {
            'citationcount': 5716,
            'displayname': 'Media economics',
            'fieldofstudyid': 2776232172,
            'level': 2,
            'maintype': None,
            'papercount': 609,
            'paperfamilycount': 552,
            'rank': 14932
        },
        {
            'citationcount': 16708,
            'displayname': 'Sterilization (economics)',
            'fieldofstudyid': 148761745,
            'level': 4,
            'maintype': None,
            'papercount': 2565,
            'paperfamilycount': 2439,
            'rank': 13589
        },
        {
            'citationcount': 3920527,
            'displayname': 'Monetary economics',
            'fieldofstudyid': 556758197,
            'level': 1,
            'maintype': None,
            'papercount': 369847,
            'paperfamilycount': 319767,
            'rank': 8363
        },
        {
            'citationcount': 1992281,
            'displayname': 'Law and economics',
            'fieldofstudyid': 190253527,
            'level': 1,
            'maintype': None,
            'papercount': 497813,
            'paperfamilycount': 480695,
            'rank': 8533
        },
        {
            'citationcount': 11238,
            'displayname': 'Engineering economics',
            'fieldofstudyid': 75678037,
            'level': 2,
            'maintype': None,
            'papercount': 2232,
            'paperfamilycount': 2222,
            'rank': 13811
        },
        {
            'citationcount': 7090,
            'displayname': 'Medical economics',
            'fieldofstudyid': 2993121764,
            'level': 3,
            'maintype': None,
            'papercount': 1524,
            'paperfamilycount': 1514,
            'rank': 14254
        },
        {
            'citationcount': 356,
            'displayname': 'Mesoeconomics',
            'fieldofstudyid': 81436501,
            'level': 2,
            'maintype': None,
            'papercount': 115,
            'paperfamilycount': 109,
            'rank': 17078
        },
        {
            'citationcount': 41222,
            'displayname': 'Cultural economics',
            'fieldofstudyid': 36200757,
            'level': 3,
            'maintype': None,
            'papercount': 3584,
            'paperfamilycount': 3480,
            'rank': 12988
        },
        {
            'citationcount': 21355,
            'displayname': 'Process economics',
            'fieldofstudyid': 2993570610,
            'level': 2,
            'maintype': None,
            'papercount': 359,
            'paperfamilycount': 350,
            'rank': 14040
        },
        {
            'citationcount': 508,
            'displayname': 'Techno economics',
            'fieldofstudyid': 2986344143,
            'level': 3,
            'maintype': None,
            'papercount': 171,
            'paperfamilycount': 170,
            'rank': 16719
        },
        {
            'citationcount': 115400,
            'displayname': 'Evolutionary economics',
            'fieldofstudyid': 154848440,
            'level': 2,
            'maintype': None,
            'papercount': 5014,
            'paperfamilycount': 4524,
            'rank': 12114
        },
        {
            'citationcount': 76,
            'displayname': 'Nanoeconomics',
            'fieldofstudyid': 2775901687,
            'level': 2,
            'maintype': None,
            'papercount': 31,
            'paperfamilycount': 28,
            'rank': 18532
        },
        {
            'citationcount': 16,
            'displayname': 'Power theory of economics',
            'fieldofstudyid': 2776713284,
            'level': 2,
            'maintype': None,
            'papercount': 4,
            'paperfamilycount': 4,
            'rank': 20212
        },
        {
            'citationcount': 3545,
            'displayname': 'Geoeconomics',
            'fieldofstudyid': 2775982628,
            'level': 4,
            'maintype': None,
            'papercount': 565,
            'paperfamilycount': 557,
            'rank': 15100
        },
        {
            'citationcount': 96587,
            'displayname': 'New Keynesian economics',
            'fieldofstudyid': 10688316,
            'level': 3,
            'maintype': None,
            'papercount': 8093,
            'paperfamilycount': 5888,
            'rank': 12166
        },
        {
            'citationcount': 30922,
            'displayname': 'Transport economics',
            'fieldofstudyid': 168500671,
            'level': 2,
            'maintype': None,
            'papercount': 3680,
            'paperfamilycount': 3615,
            'rank': 13061
        },
        {
            'citationcount': 82299,
            'displayname': 'Innovation economics',
            'fieldofstudyid': 110599986,
            'level': 2,
            'maintype': None,
            'papercount': 5429,
            'paperfamilycount': 5352,
            'rank': 12352
        },
        {
            'citationcount': 101335,
            'displayname': 'Rationalization (economics)',
            'fieldofstudyid': 52438962,
            'level': 2,
            'maintype': None,
            'papercount': 11847,
            'paperfamilycount': 11597,
            'rank': 11904
        },
        {
            'citationcount': 75863,
            'displayname': 'Information economics',
            'fieldofstudyid': 119982944,
            'level': 2,
            'maintype': None,
            'papercount': 2494,
            'paperfamilycount': 2342,
            'rank': 12428
        },
        {
            'citationcount': 325242,
            'displayname': 'Convergence (economics)',
            'fieldofstudyid': 2777303404,
            'level': 2,
            'maintype': None,
            'papercount': 26520,
            'paperfamilycount': 22948,
            'rank': 10931
        },
        {
            'citationcount': 1606,
            'displayname': 'Dematerialization (economics)',
            'fieldofstudyid': 2779721780,
            'level': 2,
            'maintype': None,
            'papercount': 311,
            'paperfamilycount': 309,
            'rank': 15773
        },
        {
            'citationcount': 5661,
            'displayname': 'Identity economics',
            'fieldofstudyid': 154054963,
            'level': 3,
            'maintype': None,
            'papercount': 184,
            'paperfamilycount': 172,
            'rank': 15292
        },
        {
            'citationcount': 2740831,
            'displayname': 'Index (economics)',
            'fieldofstudyid': 2781157624,
            'level': 2,
            'maintype': None,
            'papercount': 330333,
            'paperfamilycount': 321051,
            'rank': 8628
        },
        {
            'citationcount': 3633910,
            'displayname': 'Development economics',
            'fieldofstudyid': 47768531,
            'level': 1,
            'maintype': None,
            'papercount': 469277,
            'paperfamilycount': 460229,
            'rank': 8323
        }
    ]
}

snapshots['MiscTests::test_bold 1'] = 'This is a <b>test</b>.'

snapshots['MiscTests::test_bold 2'] = 'This is the <b>Economy</b> of conflicts'

snapshots['MiscTests::test_bold 3'] = '<b>Inflation</b> in <b>lebanon</b> and in France'

snapshots['MiscTests::test_bold 4'] = '<b>Inflation</b> in  <b>lebanon</b> and in France'

snapshots['QueryTests::test_multiple_queries 1'] = [
    {
        'github_urls': [
        ],
        'id': 157651980,
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'score': 0.6891477608502484,
        'tags': [
        ],
        'title': 'The Political Economy of Heterogeneity and Conflict',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 8303905,
        'nbInCitations': 1593,
        'nbOutCitations': 30,
        'score': 0.689580003759732,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'Ethnicity, Insurgency, And Civil War',
        'year': 2003
    },
    {
        'github_urls': [
        ],
        'id': 143712489,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.6933264886099879,
        'tags': [
        ],
        'title': 'Conflict as a "Normal Economic Activity": The Contribution of Jack Hirshleifer, 1925-2005',
        'year': 2011
    },
    {
        'github_urls': [
        ],
        'id': 115361316,
        'nbInCitations': 85,
        'nbOutCitations': 0,
        'score': 0.7035439373376936,
        'tags': [
        ],
        'title': 'Causes of War: Power and the Roots of Conflict',
        'year': 2000
    },
    {
        'github_urls': [
        ],
        'id': 150935922,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.7287242668399478,
        'tags': [
        ],
        'title': 'Equilibrium Structure and Strategic Behavior in an Economic Model of Conflict',
        'year': 1995
    },
    {
        'github_urls': [
        ],
        'id': 153935554,
        'nbInCitations': 299,
        'nbOutCitations': 0,
        'score': 0.7520220368302116,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'A General Equilibrium Model of Insurrections',
        'year': 1991
    },
    {
        'github_urls': [
        ],
        'id': 141846582,
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'score': 0.7576219957073926,
        'tags': [
        ],
        'title': 'Economics of War and Peace: Economic, Legal, and Political Perspectives',
        'year': 2010
    },
    {
        'github_urls': [
        ],
        'id': 16307836,
        'nbInCitations': 71,
        'nbOutCitations': 50,
        'score': 0.7725674691323746,
        'tags': [
        ],
        'title': 'Poverty and violent conflict: A micro-level perspective on the causes and duration of warfare',
        'year': 2009
    },
    {
        'github_urls': [
        ],
        'id': 154424602,
        'nbInCitations': 87,
        'nbOutCitations': 0,
        'score': 0.7884886980566163,
        'tags': [
        ],
        'title': 'Workers, Warriors and Criminals: Social Conflict in General Equilibrium',
        'year': 2011
    },
    {
        'github_urls': [
        ],
        'id': 154652234,
        'nbInCitations': 86,
        'nbOutCitations': 0,
        'score': 0.7977172079338937,
        'tags': [
        ],
        'title': 'BARGAINING THEORY AND INTERNATIONAL CONFLICT',
        'year': 2002
    },
    {
        'github_urls': [
        ],
        'id': 153489233,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8134336202506027,
        'tags': [
        ],
        'title': 'ÁRMED CONFLICT, PEACE AND ECONOMICS',
        'year': 2014
    },
    {
        'github_urls': [
        ],
        'id': 158387887,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8277013583331592,
        'tags': [
        ],
        'title': 'Economics of War and Peace',
        'year': 2010
    },
    {
        'github_urls': [
        ],
        'id': 162691181,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8290400030931765,
        'tags': [
        ],
        'title': 'Conflict and economic consequences: comparative notes on "going to war"',
        'year': 2012
    },
    {
        'github_urls': [
        ],
        'id': 6146506,
        'nbInCitations': 0,
        'nbOutCitations': 23,
        'score': 0.8315824702635123,
        'tags': [
        ],
        'title': 'Economics, conflict and war',
        'year': 2008
    },
    {
        'github_urls': [
        ],
        'id': 152926004,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8333529001598525,
        'tags': [
        ],
        'title': 'Economics of Rivalry, Conflict and Cooperation',
        'year': 2010
    },
    {
        'github_urls': [
        ],
        'id': 14415686,
        'nbInCitations': 7,
        'nbOutCitations': 20,
        'score': 0.8416225397740063,
        'tags': [
        ],
        'title': 'Conflict and Trade: An Economics Approach to Political Interactions',
        'year': 1992
    },
    {
        'github_urls': [
        ],
        'id': 158883675,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8420759497676857,
        'tags': [
        ],
        'title': 'Economic and Political Aspects of Wars and Armed Conflicts',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 154011419,
        'nbInCitations': 1,
        'nbOutCitations': 19,
        'score': 0.8514703543533073,
        'tags': [
        ],
        'title': 'The costs of conflict: A choice-theoretic, equilibrium analysis',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 156140086,
        'nbInCitations': 5,
        'nbOutCitations': 0,
        'score': 0.8516621638360283,
        'tags': [
        ],
        'title': 'Economic Organization and Conflict',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 17180083,
        'nbInCitations': 582,
        'nbOutCitations': 4,
        'score': 0.8600485887742867,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'On economic causes of civil war',
        'year': 1998
    },
    {
        'github_urls': [
        ],
        'id': 159133460,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8683132343806952,
        'tags': [
        ],
        'title': 'Principles of Conflict Economics: The Political Economy of War, Terrorism, Genocide, and Peace',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 156769305,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8728463520141398,
        'tags': [
        ],
        'title': 'Economics and Social Conflict',
        'year': 2013
    },
    {
        'github_urls': [
        ],
        'id': 201642697,
        'nbInCitations': 41,
        'nbOutCitations': 20,
        'score': 0.8809400989807556,
        'tags': [
        ],
        'title': 'Conflict and Trade: An Economics Approach to Political International Interactions',
        'year': 1999
    },
    {
        'github_urls': [
        ],
        'id': 152898221,
        'nbInCitations': 13,
        'nbOutCitations': 0,
        'score': 0.8889031839162574,
        'tags': [
        ],
        'title': 'Economic Theories of Peace and War',
        'year': 2004
    },
    {
        'github_urls': [
        ],
        'id': 626761,
        'nbInCitations': 1829,
        'nbOutCitations': 23,
        'score': 0.9068680333009635,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'Greed and Grievance in Civil War',
        'year': 2001
    },
    {
        'github_urls': [
        ],
        'id': 201495757,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.9182618399676757,
        'tags': [
        ],
        'title': 'The economics of conflict, production, and exchange',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 55232315,
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'score': 0.9227577407888086,
        'tags': [
        ],
        'title': 'War and Conflict in Economics: Theories, Applications, and Recent Trends',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 6335379,
        'nbInCitations': 7,
        'nbOutCitations': 17,
        'score': 0.9316114158933326,
        'tags': [
        ],
        'title': 'Dynamics of Military Conflict: an Economics Perspective',
        'year': 2014
    },
    {
        'github_urls': [
        ],
        'id': 53450035,
        'nbInCitations': 37,
        'nbOutCitations': 92,
        'score': 0.9479241713365362,
        'tags': [
        ],
        'title': 'Economics and Violent Conflict',
        'year': 2003
    },
    {
        'github_urls': [
        ],
        'id': 150572740,
        'nbInCitations': 2,
        'nbOutCitations': 0,
        'score': 0.9516197415148552,
        'tags': [
        ],
        'title': 'Economics of conflict and peace',
        'year': 1997
    }
]

snapshots['QueryTests::test_multiple_queries 2'] = [
    {
        'authors': [
            [
                600239713,
                'E. Spolaore'
            ],
            [
                2227285919,
                'R. Wacziarg'
            ]
        ],
        'github_urls': [
        ],
        'id': 157651980,
        'journalName': 'National Bureau of Economic Research',
        'language': 'un',
        'magId': 2593496185,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'paperAbstract': "In this paper we present a conceptual framework linking cultural heterogeneity to inter-group conflict. When conflict is about control of public goods, more heterogeneous groups are expected to fight more with each other. In contrast, when conflict is about rival goods, more similar groups are more likely to engage in war with each other. We formalize these ideas within an analytical model and discuss recent empirical studies that are consistent with the model's implications.",
        'pdfUrls': [
            'https://papers.ssrn.com/sol3/papers2.cfm?abstract_id=2909642'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:157651980',
        'title': 'The Political Economy of Heterogeneity and Conflict',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                54438461,
                'D. D. Laitin'
            ],
            [
                2151351632,
                'J. D. Fearon'
            ]
        ],
        'github_urls': [
        ],
        'id': 8303905,
        'journalName': 'American Political Science Review',
        'language': 'un',
        'magId': 2151780178,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 1593,
        'nbOutCitations': 30,
        'paperAbstract': 'Between 1945 and 1999, about 3.33 million battle deaths occurred in the 25 interstate wars that killed at least 1,000 and had at least 100 dead on each side. These wars involved just 25 states that suffered casualties of at least 1,000 and had a median duration of not quite 3 months. In contrast, in the same period there were roughly 127 civil wars that killed at least 1,000, 25 of which were ongoing in 1999. A conservative estimate of the total dead as a direct result of these conflicts is 16.2 million, five times the interstate toll. These civil wars occurred in 73 states—more than a third of the United Nations system—and had a median duration of roughly six years. 1 The civil conflicts in this period surely produced refugee flows far greater than their death toll and far greater than the refugee flows associated with interstate wars since 1945. Cases such as Afghanistan, Somalia, and Lebanon testify to the economic devastation that civil wars can produce. By these crude measures, civil war has been a far greater scourge than interstate war in this period, though it has been studied far less. What explains the recent prevalence of violent civil conflict around the world? Is it due to the end of the Cold War and associated changes in the international system, or is it the result of longer-term trends? Why have some countries had civil wars while others have not? and Why did the wars break out when they did? We address these questions using data for the period 1945 to 1999 on the 161 countries that had a population of at least half a million in 1990.',
        'pdfUrls': [
            'http://www.cambridge.org/core/journals/american-political-science-review/article/ethnicity-insurgency-and-civil-war/B1D5D0E7C782483C5D7E102A61AD6605'
        ],
        'question': 'How do civil wars affect the death toll?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:8303905',
        'title': 'Ethnicity, Insurgency, And Civil War',
        'tldr': 'Between 1945 and 1999 there were roughly 127 civil wars that killed at least 1,000, 25 of which were ongoing in 1999. A conservative estimate of the total dead as a direct result of these conflicts is 16.2 million, five times the interstate toll.',
        'venue': None,
        'year': 2003
    },
    {
        'authors': [
            [
                2690042234,
                'T. T. Rangil'
            ]
        ],
        'github_urls': [
        ],
        'id': 143712489,
        'journalName': 'History of Political Economy',
        'language': 'un',
        'magId': 1984842730,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'The writings of the American economist Jack Hirshleifer (1925–2005) are considered some of the most influential contributions to the economics of conflict. This article examines how Hirshleifer transformed the behavioral assumptions of Homo economicus (the self-interest model and the concept of rationality) to offer economically grounded explanations for conflicts. We explain how, through his interactions with sociobiologists and game theorists, he reduced self-interest to mere selfishness and redefined rationality to encompass emotions and feelings. The final result was a disciplinary reclassification of conflict as a subvariety of selfish, rational behavior amenable to economic analysis.',
        'pdfUrls': [
            'https://read.dukeupress.edu/hope/article-abstract/43/4/625/12451/Conflict-as-a-Normal-Economic-Activity-The'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:143712489',
        'title': 'Conflict as a "Normal Economic Activity": The Contribution of Jack Hirshleifer, 1925-2005',
        'tldr': '',
        'venue': None,
        'year': 2011
    },
    {
        'authors': [
            [
                2799799320,
                'T. G. Mahnken'
            ]
        ],
        'github_urls': [
        ],
        'id': 115361316,
        'journalName': 'Naval War College Review',
        'language': 'un',
        'magId': 2885431712,
        'n_author': [
            0
        ],
        'nbInCitations': 85,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://digital-commons.usnwc.edu/nwc-review/vol53/iss3/12/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:115361316',
        'title': 'Causes of War: Power and the Roots of Conflict',
        'tldr': '',
        'venue': None,
        'year': 2000
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 150935922,
        'journalName': '',
        'language': 'un',
        'magId': 12929333,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'None'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:150935922',
        'title': 'Equilibrium Structure and Strategic Behavior in an Economic Model of Conflict',
        'tldr': '',
        'venue': None,
        'year': 1995
    },
    {
        'authors': [
            [
                3121328005,
                'H. I. Grossman'
            ]
        ],
        'github_urls': [
        ],
        'id': 153935554,
        'journalName': 'The American Economic Review',
        'language': 'un',
        'magId': 1575812287,
        'n_author': [
            0
        ],
        'nbInCitations': 299,
        'nbOutCitations': 0,
        'paperAbstract': "This paper develops a positive theory of insurrections that treats insurrection and its deterrence or suppression as economic activities that compete with production for scarce resources. The general equilibrium analytical framework reveals how the allocation of labor time among insurrection, soldiering, and production and the probabilistic distribution of income between the peasant families and the ruler's clientele both depend on the technology of insurrection. A central result is that equilibria with more time allocated to insurrection and a higher probability of a successful insurrection have lower production and total income, but nevertheless can have higher expected income for the peasants. Copyright 1991 by American Economic Association.",
        'pdfUrls': [
            'https://econpapers.repec.org/RePEc:aea:aecrev:v:81:y:1991:i:4:p:912-21'
        ],
        'question': 'How do insurrection, soldiering, and production affect labor time allocation?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:153935554',
        'title': 'A General Equilibrium Model of Insurrections',
        'tldr': 'The general equilibrium analytical framework reveals how the allocation of labor time among insurrection, soldiering, and production depends on the technology of insurrection. equilibria with more time allocated to insurrection and a higher probability of a successful insurrection have lower production and total income.',
        'venue': None,
        'year': 1991
    },
    {
        'authors': [
            [
                2150691331,
                'J. Brauer'
            ],
            [
                2168042330,
                'B. E. Goldsmith'
            ]
        ],
        'github_urls': [
        ],
        'id': 141846582,
        'journalName': 'Contributions to Conflict Management, Peace Economics and Development',
        'language': 'un',
        'magId': 577176003,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'paperAbstract': '"Economics of War and Peace: Economic, Legal, and Political Perspectives" brings together recent, cutting-edge research on economic factors affecting peace and war. This important area of continuing research was the focus of an international conference held at the University of Sydney in June 2009 and these chapters are partly drawn from among the best contributions to that meeting. The book weaves together threads from a number of themes in current research including new theoretical perspectives on the economic foundations of peace, violence and war within countries, connections between international trade and inter-state conflict, and the role of legal/institutional factors in international and internal conflict. Through a focused exploration of these related topics emerge areas of scholarly consensus as well as areas of continued debate. International in scope, it is the only book to explicitly bring together economic, legal and political scholarship to focus on the problem of conflict. It employs a range of modern social science analytical methods, including qualitative cases, econometrics, and game-theoretic models, to rigorously advance understanding of conflict within and between countries.',
        'pdfUrls': [
            'http://www.gbv.de/dms/zbw/627456685.pdf'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:141846582',
        'title': 'Economics of War and Peace: Economic, Legal, and Political Perspectives',
        'tldr': '',
        'venue': 'Contributions to Conflict Management, Peace Economics and Development',
        'year': 2010
    },
    {
        'authors': [
            [
                1773004899,
                'P. Justino'
            ]
        ],
        'github_urls': [
        ],
        'id': 16307836,
        'journalName': '',
        'language': 'un',
        'magId': 2147242040,
        'n_author': [
            0
        ],
        'nbInCitations': 71,
        'nbOutCitations': 50,
        'paperAbstract': 'This paper argues that endogenous mechanisms linking processes of violent conflict and household poverty provide valuable micro foundations to the ongoing debate on the causes and duration of armed conflicts. Household poverty affects the onset, sustainability and duration of violent conflict due to the direct and indirect effects of violence on the economic behaviour and decisions of households in conflict areas. These effects lead to the emergence of symbiotic relationships between armed groups and households living in areas they control that may sustain the conflict for a long time. The strength of this relationship is a function of two interdependent variables, namely household vulnerability to poverty and household vulnerability to violence.',
        'pdfUrls': [
            'http://journals.sagepub.com/doi/abs/10.1177/0022343309102655'
        ],
        'question': 'How do endogenous mechanisms linking violent conflict and household poverty affect the onset, sustainability and',
        's2Url': 'https://api.semanticscholar.org/CorpusID:16307836',
        'title': 'Poverty and violent conflict: A micro-level perspective on the causes and duration of warfare',
        'tldr': 'The paper argues that endogenous mechanisms linking violent conflict and household poverty provide valuable micro foundations to the ongoing debate on the causes and duration of armed conflicts. Household poverty affects the onset, sustainability and duration of violent conflict due to the direct and indirect effects of violence on the economic behaviour and decisions of households in conflict areas.',
        'venue': 'Journal of Peace Research',
        'year': 2009
    },
    {
        'authors': [
            [
                2095798042,
                'E. D. Bó'
            ],
            [
                2157902508,
                'P. D. Bó'
            ]
        ],
        'github_urls': [
        ],
        'id': 154424602,
        'journalName': 'Journal of the European Economic Association',
        'language': 'un',
        'magId': 2102817613,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 87,
        'nbOutCitations': 0,
        'paperAbstract': 'We analyze how economy-wide forces (i.e. shocks to terms of trade, technology and endowments) affect the intensity of social conflict. We see conflict phenomena such as crime and civil war as involving resource appropriation activities. We show that not all shocks that could make society richer will reduce conflict. Positive shocks to labor intensive industries will diminish social conflict, while positive shocks to capital intensive industries will increase it. The key requirement is that appropriation activities be more labor intensive than the economy. Our model can explain the positive association between crime and inequality, and the curse of natural resources; it predicts that aid in kind to war-ridden societies will have perverse effects, and offers guidance on how to integrate international trade policy and peacekeeping efforts. Including appropriation activities into a canonic general equilibrium model introduces a social constraint to policy analysis. Thus, we can also account for populist policies, apparently inefficient redistribution and national development strategies.',
        'pdfUrls': [
            'https://www.aeaweb.org/assa/2005/0107_0800_1103.pdf'
        ],
        'question': 'How do economic forces affect the intensity of social conflict?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:154424602',
        'title': 'Workers, Warriors and Criminals: Social Conflict in General Equilibrium',
        'tldr': 'We analyze how economy-wide forces affect the intensity of social conflict. We see conflict phenomena such as crime and civil war as involving resource appropriation activities.',
        'venue': None,
        'year': 2011
    },
    {
        'authors': [
            [
                3170017165,
                'R. Powell'
            ]
        ],
        'github_urls': [
        ],
        'id': 154652234,
        'journalName': 'Annual Review of Political Science',
        'language': 'un',
        'magId': 2165933393,
        'n_author': [
            0
        ],
        'nbInCitations': 86,
        'nbOutCitations': 0,
        'paperAbstract': " International relations theory has long seen the origins, conduct, and termination of war as a bargaining process. Recent formal work on these issues draws very heavily on Rubinstein's (1982) seminal analysis of the bargaining problem and the research that flowed from it. There is now what might be called a standard or canonical model of the origins of war that sees this outcome as a bargaining breakdown. This essay reviews this standard model and current efforts to extend it to the areas of (a) multilateral bargaining, which is at the heart of old issues such as balancing and bandwagoning as well as newer ones such as the role of third-party mediation; (b) the effects of domestic politics on international outcomes; (c) efforts to explicitly model intra-war bargaining; and (d) dynamic commitment problems.",
        'pdfUrls': [
            'http://anthro.annualreviews.org/doi/abs/10.1146/annurev.polisci.5.092601.141138'
        ],
        'question': 'What is the origins of war?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:154652234',
        'title': 'BARGAINING THEORY AND INTERNATIONAL CONFLICT',
        'tldr': 'International relations theory has long seen the origins, conduct, and termination of war as a bargaining process. There is now a standard or canonical model of the origins of war that sees this outcome as a bargaining breakdown.',
        'venue': None,
        'year': 2002
    },
    {
        'authors': [
            [
                702502192,
                'G. D. V. Agudelo'
            ],
            [
                2121176568,
                'V. T. Bustamante'
            ],
            [
                2150124719,
                'J. B. Marín'
            ]
        ],
        'github_urls': [
        ],
        'id': 153489233,
        'journalName': 'Revista de Economía del Caribe',
        'language': 'un',
        'magId': 2013623756,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://rcientificas.uninorte.edu.co/index.php/economia/article/viewFile/6174/4695'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:153489233',
        'title': 'ÁRMED CONFLICT, PEACE AND ECONOMICS',
        'tldr': '',
        'venue': 'Revista de Economía del Caribe',
        'year': 2014
    },
    {
        'authors': [
            [
                2772280447,
                'B. Goldsmith'
            ]
        ],
        'github_urls': [
        ],
        'id': 158387887,
        'journalName': '',
        'language': 'un',
        'magId': 2771175901,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Presents the research on economic factors affecting peace and war. This title includes theoretical perspectives on the economic foundations of peace, violence and war within countries, connections between international trade and inter-state conflict, and the role of legal/institutional factors in international and internal conflict.',
        'pdfUrls': [
            'https://books.emeraldinsight.com/page/detail/Economics-of-War-and-Peace/?k=9780857240040'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:158387887',
        'title': 'Economics of War and Peace',
        'tldr': '',
        'venue': None,
        'year': 2010
    },
    {
        'authors': [
            [
                806307504,
                'L. Jcr'
            ],
            [
                2099503092,
                'd. W. Hf'
            ]
        ],
        'github_urls': [
        ],
        'id': 162691181,
        'journalName': '',
        'language': 'un',
        'magId': 2154691301,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://isaconf.confex.com/isaconf/wc2014/webprogram/Paper48944.html'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:162691181',
        'title': 'Conflict and economic consequences: comparative notes on "going to war"',
        'tldr': '',
        'venue': None,
        'year': 2012
    },
    {
        'authors': [
            [
                2105604964,
                'J. Dunne'
            ],
            [
                2276569092,
                'F. Coulomb'
            ]
        ],
        'github_urls': [
        ],
        'id': 6146506,
        'journalName': '',
        'language': 'un',
        'magId': 2945283801,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 23,
        'paperAbstract': '',
        'pdfUrls': [
            'https://ideas.repec.org/p/hal/journl/hal-02051663.html'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:6146506',
        'title': 'Economics, conflict and war',
        'tldr': '',
        'venue': None,
        'year': 2008
    },
    {
        'authors': [
            [
                2073665876,
                'P. Gangopadhyay'
            ]
        ],
        'github_urls': [
        ],
        'id': 152926004,
        'journalName': '',
        'language': 'un',
        'magId': 1512195694,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'This book offers an extensive and original study of the dynamics of rivalry, evolution of costly and violent conflicts, and potential cooperation among powerful players. It unravels the special features of the global socio-economic system that can make it extremely fragile and vulnerable. It serves as a good reference source for anyone interested in some of the pressing and emerging problems of the global system, such as intra-national and interethnic conflicts, climate change challenges, poverty and terrorism, and provides useful and rigorous insights into the collective bid to resolve some of these problems. Written in a simple and accessible manner, this book will help researchers and policy makers in understanding and abetting costly conflicts.',
        'pdfUrls': [
            'https://www.gbv.de/dms/zbw/629519900.pdf'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:152926004',
        'title': 'Economics of Rivalry, Conflict and Cooperation',
        'tldr': '',
        'venue': None,
        'year': 2010
    },
    {
        'authors': [
            [
                1992983747,
                'S. W. Polachek'
            ]
        ],
        'github_urls': [
        ],
        'id': 14415686,
        'journalName': '',
        'language': 'un',
        'magId': 1974064784,
        'n_author': [
            0
        ],
        'nbInCitations': 7,
        'nbOutCitations': 20,
        'paperAbstract': "The Klein/Gronicki/Kosaka contributions dig deeply into the impact of revolutionary political change in Eastern European countries upon their economies and indirectly through trade upon Western European economies, focussing particularly on the repercussions of anticipated arms cutbacks. However, when we examine trade, a critical issue to most national and regional economies, and a phenomena that is directly and indirectly tied in a major way to a country's military expenditures (Polachek provides empirical support for this assertion), it then becomes absolutely essential to inquire in general how political conflict affects trade and vice versa. In his contribution Polachek concentrates on political conflict as affected by trade. Can one argue that the greater the trade between an actor country and a target, the smaller the amount of actor to target conflict (or the greater the amount of cooperation)? Since the greater the inelasticity of the demand for imports and the supply of exports, the greater with increased trade the respective consumer surplus and producer surplus (measures of welfare gains), can we state: the greater the inelasticity of import demand and export supply of an actor country to a target, the smaller the amount of actor to target conflict. Polachek also looks at the reverse question, though not as extensively: does political conflict affect the level of trade? The author ingeniously exploits the several sets of data developed by political scientists, each inadequate in certain ways, and several analytical techniques (each also deficient in one way or another), to obtain relatively robust findings on the first of these two critical questions.",
        'pdfUrls': [
            'https://www.degruyter.com/view/j/peps.1999.5.issue-2/peps.1999.5.2.1022/peps.1999.5.2.1022.xml'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:14415686',
        'title': 'Conflict and Trade: An Economics Approach to Political Interactions',
        'tldr': '',
        'venue': 'Economics of Arms Reduction and the Peace Process',
        'year': 1992
    },
    {
        'authors': [
            [
                2906456209,
                'M. Palczewska'
            ]
        ],
        'github_urls': [
        ],
        'id': 158883675,
        'journalName': 'Chinese Business Review',
        'language': 'un',
        'magId': 2906390504,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://sin.akademia.mil.pl/publications/details/i3051'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:158883675',
        'title': 'Economic and Political Aspects of Wars and Armed Conflicts',
        'tldr': '',
        'venue': None,
        'year': 2018
    },
    {
        'authors': [
            [
                2167953235,
                'B. Walia'
            ],
            [
                2255255695,
                'S. Sanders'
            ],
            [
                2409682982,
                'Y. Chang'
            ]
        ],
        'github_urls': [
        ],
        'id': 154011419,
        'journalName': 'Economics Letters',
        'language': 'un',
        'magId': 2024405933,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 1,
        'nbOutCitations': 19,
        'paperAbstract': 'In models of (destructive) armed conflict, it is standard to account for the endogeneity of arming allocations made by incumbent government and rebel parties. Indeed, standard contest-theoretic (microeconomic) models of behavior recognize that allocations change with shifts in marginal benefit or marginal cost. Taking governments and rebels as responsive to such shifts, the present study applies standard, contest-theoretic, equilibrium analysis to the Smith et al. (2014) model of conflict and cooperation. This alternative solution methodology yields starkly different results. Within the present analysis, there does not exist greater scope for cooperation given endogenously-destructive arming rather than exogenously-destructive arming.',
        'pdfUrls': [
            'https://econpapers.repec.org/article/eeeecolet/v_3a131_3ay_3a2015_3ai_3ac_3ap_3a62-65.htm'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:154011419',
        'title': 'The costs of conflict: A choice-theoretic, equilibrium analysis',
        'tldr': '',
        'venue': None,
        'year': 2015
    },
    {
        'authors': [
            [
                2124012603,
                'D. W. Carlton'
            ]
        ],
        'github_urls': [
        ],
        'id': 156140086,
        'journalName': '',
        'language': 'un',
        'magId': 2339547347,
        'n_author': [
            0
        ],
        'nbInCitations': 5,
        'nbOutCitations': 0,
        'paperAbstract': 'Economic institutions and the structure of economic organziations can play a large role in either accentuating or diminishing tensions between groups. I draw on two lines of economic research : the theory of the firm, including agency theory, and international trade. I show that there is a fundamental externality that tends to accentuate conflict among groups. By altering trade patterns and firm structure, conflict can be reduced and output increased. (JEL: L 14, D 23, D 47)',
        'pdfUrls': [
            'https://www.jstor.org/stable/40751794'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:156140086',
        'title': 'Economic Organization and Conflict',
        'tldr': '',
        'venue': None,
        'year': 2016
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 17180083,
        'journalName': '',
        'language': 'un',
        'magId': None,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 582,
        'nbOutCitations': 4,
        'paperAbstract': '',
        'pdfUrls': [
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:17180083',
        'title': 'On economic causes of civil war',
        'tldr': '',
        'venue': 'Oxford Economic Papers',
        'year': 1998
    },
    {
        'authors': [
            [
                2131249502,
                'C. H. Anderton'
            ],
            [
                3129005348,
                'J. R. Carter'
            ]
        ],
        'github_urls': [
        ],
        'id': 159133460,
        'journalName': '',
        'language': 'un',
        'magId': 2936999067,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://dx.doi.org/10.1017/9781316875506'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:159133460',
        'title': 'Principles of Conflict Economics: The Political Economy of War, Terrorism, Genocide, and Peace',
        'tldr': '',
        'venue': None,
        'year': 2019
    },
    {
        'authors': [
            [
                2076062243,
                'C. D. Mildenberger'
            ]
        ],
        'github_urls': [
        ],
        'id': 156769305,
        'journalName': '',
        'language': 'un',
        'magId': 2480229600,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://link.springer.com/10.1057/9781137281890'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:156769305',
        'title': 'Economics and Social Conflict',
        'tldr': '',
        'venue': None,
        'year': 2013
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 201642697,
        'journalName': 'Peace Economics, Peace Science and Public Policy',
        'language': 'un',
        'magId': None,
        'n_author': [
            0
        ],
        'nbInCitations': 41,
        'nbOutCitations': 20,
        'paperAbstract': "The Klein/Gronicki/Kosaka contributions dig deeply into the impact of revolutionary political change in Eastern European countries upon their economies and indirectly through trade upon Western European economies, focussing particularly on the repercussions of anticipated arms cutbacks. However, when we examine trade, a critical issue to most national and regional economies, and a phenomena that is directly and indirectly tied in a major way to a country's military expenditures (Polachek provides empirical support for this assertion), it then becomes absolutely essential to inquire in general how political conflict affects trade and vice versa. In his contribution Polachek concentrates on political conflict as affected by trade. Can one argue that the greater the trade between an actor country and a target, the smaller the amount of actor to target conflict (or the greater the amount of cooperation)? Since the greater the inelasticity of the demand for imports and the supply of exports, the greater with increased trade the respective consumer surplus and producer surplus (measures of welfare gains), can we state: the greater the inelasticity of import demand and export supply of an actor country to a target, the smaller the amount of actor to target conflict. Polachek also looks at the reverse question, though not as extensively: does political conflict affect the level of trade? The author ingeniously exploits the several sets of data developed by political scientists, each inadequate in certain ways, and several analytical techniques (each also deficient in one way or another), to obtain relatively robust findings on the first of these two critical questions.",
        'pdfUrls': [
        ],
        'question': 'How does trade affect political conflict?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:201642697',
        'title': 'Conflict and Trade: An Economics Approach to Political International Interactions',
        'tldr': 'Polachek concentrates on political conflict as affected by trade.',
        'venue': None,
        'year': 1999
    },
    {
        'authors': [
            [
                2717631681,
                'F. Coulomb'
            ]
        ],
        'github_urls': [
        ],
        'id': 152898221,
        'journalName': 'Routledge Studies in Defence and Peace Economics',
        'language': 'un',
        'magId': 1542471030,
        'n_author': [
            0
        ],
        'nbInCitations': 13,
        'nbOutCitations': 0,
        'paperAbstract': 'Introduction Part 1:Economy, Factor of Peace or War. A Theoretical Dichotomy Which Appeared with Political Economy During the 18th Century 1. National Power Benefits From The Economy 2. Economy as a Factor of Peace 3. The Hesitations and Internal Differences within each Perspective of the Economy as a Factor of War and Peace Part Two: War and Peace, Resultant of an Economic System. New Economic Analyses on Defence-Related Issues Since the Mid-19th Century 4. War and the Threat of War at the Heart of the Capitalism System Functioning 5. "Turbulence" Inherent to Capitalism Part Three: From New Debates Opened by Economics on Peace and War Factors to Resurgence of the Political Economy\'s Perspective 6. Peace and War Factors Revealed by the Economic Science 7. The Strategic Dimension of Political Economy and the Concept of \'Economic War\'.',
        'pdfUrls': [
            'https://www.taylorfrancis.com/books/9780429233494'
        ],
        'question': 'What is the role of political economy in peace or war?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:152898221',
        'title': 'Economic Theories of Peace and War',
        'tldr': 'Political Economy was a factor of Peace or War during the 18th Century.',
        'venue': 'Routledge Studies in Defence and Peace Economics',
        'year': 2004
    },
    {
        'authors': [
            [
                1502687800,
                'A. Hoeffler'
            ],
            [
                2002927953,
                'P. Collier'
            ]
        ],
        'github_urls': [
        ],
        'id': 626761,
        'journalName': '',
        'language': 'un',
        'magId': 2097432728,
        'n_author': [
            0
        ],
        'nbInCitations': 1829,
        'nbOutCitations': 23,
        'paperAbstract': "The authors compare two contrasting motivations for rebellion: greed and grievance. Most rebellions are ostensibly in pursuit of a cause, supported by a narrative of grievance. But since grievance assuagement through rebellion is a public good that a government will not supply, economists predict such rebellions would be rare. Empirically, many rebellions appear to be linked to the capture of resources (such as diamonds in Angola, and Sierra Leone, drugs in Colombia, and timber in Cambodia). The authors set up a simple rational choice model of greed-rebellion, and contrasts its predictions with those of a simple grievance model. Some countries return to conflict repeatedly. Are they conflict-prone, or is there a feedback effect whereby conflict generates grievance, which in turn generates further conflict? The authors show why such a feedback effect might be present in both greed-motivated and grievance rebellions. The authors' results contrast with conventional beliefs, about the causes of conflict. A stylized version of conventional beliefs would be that grievance begets conflict, which begets grievance, which begets further conflict. With such a model, the only point at which to intervene is to reduce the level of objective grievance. The authors' model suggests that what actually happens is that opportunities for predation (controlling primary commodity exports) cause conflict, and the grievances this generates induce diasporas to finance further conflict. The point of policy intervention here is to reduce the absolute, and relative attraction of primary commodity predation, and to reduce the ability of diasporas to fund rebel movements.",
        'pdfUrls': [
            'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=630727&rec=1&srcabs=318597&alg=7&pos=1'
        ],
        'question': 'How do greed and grievance affect rebellion?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:626761',
        'title': 'Greed and Grievance in Civil War',
        'tldr': 'Authors compare two contrasting motivations for rebellion: greed and grievance. They set up a simple rational choice model of greed-rebellion.',
        'venue': 'Quarterly Journal of Economics',
        'year': 2001
    },
    {
        'authors': [
            [
                2131249502,
                'C. H. Anderton'
            ]
        ],
        'github_urls': [
        ],
        'id': 201495757,
        'journalName': '',
        'language': 'un',
        'magId': 2965510803,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.taylorfrancis.com/books/e/9781315240138/chapters/10.4324/9781315240138-11'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:201495757',
        'title': 'The economics of conflict, production, and exchange',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                2031023982,
                'R. M. Sheremeta'
            ],
            [
                2307095496,
                'E. O. Kimbrough'
            ],
            [
                2738365255,
                'K. Laughren'
            ]
        ],
        'github_urls': [
        ],
        'id': 55232315,
        'journalName': 'Journal of Economic Behavior and Organization',
        'language': 'un',
        'magId': 2739690392,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'paperAbstract': 'We review the main economic models of war and conflict. These models vary in details, but their implications are qualitatively consistent, highlighting key commonalities across a variety of conflict settings. Recent empirical literature, employing both laboratory and field data, in many cases confirms the basic implications of conflict theory. However, this literature also presents important challenges to the way economists traditionally model conflict. We finish our review by suggesting ways to address these challenges.',
        'pdfUrls': [
            'https://econpapers.repec.org/RePEc:pra:mprapa:80277'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:55232315',
        'title': 'War and Conflict in Economics: Theories, Applications, and Recent Trends',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                2145463474,
                'L. Reimer'
            ],
            [
                2289656152,
                'K. Beckmann'
            ]
        ],
        'github_urls': [
        ],
        'id': 6335379,
        'journalName': 'Review of Economics',
        'language': 'un',
        'magId': 149824699,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 7,
        'nbOutCitations': 17,
        'paperAbstract': "Using examples for each type of model, we consider dynamic games, differential games, and simulation as alternative ways of extending the standard static economic model of conflict to study patterns of conflict dynamics. It turns out that computational requirements and theoretical difficulties impose tight limits on what can be achieved using the first two approaches. In particular, we are unable to study dynamic military conflict as a series of ``battles'' that are resolved individually. A simulation study based on a new model of adaptive, boundedly rational decision making, however, is shown not to be subject to this limitation. Plausible patterns of conflict dynamics emerge, which we can link to both historical conflict and standard tenets of military theory.",
        'pdfUrls': [
            'https://www.degruyter.com/view/j/roe.2014.65.issue-2/roe-2014-0205/roe-2014-0205.xml'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:6335379',
        'title': 'Dynamics of Military Conflict: an Economics Perspective',
        'tldr': '',
        'venue': None,
        'year': 2014
    },
    {
        'authors': [
            [
                2116540548,
                'M. Humphreys'
            ]
        ],
        'github_urls': [
        ],
        'id': 53450035,
        'journalName': '',
        'language': 'un',
        'magId': 25394324,
        'n_author': [
            0
        ],
        'nbInCitations': 37,
        'nbOutCitations': 92,
        'paperAbstract': 'The present invention permits a screw or male member to align prior to entering a threaded section and being driven. This alignment can avoid cross threading of the screw and the internal threads as often happens with power driven screws. The present invention generally includes a device with an unthreaded section and a threaded section. A screw or male member passes through the unthreaded section prior to entering the threaded section and causes the screw or male member to be aligned before being driven.',
        'pdfUrls': [
            'http://www.hpcrresearch.org/sites/default/files/publications/Essay.pdf'
        ],
        'question': 'How does a screw or male member align prior to entering a threaded section?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:53450035',
        'title': 'Economics and Violent Conflict',
        'tldr': 'The present invention permits a screw or male member to align prior to entering a threaded section and being driven. A screw or male member passes through the unthreaded section prior to entering the threaded section.',
        'venue': None,
        'year': 2003
    },
    {
        'authors': [
            [
                1536841065,
                'W. G. Gissy'
            ],
            [
                2150691331,
                'J. Brauer'
            ]
        ],
        'github_urls': [
        ],
        'id': 150572740,
        'journalName': '',
        'language': 'un',
        'magId': 2970981983,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 2,
        'nbOutCitations': 0,
        'paperAbstract': 'Contents: Introduction Theory-Approaches and Approaches to Theory: Economics and peace-theory on the eve of World War I More with less: economics of non-offensive defense, with special reference to Argentina The economics of conflict, production and exchange The distribution of military expenditures in the United States: spatial, sectoral, technological and occupational. The Opportunity Costs of Military Expenditures: Human Development, and Economic Development and Growth: Opportunity costs of military expenditures: evidence from the United States Military expenditures and fiscal constraints in Pakistan Peace in Guatemala? The story of San Lucas TolimA!n From apartheid to democracy: the economic dimensions of demilitarizing South African society Do military expenditures create net employment? the case of US military-nuclear production sites. The Economic Cost of War and its Aftermath: The Sudan: the cost of the second civil war (1983-1993) That splendid little wa: the costs of the Spanish-American war Estimates of the economic cost of armed conflict: the Iran-Iraq war and the Sri Lankan civil war Research note: costing the direct health burden of political violence in developing countries. Securing Security: War and peace from a perspective of international public economics A world treasury Policies for peace: an analysis of the causes of military expenditures and the means to disarmament Creating global security: Japan as a potential catalyst.',
        'pdfUrls': [
            'https://www.taylorfrancis.com/books/e/9781315240138'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:150572740',
        'title': 'Economics of conflict and peace',
        'tldr': '',
        'venue': None,
        'year': 1997
    }
]

snapshots['QueryTests::test_multiple_queries 3'] = [
    {
        'github_urls': [
        ],
        'id': 15835932,
        'nbInCitations': 2,
        'nbOutCitations': 12,
        'score': 0.7152299131978479,
        'tags': [
        ],
        'title': 'Constant-Round Zero-Knowledge Proofs of Knowledge',
        'year': 2010
    },
    {
        'github_urls': [
        ],
        'id': 32178623,
        'nbInCitations': 15,
        'nbOutCitations': 27,
        'score': 0.717119517916837,
        'tags': [
        ],
        'title': 'Physical Zero-Knowledge Proofs of Physical Properties',
        'year': 2014
    },
    {
        'github_urls': [
        ],
        'id': 7623635,
        'nbInCitations': 86,
        'nbOutCitations': 33,
        'score': 0.7330599410368158,
        'tags': [
        ],
        'title': 'Zero-knowledge from secure multiparty computation',
        'year': 2007
    },
    {
        'github_urls': [
        ],
        'id': 958428,
        'nbInCitations': 91,
        'nbOutCitations': 12,
        'score': 0.7332582499772805,
        'tags': [
        ],
        'title': 'Zero-knowledge sets',
        'year': 2003
    },
    {
        'github_urls': [
        ],
        'id': 44311103,
        'nbInCitations': 43,
        'nbOutCitations': 0,
        'score': 0.7333798757358013,
        'tags': [
        ],
        'title': 'Publicly Verifiable Non-Interactive Zero-Knowledge Proofs',
        'year': 1990
    },
    {
        'github_urls': [
        ],
        'id': 5302066,
        'nbInCitations': 52,
        'nbOutCitations': 42,
        'score': 0.7371956671513407,
        'tags': [
        ],
        'title': 'Zero-knowledge using garbled circuits: how to prove non-algebraic statements efficiently',
        'year': 2013
    },
    {
        'github_urls': [
        ],
        'id': 117395193,
        'nbInCitations': 0,
        'nbOutCitations': 2,
        'score': 0.7505533993163509,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs and Protocols',
        'year': 2005
    },
    {
        'github_urls': [
        ],
        'id': 125986924,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.750943012903068,
        'tags': [
        ],
        'title': 'Zero-knowledge proofs for secure computation',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 26668341,
        'nbInCitations': 9,
        'nbOutCitations': 0,
        'score': 0.7566897509875092,
        'tags': [
        ],
        'title': 'Zero-knowledge sets with short proofs',
        'year': 2008
    },
    {
        'github_urls': [
        ],
        'id': 6786255,
        'nbInCitations': 16,
        'nbOutCitations': 20,
        'score': 0.7836043044969705,
        'tags': [
        ],
        'title': 'Zero-Knowledge Sets With Short Proofs',
        'year': 2011
    },
    {
        'github_urls': [
        ],
        'id': 126287569,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.7892913789366733,
        'tags': [
        ],
        'title': 'Zero-knowledge proof system and method',
        'year': 2002
    },
    {
        'github_urls': [
        ],
        'id': 16831210,
        'nbInCitations': 17,
        'nbOutCitations': 15,
        'score': 0.7951369801514067,
        'tags': [
        ],
        'title': 'Zero-knowledge proofs of retrievability',
        'year': 2011
    },
    {
        'github_urls': [
        ],
        'id': 125018029,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8010421611906569,
        'tags': [
        ],
        'title': 'Chapter 12 Proof systems and zero knowledge',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 9636229,
        'nbInCitations': 34,
        'nbOutCitations': 40,
        'score': 0.8064119838691122,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs from Secure Multiparty Computation',
        'year': 2009
    },
    {
        'github_urls': [
        ],
        'id': 203669302,
        'nbInCitations': 27,
        'nbOutCitations': 0,
        'score': 0.8083633315059124,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs of Knowledge Without Interaction (Extended Abstract)',
        'year': 1992
    },
    {
        'github_urls': [
        ],
        'id': 115209432,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8443772093989037,
        'tags': [
        ],
        'title': 'Zero-knowledge proofs',
        'year': 1987
    },
    {
        'github_urls': [
        ],
        'id': 199082236,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8443772093989037,
        'tags': [
        ],
        'title': 'Zero-knowledge proofs',
        'year': 1993
    },
    {
        'github_urls': [
        ],
        'id': 38600260,
        'nbInCitations': 164,
        'nbOutCitations': 2,
        'score': 0.8712658132935791,
        'tags': [
        ],
        'title': 'Zero knowledge proofs of knowledge in two rounds',
        'year': 1989
    },
    {
        'github_urls': [
        ],
        'id': 40746624,
        'nbInCitations': 15,
        'nbOutCitations': 0,
        'score': 0.878365915607169,
        'tags': [
        ],
        'title': 'Zero knowledge proofs of identity',
        'year': 1987
    },
    {
        'github_urls': [
        ],
        'id': 117536261,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8798662556324494,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 124498444,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8798662556324494,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 19799340,
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'score': 0.8808289127811741,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs in Theory and Practice',
        'year': 2014
    },
    {
        'github_urls': [
        ],
        'id': 70304423,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.886065207373209,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proofs',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 62199478,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.8898300372169159,
        'tags': [
        ],
        'title': 'Zero knowledge proofs',
        'year': 1988
    },
    {
        'github_urls': [
        ],
        'id': 9078920,
        'nbInCitations': 0,
        'nbOutCitations': 2,
        'score': 0.9028242039241051,
        'tags': [
        ],
        'title': 'Zero Knowledge Proofs',
        'year': 2007
    },
    {
        'github_urls': [
        ],
        'id': 125329190,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.9204887447036324,
        'tags': [
        ],
        'title': 'Zero Knowledge Proofs',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 18186246,
        'nbInCitations': 4,
        'nbOutCitations': 5,
        'score': 0.9233965524219915,
        'tags': [
        ],
        'title': 'Proofs of Zero Knowledge',
        'year': 2004
    },
    {
        'github_urls': [
        ],
        'id': 2950602,
        'nbInCitations': 541,
        'nbOutCitations': 12,
        'score': 0.924001472550978,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'Zero-knowledge proofs of identity',
        'year': 2006
    },
    {
        'github_urls': [
        ],
        'id': 208886660,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.938778413510735,
        'tags': [
        ],
        'title': 'Zero-knowledge-proof',
        'year': 2011
    },
    {
        'github_urls': [
        ],
        'id': 86562484,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.9524016374607767,
        'tags': [
        ],
        'title': 'Zero-Knowledge Proof',
        'year': 2010
    }
]

snapshots['QueryTests::test_multiple_queries 4'] = [
    {
        'authors': [
            [
                30238620,
                'Y. Lindell'
            ]
        ],
        'github_urls': [
        ],
        'id': 15835932,
        'journalName': 'IACR Cryptology ePrint Archive',
        'language': 'un',
        'magId': 97043427,
        'n_author': [
            0
        ],
        'nbInCitations': 2,
        'nbOutCitations': 12,
        'paperAbstract': 'In this note, we show the existence of constant-round computational zero-knowledge proofs of knowledge for all N P. The existence of constant-round zero-knowledge proofs was proven by Goldreich and Kahan (Journal of Cryptology, 1996), and the existence of constant-round zeroknowledge arguments of knowledge was proven by Feige and Shamir (CRYPTO 1989). Although it is widely believed that there exist constant-round zero-knowledge proofs of knowledge for all N P, to the best of our knowledge, no proof of this fact has been published.',
        'pdfUrls': [
            'https://eccc.weizmann.ac.il/report/2011/003'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:15835932',
        'title': 'Constant-Round Zero-Knowledge Proofs of Knowledge',
        'tldr': '',
        'venue': 'IACR Cryptology ePrint Archive',
        'year': 2010
    },
    {
        'authors': [
            [
                1023361224,
                'M. Naor'
            ],
            [
                2148140415,
                'D. Freund'
            ],
            [
                2396724737,
                'B. Fisch'
            ]
        ],
        'github_urls': [
        ],
        'id': 32178623,
        'journalName': '',
        'language': 'un',
        'magId': 99938045,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 15,
        'nbOutCitations': 27,
        'paperAbstract': 'Is it possible to prove that two DNA-fingerprints match, or that they do not match, without revealing any further information about the fingerprints? Is it possible to prove that two objects have the same design without revealing the design itself? In the digital domain, zero-knowledge is an established concept where a prover convinces a verifier of a statement without revealing any information beyond the statement’s validity. However, zero-knowledge is not as well-developed in the context of problems that are inherently physical. In this paper, we are interested in protocols that prove physical properties of physical objects without revealing further information. The literature lacks a unified formal framework for designing and analyzing such protocols. We suggest the first paradigm for formally defining, modeling, and analyzing physical zero-knowledge (PhysicalZK) protocols, using the Universal Composability framework. We also demonstrate applications of physical zero-knowledge to DNA profiling and neutron radiography. Finally, we explore public observation proofs, an analog of public-coin proofs in the context of PhysicalZK.',
        'pdfUrls': [
            'http://dblp.uni-trier.de/db/conf/crypto/crypto2014-2.html#FischFN14'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:32178623',
        'title': 'Physical Zero-Knowledge Proofs of Physical Properties',
        'tldr': 'In the digital domain, zero-knowledge is an established concept where a prover convinces a verifier of a statement without revealing any information beyond the statement’s validity. In this paper, we are interested in protocols that prove physical properties of physical objects without revealing further information. We suggest the first paradigm for formally defining, modeling, and analyzing physical zero-knowledge protocols, using the Universal Composability framework.',
        'venue': 'CRYPTO',
        'year': 2014
    },
    {
        'authors': [
            [
                114908009,
                'Y. Ishai'
            ],
            [
                307687659,
                'E. Kushilevitz'
            ],
            [
                1482108584,
                'R. Ostrovsky'
            ],
            [
                2159933393,
                'A. Sahai'
            ]
        ],
        'github_urls': [
        ],
        'id': 7623635,
        'journalName': '',
        'language': 'un',
        'magId': 1980227445,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 86,
        'nbOutCitations': 33,
        'paperAbstract': 'We present a general construction of a zero-knowledge proof for an NP relation R(x,w) which only makes a black-box use of a secure protocol for a related multi-partyfunctionality f. The latter protocol is only required to be secure against a small number of "honest but curious" players. As an application, we can translate previous results on the efficiency of secure multiparty computation to the domain of zero-knowledge, improving over previous constructions of efficient zero-knowledge proofs. In particular, if verifying R on a witness of length m can be done by a circuit C of size s, and assuming one-way functions exist, we get the following types of zero-knowledge proof protocols. Approaching the witness length. If C has constant depth over ∧,∨,⊕, - gates of unbounded fan-in, we get a zero-knowledge protocol with communication complexity m·poly(k)·polylog(s), where k is a security parameter. Such a protocol can be implemented in either the standard interactive model or, following a trusted setup, in a non-interactive model. "Constant-rate" zero-knowledge. For an arbitrary circuit C of size s and a bounded fan-in, we geta zero-knowledge protocol with communication complexity O(s)+poly(k). Thus, for large circuits, the ratio between the communication complexity and the circuit size approaches a constant. This improves over the O(ks) complexity of the best previous protocols.',
        'pdfUrls': [
            'http://portal.acm.org/citation.cfm?doid=1250790.1250794'
        ],
        'question': 'How can we construct a zero-knowledge proof for an NP relation R(x',
        's2Url': 'https://api.semanticscholar.org/CorpusID:7623635',
        'title': 'Zero-knowledge from secure multiparty computation',
        'tldr': 'We present a general construction of a zero-knowledge proof for an NP relation R(x,w) which only makes a black-box use of a secure protocol for a related multi-partyfunctionality f. As an application, we can translate previous results on the efficiency of secure multiparty computation to the domain of zero-knowledge.',
        'venue': "STOC '07",
        'year': 2007
    },
    {
        'authors': [
            [
                699581604,
                'S. Micali'
            ],
            [
                2144633556,
                'M. O. Rabin'
            ],
            [
                2974725642,
                'J. Kilian'
            ]
        ],
        'github_urls': [
        ],
        'id': 958428,
        'journalName': '44th Annual IEEE Symposium on Foundations of Computer Science, 2003. Proceedings.',
        'language': 'un',
        'magId': 2166618966,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 91,
        'nbOutCitations': 12,
        'paperAbstract': 'We show how a polynomial-time prover can commit to an arbitrary finite set S of strings so that, later on, he can, for any string x, reveal with a proof whether x /spl isin/ S or x /spl notin/ S, without revealing any knowledge beyond the verity of these membership assertions. Our method is non interactive. Given a public random string, the prover commits to a set by simply posting a short and easily computable message. After that, each time it wants to prove whether a given element is in the set, it simply posts another short and easily computable proof, whose correctness can be verified by any one against the public random string. Our scheme is very efficient; no reasonable prior way to achieve our desiderata existed. Our new primitive immediately extends to providing zero-knowledge databases.',
        'pdfUrls': [
            'http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=1238183'
        ],
        'question': 'How can a-time prover commit to an arbitrary finite set S of strings',
        's2Url': 'https://api.semanticscholar.org/CorpusID:958428',
        'title': 'Zero-knowledge sets',
        'tldr': 'We show how a-time prover can commit to an arbitrary finite set S of strings so that, later on, he can, for any string x, reveal with a proof whether x /spl isin/ S or x /spl notin/ S, without revealing any knowledge beyond the verity of these membership assertions. Our new primitive immediately extends to providing zero-knowledge databases.',
        'venue': '44th Annual IEEE Symposium on Foundations of Computer Science, 2003. Proceedings.',
        'year': 2003
    },
    {
        'authors': [
            [
                2026354139,
                'D. Lapidot'
            ],
            [
                2201755339,
                'A. Shamir'
            ]
        ],
        'github_urls': [
        ],
        'id': 44311103,
        'journalName': '',
        'language': 'un',
        'magId': 1538332662,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 43,
        'nbOutCitations': 0,
        'paperAbstract': 'In this paper we construct the first publicly verifiable non-interactive zero-knowledge proof for any NP statement under the general assumption that one way permutations exist. If the prover is polynomially bounded then our scheme is based on the stronger assumption that trapdoor permutations exist. In both cases we assume that P and V have a common random string, and use it to prove a single theorem (which may be chosen as a function of the known string).',
        'pdfUrls': [
            'https://doi.org/10.1007/3-540-38424-3_26'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:44311103',
        'title': 'Publicly Verifiable Non-Interactive Zero-Knowledge Proofs',
        'tldr': 'We construct the first publicly non-interactive zero-knowledge proof for any NP statement.',
        'venue': 'CRYPTO',
        'year': 1990
    },
    {
        'authors': [
            [
                276520774,
                'M. Jawurek'
            ],
            [
                1941687626,
                'F. Kerschbaum'
            ],
            [
                2080023441,
                'C. Orlandi'
            ]
        ],
        'github_urls': [
        ],
        'id': 5302066,
        'journalName': '',
        'language': 'un',
        'magId': 2058648304,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 52,
        'nbOutCitations': 42,
        'paperAbstract': 'Zero-knowledge protocols are one of the fundamental concepts in modern cryptography and have countless applications. However, after more than 30 years from their introduction, there are only very few languages (essentially those with a group structure) for which we can construct zero-knowledge protocols that are efficient enough to be used in practice. In this paper we address the problem of how to construct efficient zero-knowledge protocols for generic languages and we propose a protocol based on Yao\'s garbled circuit technique. The motivation for our work is that in many cryptographic applications it is useful to be able to prove efficiently statements of the form e.g., "I know x s.t.y = SHA-256(x)" for a common input y (or other "unstructured" languages), but no efficient protocols for this task are currently known. It is clear that zero-knowledge is a subset of secure two-party computation (i.e., any protocol for generic secure computation can be used to do zero-knowledge). The main contribution of this paper is to construct an efficient protocol for the special case of secure two-party computation where only one party has input (like in the zero-knowledge case). The protocol achieves active security and is essentially only twice as slow as the passive secure version of Yao\'s garbled circuit protocol. This is a great improvement with respect to the cut-n-choose technique to make Yao\'s protocol actively secure, where the complexity grows linearly with the security parameter.',
        'pdfUrls': [
            'https://doi.acm.org/10.1145/2508859.2516662'
        ],
        'question': "How does Yao's garbled circuit technique affect security?",
        's2Url': 'https://api.semanticscholar.org/CorpusID:5302066',
        'title': 'Zero-knowledge using garbled circuits: how to prove non-algebraic statements efficiently',
        'tldr': "We propose a protocol based on Yao's garbled circuit technique. The protocol achieves active security and is essentially only twice as slow as Yao's garbled circuit protocol.",
        'venue': "CCS '13",
        'year': 2013
    },
    {
        'authors': [
            [
                2636097520,
                'N. Vyahhi'
            ]
        ],
        'github_urls': [
        ],
        'id': 117395193,
        'journalName': '',
        'language': 'un',
        'magId': 180646542,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 2,
        'paperAbstract': 'A proof is whatever convinces me. Shimon Even, 1978. Zero-knowledge proof is usual proof, but you must not give more information to verifier, than your statement (which you prove) can give alone. So, in this paper, some facts about zero-knowledge, interactive protocols and proofs will be given. Also, with examples.',
        'pdfUrls': [
            'http://www14.in.tum.de/konferenzen/Jass05/courses/1/papers/vyahhi_paper.pdf'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:117395193',
        'title': 'Zero-Knowledge Proofs and Protocols',
        'tldr': '',
        'venue': None,
        'year': 2005
    },
    {
        'authors': [
            [
                2197828808,
                'G. Couteau'
            ]
        ],
        'github_urls': [
        ],
        'id': 125986924,
        'journalName': '',
        'language': 'un',
        'magId': 2785078146,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'In this thesis, we study zero-knowledge proofs, a cryptographic primitive that allows to prove a statement while yielding nothing beyond its truth, and their applications to secure computation. Specifically, we first introduce a new type of zero-knowledge proofs, called implicit zero-knowledge arguments, that stands between two existing notions, interactive zeroknowledge proofs and non-interactive zero-knowledge proofs. Our new notion provides the same efficiency benefits than the latter when used to design roundefficient secure computation protocols, but it can be built from essentially the same cryptographic assumptions than the former, which allows to get improved efficiency and security guarantees. Second, we revisit a zero-knowledge proof system that is particularly useful for secure computation protocols manipulating integers, and show that the known security analysis can be improved to base the proof system on a more wellstudied assumption. Eventually, we introduce a new method to build zero-knowledge proof systems over the integers, which particularly improves over existing methods in a client-server model, where a weak client executes a secure computation protocol with a powerful server.',
        'pdfUrls': [
            'https://hal.inria.fr/tel-01668125/document'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:125986924',
        'title': 'Zero-knowledge proofs for secure computation',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                2098430168,
                'D. Fiore'
            ],
            [
                2289125662,
                'D. Catalano'
            ],
            [
                2639107319,
                'M. Messina'
            ]
        ],
        'github_urls': [
        ],
        'id': 26668341,
        'journalName': '',
        'language': 'un',
        'magId': 2115501399,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 9,
        'nbOutCitations': 0,
        'paperAbstract': "Zero Knowledge Sets, introduced by Micali, Rabin and Kilian in [17], allow a prover to commit to a secret set S in a way such that it can later prove, non interactively, statements of the form x ∈ S (or x ∉ S), without revealing any further information (on top of what explicitly revealed by the inclusion/exclusion statements above) on S, not even its size. Later, Chase et al. [5] abstracted away the Micali, Rabin and Kilian's construction by introducing an elegant new variant of commitments that they called (trapdoor) mercurial commitments. Using this primitive, it was shown in [5,4] how to construct zero knowledge sets from a variety of assumptions (both general and number theoretic). ::: ::: In this paper we introduce the notion of trapdoor q-mercurial commitments (qTMCs), a notion of mercurial commitment that allows the sender to commit to an ordered sequence of exactly q messages, rather than to a single one. Following [17,5] we show how to construct ZKS from qTMCs and collision resistant hash functions. ::: ::: Then, we present an efficient realization of qTMCs that is secure under the so called Strong Diffie Hellman assumption, a number theoretic conjecture recently introduced by Boneh and Boyen in [3]. Using our scheme as basic building block, we obtain a construction of ZKS that allows for proofs that are much shorter with respect to the best previously known implementations. In particular, for an appropriate choice of the parameters, our proofs are up to 33% shorter for the case of proofs of membership, and up to 73% shorter for the case of proofs of non membership.",
        'pdfUrls': [
            'https://link.springer.com/chapter/10.1007%2F978-3-540-78967-3_25'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:26668341',
        'title': 'Zero-knowledge sets with short proofs',
        'tldr': '',
        'venue': 'EUROCRYPT',
        'year': 2008
    },
    {
        'authors': [
            [
                2098430168,
                'D. Fiore'
            ],
            [
                2274932001,
                'M. Messina'
            ],
            [
                2289125662,
                'D. Catalano'
            ],
            [
                2674807477,
                'M. D. Raimondo'
            ]
        ],
        'github_urls': [
        ],
        'id': 6786255,
        'journalName': 'IEEE Transactions on Information Theory',
        'language': 'un',
        'magId': 2125557460,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 16,
        'nbOutCitations': 20,
        'paperAbstract': "Zero knowledge sets (ZKS), introduced by Micali, Rabin, and Kilian in 2003, allow a prover to commit to a secret set S in a way such that it can later prove, non interactively, statements of the form x ∈ S (or x ∉ S), without revealing any further information (on top of what explicitly revealed by the inclusion/exclusion statements above) on S, not even its size. Later, Chase abstracted away the Micali, Rabin, and Kilian's construction by introducing an elegant new variant of commitments that they called (trapdoor) mercurial commitments. Using this primitive, it was shown how to construct zero knowledge sets from a variety of assumptions (both general and number theoretic). This paper introduces the notion of trapdoor q -mercurial commitments (\\ssr qTMCs), a notion of mercurial commitment that allows the sender to commit to an ordered sequence of exactly q messages, rather than to a single one. Following the previous work, it is shown how to construct ZKS from \\ssr qTMCs and collision resistant hash functions. Then, it is presented an efficient realization of \\ssr qTMCs that is secure under the so called Strong Diffie Hellman (SDH) assumption, a number theoretic conjecture recently introduced by Boneh and Boyen. Using such scheme as basic building block, it is obtained a construction of ZKS that allows for proofs that are much shorter with respect to the best previously known implementations. In particular, for an appropriate choice of the parameters, our proofs are up to 33% shorter for the case of proofs of membership, and up to 73% shorter for the case of proofs of nonmembership. Experimental tests confirm practical time performances.",
        'pdfUrls': [
            'https://link.springer.com/content/pdf/10.1007/978-3-540-78967-3_25.pdf'
        ],
        'question': 'What is the concept of trapdoor q -mercurial commitments?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:6786255',
        'title': 'Zero-Knowledge Sets With Short Proofs',
        'tldr': 'This paper introduces the notion of trapdoor q -mercurial commitments (sssr qTMCs) It allows a prover to commit to a secret set S in a way such as it can later prove, non interactively, statements of the form x  S (or x  S) without revealing any further information.',
        'venue': 'IEEE Transactions on Information Theory',
        'year': 2011
    },
    {
        'authors': [
            [
                2115143635,
                'S. Obana'
            ],
            [
                2151356658,
                'K. Sako'
            ],
            [
                2774641301,
                'J. Furukawa'
            ]
        ],
        'github_urls': [
        ],
        'id': 126287569,
        'journalName': '',
        'language': 'un',
        'magId': 2886482013,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://patents.google.com/patent/DE60220600T2/en'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:126287569',
        'title': 'Zero-knowledge proof system and method',
        'tldr': '',
        'venue': None,
        'year': 2002
    },
    {
        'authors': [
            [
                2102996759,
                'H. Hu'
            ],
            [
                2166892783,
                'Z. Hu'
            ],
            [
                2170586962,
                'H. Wang'
            ],
            [
                2281944180,
                'G. Ahn'
            ],
            [
                2692935519,
                'Y. Zhu'
            ]
        ],
        'github_urls': [
        ],
        'id': 16831210,
        'journalName': 'Science China Information Sciences',
        'language': 'un',
        'magId': 2271004365,
        'n_author': [
            0,
            1,
            2,
            3,
            4
        ],
        'nbInCitations': 17,
        'nbOutCitations': 15,
        'paperAbstract': 'Proof of retrievability (POR) is a technique for ensuring the integrity of data in outsourced storage services. In this paper, we address the construction of POR protocol on the standard model of interactive proof systems. We propose the first interactive POR scheme to prevent the fraudulence of prover and the leakage of verified data. We also give full proofs of soundness and zero-knowledge properties by constructing a polynomialtime rewindable knowledge extractor under the computational Diffie-Hellman assumption. In particular, the verification process of this scheme requires a low, constant amount of overhead, which minimizes communication complexity.',
        'pdfUrls': [
            'https://core.ac.uk/display/155434731'
        ],
        'question': 'How to prevent fraudulence of prover and the leakage of verified data?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:16831210',
        'title': 'Zero-knowledge proofs of retrievability',
        'tldr': 'We propose the first interactive POR scheme to prevent fraudulence of prover and the leakage of verified data. We also give full of soundness proofs and zero-knowledge properties by constructing a zero-time rewindable knowledge extractor.',
        'venue': 'Science China Information Sciences',
        'year': 2011
    },
    {
        'authors': [
            [
                672764664,
                'J. v. z. Gathen'
            ]
        ],
        'github_urls': [
        ],
        'id': 125018029,
        'journalName': 'CryptoSchool',
        'language': 'un',
        'magId': 2399748547,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'In an interactive proof system, a prover called Paula knows some fact and tries to convince a verifier Victor of its truth. This might be some property of a secret key, say, that its least bit is 0.',
        'pdfUrls': [
            'https://rd.springer.com/chapter/10.1007/978-3-662-48425-8_19'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:125018029',
        'title': 'Chapter 12 Proof systems and zero knowledge',
        'tldr': '',
        'venue': 'CryptoSchool',
        'year': 2015
    },
    {
        'authors': [
            [
                114908009,
                'Y. Ishai'
            ],
            [
                307687659,
                'E. Kushilevitz'
            ],
            [
                1482108584,
                'R. Ostrovsky'
            ],
            [
                2159933393,
                'A. Sahai'
            ]
        ],
        'github_urls': [
        ],
        'id': 9636229,
        'journalName': 'SIAM J. Comput.',
        'language': 'un',
        'magId': 2069535412,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 34,
        'nbOutCitations': 40,
        'paperAbstract': 'A zero-knowledge proof allows a prover to convince a verifier of an assertion without revealing any further information beyond the fact that the assertion is true. Secure multiparty computation allows $n$ mutually suspicious players to jointly compute a function of their local inputs without revealing to any $t$ corrupted players additional information beyond the output of the function. We present a new general connection between these two fundamental notions. Specifically, we present a general construction of a zero-knowledge proof for an NP relation $R(x,w)$, which makes only a black-box use of any secure protocol for a related multiparty functionality $f$. The latter protocol is required only to be secure against a small number of “honest but curious” players. We also present a variant of the basic construction that can leverage security against a large number of malicious players to obtain better efficiency. As an application, one can translate previous results on the efficiency of secure multiparty computation to the domain of zero-knowledge, improving over previous constructions of efficient zero-knowledge proofs. In particular, if verifying $R$ on a witness of length $m$ can be done by a circuit $C$ of size $s$, and assuming that one-way functions exist, we get the following types of zero-knowledge proof protocols: (1) Approaching the witness length. If $C$ has constant depth over $\\wedge,\\vee,\\oplus,\\neg$ gates of unbounded fan-in, we get a zero-knowledge proof protocol with communication complexity $m\\cdot{poly}(k)\\cdot{polylog}(s)$, where $k$ is a security parameter. (2) “Constant-rate” zero-knowledge. For an arbitrary circuit $C$ of size $s$ and a bounded fan-in, we get a zero-knowledge protocol with communication complexity $O(s)+{poly}(k,\\log s)$. Thus, for large circuits, the ratio between the communication complexity and the circuit size approaches a constant. This improves over the $O(ks)$ complexity of the best previous protocols.',
        'pdfUrls': [
            'http://dblp.uni-trier.de/db/journals/siamcomp/siamcomp39.html#IshaiKOS09'
        ],
        'question': 'How can a zero-knowledge proof be used to prove an assertion?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:9636229',
        'title': 'Zero-Knowledge Proofs from Secure Multiparty Computation',
        'tldr': 'A zero-knowledge proof allows a prover to convince a verifier of an assertion without revealing any further information beyond the fact that the assertion is true. Secure multiparty computation allows mutually suspicious players to jointly compute a function of their local inputs.',
        'venue': 'SIAM J. Comput.',
        'year': 2009
    },
    {
        'authors': [
            [
                1931511623,
                'A. D. Santis'
            ],
            [
                2291003365,
                'G. Persiano'
            ]
        ],
        'github_urls': [
        ],
        'id': 203669302,
        'journalName': '',
        'language': 'un',
        'magId': 2096571200,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 27,
        'nbOutCitations': 0,
        'paperAbstract': 'A zero-knowledge proof system of knowledge is a protocol between two parties called the prover and the verifier. The prover wants to convince the verifier that he “knows” the proof of a given theorem without revealing any additional information. This is different from a zero-knowledge proof system of membership where the prover convinces the verifier only of the veridicity of the statement. Zero-knowledge proofs of knowledge are very useful tools in the design of secure protocols. Though, the concept of a proof of knowledge is a very subtle one and great care is needed to obtain a satisfying formalization. In this paper, we investigate the concept of a zero-knowledge proof of knowledge in the noninteractive model of [5, 61. Here, the prover and the verifier share a short random string and the only communication allowed is from the prover to the verifier. Although this is a simpler model than the interactive one, still formalizing zeroknowledge proofs of knowledge is a delicate task. The main results of the paper are the following e We present formal definitions for the concept of non-interactive zero-knowledge proofs',
        'pdfUrls': [
            'https://dblp.uni-trier.de/db/conf/focs/focs92.html#SantisP92'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:203669302',
        'title': 'Zero-Knowledge Proofs of Knowledge Without Interaction (Extended Abstract)',
        'tldr': "A zero-knowledge proof system of knowledge is a protocol between two parties called the prover and the verifier. The prover wants to convince the verifier that he 'knows' the proof of a given theorem without revealing any additional information. We present formal definitions for the concept of non-interactive zero-knowledge proofs of knowledge.",
        'venue': 'FOCS 1992',
        'year': 1992
    },
    {
        'authors': [
            [
                2676273062,
                'P. Wayner'
            ]
        ],
        'github_urls': [
        ],
        'id': 115209432,
        'journalName': '',
        'language': 'un',
        'magId': 97619628,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://dl.acm.org/citation.cfm?id=31350'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:115209432',
        'title': 'Zero-knowledge proofs',
        'tldr': '',
        'venue': None,
        'year': 1987
    },
    {
        'authors': [
            [
                2146149006,
                'C. C. McGeoch'
            ]
        ],
        'github_urls': [
        ],
        'id': 199082236,
        'journalName': 'American Mathematical Monthly',
        'language': 'un',
        'magId': 2078850651,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'On a moonless night the spy returns to the castle after a reconnoitering mission to the enemy camp. As he nears the gate a voice whispers, "What\'s the password?" But is it friend or foe who whispers? How can the spy show that he knows the password without actually revealing it to a possible imposter? The spy\'s dilemma is commonplace now with the widespread use of telecommunications. When your automatic teller machine communicates with your bank, each must be assured that the other is legitimate; the electronic "passwords" must be unforgeable and must be of no use to imposters and eavesdroppers. One method that has been proposed for exchanging passwords in this context is the zero-knowledge proof. Renaissance mathematicians developed their own primitive zero-knowledge proof systems. When both Tartaglia and Fior claimed knowledge of an algebraic solution to cubic equations, a contest was arranged in which each proposed thirty problems for the other to solve. In the end, Tartaglia had solved all thirty, thus providing a convincing demonstration that he knew the method without actually revealing it. Fior solved none. (It turned out that each had worked out solutions to certain classes of cubics, but neither had solved the general problem [2]). We\'ve progressed considerably in formalizing this idea. An interactive protocol comprises two algorithms P (the prover) and V (the verifier) that read a common input string w of length Iwl and then compute and communicate in alternating turns to determine whether w has some specified property. The verifier is polynomially-bounded: it must eventually halt and its total computation time must be bounded by a fixed polynomial in Iw 1. When it halts, the verifier outputs either accept or reject depending upon whether the property holds for w. The verifier is probabilistic, that is, allowed to make random choices during the computation according to the results of coin tosses. The prover is allowed to have unlimited computational power. A language is a set of strings. An interactive proof system for Z is an interactive protocol in which P helps V to decide whether w E -Z. We require that with high probability the verifier be correct when accepting or rejecting the membership of w in -Z. More precisely, for every constant c > 0, for sufficiently large w E -Z the probability (over all coin tosses) that V halts and accepts must be at least 1 Iwl c. If w e -Z then we require that no prover P* be able to convince V otherwise: that is, for every c > 0 and large enough w, and for any interactive protocol (P*, V), V rejects with probability at least 1 Iw Ic.',
        'pdfUrls': [
            'https://www.jstor.org/stable/2323894'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:199082236',
        'title': 'Zero-knowledge proofs',
        'tldr': '',
        'venue': None,
        'year': 1993
    },
    {
        'authors': [
            [
                672946669,
                'U. Feige'
            ],
            [
                2201755339,
                'A. Shamir'
            ]
        ],
        'github_urls': [
        ],
        'id': 38600260,
        'journalName': '',
        'language': 'un',
        'magId': 1502416796,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 164,
        'nbOutCitations': 2,
        'paperAbstract': 'We construct constant round ZKIPs for any NP language, under the sole assumption that oneway functions exist. Under the stronger Certified Discrete Log assumption, our construction yields perfect zero knowledge protocols. Our protocols rely on two novel ideas: One for constructing commitment schemes, the other for constructing subprotocols which are not known to be zero knowledge, yet can be proven not to reveal useful information.',
        'pdfUrls': [
            'https://rd.springer.com/chapter/10.1007/0-387-34805-0_46'
        ],
        'question': 'How do constant round ZKIPs work?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:38600260',
        'title': 'Zero knowledge proofs of knowledge in two rounds',
        'tldr': 'We construct constant round ZKIPs for any NP language. Under the stronger Certified Discrete Log assumption, our construction yields perfect zero knowledge protocols.',
        'venue': 'CRYPTO',
        'year': 1989
    },
    {
        'authors': [
            [
                381246873,
                'U. Fiege'
            ],
            [
                1577021311,
                'A. Fiat'
            ],
            [
                2201755339,
                'A. Shamir'
            ]
        ],
        'github_urls': [
        ],
        'id': 40746624,
        'journalName': '',
        'language': 'un',
        'magId': 2152005134,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 15,
        'nbOutCitations': 0,
        'paperAbstract': 'In this paper we extend the notion of zero knowledge proofs of membership (which reveal one bit of information) to zero knowledge proofs of knowledge (which reveal no information whatsoever). After formally defining this notion, we show its relevance to identification schemes, in which parties prove their identity by demonstrating their knowledge rather than by proving the validity of assertions. We describe a novel scheme which is provably secure if factoring is difficult and whose practical implementations are about two orders of magnitude faster than RSA-based identification schemes. In the last part of the paper we consider the question of sequential versus parallel executions of zero knowledge protocols, define a new notion of “transferable information”, and prove that the parallel version of our identification scheme (which is not known to be zero knowledge) is secure since it reveals no transferable information.',
        'pdfUrls': [
            'https://www.researchgate.net/profile/Amos_Fiat/publication/225604161_Zero-knowledge_proofs_of_identity/links/55055e230cf24cee3a044eb0.pdf'
        ],
        'question': 'How do zero knowledge proofs of membership affect identification schemes?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:40746624',
        'title': 'Zero knowledge proofs of identity',
        'tldr': 'We extend the notion of zero knowledge proofs of membership to zero knowledge proofs of knowledge. We show its relevance to identification schemes, in which parties prove their identity by demonstrating their knowledge rather than proving the validity of assertions.',
        'venue': 'STOC',
        'year': 1987
    },
    {
        'authors': [
            [
                2128686230,
                'A. Dominguez'
            ],
            [
                2160587142,
                'A. Fry'
            ]
        ],
        'github_urls': [
        ],
        'id': 117536261,
        'journalName': '',
        'language': 'un',
        'magId': 222334672,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://digitalcommons.wou.edu/aes_event/2015/all/254/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:117536261',
        'title': 'Zero-Knowledge Proofs',
        'tldr': '',
        'venue': None,
        'year': 2015
    },
    {
        'authors': [
            [
                2110748698,
                'N. P. Smart'
            ]
        ],
        'github_urls': [
        ],
        'id': 124498444,
        'journalName': 'Information Security and Cryptography',
        'language': 'un',
        'magId': 2461064430,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Suppose Alice has a password and wants to log in to a website run by Bob, but she does not quite trust the computer Bob is using to verify the password. If she just sends the password to Bob then Bob’s computer will learn the whole password. To get around this problem one often sees websites that ask for the first, fourth and tenth letter of a password one time, and then maybe the first, second and fifth the second time and so on. In this way Bob’s computer only learns three letters at a time. So the password can be checked but in each iteration of checking only three letters are leaked. It clearly would be better if Bob could verify that Alice has the password in such a way that Alice never has to reveal any of the password to Bob. This is the problem this chapter will try to solve.',
        'pdfUrls': [
            'https://rd.springer.com/chapter/10.1007/978-3-319-21936-3_21'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:124498444',
        'title': 'Zero-Knowledge Proofs',
        'tldr': '',
        'venue': 'Information Security and Cryptography',
        'year': 2015
    },
    {
        'authors': [
            [
                2791124870,
                'D. Bernhard'
            ]
        ],
        'github_urls': [
        ],
        'id': 19799340,
        'journalName': '',
        'language': 'un',
        'magId': 2611920647,
        'n_author': [
            0
        ],
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'paperAbstract': 'Zero-knowledge proof schemes are one of the main building blocks of modern cryptography. Using the Helios voting protocol as a practical example, we show mistakes in the previous understanding of these proof schemes and the resulting security problems. We proceed to deVne a hierarchy of security notions that solidiVes our understanding of proof schemes: weak proof schemes, strong proof schemes and multi-proofs. We argue that the problems in Helios result from its use of weak proofs and show how these proofs can be made strong. We provide the Vrst proof of ballot privacy for full Helios ballots with strong proofs. In Helios, a proof scheme commonly known as Fiat-Shamir-Schnorr is used to strengthen encryption, a construction also known as Signed ElGamal or more generally, Encrypt+PoK. We show that in the Encrypt+PoK construction, our hierarchy of proof scheme notions corresponds naturally to a well-known hierarchy of security notions for public-key encryption: weak proofs yield chosen-plaintext secure encryption, strong proofs yield non-malleable encryption and multi-proofs yield chosen-ciphertext secure encryption. Next, we ask whether Signed ElGamal is chosen-ciphertext secure, a question closely related but not identical to whether Fiat-Shamir-Schnorr proofs are multi-proofs. We answer both these questions negatively: under a reasonable assumption, the failure of which would cast doubt on the security of Schnorr-like proofs, we prove that Signed ElGamal cannot be shown to be chosenciphertext secure by a reduction to the security of plain ElGamal. This answers an open question, to our knowledge Vrst asked by Shoup and Gennaro in a paper published in 1998.',
        'pdfUrls': [
            'None'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:19799340',
        'title': 'Zero-Knowledge Proofs in Theory and Practice',
        'tldr': '',
        'venue': None,
        'year': 2014
    },
    {
        'authors': [
            [
                2894457295,
                'S. Rubinstein-Salzedo'
            ]
        ],
        'github_urls': [
        ],
        'id': 70304423,
        'journalName': 'Cryptography',
        'language': 'un',
        'magId': 2894524312,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Generally, in mathematics, the goal of a proof is for the writer to convey knowledge and understanding to the reader. (However, you may doubt this claim based on some books or papers you have read or talks you have attended, although surely not any of mine.) But from time to time, the prover wants to obfuscate some key pieces of information. As we shall see, being able to obfuscate some key pieces of information in the proof has important cryptographic implications.',
        'pdfUrls': [
            'https://link.springer.com/chapter/10.1007/978-3-319-94818-8_16'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:70304423',
        'title': 'Zero-Knowledge Proofs',
        'tldr': '',
        'venue': 'Cryptography',
        'year': 2018
    },
    {
        'authors': [
            [
                2236373878,
                'S. M. Collin'
            ]
        ],
        'github_urls': [
        ],
        'id': 62199478,
        'journalName': 'Computer Fraud & Security Bulletin',
        'language': 'un',
        'magId': 2086297655,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.sciencedirect.com/science/article/pii/0142049688900215'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:62199478',
        'title': 'Zero knowledge proofs',
        'tldr': '',
        'venue': None,
        'year': 1988
    },
    {
        'authors': [
            [
                2811250751,
                'M. Zitnik'
            ]
        ],
        'github_urls': [
        ],
        'id': 9078920,
        'journalName': '',
        'language': 'un',
        'magId': 2013612921,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 2,
        'paperAbstract': '',
        'pdfUrls': [
            'https://doi.acm.org/10.1145/2517258'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:9078920',
        'title': 'Zero Knowledge Proofs',
        'tldr': '',
        'venue': None,
        'year': 2007
    },
    {
        'authors': [
            [
                2226073292,
                'K. Balasubramanian'
            ],
            [
                2747382606,
                'K. Mala'
            ]
        ],
        'github_urls': [
        ],
        'id': 125329190,
        'journalName': 'Advances in Information Security, Privacy, and Ethics',
        'language': 'un',
        'magId': 2745570206,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.igi-global.com/chapter/zero-knowledge-proofs/188517'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:125329190',
        'title': 'Zero Knowledge Proofs',
        'tldr': '',
        'venue': 'Advances in Information Security, Privacy, and Ethics',
        'year': 2018
    },
    {
        'authors': [
            [
                2554227864,
                'M. Bauer'
            ]
        ],
        'github_urls': [
        ],
        'id': 18186246,
        'journalName': 'ArXiv',
        'language': 'un',
        'magId': 1615912323,
        'n_author': [
            0
        ],
        'nbInCitations': 4,
        'nbOutCitations': 5,
        'paperAbstract': "We present a protocol for verification of ``no such entry'' replies from databases. We introduce a new cryptographic primitive as the underlying structure, the keyed hash tree, which is an extension of Merkle's hash tree. We compare our scheme to Buldas et al.'s Undeniable Attesters and Micali et al.'s Zero Knowledge Sets.",
        'pdfUrls': [
            'https://arxiv.org/abs/cs/0406058'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:18186246',
        'title': 'Proofs of Zero Knowledge',
        'tldr': '',
        'venue': 'ArXiv',
        'year': 2004
    },
    {
        'authors': [
            [
                672946669,
                'U. Feige'
            ],
            [
                1577021311,
                'A. Fiat'
            ],
            [
                2201755339,
                'A. Shamir'
            ]
        ],
        'github_urls': [
        ],
        'id': 2950602,
        'journalName': 'Journal of Cryptology',
        'language': 'un',
        'magId': 1979215153,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 541,
        'nbOutCitations': 12,
        'paperAbstract': 'In this paper we extend the notion of interactive proofs of assertions to interactive proofs of knowledge. This leads to the definition of unrestricted input zero-knowledge proofs of knowledge in which the prover demonstrates possession of knowledge without revealing any computational information whatsoever (not even the one bit revealed in zero-knowledge proofs of assertions). We show the relevance of these notions to identification schemes, in which parties prove their identity by demonstrating their knowledge rather than by proving the validity of assertions. We describe a novel scheme which is provably secure if factoring is difficult and whose practical implementations are about two orders of magnitude faster than RSA-based identification schemes. The advantages of thinking in terms of proofs of knowledge rather than proofs of assertions are demonstrated in two efficient variants of the scheme: unrestricted input zero-knowledge proofs of knowledge are used in the construction of a scheme which needs no directory; a version of the scheme based on parallel interactive proofs (which are not known to be zero knowledge) is proved secure by observing that the identification protocols are proofs of knowledge.',
        'pdfUrls': [
            'https://doi.org/10.1007/BF02351717'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:2950602',
        'title': 'Zero-knowledge proofs of identity',
        'tldr': 'We extend the notion of interactive proofs of assertions to interactive proofs of knowledge. We show the relevance of these notions to ID schemes, in which parties prove their identity by demonstrating knowledge rather than proving the validity of assertions.',
        'venue': 'Journal of Cryptology',
        'year': 2006
    },
    {
        'authors': [
            [
                208995799,
                'N. K. Juarah'
            ],
            [
                345701226,
                'R. H. Makarin'
            ],
            [
                2132775091,
                'N. D. M. Yusoff'
            ],
            [
                2138750902,
                'I. F. T. Alshaikhli'
            ],
            [
                2168552182,
                'S. K. M. Bakri'
            ]
        ],
        'github_urls': [
        ],
        'id': 208886660,
        'journalName': '',
        'language': 'un',
        'magId': 32599945,
        'n_author': [
            0,
            1,
            2,
            3,
            4
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://irep.iium.edu.my/20657/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:208886660',
        'title': 'Zero-knowledge-proof',
        'tldr': '',
        'venue': None,
        'year': 2011
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 86562484,
        'journalName': '',
        'language': 'un',
        'magId': 2912417131,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'None'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:86562484',
        'title': 'Zero-Knowledge Proof',
        'tldr': '',
        'venue': None,
        'year': 2010
    }
]

snapshots['QueryTests::test_multiple_queries 5'] = [
    {
        'github_urls': [
        ],
        'id': 43704120,
        'nbInCitations': 2,
        'nbOutCitations': 0,
        'score': 0.10489183525651227,
        'tags': [
        ],
        'title': "AIS' current role in anesthesiology risk management remains uncertain.",
        'year': 2005
    },
    {
        'github_urls': [
        ],
        'id': 110700180,
        'nbInCitations': 4,
        'nbOutCitations': 0,
        'score': 0.1062701425436835,
        'tags': [
        ],
        'title': 'Automated Information System (AIS) Alarm System',
        'year': 1997
    },
    {
        'github_urls': [
        ],
        'id': 44224686,
        'nbInCitations': 0,
        'nbOutCitations': 4,
        'score': 0.1142086430465604,
        'tags': [
        ],
        'title': 'Aircraft Automatic Control System Failure and Flight Safety',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 43899643,
        'nbInCitations': 4,
        'nbOutCitations': 0,
        'score': 0.11512582973641156,
        'tags': [
        ],
        'title': 'AI for Public Health: Self-Screening for Eye Diseases',
        'year': 1998
    },
    {
        'github_urls': [
        ],
        'id': 15992566,
        'nbInCitations': 7,
        'nbOutCitations': 8,
        'score': 0.12005644489032387,
        'tags': [
        ],
        'title': 'System safety through automatic high-level code transformations: an experimental evaluation',
        'year': 2001
    },
    {
        'github_urls': [
        ],
        'id': 293309,
        'nbInCitations': 4,
        'nbOutCitations': 2,
        'score': 0.14057591502531588,
        'tags': [
        ],
        'title': 'Vehicle safety regulations and ADAS: tensions between law and technology',
        'year': 2004
    },
    {
        'github_urls': [
        ],
        'id': 55168040,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.1756908747393288,
        'tags': [
        ],
        'title': 'An Intelligent System of Supervision and Safety of Flight Operations',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 64273217,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.17938226966872425,
        'tags': [
        ],
        'title': 'Äì System Acceptance Test Specifications and Testing',
        'year': 2003
    },
    {
        'github_urls': [
        ],
        'id': 213924446,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.19007517618055134,
        'tags': [
        ],
        'title': 'AI Can Now Identify Heart, Death Risks',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 207455148,
        'nbInCitations': 2,
        'nbOutCitations': 18,
        'score': 0.19674948317640958,
        'tags': [
        ],
        'title': 'Safety-Critical Personality Aspects in Human-Machine Teams of Aviation',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 114874053,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.2461329097306665,
        'tags': [
        ],
        'title': 'ADAS Reliability and Safety',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 31527004,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.2893504690180853,
        'tags': [
        ],
        'title': 'AI and matters of clinical and financial life or death.',
        'year': 1997
    },
    {
        'github_urls': [
        ],
        'id': 76919717,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.2893504690180853,
        'tags': [
        ],
        'title': 'AI and matters of clinical and financial life or death.',
        'year': 1997
    },
    {
        'github_urls': [
        ],
        'id': 129248823,
        'nbInCitations': 78,
        'nbOutCitations': 0,
        'score': 0.3101395012193097,
        'tags': [
        ],
        'title': 'Automatic Identification System (AIS) : data reliability and human error implications',
        'year': 2007
    },
    {
        'github_urls': [
        ],
        'id': 209772984,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.6776283305638394,
        'tags': [
        ],
        'title': 'AI and Automotive Safety',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 211096696,
        'nbInCitations': 0,
        'nbOutCitations': 48,
        'score': 0.8796479149353186,
        'tags': [
        ],
        'title': 'AI safety: state of the field through quantitative lens',
        'year': 2020
    }
]

snapshots['QueryTests::test_multiple_queries 6'] = [
    {
        'authors': [
            [
                2423227234,
                'P. E. Lane'
            ]
        ],
        'github_urls': [
        ],
        'id': 43704120,
        'journalName': 'Anesthesia and analgesia',
        'language': 'un',
        'magId': 2017008178,
        'n_author': [
            0
        ],
        'nbInCitations': 2,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://europepmc.org/article/MED/15845724'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:43704120',
        'title': "AIS' current role in anesthesiology risk management remains uncertain.",
        'tldr': '',
        'venue': 'Anesthesia and analgesia',
        'year': 2005
    },
    {
        'authors': [
            [
                2666354701,
                'W. Hunteman'
            ]
        ],
        'github_urls': [
        ],
        'id': 110700180,
        'journalName': '',
        'language': 'un',
        'magId': 2075717348,
        'n_author': [
            0
        ],
        'nbInCitations': 4,
        'nbOutCitations': 0,
        'paperAbstract': 'The Automated Information Alarm System is a joint effort between Los Alamos National Laboratory, Lawrence Livermore National Laboratory, and Sandia National Laboratory to demonstrate and implement, on a small-to-medium sized local area network, an automated system that detects and automatically responds to attacks that use readily available tools and methodologies. The Alarm System will sense or detect, assess, and respond to suspicious activities that may be detrimental to information on the network or to continued operation of the network. The responses will allow stopping, isolating, or ejecting the suspicious activities. The number of sensors, the sensitivity of the sensors, the assessment criteria, and the desired responses may be set by the using organization to meet their local security policies.',
        'pdfUrls': [
            'https://www.osti.gov/servlets/purl/527545'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:110700180',
        'title': 'Automated Information System (AIS) Alarm System',
        'tldr': '',
        'venue': None,
        'year': 1997
    },
    {
        'authors': [
            [
                2322035315,
                'M. Šlihta'
            ],
            [
                2523908982,
                'V. Šestakovs'
            ],
            [
                2955723409,
                'R. Karunanidhi'
            ]
        ],
        'github_urls': [
        ],
        'id': 44224686,
        'journalName': 'Transport and Aerospace Engineering',
        'language': 'un',
        'magId': 2617787650,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 4,
        'paperAbstract': ' This article presents a mathematical model estimating the probability of successful completion of the aircraft’s flight in case of aviation equipment failure in flight. This paper shows the relationship between the aircraft’s automatic control system and flight safety. The calculations of probability are made for the successful completion of the flight on Boeing 737 aircraft when the automatic control system has failed.',
        'pdfUrls': [
            'https://ortus.rtu.lv/science/lv/publications/23768'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:44224686',
        'title': 'Aircraft Automatic Control System Failure and Flight Safety',
        'tldr': '',
        'venue': None,
        'year': 2016
    },
    {
        'authors': [
            [
                2099969909,
                'G. Cheng'
            ],
            [
                2101154754,
                'X. Liu'
            ],
            [
                2461934818,
                'J. Wu'
            ]
        ],
        'github_urls': [
        ],
        'id': 43899643,
        'journalName': 'IEEE Intell. Syst.',
        'language': 'un',
        'magId': 2031058913,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 4,
        'nbOutCitations': 0,
        'paperAbstract': 'A software-based visual-field testing (perimetry) system is described which incorporates several AI components, including machine learning, an intelligent user interface and pattern discovery. This system has been successfully used for self-screening in several different public environments.',
        'pdfUrls': [
            'http://ieeexplore.ieee.org/document/722349/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:43899643',
        'title': 'AI for Public Health: Self-Screening for Eye Diseases',
        'tldr': '',
        'venue': 'IEEE Intell. Syst.',
        'year': 1998
    },
    {
        'authors': [
            [
                1983260295,
                'P. Cheynet'
            ],
            [
                2129920293,
                'R. Velazco'
            ],
            [
                2139525092,
                'M. Violante'
            ],
            [
                2155200845,
                'M. Rebaudengo'
            ],
            [
                3132917514,
                'M. S. Reorda'
            ],
            [
                3162381017,
                'B. Nicolescu'
            ]
        ],
        'github_urls': [
        ],
        'id': 15992566,
        'journalName': 'Proceedings Design, Automation and Test in Europe. Conference and Exhibition 2001',
        'language': 'un',
        'magId': 2118827830,
        'n_author': [
            0,
            1,
            2,
            3,
            4,
            5
        ],
        'nbInCitations': 7,
        'nbOutCitations': 8,
        'paperAbstract': 'This paper deals with a software modification strategy allowing the on-line detection of transient errors. Being based on a set of rules for introducing redundancy in the high-level code, the method can be completely automated, and is particularly suited for low-cost safety-critical microprocessor-based applications. Experimental results from software and hardware fault injection campaigns are presented and discussed, demonstrating the effectiveness of the approach in terms of fault detection capabilities.',
        'pdfUrls': [
            'http://ieeexplore.ieee.org/document/915040/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:15992566',
        'title': 'System safety through automatic high-level code transformations: an experimental evaluation',
        'tldr': '',
        'venue': 'Proceedings Design, Automation and Test in Europe. Conference and Exhibition 2001',
        'year': 2001
    },
    {
        'authors': [
            [
                2660467974,
                'K. v. Wees'
            ]
        ],
        'github_urls': [
        ],
        'id': 293309,
        'journalName': '2004 IEEE International Conference on Systems, Man and Cybernetics (IEEE Cat. No.04CH37583)',
        'language': 'un',
        'magId': 2170582157,
        'n_author': [
            0
        ],
        'nbInCitations': 4,
        'nbOutCitations': 2,
        'paperAbstract': 'The introduction of advanced driver assistance systems (ADAS) in road traffic raises many complex questions. One of them is to what extent current legal frameworks are fit to accommodate the market introduction of ADAS and on which points they need to be amended to adequately facilitate the smooth implementation of ADAS. This paper is focusing on vehicle safety regulation. The ratio behind this type of regulation is that governments want to assure some minimum levels of safety of vehicles and included equipment. However, in areas of innovative, rapidly developing technologies such as ADAS formal regulation is often criticized for being too slow and to inflexible, obstructing technological developments. In this paper the current European regulatory framework is analysed. It is concluded that the speed of technological developments as well as the innovative and specific nature of ADAS technology call for modifications in the legal framework in order to keep a desired balance between governmental safety concerns and unobstructed development of ADAS.',
        'pdfUrls': [
            'http://ieeexplore.ieee.org/document/1400971/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:293309',
        'title': 'Vehicle safety regulations and ADAS: tensions between law and technology',
        'tldr': '',
        'venue': '2004 IEEE International Conference on Systems, Man and Cybernetics (IEEE Cat. No.04CH37583)',
        'year': 2004
    },
    {
        'authors': [
            [
                2436753639,
                'A. Wróblewska'
            ],
            [
                2672871231,
                'W. Krupa'
            ],
            [
                2801010758,
                'A. Linka'
            ]
        ],
        'github_urls': [
        ],
        'id': 55168040,
        'journalName': 'Journal of KONBiN',
        'language': 'un',
        'magId': 2802379870,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': ' The paper presents the functionality and applicability of AeroSafetyShow Demonstrator+PL (ASSD+PL). Software was invented and developed by a scientific consortium between Żelazny6 Wojciech Krupa company and Poznan University of Technology. Project was co-financed by the European Union and the National Centre for Research and Development. ASSD+PL is an intelligent system, which allows to increase the safety of flight operations by conducting surveillance in the real time. This system is the first controlling software which offering such a wide range of functionalities.',
        'pdfUrls': [
            'https://sciendo.com/pdf/10.1515/jok-2017-0041'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:55168040',
        'title': 'An Intelligent System of Supervision and Safety of Flight Operations',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                2485205407,
                'D. Stokes'
            ]
        ],
        'github_urls': [
        ],
        'id': 64273217,
        'journalName': 'Testing Computers Systems for FDA/MHRA Compliance',
        'language': 'un',
        'magId': 2504870077,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'None'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:64273217',
        'title': 'Äì System Acceptance Test Specifications and Testing',
        'tldr': '',
        'venue': 'Testing Computers Systems for FDA/MHRA Compliance',
        'year': 2003
    },
    {
        'authors': [
            [
                2955465065,
                'M. Staff'
            ]
        ],
        'github_urls': [
        ],
        'id': 213924446,
        'journalName': '',
        'language': 'un',
        'magId': 2993280754,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Geisinger study finds AI can examine ECG results to identify patients who are at risk of dying within a year or abnormal heart rhythms.',
        'pdfUrls': [
            'None'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:213924446',
        'title': 'AI Can Now Identify Heart, Death Risks',
        'tldr': '',
        'venue': None,
        'year': 2019
    },
    {
        'authors': [
            [
                2480558704,
                'S. Eschen'
            ],
            [
                2495834040,
                'K. Gayraud'
            ],
            [
                2567704463,
                'D. Keye-Ehing'
            ]
        ],
        'github_urls': [
        ],
        'id': 207455148,
        'journalName': 'i-com',
        'language': 'un',
        'magId': 2565235581,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 2,
        'nbOutCitations': 18,
        'paperAbstract': ': Working safely and successfully in highly automated ::: human-machine interfaces of future aviation is not ::: only a matter of performance, but also of personality. This ::: study examines which personality aspects correlate with ::: safety-critical performance in human-machine teams. ::: The research tools HTQ (Hybrid Team Questionnaire) and ::: HINT (Hybrid Interaction Scenario) were combined for a ::: comprehensive exploratory study. The HTQ includes personality ::: scales measuring broad factors of personality (Big ::: Five) as well as more specific scales and was added with ::: objective personality assessments to measure risk taking. ::: The simulation tool HINT simulates relevant processes in ::: future human-machine team interaction in aviation. In ::: a study with 156 applicants for aviation careers, safety-critical ::: relations of some facets of general personality ::: as well as risk taking were found. Especially personality ::: aspects concerning disinhibiting, spontaneous behaviour ::: and sensation seeking show correlations with poorer performance ::: in the HINT simulation.',
        'pdfUrls': [
            'https://dblp.uni-trier.de/db/journals/icom/icom15.html#EschenKG16'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:207455148',
        'title': 'Safety-Critical Personality Aspects in Human-Machine Teams of Aviation',
        'tldr': '',
        'venue': None,
        'year': 2016
    },
    {
        'authors': [
            [
                2283614549,
                'L. Raffaelli'
            ],
            [
                2608166307,
                'G. Fayolle'
            ],
            [
                2636122548,
                'F. Vallée'
            ]
        ],
        'github_urls': [
        ],
        'id': 114874053,
        'journalName': '',
        'language': 'un',
        'magId': 2603551489,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Summary Safety and reliability validation of Advanced Driver Assistance Systems (ADAS) is not a trivial issue. Build at a low cost level a sufficiently detailed campaign in order to validate safety related and reliability related goals for an ADAS is very difficult, since this kind of systems can encounter an almost infinite number of situations. Now, this kind of systems tends to be more and more integrated in modern cars, what makes of the problem of ADAS validation an important stake. In the event of an accident, the manufacturer can be held legally responsible. In this context, the COVADEC project has started in the mid-2013. The COVADEC project aims to provide methods and techniques for automotive OEMs and suppliers who face these problems, while enhancing the global knowledge of automotive safety standard likes ISO 26262 applicability to design and validation of ADAS sensors, and shed light on its limitations, in order to propose solutions. This document presents a summary of the works realized within this project, with the met hard points and the solutions implemented to solve them.',
        'pdfUrls': [
            'https://hal.inria.fr/hal-01398428'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:114874053',
        'title': 'ADAS Reliability and Safety',
        'tldr': '',
        'venue': None,
        'year': 2016
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 31527004,
        'journalName': 'Health management technology',
        'language': 'un',
        'magId': None,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:31527004',
        'title': 'AI and matters of clinical and financial life or death.',
        'tldr': '',
        'venue': 'Health management technology',
        'year': 1997
    },
    {
        'authors': [
            [
                2541577474,
                'E. Sm'
            ]
        ],
        'github_urls': [
        ],
        'id': 76919717,
        'journalName': 'Health management technology',
        'language': 'un',
        'magId': 2411810926,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.ncbi.nlm.nih.gov/pubmed/10169799'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:76919717',
        'title': 'AI and matters of clinical and financial life or death.',
        'tldr': '',
        'venue': None,
        'year': 1997
    },
    {
        'authors': [
            [
                2116612387,
                'A. Wall'
            ],
            [
                2505844076,
                'J. Wang'
            ],
            [
                2569026020,
                'P. Brooks'
            ],
            [
                2653959638,
                'A. Harati-Mokhtari'
            ]
        ],
        'github_urls': [
        ],
        'id': 129248823,
        'journalName': 'Journal of Navigation',
        'language': 'un',
        'magId': 2075236191,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 78,
        'nbOutCitations': 0,
        'paperAbstract': 'This paper examines the recent introduction of the AIS to the ship\'s bridge and its potential impact on the safety of marine navigation. Research has shown that 80 to 85% of all recorded maritime accidents are directly due to human error or associated with human error. Safety is an important element of marine navigation and many people at different levels are involved in its management. The safe and efficient performance of joint systems, is heavily dependent upon how functions are allocated between the human and the machine. This paper investigates different regulations, supervision for proper use, training, and management of AIS users. It uses previous research and three separate AIS studies to identify problems. The potential of the AIS to cause problems is analysed. The classic human factor "Swiss Cheese" Model of system failure has been modified for the AIS to investigate a possible accident trajectory. The paper then concludes with recommendations and suggestions for improvements and further work.',
        'pdfUrls': [
            'https://trid.trb.org/view/845025'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:129248823',
        'title': 'Automatic Identification System (AIS) : data reliability and human error implications',
        'tldr': 'Research has shown 80 to 85% of all recorded maritime accidents are directly caused by human error. This paper investigates different regulations, supervision for proper use, training, and management of AIS users. The classic human factor "Swiss Cheese" model of system failure has been modified for the AIS to investigate a possible accident trajectory.',
        'venue': None,
        'year': 2007
    },
    {
        'authors': [
            [
                2898412409,
                'C. Wasner'
            ],
            [
                2987357956,
                'J. Traxler'
            ]
        ],
        'github_urls': [
        ],
        'id': 209772984,
        'journalName': 'ATZelectronics worldwide',
        'language': 'un',
        'magId': 2986109967,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://link.springer.com/article/10.1007%2Fs38314-019-0128-z'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:209772984',
        'title': 'AI and Automotive Safety',
        'tldr': '',
        'venue': 'ATZelectronics worldwide',
        'year': 2019
    },
    {
        'authors': [
            [
                2118386840,
                'M. Brčić'
            ],
            [
                3005782231,
                'A. Sandic'
            ],
            [
                3006495053,
                'M. Juric'
            ]
        ],
        'github_urls': [
        ],
        'id': 211096696,
        'journalName': 'ArXiv',
        'language': 'un',
        'magId': 3006422073,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 48,
        'paperAbstract': "Last decade has seen major improvements in the performance of artificial intelligence which has driven wide-spread applications. Unforeseen effects of such mass-adoption has put the notion of AI safety into the public eye. AI safety is a relatively new field of research focused on techniques for building AI beneficial for humans. While there exist survey papers for the field of AI safety, there is a lack of a quantitative look at the research being conducted. The quantitative aspect gives a data-driven insight about the emerging trends, knowledge gaps and potential areas for future research. In this paper, bibliometric analysis of the literature finds significant increase in research activity since 2015. Also, the field is so new that most of the technical issues are open, including: explainability with its long-term utility, and value alignment which we have identified as the most important long-term research topic. Equally, there is a severe lack of research into concrete policies regarding AI. As we expect AI to be the one of the main driving forces of changes in society, AI safety is the field under which we need to decide the direction of humanity's future.",
        'pdfUrls': [
            'https://au.arxiv.org/abs/2002.05671'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:211096696',
        'title': 'AI safety: state of the field through quantitative lens',
        'tldr': '',
        'venue': 'ArXiv',
        'year': 2020
    }
]

snapshots['QueryTests::test_single_query 1'] = [
    {
        'github_urls': [
        ],
        'id': 69624998,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.3756142812456047,
        'tags': [
        ],
        'title': 'Deep Learning: From Data Extraction to Large-Scale Analysis',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 53757248,
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'score': 0.3853694199463484,
        'tags': [
        ],
        'title': 'Deep learning: Evolution and expansion',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 740114,
        'nbInCitations': 74,
        'nbOutCitations': 18,
        'score': 0.40848807313837515,
        'tags': [
        ],
        'title': 'Deep learning via semi-supervised embedding',
        'year': 2008
    },
    {
        'github_urls': [
        ],
        'id': 145910599,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.4143013534705348,
        'tags': [
        ],
        'title': 'Deep Learning: An Overview and Innovative Approach in Machine Learning',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 208090262,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.41526037418154343,
        'tags': [
        ],
        'title': 'Deep learning: Generative adversarial networks and adversarial methods',
        'year': 2020
    },
    {
        'github_urls': [
        ],
        'id': 59249490,
        'nbInCitations': 3,
        'nbOutCitations': 199,
        'score': 0.43760401199034976,
        'tags': [
        ],
        'title': 'Deep Learning: Current and Emerging Applications in Medicine and Technology',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 1658773,
        'nbInCitations': 6180,
        'nbOutCitations': 1,
        'score': 0.4463282846518005,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'Reducing the Dimensionality of Data with Neural Networks',
        'year': 2006
    },
    {
        'github_urls': [
        ],
        'id': 191519335,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.44906514283468785,
        'tags': [
        ],
        'title': 'Deep Learning is the Core Method of Machine Learning',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 3506178,
        'nbInCitations': 9,
        'nbOutCitations': 32,
        'score': 0.45556686371371036,
        'tags': [
        ],
        'title': 'Deep Learning as a Mixed Convex-Combinatorial Optimization Problem',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 86558517,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.46073613238345973,
        'tags': [
        ],
        'title': 'Deep Learning and Its Applications to Natural Language Processing',
        'year': 2019
    },
    {
        'github_urls': [
            'https://github.com/lisa-lab/DeepLearningTutorials.'
        ],
        'id': 64035733,
        'nbInCitations': 2,
        'nbOutCitations': 0,
        'score': 0.46525400937665706,
        'tags': [
        ],
        'title': 'Deep Learning and Its Parallelization',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 13305088,
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'score': 0.4852539738618844,
        'tags': [
        ],
        'title': 'Deep learning approaches to problems in speech recognition, computational chemistry, and natural language text processing',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 55409477,
        'nbInCitations': 3,
        'nbOutCitations': 0,
        'score': 0.48567164466898705,
        'tags': [
        ],
        'title': 'Deep Learning Techniques and its Various Algorithms and Techniques',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 31062300,
        'nbInCitations': 337,
        'nbOutCitations': 0,
        'score': 0.49283125250552606,
        'tags': [
        ],
        'title': 'Deep Learning via Semi-Supervised Embedding',
        'year': 2012
    },
    {
        'github_urls': [
        ],
        'id': 64207595,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.5049037076297771,
        'tags': [
        ],
        'title': 'Deep Learning for Speech and Language Processing - From Machine Learning and Signal Processing Perspectives',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 57086764,
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'score': 0.5370046573729396,
        'tags': [
        ],
        'title': 'Deep Learning Models for Unsupervised and Transfer Learning',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 23388091,
        'nbInCitations': 6,
        'nbOutCitations': 13,
        'score': 0.5689490642506146,
        'tags': [
        ],
        'title': 'Deep learning: an overview and main paradigms',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 54460325,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.5867901509993197,
        'tags': [
        ],
        'title': 'Deep Learning and Current Trends in Machine Learning',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 3797027,
        'nbInCitations': 38,
        'nbOutCitations': 164,
        'score': 0.5878306347670792,
        'tags': [
        ],
        'title': 'Deep Learning and Its Applications in Biomedicine',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 211121059,
        'nbInCitations': 0,
        'nbOutCitations': 13,
        'score': 0.6064873321920846,
        'tags': [
        ],
        'title': 'Real-World Application of Machine Learning and Deep Learning',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 195513314,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.6369051776464605,
        'tags': [
        ],
        'title': 'Deep learning: a branch of machine learning',
        'year': 2019
    },
    {
        'github_urls': [
        ],
        'id': 6265469,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.6799883328387397,
        'tags': [
        ],
        'title': 'Deep learning for pattern learning and recognition',
        'year': 2015
    },
    {
        'github_urls': [
            'https://github.com/D-X-Y/ResNeXt-DenseNet/blob/master/README.md'
        ],
        'id': 206594692,
        'nbInCitations': 30469,
        'nbOutCitations': 40,
        'score': 0.7326947598155535,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'Deep Residual Learning for Image Recognition',
        'year': 2016
    },
    {
        'github_urls': [
        ],
        'id': 2309950,
        'nbInCitations': 6369,
        'nbOutCitations': 21,
        'score': 0.7670453022170165,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'A Fast Learning Algorithm for Deep Belief Nets',
        'year': 2006
    },
    {
        'github_urls': [
        ],
        'id': 61768184,
        'nbInCitations': 184,
        'nbOutCitations': 0,
        'score': 0.8377993352361067,
        'tags': [
        ],
        'title': 'Deep Learning and Its Applications to Signal and Information Processing',
        'year': 2011
    },
    {
        'github_urls': [
        ],
        'id': 207763512,
        'nbInCitations': 17438,
        'nbOutCitations': 30,
        'score': 0.8392160960514945,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'ImageNet classification with deep convolutional neural networks',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 3074096,
        'nbInCitations': 12555,
        'nbOutCitations': 77,
        'score': 0.9155338285335592,
        'tags': [
            {
                'color': '#A3BAE3',
                'tag': 'Seminal'
            }
        ],
        'title': 'Deep learning',
        'year': 2015
    },
    {
        'github_urls': [
        ],
        'id': 67107441,
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'score': 0.9219391745456602,
        'tags': [
        ],
        'title': 'Deep Learning and Neural Networks',
        'year': 2018
    },
    {
        'github_urls': [
        ],
        'id': 65275290,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.9508992907708416,
        'tags': [
        ],
        'title': 'Machine Learning and Deep Learning',
        'year': 2017
    },
    {
        'github_urls': [
        ],
        'id': 62795222,
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'score': 0.9527335566249684,
        'tags': [
        ],
        'title': 'Machine Learning and Deep Learning',
        'year': 2019
    }
]

snapshots['QueryTests::test_single_query 2'] = [
    {
        'authors': [
            [
                2905252789,
                'M. Voets'
            ]
        ],
        'github_urls': [
        ],
        'id': 69624998,
        'journalName': '',
        'language': 'un',
        'magId': 2904555792,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://munin.uit.no/handle/10037/12808'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:69624998',
        'title': 'Deep Learning: From Data Extraction to Large-Scale Analysis',
        'tldr': '',
        'venue': None,
        'year': 2018
    },
    {
        'authors': [
            [
                2093412048,
                'R. Wason'
            ]
        ],
        'github_urls': [
        ],
        'id': 53757248,
        'journalName': 'Cognitive Systems Research',
        'language': 'un',
        'magId': 2888956734,
        'n_author': [
            0
        ],
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'paperAbstract': ' This paper historically attempts to map the significant success of deep neural networks in notably varied classification problems and application domains with near human-level performance. The paper also addresses the various doubts surrounding the acceptance of deep learning as a science of future. The manuscript attempts to unveil the hidden capabilities of deep neural networks in enabling machines perform the human way tasks which can be learned through what we call observation and experience.',
        'pdfUrls': [
            'https://doi.org/10.1016/j.cogsys.2018.08.023'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:53757248',
        'title': 'Deep learning: Evolution and expansion',
        'tldr': '',
        'venue': 'Cognitive Systems Research',
        'year': 2018
    },
    {
        'authors': [
            [
                130200899,
                'R. Collobert'
            ],
            [
                2058584252,
                'J. Weston'
            ],
            [
                2302942175,
                'F. Ratle'
            ]
        ],
        'github_urls': [
        ],
        'id': 740114,
        'journalName': '',
        'language': 'un',
        'magId': 2159291644,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 74,
        'nbOutCitations': 18,
        'paperAbstract': 'We show how nonlinear embedding algorithms popular for use with shallow semi-supervised learning techniques such as kernel methods can be applied to deep multilayer architectures, either as a regularizer at the output layer, or on each layer of the architecture. This provides a simple alternative to existing approaches to deep learning whilst yielding competitive error rates compared to those methods, and existing shallow semi-supervised techniques.',
        'pdfUrls': [
            'http://portal.acm.org/citation.cfm?id=1390156.1390303'
        ],
        'question': 'How can nonlinear embedding algorithms be applied to deep multilayer architectures?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:740114',
        'title': 'Deep learning via semi-supervised embedding',
        'tldr': 'We show how nonlinear embedding algorithms can be applied to deep multilayer architectures.',
        'venue': "ICML '08",
        'year': 2008
    },
    {
        'authors': [
            [
                2145470339,
                'S. K. Gupta'
            ],
            [
                2355221929,
                'A. Chaturvedi'
            ],
            [
                2481885789,
                'A. Sinha'
            ],
            [
                2936164306,
                'A. Tiwari'
            ]
        ],
        'github_urls': [
        ],
        'id': 145910599,
        'journalName': 'Hidden Link Prediction in Stochastic Social Networks',
        'language': 'un',
        'magId': 2939133744,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.igi-global.com/chapter/deep-learning/227201'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:145910599',
        'title': 'Deep Learning: An Overview and Innovative Approach in Machine Learning',
        'tldr': '',
        'venue': 'Hidden Link Prediction in Stochastic Social Networks',
        'year': 2019
    },
    {
        'authors': [
            [
                1984512120,
                'C. Ledig'
            ],
            [
                1998405790,
                'J. M. Wolterink'
            ],
            [
                2045848816,
                'I. Išgum'
            ],
            [
                2254647456,
                'K. Kamnitsas'
            ]
        ],
        'github_urls': [
        ],
        'id': 208090262,
        'journalName': 'Handbook of Medical Image Computing and Computer Assisted Intervention',
        'language': 'un',
        'magId': 2981585480,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': ' Generative adversarial networks (GANs) and other adversarial methods are based on a game-theoretical perspective on joint optimization of two neural networks as players in a game. Adversarial techniques have been extensively used to synthesize and analyze biomedical images. This chapter provides an introduction to GANs and adversarial methods, with an overview of biomedical image analysis tasks that have benefited from such methods. We conclude with a discussion of strengths and limitations of adversarial methods in biomedical image analysis, and propose potential future research directions.',
        'pdfUrls': [
            'https://researchinformation.amsterdamumc.org/en/publications/deep-learning-generative-adversarial-networks-and-adversarial-met'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:208090262',
        'title': 'Deep learning: Generative adversarial networks and adversarial methods',
        'tldr': '',
        'venue': 'Handbook of Medical Image Computing and Computer Assisted Intervention',
        'year': 2020
    },
    {
        'authors': [
            [
                2186052279,
                'H. Hess'
            ],
            [
                2931562645,
                'A. Akay'
            ]
        ],
        'github_urls': [
        ],
        'id': 59249490,
        'journalName': 'IEEE Journal of Biomedical and Health Informatics',
        'language': 'un',
        'magId': 2913682694,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 3,
        'nbOutCitations': 199,
        'paperAbstract': 'Machine learning is enabling researchers to analyze and understand increasingly complex physical and biological phenomena in traditional fields such as biology, medicine, and engineering and emerging fields like synthetic biology, automated chemical synthesis, and biomanufacturing. These fields require new paradigms toward understanding increasingly complex data and converting such data into medical products and services for patients. The move toward deep learning and complex modeling is an attempt to bridge the gap between acquiring massive quantities of complex data, and converting such data into practical insights. Here, we provide an overview of the field of machine learning, its current applications and needs in traditional and emerging fields, and discuss an illustrative attempt at using deep learning to understand swarm behavior of molecular shuttles.',
        'pdfUrls': [
            'https://doi.org/10.1109/JBHI.2019.2894713'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:59249490',
        'title': 'Deep Learning: Current and Emerging Applications in Medicine and Technology',
        'tldr': '',
        'venue': 'IEEE Journal of Biomedical and Health Informatics',
        'year': 2019
    },
    {
        'authors': [
            [
                563069026,
                'G. E. Hinton'
            ],
            [
                2031945151,
                'R. Salakhutdinov'
            ]
        ],
        'github_urls': [
        ],
        'id': 1658773,
        'journalName': 'Science',
        'language': 'un',
        'magId': 2100495367,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 6180,
        'nbOutCitations': 1,
        'paperAbstract': 'High-dimensional data can be converted to low-dimensional codes by training a multilayer neural network with a small central layer to reconstruct high-dimensional input vectors. Gradient descent can be used for fine-tuning the weights in such “autoencoder” networks, but this works well only if the initial weights are close to a good solution. We describe an effective way of initializing the weights that allows deep autoencoder networks to learn low-dimensional codes that work much better than principal components analysis as a tool to reduce the dimensionality of data.',
        'pdfUrls': [
            'https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=200902233991751269'
        ],
        'question': 'How do deep autoencoder networks learn low-dimensional codes?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:1658773',
        'title': 'Reducing the Dimensionality of Data with Neural Networks',
        'tldr': 'We describe an effective way of initializing the weights that allow deep autoencoder networks to learn low-dimensional codes.',
        'venue': 'Science',
        'year': 2006
    },
    {
        'authors': [
            [
                2947575399,
                'M. R. B. Emdad'
            ]
        ],
        'github_urls': [
        ],
        'id': 191519335,
        'journalName': 'International journal of engineering research and technology',
        'language': 'un',
        'magId': 2947033248,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.ijert.org/deep-learning-is-the-core-method-of-machine-learning'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:191519335',
        'title': 'Deep Learning is the Core Method of Machine Learning',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                1986316548,
                'A. L. Friesen'
            ],
            [
                2169012919,
                'P. Domingos'
            ]
        ],
        'github_urls': [
        ],
        'id': 3506178,
        'journalName': '',
        'language': 'un',
        'magId': 2765185632,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 9,
        'nbOutCitations': 32,
        'paperAbstract': 'As neural networks grow deeper and wider, learning networks with hard-threshold activations is becoming increasingly important, both for network quantization, which can drastically reduce time and energy requirements, and for creating large integrated systems of deep networks, which may have non-differentiable components and must avoid vanishing and exploding gradients for effective learning. However, since gradient descent is not applicable to hard-threshold functions, it is not clear how to learn networks of them in a principled way. We address this problem by observing that setting targets for hard-threshold hidden units in order to minimize loss is a discrete optimization problem, and can be solved as such. The discrete optimization goal is to find a set of targets such that each unit, including the output, has a linearly separable problem to solve. Given these targets, the network decomposes into individual perceptrons, which can then be learned with standard convex approaches. Based on this, we develop a recursive mini-batch algorithm for learning deep hard-threshold networks that includes the popular but poorly justified straight-through estimator as a special case. Empirically, we show that our algorithm improves classification accuracy in a number of settings, including for AlexNet and ResNet-18 on ImageNet, when compared to the straight-through estimator.',
        'pdfUrls': [
            'https://uk.arxiv.org/abs/1710.11573'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:3506178',
        'title': 'Deep Learning as a Mixed Convex-Combinatorial Optimization Problem',
        'tldr': '',
        'venue': 'In Proceedings of the International Conference on Learning Representations (ICLR) 2018',
        'year': 2017
    },
    {
        'authors': [
            [
                2572041914,
                'L. Luo'
            ],
            [
                2911671681,
                'D. Ling'
            ],
            [
                2912860201,
                'L. P. Chueng'
            ],
            [
                3188102685,
                'H. Yang'
            ],
            [
                3188493285,
                'F. Y. L. Chin'
            ]
        ],
        'github_urls': [
        ],
        'id': 86558517,
        'journalName': 'Deep Learning: Fundamentals, Theory and Applications',
        'language': 'un',
        'magId': 2911658506,
        'n_author': [
            0,
            1,
            2,
            3,
            4
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Natural language processing (NLP), utilizing computer programs to process large amounts of language data, is a key research area in artificial intelligence and computer science. Deep learning technologies have been well developed and applied in this area. However, the literature still lacks a succinct survey, which would allow readers to get a quick understanding of (1) how the deep learning technologies apply to NLP and (2) what the promising applications are. In this survey, we try to investigate the recent developments of NLP, centered around natural language understanding, to answer these two questions. First, we explore the newly developed word embedding or word representation methods. Then, we describe two powerful learning models, Recurrent Neural Networks and Convolutional Neural Networks. Next, we outline five key NLP applications, including (1) part-of-speech tagging and named entity recognition, two fundamental NLP applications; (2) machine translation and automatic English grammatical error correction, two applications with prominent commercial value; and (3) image description, an application requiring technologies of both computer vision and NLP. Moreover, we present a series of benchmark datasets which would be useful for researchers to evaluate the performance of models in the related applications.',
        'pdfUrls': [
            'https://link.springer.com/chapter/10.1007%2F978-3-030-06073-2_4'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:86558517',
        'title': 'Deep Learning and Its Applications to Natural Language Processing',
        'tldr': '',
        'venue': 'Deep Learning: Fundamentals, Theory and Applications',
        'year': 2019
    },
    {
        'authors': [
            [
                2123694934,
                'G. Zhang'
            ],
            [
                2641002340,
                'X. Li'
            ],
            [
                2671515484,
                'K. Li'
            ],
            [
                2705902021,
                'W. Zheng'
            ]
        ],
        'github_urls': [
            'https://github.com/lisa-lab/DeepLearningTutorials.'
        ],
        'id': 64035733,
        'journalName': 'Big Data',
        'language': 'un',
        'magId': 2486847405,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 2,
        'nbOutCitations': 0,
        'paperAbstract': 'In recent years, deep learning has been extensively studied as a new way to train multilayer neural networks. Deep learning is a set of algorithms in machine learning, which attempts to model high-level abstractions in input data by using multiple nonlinear transformations. Many great achievements of deep learning have been made in speech recognition, computer vision, and natural language processing. Considering that data volume increases rapidly, deep learning becomes more and more important in predictive analytics of big data. We need tens of millions of parameters and billions of samples to train a high quality and practical deep learning model. As the number of parameters and training data are still growing rapidly in the Big Data era, the speed to train a practical model is limited by sequential algorithms and intensive data computation. Therefore, deep learning has been accelerated in parallel with GPUs and clusters in recent years. This chapter introduces several mainstream deep learning approaches developed over the past decades, as well as optimization methods for deep learning in parallel.',
        'pdfUrls': [
            'http://www.sciencedirect.com/science/article/pii/B9780128053942000040'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:64035733',
        'title': 'Deep Learning and Its Parallelization',
        'tldr': '',
        'venue': 'Big Data',
        'year': 2016
    },
    {
        'authors': [
            [
                2360825425,
                'G. E. Dahl'
            ]
        ],
        'github_urls': [
        ],
        'id': 13305088,
        'journalName': '',
        'language': 'un',
        'magId': 2292368352,
        'n_author': [
            0
        ],
        'nbInCitations': 8,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://tspace.library.utoronto.ca/handle/1807/69304?mode=full'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:13305088',
        'title': 'Deep learning approaches to problems in speech recognition, computational chemistry, and natural language text processing',
        'tldr': '',
        'venue': None,
        'year': 2015
    },
    {
        'authors': [
            [
                2629078425,
                'N. Bhatia'
            ],
            [
                2717027404,
                'C. Rana'
            ]
        ],
        'github_urls': [
        ],
        'id': 55409477,
        'journalName': '',
        'language': 'un',
        'magId': 2211806656,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 3,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://ijeir.org/index.php/new-issue?controller=publications&task=show&modelkey=tabular&id=524'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:55409477',
        'title': 'Deep Learning Techniques and its Various Algorithms and Techniques',
        'tldr': '',
        'venue': None,
        'year': 2015
    },
    {
        'authors': [
            [
                130200899,
                'R. Collobert'
            ],
            [
                2025229873,
                'H. Mobahi'
            ],
            [
                2058584252,
                'J. Weston'
            ],
            [
                2302942175,
                'F. Ratle'
            ]
        ],
        'github_urls': [
        ],
        'id': 31062300,
        'journalName': '',
        'language': 'un',
        'magId': 2407712691,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 337,
        'nbOutCitations': 0,
        'paperAbstract': 'We show how nonlinear embedding algorithms popular for use with "shallow" semi-supervised learning techniques such as kernel methods can be easily applied to deep multi-layer architectures, either as a regularizer at the output layer, or on each layer of the architecture. This trick provides a simple alternative to existing approaches to deep learning whilst yielding competitive error rates compared to those methods, and existing shallow semi-supervised techniques.',
        'pdfUrls': [
            'https://doi.org/10.1007/978-3-642-35289-8_34'
        ],
        'question': 'How can nonlinear embedding algorithms be applied to deep multi-layer architectures?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:31062300',
        'title': 'Deep Learning via Semi-Supervised Embedding',
        'tldr': 'We show how nonlinear embedding algorithms can be easily applied to deep multi-layer architectures.',
        'venue': 'Neural Networks: Tricks of the Trade',
        'year': 2012
    },
    {
        'authors': [
            [
                2101552792,
                'L. Deng'
            ]
        ],
        'github_urls': [
        ],
        'id': 64207595,
        'journalName': '',
        'language': 'un',
        'magId': 2484788211,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Interspeech-tutorial-2015-LiDeng-Sept6.pptx'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:64207595',
        'title': 'Deep Learning for Speech and Language Processing - From Machine Learning and Signal Processing Perspectives',
        'tldr': '',
        'venue': None,
        'year': 2015
    },
    {
        'authors': [
            [
                2191276622,
                'N. Srivastava'
            ]
        ],
        'github_urls': [
        ],
        'id': 57086764,
        'journalName': '',
        'language': 'un',
        'magId': 2790157636,
        'n_author': [
            0
        ],
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'https://tspace.library.utoronto.ca/bitstream/1807/80672/3/Srivastava_Nitish_201711_PhD_thesis.pdf'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:57086764',
        'title': 'Deep Learning Models for Unsupervised and Transfer Learning',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
            [
                2045668823,
                'V. Golovko'
            ]
        ],
        'github_urls': [
        ],
        'id': 23388091,
        'journalName': 'Optical Memory and Neural Networks',
        'language': 'un',
        'magId': 2604802223,
        'n_author': [
            0
        ],
        'nbInCitations': 6,
        'nbOutCitations': 13,
        'paperAbstract': 'In the present paper, we examine and analyze main paradigms of learning of multilayer neural networks starting with a single layer perceptron and ending with deep neural networks, which are considered regarded as a breakthrough in the field of the intelligent data processing. The baselessness of some ideas about the capacity of multilayer neural networks is shown and transition to deep neural networks is justified. We discuss the principal learning models of deep neural networks based on the restricted Boltzmann machine (RBM), an autoassociative approach and a stochastic gradient method with a Rectified Linear Unit (ReLU) activation function of neural elements.',
        'pdfUrls': [
            'https://link.springer.com/article/10.3103/S1060992X16040081'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:23388091',
        'title': 'Deep learning: an overview and main paradigms',
        'tldr': '',
        'venue': 'Optical Memory and Neural Networks',
        'year': 2016
    },
    {
        'authors': [
            [
                1964212709,
                'G. Tirkes'
            ],
            [
                2137024135,
                'M. Karakaya'
            ],
            [
                2152767980,
                'A. Bostan'
            ],
            [
                2156748970,
                'G. Sengul'
            ],
            [
                2884075291,
                'C. Ç. Ekin'
            ]
        ],
        'github_urls': [
        ],
        'id': 54460325,
        'journalName': '2018 3rd International Conference on Computer Science and Engineering (UBMK)',
        'language': 'un',
        'magId': 2904780335,
        'n_author': [
            0,
            1,
            2,
            3,
            4
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Academic interest and commercial attention can be used to identify how much potential a novel technology may have. Since the prospective advantages in it may help solving some problems that are not solved yet or improving the performance of readily available ones. In this study, we have investigated the Web of Science (WOS) indexing service database for the publications on Deep Learning (DL), Machine Learning (ML), Convolutional Neural Networks (CNN), and Image Processing to reveal out the current trend. The figures indicate the strong potential in DL approach especially in image processing domain.',
        'pdfUrls': [
            'http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=8566365'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:54460325',
        'title': 'Deep Learning and Current Trends in Machine Learning',
        'tldr': '',
        'venue': '2018 3rd International Conference on Computer Science and Engineering (UBMK)',
        'year': 2018
    },
    {
        'authors': [
            [
                2156411412,
                'W. Shu'
            ],
            [
                2276795514,
                'Z. Xie'
            ],
            [
                2304192564,
                'F. Liu'
            ],
            [
                2559590819,
                'W. Li'
            ],
            [
                2701866245,
                'X. Bo'
            ],
            [
                2790642710,
                'H. Tan'
            ],
            [
                2791960874,
                'D. Song'
            ],
            [
                2792988815,
                'Y. Zhou'
            ],
            [
                2793440846,
                'C. Cao'
            ]
        ],
        'github_urls': [
        ],
        'id': 3797027,
        'journalName': 'Genomics, Proteomics & Bioinformatics',
        'language': 'un',
        'magId': 2789367970,
        'n_author': [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8
        ],
        'nbInCitations': 38,
        'nbOutCitations': 164,
        'paperAbstract': ' Advances in biological and medical technologies have been providing us explosive volumes of biological and physiological data, such as medical images , electroencephalography, genomic and protein sequences. Learning from these data facilitates the understanding of human health and disease. Developed from artificial neural networks, deep learning -based algorithms show great promise in extracting features and learning patterns from complex data. The aim of this paper is to provide an overview of deep learning techniques and some of the state-of-the-art applications in the biomedical field. We first introduce the development of artificial neural network and deep learning. We then describe two main components of deep learning, i.e. , deep learning architectures and model optimization. Subsequently, some examples are demonstrated for deep learning applications, including medical image classification, genomic sequence analysis, as well as protein structure classification and prediction. Finally, we offer our perspectives for the future directions in the field of deep learning.',
        'pdfUrls': [
            'https://www.mendeley.com/catalogue/deep-learning-applications-biomedicine/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:3797027',
        'title': 'Deep Learning and Its Applications in Biomedicine',
        'tldr': 'Deep learning algorithms show great promise in extracting features and learning patterns from complex data. We describe two main components of deep learning, deep learning architectures and model optimization.',
        'venue': 'Genomics, Proteomics & Bioinformatics',
        'year': 2018
    },
    {
        'authors': [
            [
                3005843063,
                'S. R. Sree'
            ],
            [
                3006653358,
                'S. Vyshnavi'
            ],
            [
                3047037995,
                'N. Jayapandian'
            ]
        ],
        'github_urls': [
        ],
        'id': 211121059,
        'journalName': '2019 International Conference on Smart Systems and Inventive Technology (ICSSIT)',
        'language': 'un',
        'magId': 3006558083,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 0,
        'nbOutCitations': 13,
        'paperAbstract': "The world today is running on the latest computer technologies and one of those is machine learning. The real life example that most of us know is speech recognition. Google Assistant is the common example for this Speech recognition. This google assistant is not only limited till ‘Ok Google’, but it responds to all your questions in a smart way. It can manage all your calls or can book appointments. Imagine you fell down while de-boarding a bus. So, Next time you take care so that you don't fall that is something that your brain has interpreted from your past experience. This is what exactly deep learning is, it imitates human brain works. Deep learning is sub-branch of machine learning. It is able to build all new things based on its previous experiences. Many of us have heard about driverless cars and medical diagnosis. Recently google has developed a new technology where all your cardiovascular events can be predicted by eye scan so, that doctors can get a clear view of what is inside the body of a patient. These all are developed using machine learning. It has a capability to change the human world into a complete robotic world. Anyways, it also has its own disadvantages. This article discusses about those, Scope of machine learning, its Market potential, financial growth and Current applications of machine learning.",
        'pdfUrls': [
            'http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=8987844'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:211121059',
        'title': 'Real-World Application of Machine Learning and Deep Learning',
        'tldr': '',
        'venue': '2019 International Conference on Smart Systems and Inventive Technology (ICSSIT)',
        'year': 2019
    },
    {
        'authors': [
            [
                2948046021,
                'P. R. Kumar'
            ],
            [
                2948765318,
                'E. B. K. Manash'
            ]
        ],
        'github_urls': [
        ],
        'id': 195513314,
        'journalName': 'Journal of Physics: Conference Series',
        'language': 'un',
        'magId': 2948382308,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'http://ui.adsabs.harvard.edu/abs/2019JPhCS1228a2045R/abstract'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:195513314',
        'title': 'Deep learning: a branch of machine learning',
        'tldr': '',
        'venue': 'Journal of Physics: Conference Series',
        'year': 2019
    },
    {
        'authors': [
            [
                2723895958,
                'C. L. P. Chen'
            ]
        ],
        'github_urls': [
        ],
        'id': 6265469,
        'journalName': '2015 IEEE 10th Jubilee International Symposium on Applied Computational Intelligence and Informatics',
        'language': 'un',
        'magId': 2100038104,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': 'Deep learning is a set of algorithms in machine learning that attempt to learn in multiple levels, corresponding to different levels of abstraction. It is typically used to abstract useful information from data. The levels in these learned statistical models correspond to distinct levels of concepts, where higher-level concepts are defined from lower-level ones, and the same lower level concepts can help to define many higher-level concepts. Alternatively, the main advantage of deep learning is about learning multiple levels of representation and abstraction that help to make sense of data such as images, sound, and text. This talk is to overview the foundationa, data representation capability of deep networks, and to investigate efficient deep learning algorithms, and meaningful applications.',
        'pdfUrls': [
            'http://ieeexplore.ieee.org/document/7208200/'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:6265469',
        'title': 'Deep learning for pattern learning and recognition',
        'tldr': '',
        'venue': '2015 IEEE 10th Jubilee International Symposium on Applied Computational Intelligence and Informatics',
        'year': 2015
    },
    {
        'authors': [
            [
                2119543935,
                'S. Ren'
            ],
            [
                2164292938,
                'K. He'
            ],
            [
                2200192130,
                'J. Sun'
            ],
            [
                2499063207,
                'X. Zhang'
            ]
        ],
        'github_urls': [
            'https://github.com/D-X-Y/ResNeXt-DenseNet/blob/master/README.md'
        ],
        'id': 206594692,
        'journalName': '2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)',
        'language': 'un',
        'magId': 2194775991,
        'n_author': [
            0,
            1,
            2,
            3
        ],
        'nbInCitations': 30469,
        'nbOutCitations': 40,
        'paperAbstract': 'Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers—8× deeper than VGG nets [40] but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers. The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions1, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.',
        'pdfUrls': [
            'https://lib-arxiv-008.serverfarm.cornell.edu/pdf/1512.03385.pdf'
        ],
        'question': 'How do residual learning frameworks affect the training of networks?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:206594692',
        'title': 'Deep Residual Learning for Image Recognition',
        'tldr': 'We present a residual learning framework to ease the training of networks that are substantially deeper than previously. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions.',
        'venue': '2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)',
        'year': 2016
    },
    {
        'authors': [
            [
                563069026,
                'G. E. Hinton'
            ],
            [
                1354816936,
                'Y. W. Teh'
            ],
            [
                1617862073,
                'S. Osindero'
            ]
        ],
        'github_urls': [
        ],
        'id': 2309950,
        'journalName': 'Neural Computation',
        'language': 'un',
        'magId': 2136922672,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 6369,
        'nbOutCitations': 21,
        'paperAbstract': 'We show how to use "complementary priors" to eliminate the explaining-away effects that make inference difficult in densely connected belief nets that have many hidden layers. Using complementary priors, we derive a fast, greedy algorithm that can learn deep, directed belief networks one layer at a time, provided the top two layers form an undirected associative memory. The fast, greedy algorithm is used to initialize a slower learning procedure that fine-tunes the weights using a contrastive version of the wake-sleep algorithm. After fine-tuning, a network with three hidden layers forms a very good generative model of the joint distribution of handwritten digit images and their labels. This generative model gives better digit classification than the best discriminative learning algorithms. The low-dimensional manifolds on which the digits lie are modeled by long ravines in the free-energy landscape of the top-level associative memory, and it is easy to explore these ravines by using the directed connections to display what the associative memory has in mind.',
        'pdfUrls': [
            'http://doi.org/10.1162/neco.2006.18.7.1527'
        ],
        'question': 'How can we eliminate explaining-away effects in densely connected belief nets?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:2309950',
        'title': 'A Fast Learning Algorithm for Deep Belief Nets',
        'tldr': 'We show how to use "complementary priors" to eliminate explaining-away effects in densely connected belief nets. A network with three hidden layers forms a good generative model of the joint distribution of handwritten digit images and their labels.',
        'venue': 'Neural Computation',
        'year': 2006
    },
    {
        'authors': [
            [
                2101552792,
                'L. Deng'
            ],
            [
                2103789662,
                'D. Yu'
            ]
        ],
        'github_urls': [
        ],
        'id': 61768184,
        'journalName': 'IEEE Signal Processing Magazine',
        'language': 'un',
        'magId': 2124173482,
        'n_author': [
            0,
            1
        ],
        'nbInCitations': 184,
        'nbOutCitations': 0,
        'paperAbstract': 'INTRODUCTION TO DEEP LEARNING Many traditional machine learning and signal processing techniques exploit shallow architectures, which contain a single layer of nonlinear feature transformation. Examples of shallow architectures are conventional hidden Markov models (HMMs), linear or nonlinear dynamical systems, conditional random fields (CRFs), maximum entropy (MaxEnt) models, support vector machines (SVMs), kernel regression, and multilayer perceptron (MLP) with a single hidden layer. A property common to these shallow learning models is the simple architecture that consists of only one layer responsible for transforming the raw input signals or features into a problem-specific feature space, which may be unobservable. Take the example of a support vector machine. It is a shallow linear separation model with one feature transformation layer when kernel trick is used, and with zero feature transformation layer when kernel trick is not used. Human information processing',
        'pdfUrls': [
            'https://research.microsoft.com/apps/pubs/default.aspx?id=143620'
        ],
        'question': 'What are the properties of shallow architectures?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:61768184',
        'title': 'Deep Learning and Its Applications to Signal and Information Processing',
        'tldr': 'Many traditional machine learning and signal processing techniques exploit shallow architectures. Examples of shallow architectures are conventional hidden Markov models (HMMs) and linear or nonlinear dynamical systems. A property common to these shallow learning models is the simple architecture that consists only one layer responsible for transforming the raw input signals or features into a problem-specific feature space.',
        'venue': None,
        'year': 2011
    },
    {
        'authors': [
            [
                215131072,
                'I. Sutskever'
            ],
            [
                563069026,
                'G. E. Hinton'
            ],
            [
                1171453863,
                'A. Krizhevsky'
            ]
        ],
        'github_urls': [
        ],
        'id': 207763512,
        'journalName': '',
        'language': 'un',
        'magId': 2618530766,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 17438,
        'nbOutCitations': 30,
        'paperAbstract': 'We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0%, respectively, which is considerably better than the previous state-of-the-art. The neural network, which has 60 million parameters and 650,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and three fully connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of the convolution operation. To reduce overfitting in the fully connected layers we employed a recently developed regularization method called "dropout" that proved to be very effective. We also entered a variant of this model in the ILSVRC-2012 competition and achieved a winning top-5 test error rate of 15.3%, compared to 26.2% achieved by the second-best entry.',
        'pdfUrls': [
            'https://dl.acm.org/citation.cfm?id=3098997.3065386'
        ],
        'question': 'How can we train a large convolutional neural network to classify high-resolution',
        's2Url': 'https://api.semanticscholar.org/CorpusID:207763512',
        'title': 'ImageNet classification with deep convolutional neural networks',
        'tldr': 'We trained a large convolutional neural network to classify 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest. On the test data, we achieved top-1 and top-5 error rates of 37.5% and 17.0%, respectively, which is considerably better than the previous state-of-the-art.',
        'venue': 'CACM',
        'year': 2017
    },
    {
        'authors': [
            [
                161269817,
                'Y. Bengio'
            ],
            [
                1822555116,
                'I. Goodfellow'
            ],
            [
                2328522601,
                'A. Courville'
            ]
        ],
        'github_urls': [
        ],
        'id': 3074096,
        'journalName': 'Nature',
        'language': 'un',
        'magId': 2557283755,
        'n_author': [
            0,
            1,
            2
        ],
        'nbInCitations': 12555,
        'nbOutCitations': 77,
        'paperAbstract': 'Deep learning is a form of machine learning that enables computers to learn from experience and understand the world in terms of a hierarchy of concepts. Because the computer gathers knowledge from experience, there is no need for a human computer operator to formally specify all the knowledge that the computer needs. The hierarchy of concepts allows the computer to learn complicated concepts by building them out of simpler ones; a graph of these hierarchies would be many layers deep. This book introduces a broad range of topics in deep learning. The text offers mathematical and conceptual background, covering relevant concepts in linear algebra, probability theory and information theory, numerical computation, and machine learning. It describes deep learning techniques used by practitioners in industry, including deep feedforward networks, regularization, optimization algorithms, convolutional networks, sequence modeling, and practical methodology; and it surveys such applications as natural language processing, speech recognition, computer vision, online recommendation systems, bioinformatics, and videogames. Finally, the book offers research perspectives, covering such theoretical topics as linear factor models, autoencoders, representation learning, structured probabilistic models, Monte Carlo methods, the partition function, approximate inference, and deep generative models. Deep Learning can be used by undergraduate or graduate students planning careers in either industry or research, and by software engineers who want to begin using deep learning in their products or platforms. A website offers supplementary material for both readers and instructors.',
        'pdfUrls': [
            'https://dl.acm.org/citation.cfm?id=3086952'
        ],
        'question': 'How can deep learning be used to learn from experience?',
        's2Url': 'https://api.semanticscholar.org/CorpusID:3074096',
        'title': 'Deep learning',
        'tldr': 'Deep learning is a form of machine learning that enables computers to learn from experience. The hierarchy of concepts allows the computer to learn complicated concepts by building them out of simpler ones. Deep Learning can be used by undergraduate or graduate students planning careers in either industry or research.',
        'venue': 'Nature',
        'year': 2015
    },
    {
        'authors': [
            [
                2795305703,
                'S. Mukhopadhyay'
            ]
        ],
        'github_urls': [
        ],
        'id': 67107441,
        'journalName': 'Advanced Data Analytics Using Python',
        'language': 'un',
        'magId': 2795152598,
        'n_author': [
            0
        ],
        'nbInCitations': 1,
        'nbOutCitations': 0,
        'paperAbstract': 'A neural network, specifically known as an artificial neural network (ANN), has been developed by the inventor of one of the first neurocomputers, Dr. Robert Hecht-Nielsen. He defines a neural network as follows:',
        'pdfUrls': [
            'https://rd.springer.com/chapter/10.1007/978-1-4842-3450-1_5'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:67107441',
        'title': 'Deep Learning and Neural Networks',
        'tldr': '',
        'venue': 'Advanced Data Analytics Using Python',
        'year': 2018
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 65275290,
        'journalName': '',
        'language': 'un',
        'magId': 2739803447,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
            'None'
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:65275290',
        'title': 'Machine Learning and Deep Learning',
        'tldr': '',
        'venue': None,
        'year': 2017
    },
    {
        'authors': [
        ],
        'github_urls': [
        ],
        'id': 62795222,
        'journalName': 'Regular Issue',
        'language': 'un',
        'magId': None,
        'n_author': [
            0
        ],
        'nbInCitations': 0,
        'nbOutCitations': 0,
        'paperAbstract': '',
        'pdfUrls': [
        ],
        'question': '',
        's2Url': 'https://api.semanticscholar.org/CorpusID:62795222',
        'title': 'Machine Learning and Deep Learning',
        'tldr': '',
        'venue': 'Regular Issue',
        'year': 2019
    }
]

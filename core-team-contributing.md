
# AWS Beanstalk

To deploy sur develop :
1. Commit you changes on develop
2. ```eb deploy``` (if not yet done: ```pip install awsebcli```)

Check the status of the application in aws:
to check that no rollback and healthcheck.

To deploy on production:
```
git checkout main
eb deploy
```


# pgadmin
```
conda activate omni
pgadmin4
```


# Methodo systematique pour changer le back

- dev sur le dev
- tester avec la suite de test et à la main sur localhost
- source scripts/update_gunicorn_dev
- checker le nouvel algo https://front-git-dev-omniscienceacademy.vercel.app/
- comparer pour voir si c'est mieux que sur https://front-git-staging-omniscienceacademy.vercel.app/
- Si A/B test validé : git push, source scripts/update_prod, source scripts/update_gunicorn_prod
- le new algo est alors dispo sur https://omniscience.academy !

# Using Pull requests

3 branches pour le front :
dev : dev front, dev back (attention à ne pas coller dans streamlit)
staging : dev front, prod back
main : prod front, prod back

2 repos pour le back:
djrestapi_dev
djrestapi

Pour faire du A/B testing sur Algo:

- dev vs staging

Pour faire valider une feature du front:

- dev > staging > prod

A/B testing back:
new : https://front-git-dev-omniscienceacademy.vercel.app/
old : https://front-git-staging-omniscienceacademy.vercel.app/

A/B testing front:
new : https://front-git-staging-omniscienceacademy.vercel.app/
old : https://omniscience.academy


# line profiling
```
python -m cProfile -o misc/profiling/test.pstats manage.py test  api.tests.QueryTests.test_single_query
snakeviz misc/profiling/test.pstats
```

# Security check
```
bandit -r . -c "pyproject.toml"
```

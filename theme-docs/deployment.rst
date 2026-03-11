==========
Deployment
==========


GitHub Pages
------------

.. code-block:: yaml

   # .github/workflows/docs.yml
   name: Deploy docs
   on:
     push:
       branches: [main]
   permissions:
     pages: write
     id-token: write
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-python@v5
           with:
             python-version: "3.12"
         - run: pip install sphinx
         - run: pip install -e .
         - run: sphinx-build -b html docs/ _build/html
         - uses: actions/upload-pages-artifact@v3
           with:
             path: _build/html
     deploy:
       needs: build
       runs-on: ubuntu-latest
       environment:
         name: github-pages
       steps:
         - uses: actions/deploy-pages@v4


GitLab Pages
------------

.. code-block:: yaml

   pages:
     image: python:3.12
     script:
       - pip install sphinx
       - pip install -e .
       - sphinx-build -b html docs/ public/
     artifacts:
       paths:
         - public/


Read the Docs
-------------

Add the theme as a dependency in ``docs/requirements.txt``:

.. code-block:: text

   sphinx>=7.0
   manticore-sphinx-theme @ git+https://github.com/yourorg/manticore-sphinx-theme.git


Self-Hosted (Nginx)
-------------------

.. code-block:: bash

   python build.py docs-prod
   rsync -avz --delete _build/html/ webserver:/var/www/docs/

Enable gzip pre-compression in Nginx:

.. code-block:: nginx

   gzip_static on;


S3 / CloudFront
----------------

.. code-block:: bash

   python build.py docs-prod
   aws s3 sync _build/html/ s3://my-docs-bucket/ --delete
   aws cloudfront create-invalidation --distribution-id XXXXX --paths "/*"

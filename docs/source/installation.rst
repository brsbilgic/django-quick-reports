Installation
============

1. Download it from PyPI

    ``pip install django-quick-reports``


2. Add ``quick_reports`` to your ``INSTALLED_APS`` setting.


.. code-block:: python

    INSTALLED_APPS = (
        ...
        'quick_reports',
    )



3. Add ``include('quick_reports.urls')`` to your url patterns.

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^reports/', include('quick_reports.urls'))
    )

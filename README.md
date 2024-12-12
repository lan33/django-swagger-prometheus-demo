* **Démarrer le serveur** : `manage.py runserver`

* **Documentation API** : avec `drf_yasg`, fichiers concernés :
   * `settings.py` : `INSTALLED_APPS drf_yasg`, `SWAGGER_SETTINGS` (pour configurer l'authentification)
   * `urls.py` : route `swagger`
   * `views.py` : `@api_view`

* **Monitorage Prometheus** : avec `prometheus_client` et `django-prometheus`, fichiers concernés :
  * `settings.py` : `INSTALLED_APPS django_prometheus`, `MIDDLEWARE django_prometheus...`
  * `urls.py` : `django_prometheus.urls`

* **Installer Prometheus** : https://prometheus.io/download/, https://prometheus.io/docs/introduction/first_steps/

* **Configurer Prometheus** : dans `prometheus.yml` :
    ```
    scrape_configs:
     - job_name: 'django'
       static_configs:
        - targets: ['localhost:8000']
   ```
* **Démarrer Prometheus** : `prometheus --config.file=prometheus.yml` pour prendre en compte des modifications de `prometheus.yml`, `prometheus` tout court sinon.

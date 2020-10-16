import os
import dj_database_url

# URL postgres://emhwxlgy:u1qrpeOswWfv96RhQkCeF1JT0csJ1IaR@balarama.db.elephantsql.com:5432/emhwxlgy

DATABASES = {
    'default': dj_database_url.config(default=os.environ['PROD_DATABASE_URL'])
}

export REACT_APP_USERS_SERVICE_URL=http://localhost

export REACT_APP_SCORES_SERVICE_URL=http://localhost

export REACT_APP_EXERCISES_SERVICE_URL=http://localhost

export REACT_APP_SCORES_SERVICE_URL=http://localhost

export REACT_APP_API_GATEWAY_URL=https://eq9oax74xe.execute-api.us-west-1.amazonaws.com/v2/execute 

docker-compose exec users python manage.py recreate_db

docker-compose exec users python manage.py seed_db

docker-compose exec exercises python manage.py recreate_db

docker-compose exec exercises python manage.py seed_db

docker-compose exec scores python manage.py recreate_db

docker-compose exec scores python manage.py seed_db
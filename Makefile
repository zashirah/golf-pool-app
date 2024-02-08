dev_initial_setup:
	python ingest/run_initial_setup.py
	cp admin.csv dbt_project/data/
	cp field*.csv dbt_project/data/
	dbt run -s +fct_field +dim_tournaments
	cp dbt_project/data/golf.duckdb evidence_project/sources/golf/
	cd evidence_project && npm run sources && npm run dev

dev_before_tournament:
	python ingest/run_before_tournament_start.py
	cp *.csv dbt_project/data/
	dbt run
	cp dbt_project/data/golf.duckdb evidence_project/sources/golf
	cd evidence_project && npm run sources && npm run dev

dev_during_tournament:
	python ingest/run_during_tournament.py
	cp *.csv dbt_project/data/
	dbt run
	cp dbt_project/data/golf.duckdb evidence_project/sources/golf
	cd evidence_project && npm run sources && npm run dev

during_tournament:
	pip install -r requirements.txt	
	python ~/ingest/run_during_tournament.py
	cp *.csv ~/dbt_project/data/
	dbt run
	cp ~/dbt_project/data/golf.duckdb ~/evidence_project/sources/golf
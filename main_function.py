from main import main  # <- importing existing logic

def run_etl(request):
    main()  # triggers ETL process
    return "ETL triggered", 200

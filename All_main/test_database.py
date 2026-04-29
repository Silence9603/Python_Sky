from sqlalchemy import create_engine, text 


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1['name'] == "QA Студия 'ТестировщикЪ'"

    connection.close()
    # inspector = inspect(db)
    # names = inspector.get_table_names()
    # assert names[0] == 'company'

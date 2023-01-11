import sqlite3 as SQL


def match_exact(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for an exact match
    3. If success return the definition
    4. If not return an empty list
    """

    #Establish connection to the dictionary database
    db = SQL.connect(r"C:\Users\cyendes\OneDrive - Environmental Works\Work Programs\API Stuff\GitHub\web-apis-with-python\data\dictionary.db")

    #Query the database for exact matches
    sql_query = "SELECT* from entries WHERE word=?"
    match = db.execute(sql_query, (word,)).fetchall()

    # TODO: Clone the connection to the database
    db.close()

    # Return the results
    return match


def match_like(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for approximate matches
    3. If success return the definition as a list
    4. If not return an empty list
    """
    # TODO: Establish connection to the dictionary database
    db = SQL.connect(r"C:\Users\cyendes\OneDrive - Environmental Works\Work Programs\API Stuff\GitHub\web-apis-with-python\data\dictionary.db")
    
    # TODO: Query the database for exact matches
    sql_query = "SELECT* from entries WHERE word LIKE?"
    match = db.execute(sql_query,("%"+word+"%",)).fetchall()

    # TODO: Clone the connection to the database
    db.close()

    # Return the results
    return match

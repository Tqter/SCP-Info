import sqlite3

database = sqlite3.connect('lang.db')

# This function will create a table named "ExampleTable"
def CreateTable():
    database.execute("drop table if exists ExampleTable")  # This deletes the table if it already exists.
    database.execute("create table ExampleTable"
                     "(exampleString str primary key not null,"
                     # ^ This declares a column called "exampleString", that stores data.
                     # "Primary Key" means that nothing else can exist in the table with the same name. This is typically used for storing IDs.
                     "exampleInt int default 0,"
                     # ^ This creates the "exampleInt" column. It can only be a number, and it defaults to 0.
                     "exampleBool bool default false);")

    database.commit()


def SelectAllFromTable():
    data = database.execute(
        "select * from ExampleTable").fetchall()
    print(data)


def SelectFromTableWithStr(string: str):
    data = database.execute("select * from ExampleTable where exampleString = ?", (string,)).fetchone()
    """
    Ok so there is a lot going on here. I'll explain it all.
    Here, the "*" means we select all the data in the columns. However, we only get certain rows because of the
    "where exampleString = ?". That "?" allows us to subsitute literally anything into it, as long as it is in the Tuple
    out side of the string. "(string,)". If you are only using one selector, make sure that the comma follows the variable name
    The variables that correspond to the question marks must be in order. EX: string = ?, int = ? your tuple would look like
    (string, int). "fetchone()" means that it will only grab the first result to come back as true.
    """
    print(data)


def WriteToTable(string: str, integer: int, boolean: bool):
    database.execute("update ExampleTable set exampleInt = ?, exampleBool = ? where exampleString = ?",
                     (integer, boolean, string))
    """
    This will update exampleInt and exampleBool to be what ever you passed in, only where exampleString = string. 
    This one is pretty straight forward.
    """
    database.commit()  # Make sure you commit!


def CreateNewRow(string: str, integer: int):
    database.execute("insert into ExampleTable (exampleString, exampleInt) values (?,?)", (string, integer))
    """
    This one is pretty simple too. This creates a new entry in the table, and assigns it whatever we passed in right before "values"
    The exampleString is needed, as it is set to "not null" up above. If we were to miss it, and error would be thrown.
    We are also setting exampleInt, which can really be any number.
    Once again, the question marks must match the order of the variables.
    """
    database.commit()  # Don't forget to commit!





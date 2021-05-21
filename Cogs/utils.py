import sqlite3
import builtins
db = sqlite3.connect("database.db")
db.execute("""
CREATE TABLE IF NOT EXISTS guilds (
    GuildID integer PRIMARY KEY,
    Prefix text DEFAULT "'"
);""")
db.commit()
builtins.db = db



def get_prefix(guild_id):
  data = db.execute("select prefix from guilds where GuildId = ?",(guild_id,)).fetchone()
  if data is None:
    db.execute("insert into guilds (GuildID) values (?)",(guild_id,))
    db.commit()
    return "'"
  else:
    return data[0]
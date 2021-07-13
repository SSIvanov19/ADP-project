import logging
import sqlite3

class AdpprojectPipeline:
    def __init__(self):
        """
        Creating a local sqlite database and
        creating the schema if it doesn't exist already. 
        """
        self.connection = sqlite3.connect("./fandomdata.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FandomData
            (
                id INTEGER PRIMARY KEY, 
                name VARCHAR(255), 
                country VARCHAR(255), 
                imgLink VARCHAR(255)
            )
        """
        )

    def process_item(self, item, spider):
        """
        Minimal item processing and inserting it into the
        database using the `self.connection` initialized
        in the constructor.
        """

        self.cursor.execute(
            """INSERT INTO FandomData (name, country, imgLink) values (?, ?, ?)""",
            (item["name"], item["country"], item["imgLink"]),
        )
        self.connection.commit()
        logging.debug("Item stored {}".format(item["name"]))
        return item

class V0:
    def upgrade(self, cursor):
        cursor.execute('CREATE TABLE IF NOT EXISTS informations ('
                       'change_date TEXT,'
                       'version integer'
                       ');')
class QueryBuilder:
    def __init__(self):
        self.query = ""
    
    def select(self, fields):
        self.query += f"SELECT {fields} "
        return self
    
    def from_table(self, table):
        self.query += f"FROM {table} "
        return self
    
    def where(self, condition):
        self.query += f"WHERE {condition}"
        return self

qb = QueryBuilder()
qb.select("*").from_table("users").where("age > 18")
print(qb.query)

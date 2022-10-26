from odmantic import Model,Field


class User(Model):
    id: str = Field(primary_field=True)
    name: str
    email: str
    password: str
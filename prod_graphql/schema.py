import graphene
from todos_app import schema


class MyQuery(schema.TodoQuery, graphene.ObjectType):
    name=graphene.String(default_value="TungDZ")
    title = graphene.String(default_value="App123")

class MyMutation(schema.TodoMutation, graphene.ObjectType):
    pass


my_schema = graphene.Schema(query=MyQuery, mutation=MyMutation)
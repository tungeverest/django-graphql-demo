# Documents
Create a services GraphQL Server demo.

[Video Guide]( https://www.youtube.com/watch?v=vtXmOWltHAM&list=PLsC9YeVUTz3-YuHLkA2Kx5TqaPEHioldV)

[GraphQL server lib doc](https://docs.graphene-python.org/projects/django/en/latest/)

[Install](https://docs.graphene-python.org/projects/django/en/latest/installation/)

```bash
pip install graphene-django
```

```python
THIRD_PARTY_APPS = [
    "graphene_django",
]

PROJECT_APPS = [
    'todos_app',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

############ SETTING UPDATE ###########

GRAPHENE = {
    "SCHEMA": "prod_graphql.schema.my_schema"
}
```

# schema.py

```python
import graphene
from todos_app import schema


class MyQuery(schema.TodoQuery, graphene.ObjectType):
    name=graphene.String(default_value="TungDZ")
    title = graphene.String(default_value="App123")

class MyMutation(schema.TodoMutation, graphene.ObjectType):
    pass


my_schema = graphene.Schema(query=MyQuery, mutation=MyMutation)
```

# Run API
```bash
- Demo

{
  name:name
}

{
  name
  title
}
.........
- Get All

{
  todos {
    id
    title
    date
    
  }
}
.........
- Get by ID

{
  todos(id:3) {
    id
    title
    date
    
  }
}
.........
- Create new todo

mutation{
	createTodo(title:"todo 123") {
    todo {
      id
      title
      date
    }
  }  
}

mutation CreateTodo($title:String!){
	createTodo(title:$title) {
    todo {
      id
      title
      date
    }
  }  
}

Query variables
{
    "title": "test variable"
}
.........
- Update Todo by ID

mutation{
	udpateTodo(id:6, title:"todo 6666") {
		todo {
      id
      title
      date
    }
  }  
}

mutation UpdateTodo($id:Int!, $title:String!){
	udpateTodo(id:$id, title:$title) {
		todo {
      id
      title
      date
    }
  }  
}
Query String
{
    "id": 7,
    "title" : "edit todo 7"
}
.........
- Delete Todo by ID:

mutation {
  deleteTodo(id:6) {
      message
    }
}
-----
mutation DeleteTodo($id:Int!){
	deleteTodo(id:$id) {
      message
    }
} 

{
    "id": 7
}
```

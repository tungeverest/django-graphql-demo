https://www.youtube.com/watch?v=vtXmOWltHAM&list=PLsC9YeVUTz3-YuHLkA2Kx5TqaPEHioldV
https://docs.graphene-python.org/projects/django/en/latest/
https://docs.graphene-python.org/projects/django/en/latest/installation/

pip install graphene-django


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
## schema.py
import graphene


class MyQuery(graphene.ObjectType):
    name=graphene.String(default_value="TungDZ")
    


my_schema = graphene.Schema(query=MyQuery)

## test
{
  name:name
}

{
  name
  title
}

get All
{
  todos {
    id
    title
    date
    
  }
}
get ID
{
  todos(id:3) {
    id
    title
    date
    
  }
}

Create new todo

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

Update Todo by ID
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

Delete Todo by ID:

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


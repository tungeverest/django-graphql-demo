import graphene
from .models import Todo
from graphene_django import DjangoObjectType, DjangoListField

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'date')
        
class TodoQuery(graphene.ObjectType):
    # todos = DjangoListField(TodoType)
    # todos = graphene.List(TodoType)
    # todos = graphene.Field(TodoType)
    todos = graphene.List(TodoType, id=graphene.Int())
    
    # def resolve_todos(self, info):
    #     return Todo.objects.all()
    #     return Todo.objects.get(id=2)
    
    def resolve_todos(self, info, id=None):
        if id:
            return Todo.objects.filter(id=id)
        return Todo.objects.all()
    
    
class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        title = graphene.String(required=True)
        
    def mutate(self, info, title):
        todo = Todo(title=title)
        todo.save()
        return CreateTodo(todo=todo)
    
class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        
    def mutate(self, info, id, title):
        todo = Todo.objects.get(pk=id)
        todo.title = title
        todo.save()
        return UpdateTodo(todo=todo)

class DeleteTodo(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        
    def mutate(self, info, id):
        todo = Todo.objects.get(pk=id)
        todo.delete()
        return DeleteTodo(message=f"Todo ID: {id} is deleted")
    
class TodoMutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    udpate_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()

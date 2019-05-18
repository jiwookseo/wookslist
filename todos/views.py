from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import List, Todo, Detail
from .serializers import ListSerializer, TodoSerializer, DetailSerializer


@api_view(["GET", "POST"])
def lists_list(request):
    if request.method == "GET":
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            request.data['user'] = request.user.id
            serializer = ListSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def lists_detail(request, pk):
    list_item = get_object_or_404(List, pk=pk)
    serializer = ListSerializer(list_item)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def todos_list(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def todos_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def details_list(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        details = todo.details.all()
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            serializer = DetailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET", "DELETE", "PUT"])
def details_detail(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    if request.method == 'GET':
        serializer = DetailSerializer(detail)
        return Response(serializer.data)
    else:
        if request.user == detail.todo.list.user:
            if request.method == 'PUT':
                serializer = DetailSerializer(detail, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            elif request.method == 'DELETE':
                detail.delete()
                return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def todos_check(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user == todo.list.user:
        todo.check = not todo.check
        todo.save()
        return JsonResponse({'check': todo.check})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
def todos_important(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user == todo.list.user:
        todo.important = not todo.important
        todo.save()
        return JsonResponse({'important': todo.important})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


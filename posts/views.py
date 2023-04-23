from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def homepage(request: Request):
    if request.method == 'POST':
        data = request.data
        return Response(data={'Message': 'Hello World!', 'data': data}, status=status.HTTP_201_CREATED)
    response = {'Message': 'Hello World!'}
    return Response(response, status=status.HTTP_200_OK)


# @api_view(http_method_names=['GET', "POST"])
# def list_posts(request: Request):
#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {"message": "Post Created", "data": serializer.data}
#             print(serializer.data, type(serializer.data))
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     post_data = Post.objects.all()
#     serializer = PostSerializer(instance=post_data, many=True)
#     response = {"message": "posts", "data": serializer.data}
#     return Response(data=response, status=status.HTTP_200_OK)

class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    """
    APIView for listing all posts and creating a new post.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def get(self, request: Request, *args, **kwargs):
    #     post = Post.objects.all()
    #     serializer = self.serializer_class(instance=post, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def post(self, request: Request, *args, **kwargs):
    #     data = request.data
    #     serializer = self.serializer_class(data=data,)
    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {"message": "Post Created",
    #                     "data": serializer.data}
    #         return Response(data=response, status=status.HTTP_201_CREATED)


# @api_view(http_method_names=['GET', "POST"])
# def get_details(request: Request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     serializer = PostSerializer(instance=post)
#     return Response(data={"Message": serializer.data}, status=status.HTTP_200_OK)
# @api_view(http_method_names=["PUT"])
# def update_post(request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)
#     data = request.data
#     serializer = PostSerializer(instance=post, data=data)
#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "message": "Post updated Successfully",
#             "old_data": post.__dict__,
#             "updated_data": serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(http_method_names=["DELETE"])
# def delete_post(request: Request, post_id: int):
#     print(post_id)
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,):  # APIView,
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get(self, request: Request, post_id: int, *args, **kwargs):
    #     post = get_object_or_404(Post, pk=post_id)
    #     serializer = self.serializer_class(instance=post).data
    #     return Response(data=serializer, status=status.HTTP_200_OK)

    # def delete(self, request: Request, post_id: int):
    #     post = get_object_or_404(Post, pk=post_id)
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def put(self, request: Request, post_id: int):
    #     post = get_object_or_404(Post, pk=post_id)
    #     data = request.data
    #     serializer = self.serializer_class(instance=post, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         response = {"Message": f"Post id:{post_id} record updated",
    #                     "data": serializer.data}
    #         return Response(data=response, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

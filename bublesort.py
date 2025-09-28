# # # # # # # Bubble Sort with Iterations
# # # # # # arr = [5, 3, 8, 4, 2]
# # # # # # n = len(arr)

# # # # # # for i in range(n-1):   
# # # # # #     print(f"\nIteration {i+1}:")
# # # # # #     for j in range(n-i-1):  
# # # # # #         if arr[j]>arr[j+1]:   
# # # # # #             arr[j],arr[j+1]= arr[j+1], arr[j]
# # # # # #         print(arr)   
# # # # # # print("\nFinal Sorted Array:",arr)


# # # # # # Simple Bubble Sort
# # # # # arr = [5,3,8,4,2]
# # # # # n = len(arr)

# # # # # for i in range(n-1):        
# # # # #     for j in range(n-i-1):   
# # # # #         if arr[j]>arr[j+1]:  
# # # # #             arr[j],arr[j+1]=arr[j+1],arr[j]

# # # # # print("Sorted Array:", arr)


# # # # # selection sort
# # # # arr = [64, 25, 12, 22, 11]
# # # # n = len(arr)
# # # # for i in range(n):
# # # #     min_idx = i
# # # #     for j in range(i+1, n):
# # # #         if arr[j] < arr[min_idx]:
# # # #             min_idx = j
# # # #     arr[i], arr[min_idx] = arr[min_idx], arr[i]
# # # # print("Sorted array:", arr)
  

# # # # To implement insertion sort in python
# # # arr=list(map(int,input().split()))
# # # n=len(arr)
# # # for i in range(1,n):
# # #     key=arr[i]
# # #     j=i-1
# # #     while j>=0 and key<arr[j]:
# # #         arr[j+1]=arr[j]
# # #         j-=1
# # #     arr[j+1]=key
# # # print(arr)

# # # merge sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])
#     right=merge_sort(arr[mid:])
#     return merge_sort(left,right)
# def merge(left,right):
#     result=[]
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


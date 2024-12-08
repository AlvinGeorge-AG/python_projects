n=[1,222,3,4,5]
def max_list(lt):
    if len(lt)==1:
        return lt[0]
    else:
        return max(lt)
print(max_list(n))
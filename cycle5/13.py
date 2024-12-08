lt=[2]
def sum_list(lt):
    if len(lt)==1:
        return lt[0]
    else:
        return sum(lt)
print(sum_list(lt))

try :
    raise Exception('custom error')
except Exception as ex:
    print(ex)
class TestMiddleWare(object):
    def process_view(self,request,func,*args,**kwargs):
        print("process_view")

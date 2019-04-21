## CONDITIONAL FUNCTION TESTING

Vars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

class OP:
    @staticmethod
    def EQ( x,y ):
        print(x,"Equals",y)
        #print(variables[x])
        return True if x==y else False
    @staticmethod
    def NEQ( x,y ):
        print(x,"Not Equals",y)
        #print(variables[x])
        return False if x==y else True

def variable( name ):
    return Vars[name]

def compare( it ):
    print( it[0],it[1],it[2] )
    func,key,op,value = it
    return op(func(key),value)
    print(op)


print( compare( (variable, "brand", OP.EQ, "Ford") ) )
print( compare( (variable, "brand", OP.NEQ, "Ford") ) )


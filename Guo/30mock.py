# input: list(strings) output:list(strings)
# david->david123,0
# adam->1Adam1,0


#runtime: O(1) for API  and O(n) for implementAPI
#space:O(n)
import collections
class Result:
    def __init__(self):
        self.userToPassLog = collections.defaultdict(lambda x:[None,None])
    def register(self,username,password):
        if username in self.userToPassLog:
            return "Username already exists"
        else:
            self.userToPassLog[username]=[password,0]
            return "Registered Successfully"


    def login(self,username,password):
        #if not exist
        if username not in self.userToPassLog:
            return "Login Unsuccessful"
        #if already logged in or if password incorrect
        if self.userToPassLog[username][1] or self.userToPassLog[username][0]!=password:
            return "Login Unsuccessful"
        #sucess
        self.userToPassLog[username][1]=1
        return "Logged In Successfully"

    def logout(self,username):
        #not exist
        if username  not in self.userToPassLog:
            return "Logout Unsuccessful"
        #not logged in
        if  self.userToPassLog[username][1]==0:
            return "Logout Unsuccessful"
        #success
        self.userToPassLog[username][1]=0
        return "Logged Out Successfully"


    def implementAPI(self,inputStringList):
        res = []
        for instruction in inputStringList:
            input = instruction.split()
            if input[0]=='register':
                res.append(self.register(input[1],input[2]))
            elif input[0] == 'login':
                res.append(self.login(input[1],input[2]))
            else:#logout:
                res.append(self.logout(input[1]))
        return res

        
#test
result = Result()
inputStringList = ['register david david123','register adam 1Adam1','login david david123','login adam 1adam1','logout david']
expected =['Registered Successfully','Registered Successfully','Logged In Successfully','Login Unsuccessful','Logged Out Successfully']
print("Expected:",expected,"Actual:",result.implementAPI(inputStringList))


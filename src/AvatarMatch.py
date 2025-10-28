class avatarMatch:
    
    def getMatchVectors(self,avatarVector,index)-> list:
        """return a list with user_id and score

        Args:
            avatarVector (list): vectors of the avatar
            index : index of vector DB

        Returns:
            list: return a list with user_id and score
        """
        res=index.query(vector=avatarVector,top_k=10,include_metadata=True,include_score=True,include_values=False)
        result=[]
        for i in range(len(res['matches'])):
            r=[]
            user_id=res['matches'][i]["metadata"]
            score={"score":res['matches'][i]["score"]}
            r.append(user_id)
            r.append(score)
            result.append(r)
            
        return result
    
    

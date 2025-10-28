import random

class vectorStore:
    """stores the vectors of photos in the Vector DB
    """   
    
    def convertVectors(self,vector,user_id)->list:
        """makes an array with vectors and metadata

        Args:
            vector (list): vector of image
            user_id (string): unique id from the mongoose

        Returns:
            list: array with vectors + metadata
        """
        v={
            "id":str(user_id)+str(random.randint(1,100000)),
            "values":vector,
            "metadata":{"user_id":user_id}
        }
        return [v]
    
    def insertVectors(self,insertVectors,index)->None:
        """inserts vectors to DB

        Args:
            insertVectors (list): lits from convertVectors
            index : index of vector
        """
        vectors=insertVectors
        index.upsert(vectors)
        

        
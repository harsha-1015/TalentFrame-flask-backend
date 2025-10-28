
    
class CallMethods:
    def __init__(self, face, vectorstore, avatar, index):
        self.face = face
        self.vectorstore = vectorstore
        self.avatar = avatar
        self.index = index

    def storeProfilePic(self, img_url, user_id)->None:
        """stores the profile pics of actors and directors in the vector db

        Args:
            img_url (string): url of the profile pic
            user_id (string): unique user id from mongoose
        """
        face_embedding = self.face.embed_face(img_url)
        convertedVectors = self.vectorstore.convertVectors(face_embedding, user_id)
        self.vectorstore.insertVectors(convertedVectors, self.index)

    def AvatarMatchProfiles(self, avatar_url)->list:
        """returns a list of matched profile pics to the avatar image

        Args:
            avatar_url (string): url of the avatar 

        Returns:
            list: a list containing the match results, it will be a 2d list with user_id and score 
        """
        face_embedding = self.face.embed_face(avatar_url).tolist()
        matches = self.avatar.getMatchVectors(face_embedding, self.index)
        return matches



        


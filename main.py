import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from pinecone import Pinecone
from src.FaceProcessor import faceProcessor
from src.VectorStore import vectorStore
from src.AvatarMatch import avatarMatch
from src.CallMethods import CallMethods
from src.config import VECTOR_DB_KEY, VECTOR_DB_HOST


app = Flask(__name__)
CORS(app)

pc = Pinecone(api_key=VECTOR_DB_KEY)
index = pc.Index(host=VECTOR_DB_HOST)
face = faceProcessor()
vectorstore = vectorStore()
avatar = avatarMatch()
call = CallMethods(face, vectorstore, avatar, index)

@app.route("/", methods=["GET"])
def test():
    """
    Simple health check endpoint.
    """
    return jsonify({
        "status": "success",
        "message": "TalentFrame Flask backend is running 🚀"
    }), 200

    

@app.route("/storeProfilePic", methods=["POST"])
def store_profile_pic():
    """
    Expects JSON:
    {
        "img_url": "<image_url>",
        "user_id": "<unique_user_id>"
    }
    """
    try:
        data = request.get_json()
        img_url = data.get("img_url")
        user_id = data.get("user_id")

        if not img_url or not user_id:
            return jsonify({"error": "Missing img_url or user_id"}), 400

        call.storeProfilePic(img_url, user_id)
        print({"message": "Profile picture stored successfully"})
        return jsonify({"message": "Profile picture stored successfully"}), 200

    except Exception as e:
        print("Error in /storeProfilePic:", e)
        return jsonify({"error": str(e)}), 500


@app.route("/findAvatarMatch", methods=["POST"])
def find_avatar_match():
    """
    Expects JSON:
    {
        "avatar_url": "<avatar_image_url>"
    }
    Returns: list of matches
    """
    try:
        data = request.get_json()
        avatar_url = data.get("avatar_url")

        if not avatar_url:
            return jsonify({"error": "Missing avatar_url"}), 400

        matches = call.AvatarMatchProfiles(avatar_url)
        m=jsonify({"matches": matches})
        print(m)
        return jsonify({"matches": matches}), 200

    except Exception as e:
        print("Error in /findAvatarMatch:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("TalentFrame Flask backend running on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)

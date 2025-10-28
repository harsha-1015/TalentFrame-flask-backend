from deepface import DeepFace
import numpy as np

class faceProcessor:
    _detector_backend = "opencv"
    _embed_model = "ArcFace" 

    @classmethod
    def crop_faces(cls, image_path):
        """Extract and return cropped faces."""
        faces = DeepFace.extract_faces(
            img_path=image_path,
            detector_backend=cls._detector_backend,
            enforce_detection=False
        )
        return [f["face"] for f in faces]

    @classmethod
    def embed_face(cls, image_path):
        """Use DeepFace.represent to get embedding from cached model."""
        embeddings = DeepFace.represent(
            img_path=image_path,
            model_name=cls._embed_model,
            detector_backend=cls._detector_backend,
            enforce_detection=False
        )
        vec = np.array(embeddings[0]["embedding"])
        return vec

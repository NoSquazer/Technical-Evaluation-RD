# Python
from typing import Optional

# SrcUtilities
from src.database.session import SessionLocal, Database


class Service:
    def post_data_service(
        db: SessionLocal,
        field_1: str,
        author: str,
        description: str,
        my_numeric_field: int,
        my_target_field: str,
    ) -> int:
        data = {
            "field_1": field_1,
            "author": author,
            "description": description,
            "my_numeric_field": my_numeric_field,
        }

        data[my_target_field.lower()] = data[my_target_field.lower()].upper()

        data_model = Database(**data)
        db.add(data_model)
        db.commit()

        return {"id": data_model.id}

    def get_data_service(db: SessionLocal, id: int) -> Optional[dict]:
        data = db.query(Database).filter(Database.id == id).first()
        if not data:
            return None
        return {
            "id": data.id,
            "field_1": data.field_1,
            "author": data.author,
            "description": data.description,
            "my_numeric_field": data.my_numeric_field,
        }


api_service_service = Service

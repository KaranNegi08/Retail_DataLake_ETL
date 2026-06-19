import boto3 
from config.config import GLUE_DATABASE

glue = boto3.client("glue")

def create_database():
    try:
        glue.create_database(
            DatabaseInput ={
                "Name": GLUE_DATABASE
            }
        )
        print(f"Database Created {GLUE_DATABASE}")
    except glue.exceptions.AlreadyExistsException:

        print("Database Already Exists")
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    create_database()
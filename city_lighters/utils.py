import uuid
import re

def slugify_and_append_uuid(title: str) -> str:
    unique_id = str(uuid.uuid4())[:8]
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.strip().lower()) 
    slug = slug.strip('-')
    slug_with_uuid = f"{slug}-{unique_id}"
    
    return slug_with_uuid
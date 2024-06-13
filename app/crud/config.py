from sqlalchemy.orm import Session
from app.db.models import Config
from app.schemas.config import ConfigCreate, ConfigUpdate

def create_config(db: Session, config: ConfigCreate):
    """
    Create a new configuration in the database.
    
    Args:
        db (Session): Database session.
        config (ConfigCreate): The configuration details.

    Returns:
        Config: The created configuration.
    """
    db_config = Config(country_code=config.country_code, requirements=config.requirements)
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_config_by_country(db: Session, country_code: str):
    """
    Retrieve the configuration for a specific country from the database.
    
    Args:
        db (Session): Database session.
        country_code (str): The country code.

    Returns:
        Config: The configuration for the country.
    """
    return db.query(Config).filter(Config.country_code == country_code).first()

def update_config(db: Session, config: ConfigUpdate):
    """
    Update the configuration in the database.
    
    Args:
        db (Session): Database session.
        config (ConfigUpdate): The updated configuration details.

    Returns:
        Config: The updated configuration.
    """
    db_config = get_config_by_country(db, country_code=config.country_code)
    if db_config:
        db_config.requirements = config.requirements
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_config(db: Session, country_code: str):
    """
    Delete the configuration from the database.
    
    Args:
        db (Session): Database session.
        country_code (str): The country code.

    Returns:
        None
    """
    db_config = get_config_by_country(db, country_code=country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
